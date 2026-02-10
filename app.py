
from flask import Flask, redirect, render_template, request, url_for
from models.database import init_db
from models.lista import Atividade

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/lista', methods=['GET','POST'])
def agenda():
    atividades = None

    if request.method == 'POST':
        titulo_atividade = request.form['titulo-atividade']
        tipo_de_atividade = request.form['tipo-de-atividade']
        atividade = Atividade(titulo_atividade, tipo_de_atividade)
        atividade.salvar_tarefa()

    atividades = Atividade.obter_tarefas()
    return render_template('lista.html', titulo='Sua Lista de Desejos', atividades=atividades)

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Atividade.id(idTarefa)
    tarefa.excluir_tarefa()
    # return render_template('agenda.html', titulo="Agenda",
    # tarefa=tarefas)
    return redirect(url_for('agenda'))

@app.route('/update/<int:idTarefa>', methods=['GET', 'POST']) 
def update(idTarefa):
    atividades = None

    if request.method == 'POST':
        titulo_atividade = request.form['titulo-tarefa']
        tipo_de_atividade = request.form['tipo-de-atividade']
        atividade = Atividade(titulo_atividade, tipo_de_atividade, idTarefa)
        atividade.atualizar_tarefas()

    atividades = Atividade.obter_tarefas()
    tarefa_selecionada = Atividade.id(idTarefa)
    return render_template('atividade.html', titulo=f'Editando a tarefa ID: {idTarefa}',tarefa_selecionada=tarefa_selecionada, atividades=atividades)

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"
