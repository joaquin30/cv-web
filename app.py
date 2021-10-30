from flask import Flask, render_template, request, redirect
from flask.helpers import flash

app = Flask(__name__, template_folder='templates')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/form', methods=['post'])
def form():
    req = request.form
    if req['user'] == 'root' and req['pass'] == '123':
        return render_template('form.html')
    else:
        flash('Usuario o contraseña incorrecta')
        return redirect('/')


def splitByComma(s):
    return list(
        filter(lambda x: len(x) > 0,
        map(lambda x: x.strip(),
        s.split(',')))
    )

@app.route('/cv', methods=['post'])
def cv():
    req = request.form
    css = req['css']
    return render_template('cv.html',
        css = f'/static/{css}.css',
        nombre = req['nombre'],
        presentacion = req['presentación'],
        datos = splitByComma(req['datos personales']),
        estudios = splitByComma(req['estudios']),
        logros = splitByComma(req['logros']),
        habilidades = splitByComma(req['habilidades']),
        experiencia = splitByComma(req['experiencia laboral']),
        intereses = splitByComma(req['intereses']),
        referencias = splitByComma(req['referencias'])
    )

if __name__ == '__main__':
    app.run()