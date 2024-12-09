import pandas as pd

# Tabela - Curso/Disciplina
url_trad = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTzSI3la7MLXriTcXVKtsB4poLVkRtUOHRwK6n-sTik45flNyeE3n8ZJVJc-4_E12rfwFIbEeJMkc-G/pub?gid=0&single=true&output=csv"
url_abp  = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTzSI3la7MLXriTcXVKtsB4poLVkRtUOHRwK6n-sTik45flNyeE3n8ZJVJc-4_E12rfwFIbEeJMkc-G/pub?gid=56038968&single=true&output=csv"

def disc_por_curso_trad(curso):
    disc = pd.read_csv(url_trad, sep=',')
    resp = disc.query(f'CURSO == "{curso}"')['DISCIPLINA'].tolist()  
    return resp


def disc_por_curso_abp(curso):
    disc = pd.read_csv(url_abp, sep=',')
    resp = disc.query(f'CURSO == "{curso}"')['DISCIPLINA'].tolist()  
    return resp



