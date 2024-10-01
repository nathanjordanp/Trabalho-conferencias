from flask import Flask, render_template
from conferencia import Conferencia

app = Flask(__name__)


conferencia_list = [
    Conferencia(1, 'Inovações em Inteligência Artificial para Sustentabilidade', 'Discussões sobre como a inteligência artificial pode impulsionar práticas sustentáveis e enfrentar desafios ambientais globais, com foco em soluções inovadoras e aplicações práticas.', 'sustentabilidade.png', 'Data: 15 a 17 de novembro de 2024', 'Local: Centro de Convenções de São Paulo, Brasil' ), 
    Conferencia(2, 'Avanços na Inteligência Artificial: Desafios e Oportunidades', 'Exploração dos mais recentes desenvolvimentos em IA, incluindo ética, aprendizado profundo e aplicações emergentes. Discussões sobre o impacto da IA na sociedade e estratégias para enfrentar desafios futuros.', 'artificial.png', 'Data: 15 a 22 de Março de 2025', 'Local: Centro de Convenções de Genebra, Suíça'), 
    Conferencia(3, 'Inovações em Biotecnologia e Saúde Genômica', 'Foco em avanços na engenharia genética, terapias personalizadas e bioinformática. Análise dos impactos das novas tecnologias genômicas na medicina e no tratamento de doenças raras e complexas.', 'biotecnologia.png', 'Data: 22 a 24 de Outubro de 2024', 'Local: Centro de Convenções de São Paulo, Brasil'), 
]


@app.route("/")
def home():
    return render_template("index.html", conferencia_list=conferencia_list)

@app.route("/conferencia/<int:id>")
def conferencia(id):
    for conferencia in conferencia_list:
        if conferencia.get_id() == id:
            return render_template("conferencias.html", conferencia=conferencia)
    return '<h1>Ops! Nenhuma conferência encontrada!</h1>'