from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(data):

    os.makedirs("reports", exist_ok=True)

    file_path = "reports/Water_Report.pdf"

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>Water Intelligence Platform</b>", styles["Title"])
    )

    story.append(
        Paragraph("<br/>", styles["Normal"])
    )

    for key, value in data.items():
        story.append(
            Paragraph(f"<b>{key}</b> : {value}", styles["Normal"])
        )

    doc.build(story)

    return file_path