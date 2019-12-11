import os
import random
import tarot
import demons
import text_output
import html_output


random.seed()

#useful and necessary lists
names_list = []
tarot_deck = tarot.generate()
random.shuffle(tarot_deck)
kings_list = demons.create_kings(names_list)
demons_list = demons.create_demons(kings_list, names_list, tarot_deck)

#Body content made here
body_content = html_output.generate_body_content(kings_list, demons_list)
total_html_string = html_output.generate_total_page(body_content)
#Export the html file
html_output.output_final_html(total_html_string)
