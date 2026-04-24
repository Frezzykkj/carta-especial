from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Defina aqui a sua pergunta e a resposta correta
PERGUNTA = "Para ter certeza de que você não se esqueceu, oque eu sempre digo que você é para mim? ❤️"
RESPOSTA_CORRETA = "incrivel" or "especial"

@app.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        resposta_usuario = request.form.get('resposta').lower().strip()
        
        if resposta_usuario == RESPOSTA_CORRETA:
            return redirect(url_for('carta'))
        else:
            erro = "Hum, essa não é a nossa palavra secreta... Tente de novo! ❤️"
            
    return render_template('login.html', pergunta=PERGUNTA, erro=erro)

@app.route('/carta')
def carta():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)