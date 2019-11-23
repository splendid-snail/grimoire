from PIL import Image

def create_sigil(demon):
    base = Image.open("sigils/sigil_base.png")
    filename = "sigils/sigil_" + str(demon.order) + ".png"
    base.save(filename)
