import customtkinter as ctk
from tkinter import filedialog, messagebox
import re

# ---------------- Email Deduplication Logic ----------------
def normalize_email(email):
    email = email.lower()
    email = email.replace(".cpm", ".com")
    email = email.strip()
    return email

def deduplicate_pairs_from_text(text):
    seen = set()
    cleaned_list = []

    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if not line or ":" not in line:
            continue
        email, password = line.split(":", 1)
        email = normalize_email(email)
        pair = f"{email}:{password.strip()}"
        if pair not in seen:
            seen.add(pair)
            cleaned_list.append(pair)
    return cleaned_list

# ---------------- GUI ----------------
class EmailDeduplicatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Email Deduplicator")
        self.geometry("800x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # --- Input Text Frame ---
        ctk.CTkLabel(self, text="Input Emails (paste or load file):").pack(pady=(10, 0))
        self.input_text = ctk.CTkTextbox(self, height=200)
        self.input_text.pack(padx=20, fill="x")
        ctk.CTkButton(self, text="Load From File", command=self.load_input_file).pack(pady=5)

        # --- Output Text Frame ---
        ctk.CTkLabel(self, text="Deduplicated Emails:").pack(pady=(10, 0))
        self.output_text = ctk.CTkTextbox(self, height=200)
        self.output_text.pack(padx=20, fill="x")
        
        # --- Buttons ---
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)
        ctk.CTkButton(button_frame, text="Deduplicate", command=self.run_deduplication).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Save Output", command=self.save_output_file).pack(side="left", padx=10)

    # --- Load input file ---
    def load_input_file(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "r", encoding="utf-8") as f:
                self.input_text.delete("1.0", "end")
                self.input_text.insert("1.0", f.read())

    # --- Deduplicate emails ---
    def run_deduplication(self):
        text = self.input_text.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("No Input", "Please paste emails or load a file first.")
            return

        cleaned_list = deduplicate_pairs_from_text(text)
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", "\n".join(cleaned_list))
        messagebox.showinfo("Done", f"✅ Deduplicated {len(cleaned_list)} unique entries.")

    # --- Save output to file ---
    def save_output_file(self):
        text = self.output_text.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("No Output", "There is nothing to save.")
            return

        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("Saved", f"✅ Output saved to {file}")

if __name__ == "__main__":
    app = EmailDeduplicatorApp()
    app.mainloop()
