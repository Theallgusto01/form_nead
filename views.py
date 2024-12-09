from app import app
from flask import render_template, jsonify, request

from utils import disc_por_curso_trad, disc_por_curso_abp

@app.route("/")

def index():

    cursos = {
        "ADMINISTRAÇÃO",
        "BIOMEDICINA",
        "CIÊNCIAS CONTÁBEIS",
        "DIREITO",
        "ENFERMAGEM",
        "FARMÁCIA",
        "FISIOTERAPIA",
        "NUTRIÇÃO",
        "PEDAGOGIA",
        "PSICOLOGIA",
        "TECNOLOGIA EM PROCESSOS GERENCIAIS"
    }
    return render_template('form.html', cursos=cursos)

@app.route('/get_disciplina/<curso>/<mod>', methods=['GET'])
def get_disciplina(curso, mod):
    if(mod == 'Tradicional'):
        discs = disc_por_curso_trad(curso)
    else:
        discs = disc_por_curso_abp(curso)
    return jsonify(discs)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict(flat=False)
    
    return render_template('ver_form.html', data=data)

@app.route('/pag')
def teste():
    return render_template('form_abp.html')