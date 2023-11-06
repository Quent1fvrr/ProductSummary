# news_section.py

from reportlab.lib import colors
from textwrap import wrap

class NewsSection:
    def __init__(self, news_data):
        self.news_data = news_data
        self.header_font = 'Helvetica-Bold'
        self.text_font = 'Helvetica'
        self.header_size = 14
        self.text_size = 10
        self.line_spacing = 12

    def draw(self, c, y_position):
        # Draw a header for the news section
        c.setFont(self.header_font, self.header_size)
        c.setFillColor(colors.HexColor("#666666"))  # Medium grey color
        c.drawString(72, y_position, "Latest News")
        y_position -= self.line_spacing * 2  # Add some space after the header

        # Draw the news items
        c.setFont(self.text_font, self.text_size)
        c.setFillColor(colors.black)
        for news_item in self.news_data:
            # Headline
            c.setFont(self.header_font, self.text_size + 2)  # Slightly bigger font for headlines
            c.drawString(72, y_position, news_item['headline'])
            y_position -= self.line_spacing

            # News content
            c.setFont(self.text_font, self.text_size)
            wrapped_text = wrap(news_item['content'], 80)  # Assuming 'content' is the key for the text
            for line in wrapped_text:
                c.drawString(72, y_position, line)
                y_position -= self.line_spacing

            y_position -= self.line_spacing  # Extra space after each news item

        return y_position - self.line_spacing  # Extra space after the block
