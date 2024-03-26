import tkinter as tk
from PIL import Image, ImageTk
from pyautogui import hotkey

# --- functions ---

def on_click(event=None):
    # `command=` calls function without argument
    # `bind` calls function with one argument
    hotkey('ctrl', 's')

# # --- main ---

root = tk.Tk()
# Hide the root window drag bar and close button
root.overrideredirect(True)
# Make the root window always on top
root.wm_attributes("-topmost", True)
# Turn off the window shadow
root.wm_attributes("-transparent", True)
# Set the root window background color to a transparent color
root.config(bg='black')

root.geometry("45x45+0+920")

# Store the PhotoImage to prevent early garbage collection
# load image
image = Image.open("/Users/dkullas/Documents/Python_Scripts/SiriButton/siri1.png")
image = image.resize((45,45))
photo = ImageTk.PhotoImage(image)

# Display the image on a label
label = tk.Label(root, image=photo)
# Set the label background color to a transparent color
label.config(bg='black')
label.pack()

# bind click event to image
label.bind('<Button-1>', on_click)

# button with image binded to the same function 
b = tk.Button(root, image=photo, command=on_click)
b.pack()

# button with text closing window
b = tk.Button(root, text="Close", command=root.destroy)
b.pack()

root.mainloop()