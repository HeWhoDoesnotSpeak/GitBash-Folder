from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from search import fuzzySearch
from database import *
import articleCreation
import userInfo

def articles(username):
    # Closes the current window and opens the article creation page
    win.destroy()
    articleCreation.show(username)

def showUserInfo(username):
    # Closes the current window and opens the user info page
    win.destroy()
    userInfo.show(username)

# Ensures tables are created
createTables()

def Logo():
    # Declares imgTk and imgLabel as global here
    global imgLabel, imgTk  

    # A try case if the image is unable to be opened
    try:
        image = Image.open(r"C:\Users\64223\CPS\GitBash Folder\DDT logo.png")
        img = image.resize((50, 50))
        # Creates a PhotoImage object
        imgTk = ImageTk.PhotoImage(img)  
        
        # Label creation and assignment
        imgLabel = Label(logoFrame, image=imgTk)  
        # Keeps a reference to avoid garbage collection
        imgLabel.image = imgTk  
        imgLabel.grid(row=0, column=0, padx=(0, 10), pady=10, sticky='nsew')
    except FileNotFoundError:
        imgLabel = Label(logoFrame, text="Logo not found")
        imgLabel.grid(row=0, column=0, padx=(0, 10), pady=10, sticky='nsew')

historyList = None

def search(username):
    searchTerm = searchEntry.get()
    print(f"Search term: {searchTerm}")

    # Saves the search term to the history table
    saveSearchHistory(username, searchTerm)
    updateHistoryList(username)

    # Retrieves all articles and their titles
    articles = getAllArticles()
    articleTitles = [article[0] for article in articles]

    # Perform fuzzy search to find the best matches
    results = fuzzySearch(searchTerm.lower(), articleTitles)
    showSearchResults(results)

def updateHistoryList(username):
    # Updates the history list with past searches
    global historyList
    historyList.delete(0, END)
    searchHistory = getSearchHistory(username)
    for item in searchHistory:
        historyList.insert(END, item[2])

def showSearchResults(results):
    def openArticle(title):
        # Opens the article page for the selected title
        article = next((art for art in getAllArticles() if art[0] == title), None)
        if article:
            showArticlePage(article)
        else:
            messagebox.showerror("Error", "Article not found")

    win.withdraw()

    def showArticlePage(article):
        def editArticle():
            # Closes the current window and opens the edit article page
            articleWindow.destroy()
            showEditArticlePage(article)

        # Puts the article Window at thr top of the screen
        articleWindow = Toplevel(win)
        articleWindow.title("Article")
        articleWindow.attributes('-fullscreen', True)

        title, content = article
        Label(articleWindow, text=title, font=("Arial", 20)).pack(pady=10)

        # The saved information on the database put into the article when being viewed
        contentText = Text(articleWindow, wrap="word")
        contentText.insert(1.0, content)
        contentText.pack(pady=10, fill="both", expand=True)

        Button(articleWindow, text="Edit Article", command=editArticle).pack(pady=10)
        Button(articleWindow, text="Back to Search Results", command=articleWindow.destroy).pack(pady=10)

    def showEditArticlePage(article):
        def saveEdits():
            # The function when newContent is added into the article with strips and calling to outside functions
            newContent = contentText.get("1.0", END).strip()
            if newContent:
                updateArticle(title, newContent)
                messagebox.showinfo("Success", "Article updated successfully")
                articleWindow.destroy()
                # Passes the title to reopen the updated article
                openArticle(title) 
            else:
                messagebox.showwarning("Warning", "Content cannot be empty")

        articleWindow = Toplevel(win)
        articleWindow.title("Edit Article")
        articleWindow.attributes('-fullscreen', True)

        title, content = article
        Label(articleWindow, text=title, font=("Arial", 20)).pack(pady=10)

        # The context added information that is inserted when saving edits
        contentText = Text(articleWindow, wrap="word")
        contentText.insert(1.0, content)
        contentText.pack(pady=10, fill="both", expand=True)

        Button(articleWindow, text="Save Edits", command=saveEdits).pack(pady=10)
        Button(articleWindow, text="Back to Search Results", command=articleWindow.destroy).pack(pady=10)

    searchWindow = Toplevel(win)
    searchWindow.title("Search Results")
    searchWindow.attributes('-fullscreen', True)

    # Keeps a list of that goes down for multiples instances of different results
    listbox = Listbox(searchWindow, width=80, height=20)
    listbox.pack(pady=10)

    # Displays the results with titles and their relevance scores
    for title, score in results:
        listbox.insert(END, f"{title} (Score: {score})")

    def onSelect(event):
        # Handles double-click selection in the listbox which means when the user wants to view that article they have to double click
        selection = listbox.curselection()
        if selection:
            title = listbox.get(selection[0]).split(' (')[0]
            openArticle(title)
    listbox.bind("<Double-1>", onSelect)

    def homePage():
        # Returns to the home page
        searchWindow.destroy()
        win.deiconify()

    Button(searchWindow, text="Home", command=homePage).pack(pady=10)

    searchWindow.mainloop()


