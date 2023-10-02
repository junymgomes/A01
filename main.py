#apt install python3-flask
#from flask import Flask
#app = Flask(__name__)

#@app.route("/")
#def homepage():
    #return "<b>Hello App<b>"

#app.run(debug=True)

# Importe o Flask
from flask import Flask

# Crie uma instância do Flask
app = Flask(__name__)

# Defina a rota raiz ("/") e a função que será executada quando a rota for acessada
@app.route("/")
def homepage():
    return "<b1> Atividade 1 git: Edvaldo Gomes Pereira Júnior<b/1>"
    


# Verifique se este arquivo está sendo executado diretamente (não importado como um módulo)
if __name__ == "__main__":
    # Inicie o servidor Flask na porta 5000 e ative o modo de depuração
    app.run(debug=True)
