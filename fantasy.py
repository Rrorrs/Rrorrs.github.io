from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd

def fant_program():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('tp_fant.html')
    file_xl = 'anime.xlsx'
    anime = pd.read_excel(
        file_xl,
        sheet_name='Фентези',
        na_values=['N/A', 'NA'],
        keep_default_na=False).to_dict(orient='records')
    rendered_page = template.render(anime=anime)

    with open('fantasy.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)