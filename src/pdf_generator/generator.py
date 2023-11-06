import gradio as gr
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
import json

class Generator:
    def __init__(self, data):
        self.data = data
        self.width, self.height = letter
        self.margin = 72  # 1 inch margin
        self.max_width = self.width - 2 * self.margin
        self.font_size = 12
        self.line_height = 1.4 * self.font_size  # 1.4 is the line spacing factor


    def draw_wrapped_text(self, c, text, x, y, max_width, font_name, font_size):
        c.setFont(font_name, font_size)
        words = text.split()
        line = []
        for word in words:
            test_line = line + [word]
            test_line_width = stringWidth(' '.join(test_line), font_name, font_size)
            if test_line_width <= max_width:
                line = test_line
            else:
                c.drawString(x, y, ' '.join(line))
                y -= self.line_height
                line = [word]
        c.drawString(x, y, ' '.join(line))
        return y - self.line_height

    def create_pdf(self, filename):
        c = canvas.Canvas(filename, pagesize=letter)
        y_position = self.height - 2 * self.margin  # Starting below the company name

        # Summary
        y_position = self.draw_wrapped_text(c, self.data["summary"], self.margin, y_position, self.max_width, "Helvetica", self.font_size)

        # News Section
        for news_item in self.data["news"]:
            y_position -= self.line_height
            if y_position < self.margin:
                c.showPage()
                y_position = self.height - 2 * self.margin
            
            # Headline
            y_position = self.draw_wrapped_text(c, news_item["headline"], self.margin, y_position, self.max_width, "Helvetica-Bold", self.font_size)
            
            # Content
            y_position = self.draw_wrapped_text(c, news_item["content"], self.margin, y_position, self.max_width, "Helvetica", 10)
            y_position -= self.line_height  # Additional space after the content

        c.save()
        return filename