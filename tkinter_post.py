import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

def get_post_number():
    today = datetime.now().strftime("%Y-%m-%d")
    post_files = [f for f in os.listdir("./_posts") if re.match(f"{today}-\\d{{2}}\\.markdown", f)]
    return len(post_files) + 1

def generate_markdown_file(post_number, title, content):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S +0000")
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-{post_number:02d}.markdown"
    filepath = os.path.join("./_posts", filename)
    header = f"""---
layout: post
title:  "{title}"
date:   {now}
categories: jekyll update
---
"""
    markdown_content = f"{header}\n{content}\n"
    if not os.path.exists("./_posts"):
        os.makedirs("./_posts")
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    messagebox.showinfo("Success", f"Markdown file created: {filepath}")

def submit():
    title = title_entry.get()
    content = content_text.get("1.0", tk.END)
    if not title or not content.strip():
        messagebox.showwarning("Input Error", "Title and content cannot be empty.")
        return
    post_number = get_post_number()
    generate_markdown_file(post_number, title, content)
    update_info()

def update_info():
    post_count = get_post_number() - 1
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info_label.config(text=f"Today's posts: {post_count}\nCurrent time: {current_time}")
    root.after(1000, update_info)  # 每秒更新一次

# 创建Tkinter窗口
root = tk.Tk()
root.title("Markdown Post Generator")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# 信息标签
info_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0")
info_label.pack(pady=10)

# 标题输入栏
title_frame = tk.Frame(root, bg="#f0f0f0")
title_frame.pack(pady=10)
tk.Label(title_frame, text="Title:", font=("Helvetica", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
title_entry = tk.Entry(title_frame, width=40, font=("Helvetica", 12))
title_entry.pack(side=tk.LEFT, padx=5)

# 内容输入框
content_frame = tk.Frame(root, bg="#f0f0f0")
content_frame.pack(pady=10)
tk.Label(content_frame, text="Content:", font=("Helvetica", 12), bg="#f0f0f0").pack()
content_text = tk.Text(content_frame, height=15, width=50, font=("Helvetica", 12), wrap=tk.WORD)
content_text.pack(pady=5, padx=5)

# 提交按钮
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 12), command=submit, bg="#4CAF50", fg="white", activebackground="#45a049", padx=10, pady=5)
submit_button.pack(pady=20)

# 启动Tkinter主循环并更新信息
update_info()
root.mainloop()
