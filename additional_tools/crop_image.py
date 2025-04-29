from tkinter import Tk, Canvas, filedialog
from PIL import Image, ImageTk
import os    


class ImageRectangleDrawer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Image Viewer - Draw Rectangle")

        # Load and display the image
        self.image_path = image_path
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas = Canvas(root, width=self.tk_image.width(), height=self.tk_image.height(), cursor="cross")
        self.canvas.pack()

        self.canvas_image = self.canvas.create_image(0, 0, anchor='nw', image=self.tk_image)

        # Rectangle drawing variables
        self.start_x = None
        self.start_y = None
        self.rect = None

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        # Start drawing rectangle
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=1)

    def on_move_press(self, event):
        # Update rectangle as mouse moves
        cur_x, cur_y = event.x, event.y
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        crop_box = (self.start_x, self.start_y, event.x, event.y)
        cropped_image = self.image.crop(crop_box)
        # Save or show the cropped image
        new_image_path = "cropped_" + os.path.basename(self.image_path)
        print(new_image_path)
        cropped_image.save(new_image_path)
        cropped_image.show()

        # Rectangle finished (optional: print coordinates or crop logic here)
        print(f"Rectangle: ({self.start_x}, {self.start_y}) to ({event.x}, {event.y})")


def open_image_viewer():
    # Use temporary root to open file dialog
    temp_root = Tk()
    temp_root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All files", "*.*"))
    )
    temp_root.destroy()

    if file_path:
        root = Tk()
        app = ImageRectangleDrawer(root, file_path)
        root.mainloop()
    else:
        print("No file selected.")


open_image_viewer()
