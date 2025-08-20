# Email-Deduplicator
Email Deduplicator GUI
A Python application with a modern GUI for removing duplicate email:password combinations from text files or pasted input. Built with CustomTkinter for an enhanced user experience.

Features
Email Normalization: Automatically converts emails to lowercase and fixes common typos (e.g., ".cpm" → ".com")

Duplicate Removal: Identifies and removes exact email:password duplicates

File Operations: Load from and save to text files with ease

Modern Dark Theme: Clean, professional interface with dark mode styling

Batch Processing: Handles large lists of email:password pairs efficiently

How It Works
The application processes input line by line, looking for email:password pairs separated by a colon. Each email is normalized (lowercased, typo-corrected, and stripped of whitespace) before comparison. Only unique combinations are kept in the final output.

Requirements
Python 3.6+

CustomTkinter (pip install customtkinter)

Usage
Paste your email:password pairs into the input field or load from a file

Click "Deduplicate" to process the list

Review the unique entries in the output field

Save the results to a file if desired

Perfect for cleaning email lists, removing duplicate credentials, and organizing authentication data.

https://img.shields.io/badge/Python-3.6%252B-blue?style=for-the-badge&logo=python https://img.shields.io/badge/License-MIT-green?style=for-the-badge
