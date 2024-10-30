import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Frame Layouts")

# create a Frame 1
frame1 = tk.Frame(root, bg="lightblue", bd=5)
frame1.pack(fill="both", expand=True, padx=10, pady=10)

# create a Frame 2
frame2 = tk.Frame(root, bg="lightgreen", bd=5)
frame2.pack(fill="both", expand=True, padx=10, pady=10)

#add widget to frame 1
label1 = tk.Label(frame1, text="Frame 1", font=("Latin", 16))
label1.pack(pady=10)

#add widget to frame 2
label2 = tk.Label(frame2, text="Frame 2", font=("Courier New", 16))
label2.pack(pady=10)

root.mainloop()