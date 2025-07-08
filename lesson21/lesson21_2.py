import tkinter as tk

def on_button_click():
    print("Hello, Tkinter!");

def create_main_window():
    window = tk.Tk();
    window.title("Easy Tkinter example");
    window.geometry("300x200");

    btn = tk.Button(window, text="click", command=on_button_click);
    btn.pack(pady=50);

    return window;

def main():
    window = create_main_window();
    window.mainloop();

if __name__ == "__main__":
    main();