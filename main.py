import tkinter as tk
from tkinter import messagebox
from collector import fetch_poi

def start_collection():
    city = city_entry.get()
    keyword = keyword_entry.get()
    limit = int(limit_entry.get())
    key = key_entry.get()
    account = account_var.get()

    if not (city and keyword and key):
        messagebox.showerror("错误", "请填写完整信息！")
        return

    try:
        df = fetch_poi(city, keyword, key, limit)
        filename = f"data/{keyword}_{city}.csv"
        df.to_csv(filename, index=False, encoding="utf-8-sig")
        messagebox.showinfo("完成", f"采集完成！文件已保存：{filename}")
    except Exception as e:
        messagebox.showerror("错误", str(e))

root = tk.Tk()
root.title("MyAgent 高德地图数据采集模块")
root.geometry("400x400")

tk.Label(root, text="账号选择:").pack()
account_var = tk.StringVar(value="账号1")
tk.OptionMenu(root, account_var, "账号1", "账号2", "账号3").pack()

tk.Label(root, text="城市:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Label(root, text="关键词:").pack()
keyword_entry = tk.Entry(root)
keyword_entry.pack()

tk.Label(root, text="采集数量:").pack()
limit_entry = tk.Entry(root)
limit_entry.insert(0, "50")
limit_entry.pack()

tk.Label(root, text="高德API Key:").pack()
key_entry = tk.Entry(root, show="*")
key_entry.pack()

tk.Button(root, text="开始采集", command=start_collection, bg="#4CAF50", fg="white").pack(pady=10)

root.mainloop()
