import random
import text_output
import language
from language import article, archaic


def paragraph(text):
    output = "<p>" + text + "</p>\n"
    return output

def list_item(text):
    output = "<li>" + text + "</li>\n"
    return output

def generate_total_page(body_content):
    title = "Grimoire"
    subtitle = text_output.generate_subtitle()
    html_header = "<!DOCTYPE html>\n<html>\n\n<head>\n<title>" + title + "</title>\n<link rel=\"stylesheet\" href=\"https://www.w3schools.com/w3css/4/w3.css\">\n</head>\n\n"
    html_body = "<body>\n<h1>" + title + "</h1>\n" + "<p><em>" + subtitle + "</em></p><hr>\n" + body_content + "\n</body>\n\n</html>"
    return html_header + html_body

def generate_table_of_contents(kings_list, demons_list):
    output = "<h2>On the Structure of the Demonic realms</h2>"
    output += paragraph("Know that the Empire of the demonic forms is divided into SIX Kingdoms, four of those being aligned with the Cardinal points of the Compasse, and the other two with the Upper and lower Kingdoms.")
    output += paragraph("Each of these six Realmes is governed by ARTICLE ADJ King.")
    adj = archaic(random.choice(language.king_adj))
    new_article = article(adj)
    output = output.replace("ADJ", adj)
    output = output.replace("ARTICLE", new_article)
    #List begins
    output += "<ol>\n"
    for king in kings_list:
        output += "<li> The " + king.realm + " realm, governed by " + king.title + " " + king.name + "</li>\n"
    output += "</ol>\n"
    #more content
    output += paragraph("Each of these Kings is attended by a personal Host of 13 Demons or Spirits, varying in power and ability, all of whom this book will show you how to successfully Conjure. The spirits serving these kings are arrayed thus:")
    for king in kings_list:
        output += "<h3>Serving " + king.title + " " + king.name + " in the " + king.realm + " realm:</h3>\n"
        output += "<ul>"
        for demon in demons_list:
            if demon.king == king:
                output += "<li><a href=\"#" + demon.name + "\">" + demon.rank + " " + demon.name + "</a> who may " + demon.skill + "</li>\n"
        output += "</ul>\n"
    return output

def generate_body_content(kings_list, demons_list): #Actually the main body content maker function
    #intro
    output = paragraph(text_output.write_intro())
    output += "<hr>"
    #table of contents
    output += generate_table_of_contents(kings_list, demons_list)
    output += "<hr>"
    #king and realm descriptions
    for king in kings_list:
        output += "<h2>The King and Spirits of the " + king.realm + " realm</h2>\n"
        output += paragraph(text_output.describe_realm(king))
        output += "<h3>Of this realm's King</h3>\n"
        output += paragraph(text_output.describe_king(king))
        output += "<hr>\n"
        output += "<h3>Of this realm's Demons</h3>\n"
        for demon in demons_list:
            if demon.realm == king.realm:
                output += paragraph(text_output.describe_demon(demon))
                output += paragraph(text_output.describe_ritual(demon))
                output += "<hr>\n"
    return output

def output_final_html(total_html_string):
    html_file = open("grimoire.html", "w")
    html_file.write(total_html_string)
    html_file.close()
