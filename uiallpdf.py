import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import fitz  # PyMuPDF
from docx import Document
from docx2pdf import convert as word_to_pdf_convert
import pikepdf

# ------------ Feature Functions ------------

def convert_pdf_to_word(pdf_path):
    doc = fitz.open(pdf_path)
    document = Document()
    for page in doc:
        text = page.get_text()
        document.add_paragraph(text)
    output_path = os.path.splitext(pdf_path)[0] + ".docx"
    document.save(output_path)
    return output_path

def convert_word_to_pdf(docx_path):
    output_path = os.path.splitext(docx_path)[0] + ".pdf"
    word_to_pdf_convert(docx_path, output_path)
    return output_path

def merge_pdfs(pdf_files):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF file", "*.pdf")])
    if output_path:
        merger.write(output_path)
        merger.close()
        return output_path
    return None

def compress_pdf(pdf_path):  
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata(reader.metadata)
    output_path = os.path.splitext(pdf_path)[0] + "_compressed.pdf"
    with open(output_path, 'wb') as f:
        writer.write(f)
    return output_path

# ------------ GUI Functional Triggers ------------

def run_pdf_to_word():
    path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if path:
        try:
            output = convert_pdf_to_word(path)
            messagebox.showinfo("Success", f"Converted to Word:\n{output}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def run_word_to_pdf():
    path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    if path:
        try:
            output = convert_word_to_pdf(path)
            messagebox.showinfo("Success", f"Converted to PDF:\n{output}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def run_merge_pdfs():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        try:
            output = merge_pdfs(files)
            if output:
                messagebox.showinfo("Success", f"Merged PDF saved at:\n{output}")
        except Exception as e:
            messagebox.showerror("Error", str(e))






    








# ------------ GUI Layout ------------

root = tk.Tk()
root.title("Document Utility Toolkit")
root.geometry("450x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Choose an Operation", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

tk.Button(root, text="PDF to Word", command=run_pdf_to_word, width=30, height=2, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Word to PDF", command=run_word_to_pdf, width=30, height=2, bg="#2196F3", fg="white").pack(pady=10)
tk.Button(root, text="Merge PDFs", command=run_merge_pdfs, width=30, height=2, bg="#FF9800", fg="white").pack(pady=10)














root.mainloop()



