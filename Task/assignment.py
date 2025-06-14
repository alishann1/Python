import tkinter as tk
from tkinter import ttk  # For themed widgets
from PIL import Image, ImageTk  # Import Image and ImageTk from Pillow


class ImageButtonTextApp:
    def __init__(self, master):
        self.master = master
        master.title("My Window")
        master.geometry("600x450")  # Set a default window size
        master.resizable(True, True)  # Allow window resizing

        # --- Text Label (Top) ---
        self.title_label = tk.Label(master,
                                    text="Welcome to My Window!",
                                    font=("Helvetica", 16, "bold"),
                                    fg="#333333",  # Dark grey color
                                    pady=15)  # Vertical padding
        self.title_label.pack(side=tk.TOP, fill=tk.X)

        # --- Image Display ---
        # It's good practice to handle potential image loading errors.
        try:
            # Create a placeholder image URL or use a local path to your image
            # For demonstration, I'll use a placeholder.co link.
            # In a real app, replace this with your actual image file path:
            # image_path = "path/to/your/image.png"
            image_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.m.wikipedia.org%2Fwiki%2FFile%3APython-logo-notext.svg&psig=AOvVaw1ngerI8aWgz-mayF-ZIQlD&ust=1749975984688000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCIi859y-8I0DFQAAAAAdAAAAABAE"

            # Fetching an image from a URL is more complex in a simple Tkinter app,
            # as it requires downloading it first. For this example, let's assume
            # you have a local image file.
            # If you don't have one, save this placeholder image to a file like 'my_image.png'
            # and use its path.
            #
            # Example using a local file (replace 'my_image.png' with your file):
            image_path = "my_image.png"  # Create a dummy image file with this name for testing
            # Or you can use a base64 encoded image directly (not recommended for large images)

            # Attempt to open the image using Pillow
            original_image = Image.open(image_path)
            # Resize image if too large (optional)
            original_image = original_image.resize((300, 200), Image.LANCZOS)

            # Convert Pillow Image to Tkinter PhotoImage
            self.tk_image = ImageTk.PhotoImage(original_image)

            self.image_label = tk.Label(master, image=self.tk_image)
            self.image_label.pack(pady=10)  # Padding below the image

        except FileNotFoundError:
            self.image_label = tk.Label(
                master, text="Image not found! Please place 'my_image.png' in the same directory.", fg="red")
            self.image_label.pack(pady=10)
        except Exception as e:
            self.image_label = tk.Label(
                master, text=f"Error loading image: {e}", fg="red")
            self.image_label.pack(pady=10)

        # --- Buttons Frame (Middle) ---
        self.button_frame = tk.Frame(master, pady=10)
        self.button_frame.pack()

        # Button 1
        self.button1 = ttk.Button(self.button_frame,
                                  text="Click Me!",
                                  command=self.on_button_click)
        self.button1.pack(side=tk.LEFT, padx=10)  # padx for horizontal spacing

        # Button 2
        self.button2 = ttk.Button(self.button_frame,
                                  text="Say Hello",
                                  command=self.say_hello)
        self.button2.pack(side=tk.LEFT, padx=10)

        # --- Status Text (Bottom) ---
        self.status_text = tk.StringVar()  # Tkinter string variable
        self.status_text.set("Ready to interact!")
        self.status_label = tk.Label(master,
                                     textvariable=self.status_text,
                                     font=("Arial", 12),
                                     fg="green",
                                     pady=10)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    # --- Button Command Methods ---
    def on_button_click(self):
        """Action for 'Click Me!' button."""
        self.status_text.set("Button 'Click Me!' was pressed!")
        print("Button 1 clicked!")  # Also print to console for debugging

    def say_hello(self):
        """Action for 'Say Hello' button."""
        self.status_text.set("Hello there! How can I help?")
        print("Button 2 clicked: Hello!")


# --- Main Application Execution ---
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = ImageButtonTextApp(root)  # Instantiate the application
    root.mainloop()  # Start the Tkinter event loop
