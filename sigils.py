from PIL import Image
import random

base_paths = ["sigils/sigilbase_1.png", "sigils/sigilbase_2.png", "sigils/sigilbase_3.png"]
mid_paths = ["sigils/sigil_mid_1.png", "sigils/sigil_mid_2.png", "sigils/sigil_mid_3.png"]
top_paths = ["sigils/sigil_top_1.png","sigils/sigil_top_2.png","sigils/sigil_top_3.png","sigils/sigil_top_4.png","sigils/sigil_top_5.png"]

rotate_steps = [45, 90, 135, 180, 225, 270, 315, 360]
rotate_steps_90 = [90, 180, 270, 360]

def create_sigil(demon):
    base = Image.open(random.choice(base_paths))
    #base = base.rotate(random.choice(rotate_steps))

    mid = Image.open(random.choice(mid_paths))
    mid = mid.rotate(random.choice(rotate_steps))

    output = Image.alpha_composite(base, mid)

    strokes = random.randint(1,3)
    while strokes > 0:
        top = Image.open(random.choice(top_paths))
        top = top.rotate(random.choice(rotate_steps))
        output = Image.alpha_composite(output, top)
        strokes -= 1

    filename = "docs/sigils/sigil__" + str(demon.order) + ".png"
    output.save(filename)
