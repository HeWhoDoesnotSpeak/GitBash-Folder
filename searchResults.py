from tkinter import *
from tkinter import messagebox
from database import getAllArticles

# Calls the article when article in all of the article is the one that is corresponds to the title
def showSearchResults(results):
    def openArticle(title):
        article = next((art for art in getAllArticles() if art[0] == title), None)
        if article:
            showArticlePage(article)
        else:
            messagebox.showerror("Error", "Article not found")

    def showArticlePage(article):
        def backToSearch():
            articleWindow.destroy()
            showSearchResults(results)

        articleWindow = Toplevel()
        articleWindow.title("Article")
        articleWindow.geometry("600x400")

        title, content = article
        Label(articleWindow, text=title, font=("Arial", 20)).pack(pady=10)
        Label(articleWindow, text=content, wraplength=550).pack(pady=10)
        Button(articleWindow, text="Back to Search Results", command=backToSearch).pack(pady=10)

    #Search Window
    sW = Toplevel()
    sW.title("Search Results")
    sW.geometry("600x400")

    listbox = Listbox(sW, width=80, height=20)
    listbox.pack(pady=10)

    for title in results:
        listbox.insert(END, title)

    # Event for when text is clicked on, followed the mechanisms from https://python-course.eu/tkinter/events-and-binds-in-tkinter.php
    def onSelect(event):
        selection = listbox.curselection()
        if selection:
            title = listbox.get(selection[0])
            openArticle(title)

    listbox.bind("<Double-1>", onSelect)
    sW.mainloop()
