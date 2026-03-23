import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

# ---------------- Skills & Suggestions ----------------
skills_list = [
    "python", "java", "c++", "html", "css",
    "javascript", "sql", "machine learning", "data science"
]

suggestions = {
    "python": "Learn Python for automation and AI.",
    "java": "Java is useful for backend development.",
    "c++": "C++ improves problem solving skills.",
    "html": "HTML is essential for web development.",
    "css": "CSS is needed for styling websites.",
    "javascript": "JavaScript makes websites interactive.",
    "sql": "SQL is important for databases.",
    "machine learning": "Machine Learning is trending in AI field.",
    "data science": "Data Science is a high demand skill."
}

resume_text = ""

# ---------------- PDF Reader ----------------
def read_pdf(file_path):
    text = ""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF!\n{e}")
    return text.lower()

# ---------------- Upload Resume ----------------
def upload_file():
    global resume_text
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        resume_text = read_pdf(file_path)
        messagebox.showinfo("Success", "Resume uploaded successfully!")

# ---------------- Analyze Resume ----------------
def analyze_resume():
    global resume_text
    
    # If user typed text manually
    manual_text = text_box.get("1.0", tk.END).strip().lower()
    
    if not resume_text and not manual_text:
        messagebox.showwarning("Warning", "Upload or paste resume first!")
        return
    
    text = resume_text if resume_text else manual_text
    
    found = []
    missing = []
    
    for skill in skills_list:
        if skill in text:
            found.append(skill)
        else:
            missing.append(skill)
    
    score = int((len(found) / len(skills_list)) * 100)
    
    # Result text
    result = "📊 Resume Analysis Result\n\n"
    
    result += "✅ Found Skills:\n"
    result += ", ".join(found) if found else "None"
    
    result += "\n\n❌ Missing Skills:\n"
    result += ", ".join(missing) if missing else "None"
    
    result += f"\n\n⭐ Score: {score}%\n\n"
    
    result += "💡 Suggestions:\n"
    for skill in missing:
        result += f"- {suggestions[skill]}\n"
    
    result_box.config(state='normal')
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result)
    result_box.config(state='disabled')

# ---------------- Clear ----------------
def clear_all():
    global resume_text
    resume_text = ""
    text_box.delete("1.0", tk.END)
    result_box.config(state='normal')
    result_box.delete("1.0", tk.END)
    result_box.config(state='disabled')

# ---------------- GUI ----------------
root = tk.Tk()
root.title("🔥 Advanced Resume Analyzer")
root.geometry("700x600")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="Advanced Resume Analyzer", 
         font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Upload PDF", width=15, command=upload_file).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Analyze", width=15, command=analyze_resume).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Clear", width=15, command=clear_all).grid(row=0, column=2, padx=10)

# Text Input
tk.Label(root, text="Or Paste Resume Text:", bg="#f0f0f0").pack()
text_box = tk.Text(root, height=10, font=("Arial", 11))
text_box.pack(pady=10)

# Result
tk.Label(root, text="Result:", bg="#f0f0f0").pack()
result_box = tk.Text(root, height=15, font=("Arial", 11), state='disabled')
result_box.pack(pady=10)

root.mainloop()