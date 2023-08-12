import tkinter as tk
import random
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.attributes("-fullscreen", True)  # Make the window full-screen

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Create a Canvas widget to display the noise
canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack()

# Generate and update the noise every 200 milliseconds
def generate_noise():
    noise_image = Image.new("RGB", (screen_width, screen_height))
    pixels = []
    for _ in range(screen_width * screen_height):
        value = random.randint(0, 255)
        pixels.append((value, value, value))
    noise_image.putdata(pixels)
    
    noise_tk = ImageTk.PhotoImage(noise_image)
    canvas.create_image(0, 0, image=noise_tk, anchor="nw")
    canvas.image = noise_tk
    
    root.after(200, generate_noise)  # Call generate_noise after 200 milliseconds

# Start generating noise
generate_noise()

root.mainloop()