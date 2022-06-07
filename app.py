import os, jinja2

# templateLoader = jinja2.FileSystemLoader( searchpath=f"{os.path.abspath(os.getcwd())}/" )
templateLoader = jinja2.FileSystemLoader( searchpath="/" )

templateEnv = jinja2.Environment( loader=templateLoader )

TEMPLATE_FILE = f"{os.path.abspath(os.getcwd())}/ejemplo.jinja"
# TEMPLATE_FILE = "/home/juan/test_projects/uso_jinja/ejemplo.jinja"

template = templateEnv.get_template(TEMPLATE_FILE)

templateVars = { "saludo": "Buen dia", "contenido":"caldito de pollo" }

outputText = template.render(templateVars)

print(outputText)

## to file
text_file = open(f"{os.path.abspath(os.getcwd())}/salida", "w")
n = text_file.write(outputText)
text_file.close()
