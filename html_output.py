import text_output

def paragraph(text):
    output = "<p>" + text + "</p>\n"
    return output

def generate_total_page(body_content):
    title = "Grimoire"
    subtitle = text_output.generate_subtitle()
    html_header = "<!DOCTYPE html>\n<html>\n\n<head>\n<title>" + title + "</title>\n<link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n\n"
    html_body = "<body>\n<h1>" + title + "</h1>\n" + "<p><em>" + subtitle + "</em></p><hr>\n" + body_content + "\n</body>\n\n</html>"
    return html_header + html_body

def generate_body_content(kings_list, demons_list): #Actually the main body content maker function
    output = ""
    output += "<p>" + text_output.write_intro() + "</p>"
    for king in kings_list:
        output += "<h2>The King and Spirits of the " + king.realm + " realm</h2>\n"
        output += "<p>" + text_output.describe_realm(king) + "</p>\n"
        output += "<h3>Of this realm's King</h3>\n"
        output += "</p>" + text_output.describe_king(king) + "</p>\n"
        output += "<hr>\n"
        output += "<h3>Of this realm's Demons</h3>\n"
        for demon in demons_list:
            if demon.realm == king.realm:
                output += "<p>" + text_output.describe_demon(demon) + "</p>\n"
                output += "<p>" + text_output.describe_ritual(demon) + "</p>\n"
                output += "<hr>\n"
    return output

def output_final_html(total_html_string):
    html_file = open("grimoire.html", "w")
    html_file.write(total_html_string)
    html_file.close()
