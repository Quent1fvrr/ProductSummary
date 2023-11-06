
import gradio as gr
from reportlab.pdfgen import canvas
from pdf_generator.generalInfo import GeneralInfo
from pdf_generator.Figures import Figures
from pdf_generator.newsSection import NewsSection
from pdf_generator.dataLoader import dataLoader  # Assuming this class is defined elsewhere

def generate_pdf():
    data = dataLoader('data/airbus_data.json').data
    c = canvas.Canvas("airbus_company_profile.pdf")

    y_position = 800  # Starting Y position for the PDF drawing

    # Draw general info
    general_info = GeneralInfo(data['general_info'])
    y_position = general_info.draw(c, y_position)

    # Draw figures
    figures = Figures(data['figures'])
    y_position = figures.draw(c, y_position)

    # Draw news section
    news_section = NewsSection(data['news'])
    y_position = news_section.draw(c, y_position)

    c.save()
    return "airbus_company_profile.pdf"

iface = gr.Interface(fn=generate_pdf, inputs=None, outputs="file", title="Airbus Company Profile Generator", description="Click the button to generate a PDF profile for Airbus.")
iface.launch()
