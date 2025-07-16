import os

def act():
    # List PDF files in the current working directory (or specify a path)
    pdfs = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    if not pdfs:
        return "No PDF files found in the current directory."

    report = ["PDF files detected:"]
    for pdf in pdfs:
        size = os.path.getsize(pdf)
        report.append(f"{pdf} ({size // 1024} KB)")
    return "\n".join(report)
