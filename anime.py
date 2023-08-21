import tkinter as tk
import urllib.request as req
import bs4

def fetch_anime_updates():
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    })
    
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    links = root.select("h3 ul li a")

    return [(link.text, link.get("href")) for link in links]

def display_anime_updates():
    updates = fetch_anime_updates()
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, "今天更新以下動漫：\n" + "=" * 50 + "\n\n")
    for text, link in updates:
        text_widget.insert(tk.END, text + " (")
        text_widget.insert(tk.END, link, "link")
        text_widget.insert(tk.END, ")\n\n")
        text_widget.tag_configure("link", foreground="blue", underline=True)
        text_widget.tag_bind("link", "<Button-1>", lambda e, link=link: link_clicked(link))

def link_clicked(link):
    import webbrowser
    webbrowser.open_new_tab(link)

url = "https://anime1.me/"

# 建立主視窗
root = tk.Tk()
root.title("Anime1 動漫更新")
root.geometry("800x600")

# 建立按钮
update_button = tk.Button(root, text="查看最新動漫", command=display_anime_updates)
update_button.pack()

# 文本框用于顯示結果
text_widget = tk.Text(root, wrap=tk.WORD, width=70, height=25)
text_widget.pack()

root.mainloop()
