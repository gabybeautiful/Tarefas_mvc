from flask import Flask, render_template, request, redirect, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa']
        data_conclusao_form = request.form['dataConclusao']

        data_corrigida = data_conclusao_form or None 

   
        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        
        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listar_tarefas()

    return render_template(
        'base.html', 
        titulo_da_pagina='Minha lista de tarefas', 
        tarefas_da_pagina=tarefas
        )

@app.route('/delete/<int:id>')
def apagar_id_especificado(id):
       Tarefa.apagar_tarefa(id)

       return redirect(url_for('home'))


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar_id_especificado(id):

     if request.method =='POST':
          tarefa_edicao = Tarefa(
               id=id,
               titulo=request.form['tituloTarefa'],
               data_conclusao=request.form['dataConclucao']
          )

          tarefa_edicao.atualizar_tarefa()
          return redirect(url_for('home'))

     tarefas = Tarefa.listarTarefas(id)
     tarefas_selecionada = Tarefa.carregar_tarefa

     return render_template(
          'base.html',
          tarefa_edicao=tarefas_selecionada,
          tarefa_da_pagina = tarefas,
          titulo_da_pagina = tarefas
     )

if __name__ == '__main__':
    app.run()

