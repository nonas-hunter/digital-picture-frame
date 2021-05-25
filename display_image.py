"""Display image in full screen using Pillow & Tkinter."""

import tkinter
from PIL import Image, ImageTk

# Define tkinter window
root = tkinter.Tk()
# Run the following line to force full-screen
# WARNING: Can not close screen while overrideredirect == True
# root.overrideredirect(True)
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{width}x{height}+0+0")

# Open image using Pillow
with Image.open("test_images/pattern.jpg") as image:
    tkinter_image = ImageTk.PhotoImage(image)

# Create canvas and add image
canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack()
canvas.create_image(width/2,
                    height/2,
                    image=tkinter_image,
                    anchor=tkinter.CENTER)
root.mainloop()
