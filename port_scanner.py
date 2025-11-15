import socket
import threading
from queue import Queue
import tkinter as tk
from tkinter import ttk

# WORKING / BACK-END
def scan_port(ip, port, output_box):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))
        if result == 0:
            output_box.insert(tk.END, f"Open Port: {port}\n")
        sock.close()

    except:
        pass

def start_scan(ip, max_port, output_box):
    output_box.insert(tk.END, f"Starting scan on {ip} up to port {max_port}\n")
    q = Queue()

    def threader():
        while True:
            worker = q.get()
            scan_port(ip, worker, output_box)
            q.task_done()

    for x in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()
    
    for port in range(1, max_port + 1):
        q.put(port)
    q.join()
    output_box.insert(tk.END, "Scan completed...!\n")


# GUI / FRONTEND    
root = tk.Tk()
root.title("Advanced Port Scanner GUI")
root.geometry("650x500")
root.configure(bg="#0d0d0d")

title = tk.Label(root, text="Advanced Port Scanner", font=("Arial", 20, "bold"), fg="#f3f7f6", bg="#0d0d0d")
title.pack(pady=10)

# Frame for inputs
frame = tk.Frame(root, bg="#0d0d0d")
frame.pack(pady=10)

# Target IP input
tk.Label(frame, text="Target IP:", font=("Arial", 14), fg="white", bg="#0d0d0d").grid(row=0, column=0, padx=10, pady=5)
ip_entry = tk.Entry(frame, font=("Arial", 14), width=20)
ip_entry.grid(row=0, column=1, padx=10)

# Port range input
tk.Label(frame, text="Port Range:", font=("Arial", 14), fg="white", bg="#0d0d0d").grid(row=1, column=0, padx=10, pady=5)
port_entry = tk.Entry(frame, font=("Arial", 14), width=20)
port_entry.grid(row=1, column=1, padx=10)

# Start Scan Button
def start_scan_ui():
    ip = ip_entry.get()
    port_limit = int(port_entry.get())
    threading.Thread(target=start_scan, args=(ip, port_limit, output_box)).start()

# Output box section (middle)
output_frame = tk.Frame(root, bg="#0d0d0d")
output_frame.pack(pady=10)

output_box = tk.Text(output_frame, height=15, width=70, bg="#1a1a1a",
                     fg="#00ffcc", font=("Consolas", 12))
output_box.pack(side=tk.LEFT)

scroll = tk.Scrollbar(output_frame, command=output_box.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
output_box.config(yscrollcommand=scroll.set)


button_frame = tk.Frame(root, bg="#0d0d0d")
button_frame.pack(pady=15)

btn = tk.Button(button_frame, text="Start Scan", font=("Arial", 18),
                bg="#56ff4d", fg="black", command=start_scan_ui, width=12)
btn.grid(row=0, column=2, padx=15)

exit_btn = tk.Button(button_frame, text="Exit", font=("Arial", 18),
                     bg="#56ff4d", fg="black", command=root.destroy, width=12)
exit_btn.grid(row=0, column=4, padx=15)
root.mainloop()