def show(username):
    # Sets up and displays the main window
    global win, searchEntry, logoFrame, historyList

    win = Tk()
    win.title("Home Page")
    win.attributes('-fullscreen', True)

    def dele():
        win.destroy()

    # Tk's style configuration
    style = ttk.Style()
    style.configure("tFrame", background="white")
    style.configure("tButton", padding=6)
    style.configure("tLabel", padding=6)
    
    # Grid configuration
    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=2)
    win.grid_rowconfigure(0, weight=1)
    win.grid_rowconfigure(1, weight=1)
    win.grid_rowconfigure(2, weight=2)
    win.grid_rowconfigure(3, weight=1)
    win.grid_rowconfigure(4, weight=1)

    # Frames setup for the; user Info, logo, article button, search bar, history, description and video
    userInfoFrame = ttk.Frame(win, width=200, height=100, relief="solid", padding=10)
    userInfoFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    userInfoFrame.grid_columnconfigure(0, weight=1)
    userInfoFrame.grid_rowconfigure(0, weight=1)

    logoFrame = ttk.Frame(win, width=400, height=100, relief="solid", padding=10)
    logoFrame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    logoFrame.grid_columnconfigure(0, weight=1)
    logoFrame.grid_rowconfigure(0, weight=1)

    articleFrame = ttk.Frame(win, width=200, height=50, relief="solid", padding=10)
    articleFrame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    articleFrame.grid_columnconfigure(0, weight=1)
    articleFrame.grid_rowconfigure(0, weight=1)

    searchBarFrame = ttk.Frame(win, width=400, height=50, relief="solid", padding=10)
    searchBarFrame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    searchBarFrame.grid_columnconfigure(0, weight=3)
    searchBarFrame.grid_columnconfigure(1, weight=1)
    searchBarFrame.grid_rowconfigure(0, weight=1)

    historyFrame = ttk.Frame(win, width=600, height=200, relief="solid", padding=10)
    historyFrame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    historyFrame.grid_columnconfigure(0, weight=1)
    historyFrame.grid_rowconfigure(0, weight=1)

    dpFrame = ttk.Frame(win, width=600, height=100, relief="solid", padding=10)
    dpFrame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    dpFrame.grid_columnconfigure(0, weight=1)
    dpFrame.grid_rowconfigure(0, weight=1)

    videoPlayerFrame = ttk.Frame(win, width=600, height=300, relief="solid", padding=10)
    videoPlayerFrame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    videoPlayerFrame.grid_columnconfigure(0, weight=1)
    videoPlayerFrame.grid_rowconfigure(0, weight=1)

    userInfoButton = ttk.Button(userInfoFrame, text="User Info", command=lambda: showUserInfo(username))
    userInfoButton.grid(row=0, column=0, sticky="nsew")

    searchEntry = ttk.Entry(searchBarFrame)
    searchEntry.grid(row=0, column=0, sticky="nsew")
    searchButton = ttk.Button(searchBarFrame, text="🔎", command=lambda: search(username))
    searchButton.grid(row=0, column=1, sticky="nsew")

    historyLabel = ttk.Label(historyFrame, text="History")
    historyLabel.grid(row=0, column=0, sticky="nw")

    articleButton = ttk.Button(articleFrame, text="Article Creation", command=lambda: articles(username))
    articleButton.grid(row=0, column=0, sticky="nsew")

    deleteButton = ttk.Button(win, text="Close", command=dele)
    deleteButton.grid(row=2, column=9, sticky="E")

    historyList = Listbox(historyFrame)
    historyList.grid(row=1, column=0, sticky="nsew")

    dpLabel = ttk.Label(dpFrame, text="""Description of KnowLed and its features: To make a 
                        quicker and easier way to access information for a subject for studies 
                        without needing to waste unnecessary time going through multiple websites not giving 
                        what you specifically want to know. With quicker categorisation and a precise search bar 
                        that can find out the exact answer to your question when a random thought or an answer, you need to know for a test.

                        When clicking on your search there will be a score ranging from the best to worst match of your query with the higher the better likehood of being relevent to your inquiry.
                        Creating an article can allow for freedom of public releasement of information.
                        
                        Warning: If you click user info or Article Creation and your history doesn't pop up please just search something and click back to see. And Image for logo doesn't want to pop back after one run for some reason.""")
    dpLabel.grid(row=0, column=0, sticky="nsew")

    # Gives the label for the Video Player that becomes a header for it
    videoPlayerLabel = ttk.Label(videoPlayerFrame, text="Video Player")
    videoPlayerLabel.grid(row=0, column=0, sticky="nsew")

    # My attempt at trying to use tkinterVideo to be used like Pillow for a video (If possible can someone give me a comment on how to do it)
    # Watch the video manually if you want to.

    """
    # The function and variable with TkinterVideo being used and the master being VPframe as the holder and position player
    videoPlayer = TkinterVideo(master=videoPlayerFrame, scaled=True)
    videoPlayer.grid(row=1, column=0, sticky="nsew")

    # In case an error were to occur
    try:
        videoPlayer.load(r"C:\\Users\\64223\\CPS\\GitBash Folder\\KnowLED vid.mp4")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load video: {e}")

    # Play button that utilizes the play function
    playButton = ttk.Button(videoPlayerFrame, text="▶️ Play", command=videoPlayer.play)
    playButton.grid(row=2, column=0, pady=5, sticky="nsew")

    # Stop button that utilizes the stop function
    stopButton = ttk.Button(videoPlayerFrame, text="⏹️ Stop", command=videoPlayer.stop)
    stopButton.grid(row=2, column=1, pady=5, sticky="nsew")
    """

    # Calls the Logo function to display the logo
    Logo()  
    # Updates the history list with past searches
    updateHistoryList(username)
    
    win.mainloop()

if __name__ == "__main__":
    show()
