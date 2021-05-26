"""Display image in full screen using Pillow & Tkinter."""

import tkinter
from PIL import Image, ImageTk

# Define tkinter window
root = tkinter.Tk()
# Run the following line to force full-screen
# WARNING: Can not close screen while overrideredirect == True
# root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}+0+0")

# Open image using Pillow
with Image.open("test_images/pattern.jpg") as image:
    scale_height = screen_height / image.height
    scale_width = screen_width / image.width
    if scale_width < scale_height:
        width = int(image.width * scale_width)
        height = int(image.height * scale_width)
    else:
        width = int(image.width * scale_height)
        height = int(image.height * scale_height)
    # NOTE: Image.BICUBIC is an alternative to Image.LANCZOS which is slightly
    # more efficient
    tkinter_image = ImageTk.PhotoImage(image.resize((width, height),
                                                    resample=Image.LANCZOS))

# Create canvas and add image
canvas = tkinter.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()
canvas.create_image(screen_width/2,
                    screen_height/2,
                    image=tkinter_image,
                    anchor=tkinter.CENTER)
root.mainloop()
