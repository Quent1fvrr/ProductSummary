# general_info.py

# general_info.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from textwrap import wrap

class GeneralInfo:
    def __init__(self, data):
        self.data = data
        self.header_font = 'Helvetica-Bold'
        self.text_font = 'Helvetica'
        self.header_size = 16
        self.text_size = 12
        self.line_spacing = 14

    def draw(self, c, y_position):
        # Register a TrueType font (optional)
        # pdfmetrics.registerFont(TTFont('YourFontName', 'path_to_your_font.ttf'))

        # Draw a header for the general info
        c.setFont(self.header_font, self.header_size)
        c.setFillColor(colors.HexColor("#333333"))  # Dark grey color
        c.drawString(72, y_position, "General Information")
        y_position -= self.line_spacing * 2  # Add some space after the header

        # Draw a line under the header (optional)
        c.setStrokeColor(colors.HexColor("#333333"))
        c.line(72, y_position, letter[0] - 72, y_position)
        y_position -= self.line_spacing

        # Draw the text of the general info
        c.setFont(self.text_font, self.text_size)
        c.setFillColor(colors.black)
        wrapped_text = wrap(self.data['summary'], 80)  # Assuming 'summary' is the key for the text
        for line in wrapped_text:
            c.drawString(72, y_position, line)
            y_position -= self.line_spacing

        return y_position - self.line_spacing  # Extra space after the block
