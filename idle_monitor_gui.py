import tkinter as tk
from tkinter import ttk
import json
import os

LOG_FILE = "/tmp/idle_monitor_log.json"

class IdleMonitorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Idle Monitor")
        master.geometry("400x300")

        self.tree = ttk.Treeview(master, columns=('Date', 'Time', 'Message'), show='headings')
        self.tree.heading('Date', text='Date')
        self.tree.heading('Time', text='Time')
        self.tree.heading('Message', text='Message')
        self.tree.pack(pady=10, padx=10, expand=True, fill='both')

        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.refresh_button = tk.Button(master, text="Refresh", command=self.refresh_log)
        self.refresh_button.pack(pady=5)

        self.refresh_log()

    def refresh_log(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                log = json.load(f)
                for entry in reversed(log):
                    self.tree.insert('', 0, values=(entry['date'], entry['time'], entry['message']))

def main():
    root = tk.Tk()
    IdleMonitorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()