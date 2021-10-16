from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/form', methods=['post'])
def form():
    req = request.form
    if req['user'] == 'root' and req['pass'] == '123':
        return render_template('form.html')
    else:
        return redirect('/')


def splitByComma(s):
    return list(map(lambda x: x.strip(), s.split(',')))

@app.route('/cv', methods=['post'])
def cv():
    req = request.form
    return render_template('cv.html',
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