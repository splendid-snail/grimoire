from PIL import Image
import random

sigil_base_paths = ["sigils/sigilbase_1.png", "sigils/sigilbase_2.png", "sigils/sigilbase_3.png"]
addon_paths = ["sigils/sigil_bend.png", "sigils/sigil_dagger.png"]

rotate_steps = [45, 90, 135, 180, 225, 270, 315, 360]

def create_sigil(demon):
    output = Image.open(random.choice(sigil_base_paths))
    strokes = 3
    while strokes > 0:
        addon = Image.open(random.choice(addon_paths))
        addon = addon.rotate(random.choice(rotate_steps))
        output = Image.alpha_composite(output, addon)
        strokes -= 1
    filename = "sigils/sigil__" + str(demon.order) + ".png"
    output.save(filename)
