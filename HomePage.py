from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from search import fuzzySearch
from database import *

def articles():
    import articleCreation
    win.destroy()
    articleCreation.show()

# Ensure tables are created
createTables()

def Logo():
    try:
        image = Image.open("C://Users//64223//CPS//GitBash Folder//DDT logo.png")
        img = image.resize((50, 50))
        imgTk = ImageTk.PhotoImage(img)
        imgLabel = Label(logoFrame, image=imgTk)
        imgLabel.image = imgTk  # Keeps a reference to avoid garbage collection
        imgLabel.grid(row=0, column=0, padx=(0, 10), pady=10, sticky='nsew')
    except FileNotFoundError:
        imgLabel = Label(logoFrame, text="Logo not found")
        imgLabel.grid(row=0, column=0, padx=(0, 10), pady=10, sticky='nsew')

historyList = None

def search(username):
    searchTerm = searchEntry.get()
    print(f"Search term: {searchTerm}")

    # Saves the search term to the history table, so that it can be utilized later
    saveSearchHistory(username, searchTerm)
    updateHistoryList(username)

    articles = getAllArticles()
    articleTitles = [article[0] for article in articles]

    results = fuzzySearch(searchTerm.lower(), articleTitles)
    showSearchResults(results)

def updateHistoryList(username):
    global historyList
    historyList.delete(0, END)
    searchHistory = getSearchHistory(username)
    for item in searchHistory:
        historyList.insert(END, item[2])

def showSearchResults(results):
    def openArticle(title):
        article = next((art for art in getAllArticles() if art[0] == title), None)
        if article:
            showArticlePage(article)
        else:
            messagebox.showerror("Error", "Article not found")
            
    win.withdraw()

    def showArticlePage(article):
        def editArticle():
            articleWindow.destroy()
            showEditArticlePage(article)

        articleWindow = Toplevel(win)
        articleWindow.title("Article")
        articleWindow.attributes('-fullscreen',True)

        title, content = article
        Label(articleWindow, text=title, font=("Arial", 20)).pack(pady=10)

        contentText = Text(articleWindow, wrap="word")
        contentText.insert(1.0, content)
        contentText.pack(pady=10, fill="both", expand=True)

        Button(articleWindow, text="Edit Article", command=editArticle).pack(pady=10)
        Button(articleWindow, text="Back to Search Results", command=articleWindow.destroy).pack(pady=10)

    def showEditArticlePage(article):
        def saveEdits():
         # Makes it so that everything addded to the new article is from the start til the end, removing any whitespacing (uncessary spacing in a text)
            newContent = contentText.get("1.0", END).strip()
            if newContent:
                updateArticle(title, newContent)
                messagebox.showinfo("Success", "Article updated successfully")
                articleWindow.destroy()
                openArticle()
            else:
                messagebox.showwarning("Warning", "Content cannot be empty")

        articleWindow = Toplevel(win)
        articleWindow.title("Edit Article")
        articleWindow.attributes('-fullscreen',True)

        title, content = article
        Label(articleWindow, text=title, font=("Arial", 20)).pack(pady=10)

        contentText = Text(articleWindow, wrap="word")
        contentText.insert(1.0, content)
        contentText.pack(pady=10, fill="both", expand=True)

        Button(articleWindow, text="Save Edits", command=saveEdits).pack(pady=10)
        Button(articleWindow, text="Back to Search Results", command=articleWindow.destroy).pack(pady=10)

    searchWindow = Toplevel(win)
    searchWindow.title("Search Results")
    searchWindow.attributes('-fullscreen',True)

    listbox = Listbox(searchWindow, width=80, height=20)
    listbox.pack(pady=10)

    for title, _ in results:
        listbox.insert(END, title)

    def onSelect(event):
        selection = listbox.curselection()
        if selection:
            title = listbox.get(selection[0])
            openArticle(title)
    listbox.bind("<Double-1>", onSelect)

    def homePage():
        searchWindow.destroy()
        win.deiconify()

    Button(searchWindow, text="Home", command=homePage).pack(pady=10)

    searchWindow.mainloop()

def show(username):
    global win, searchEntry, logoFrame, historyList

    win = Tk()
    win.title("Home Page")
    win.attributes('-fullscreen',True)

    def dele():
        win.destroy()

    style = ttk.Style()
    style.configure("tFrame", background="white")
    style.configure("tButton", padding=6)
    style.configure("tLabel", padding=6)
    
    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=2)
    win.grid_rowconfigure(0, weight=1)
    win.grid_rowconfigure(1, weight=1)
    win.grid_rowconfigure(2, weight=2)
    win.grid_rowconfigure(3, weight=1)
    win.grid_rowconfigure(4, weight=1)

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

    videoPlayerFrame = ttk.Frame(win, width=600, height=50, relief="solid", padding=10)
    videoPlayerFrame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    videoPlayerFrame.grid_columnconfigure(0, weight=1)
    videoPlayerFrame.grid_columnconfigure(1, weight=1)
    videoPlayerFrame.grid_rowconfigure(0, weight=1)

    userInfoButton = ttk.Button(userInfoFrame, text="User Info")
    userInfoButton.grid(row=0, column=0, sticky="nsew")

    searchEntry = ttk.Entry(searchBarFrame)
    searchEntry.grid(row=0, column=0, sticky="nsew")
    searchButton = ttk.Button(searchBarFrame, text="🔎", command=lambda: search(username))
    searchButton.grid(row=0, column=1, sticky="nsew")

    historyLabel = ttk.Label(historyFrame, text="History")
    historyLabel.grid(row=0, column=0, sticky="nw")

    articleButton = ttk.Button(articleFrame, text="Article Creation", command=articles)
    articleButton.grid(row=0, column=0, sticky="nsew")

    deleteButton = ttk.Button(win, text="Close", command=dele)
    deleteButton.grid(row=2, column=9, sticky="E")

    historyList = Listbox(historyFrame)
    historyList.grid(row=1, column=0, sticky="nsew")

    dpLabel = ttk.Label(dpFrame, text="Description of KnowLed and its features")
    dpLabel.grid(row=0, column=0, sticky="nsew")

    videoPlayerLabel = ttk.Label(videoPlayerFrame, text="Video Player for later")
    videoPlayerLabel.grid(row=0, column=0, sticky="nsew")
    videoPlayer = ttk.Button(videoPlayerFrame, text="▶️")
    videoPlayer.grid(row=0, column=1, sticky="nsew")

    Logo()
    updateHistoryList(username)
    
if __name__ == "__main__":
    show()
