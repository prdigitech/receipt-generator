import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas

def generate_receipt():
    name = entry_name.get()
    amount = entry_amount.get()
    payment_method = entry_method.get()
    description = entry_description.get("1.0", tk.END).strip()

    if not name or not amount or not payment_method:
        messagebox.showwarning("Input Error", "Please fill in all the fields.")
        return

    global receipt_text
    receipt_text = (
        f"Receipt\n"
        f"----------------------------\n"
        f"Name: {name}\n"
        f"Amount: ${amount}\n"
        f"Payment Method: {payment_method}\n"
        f"Description: {description}\n"
        f"----------------------------\n"
        f"Thank you for your payment!"
    )

    text_receipt.delete("1.0", tk.END)
    text_receipt.insert(tk.END, receipt_text)

def download_pdf():
    if not receipt_text:
        messagebox.showwarning("No Receipt", "Please generate a receipt first.")
        return

    # Create a PDF file
    file_name = "receipt.pdf"
    c = canvas.Canvas(file_name)
    c.drawString(100, 750, "Payment Receipt")
    c.drawString(100, 730, "----------------------------")

    # Split the receipt text by line and write each line to the PDF
    y_position = 710
    for line in receipt_text.split("\n"):
        c.drawString(100, y_position, line)
        y_position -= 20

    c.save()
    messagebox.showinfo("Download Complete", f"Receipt downloaded as {file_name}")

# Create the main window
root = tk.Tk()
root.title("Payment Receipt Generator")

# Labels and entry fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Amount").grid(row=1, column=0, padx=10, pady=5)
entry_amount = tk.Entry(root)
entry_amount.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Payment Method").grid(row=2, column=0, padx=10, pady=5)
entry_method = tk.Entry(root)
entry_method.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Description").grid(row=3, column=0, padx=10, pady=5)
entry_description = tk.Text(root, height=5, width=30)
entry_description.grid(row=3, column=1, padx=10, pady=5)

# Receipt output
text_receipt = tk.Text(root, height=15, width=50)
text_receipt.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Buttons
btn_generate = tk.Button(root, text="Generate Receipt", command=generate_receipt)
btn_generate.grid(row=5, column=0, pady=10)

btn_download = tk.Button(root, text="Download as PDF", command=download_pdf)
btn_download.grid(row=5, column=1, pady=10)

# Initialize global variable for receipt text
receipt_text = ""

# Run the application
root.mainloop()
