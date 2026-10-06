import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

def upload_and_watermark():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
    )
    if not file_path:
        return
        
    watermark_text = text_entry.get()
    if not watermark_text:
        messagebox.showwarning("Warning", "Please enter watermark text first!")
        return

    try:
        img = Image.open(file_path).convert("RGBA")
        txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
        
        font_size = int(img.size[0] / 25)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        draw = ImageDraw.Draw(txt_layer)
        position = (img.size[0] - 20, img.size[1] - 20) 
        draw.text(position, watermark_text, fill=(255, 255, 255, 100), font=font, anchor="rb")
        
        # Combine layers and save
        combined = Image.alpha_composite(img, txt_layer)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        
        if save_path:
            combined.convert("RGB").save(save_path)
            messagebox.showinfo("Success", "Watermarked image saved successfully!")
            
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Python Watermarker")
root.geometry("400x150")

tk.Label(root, text="Enter Watermark Text:").pack(pady=5)
text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=5)

upload_btn = tk.Button(root, text="Select Image & Apply", command=upload_and_watermark)
upload_btn.pack(pady=10)

root.mainloop()