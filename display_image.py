from PIL import Image, ImageTk
import tkinter

# Define tkinter window
root = tkinter.Tk()
width, height = root.winfo_screenwidth(), root.winfo_screenheight()

# Open image using Pillow
with Image.open("test_images/pattern.jpg") as image:
    tkinter_image = ImageTk.PhotoImage(image)

# Create canvas and add image
canvas = tkinter.Canvas(root, width=width, height=height)
canvas.pack()
canvas.create_image(width/2, height/2, image=tkinter_image, anchor=tkinter.CENTER)
root.mainloop()