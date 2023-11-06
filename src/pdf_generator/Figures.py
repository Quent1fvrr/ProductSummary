# figures.py

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

class Figures:
    def __init__(self, figures_data):
        self.figures_data = figures_data
        self.header_font = 'Helvetica-Bold'
        self.text_font = 'Helvetica'
        self.header_size = 14
        self.text_size = 10
        self.line_spacing = 12

    def draw(self, c, y_position):
        # Draw a header for the figures section
        c.setFont(self.header_font, self.header_size)
        c.setFillColor(colors.HexColor("#666666"))  # Medium grey color
        c.drawString(72, y_position, "Key Figures")
        y_position -= self.line_spacing * 2  # Add some space after the header

        # Draw the figures content
        c.setFont(self.text_font, self.text_size)
        c.setFillColor(colors.black)



        for figure in self.figures_data:
            if isinstance(figure, dict) and 'label' in figure and 'value' in figure:
                c.drawString(72, y_position, f"{figure['label']}: {figure['value']}")
                y_position -= self.line_spacing
            else:
                # Handle the case where figure is not a dictionary or does not have the expected keys
                print(f"Invalid figure data: {figure}")

        return y_position - self.line_spacing  # Extra space after the block    
