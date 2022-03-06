from borb.pdf.canvas.font.simple_font.true_type_font import TrueTypeFont
from borb.pdf.canvas.font.font import Font

# Download Font
import requests

with open("IndieFlower-Regular.ttf", "wb") as ffh:
    ffh.write(
        requests.get(
            "https://github.com/google/fonts/blob/main/ofl/indieflower/IndieFlower-Regular.ttf?raw=true",
            allow_redirects=True,
        ).content
    )
