from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def generate_intel_briefing(target_ip, findings, filename="OSINT_Report.pdf"):
    """Automates the creation of a professional PDF Intelligence Briefing."""
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, f"Automated Threat Intelligence Briefing")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, 720, f"Target: {target_ip}")
    c.drawString(50, 700, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    
    c.drawString(50, 660, "--- Autonomous Findings ---")
    
    y = 630
    for finding in findings:
        c.drawString(50, y, finding)
        y -= 25
        
    c.save()
    print(f"[*] Briefing generated: {filename}")
