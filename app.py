from flask import Flask, render_template, request
from genform import genform

app = Flask(__name__, template_folder='templates')

def strip(s):
    return s.strip()

@app.route('/')
def index():
    return render_template('index.html')#, form=genform('form.txt'))

@app.route('/cv', methods=['GET', 'POST'])
def cv():
    req = request.form
    return render_template('cv.html',
        nombre=req['nombre'],
        presentacion=req['presentación'],
        datos=list(map(strip, req['datos personales'].split(','))),
        estudios=list(map(strip, req['estudios'].split(','))),
        logros=list(map(strip, req['logros'].split(','))),
        habilidades=list(map(strip, req['habilidades'].split(','))),
        experiencia=list(map(strip, req['experiencia laboral'].split(','))),
        intereses=list(map(strip, req['intereses'].split(','))),
        referencias=list(map(strip, req['referencias'].split(',')))
    )

if __name__ == '__main__':
    app.run()