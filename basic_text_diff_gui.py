import tkinter as tk
from difflib import Differ


def diff_texts():
    text1 = text_box1.get("1.0", tk.END)
    text2 = text_box2.get("1.0", tk.END)

    differ = Differ()
    diff = list(differ.compare(text1.splitlines(), text2.splitlines()))

    text_diff_box.delete("1.0", tk.END)
    for line in diff:
        if line.startswith('-'):
            text_diff_box.insert(tk.END, line + '\n', 'removed')
        elif line.startswith('+'):
            text_diff_box.insert(tk.END, line + '\n', 'added')
        elif line.startswith('?'):
            text_diff_box.insert(tk.END, line + '\n', 'changed')
        else:
            text_diff_box.insert(tk.END, line + '\n')


root = tk.Tk()
root.title("Text Diff Viewer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Text box for the first text
text_box1 = tk.Text(frame, width=40, height=20)
text_box1.grid(row=0, column=0, padx=(0, 10))

# Text box for the second text
text_box2 = tk.Text(frame, width=40, height=20)
text_box2.grid(row=0, column=1, padx=(10, 0))

# Button to compute the diff
diff_button = tk.Button(frame, text="Show Diff", command=diff_texts)
diff_button.grid(row=1, column=0, columnspan=2, pady=10)

# Text box to show the diff result
text_diff_box = tk.Text(frame, width=80, height=20)
text_diff_box.grid(row=2, column=0, columnspan=2)

# Highlighting for different changes
text_diff_box.tag_config('removed', foreground='red')
text_diff_box.tag_config('added', foreground='green')
text_diff_box.tag_config('changed', foreground='blue')

root.mainloop()
