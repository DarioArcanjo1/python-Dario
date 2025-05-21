from flask import Flask, render_template,jsonify

app = Flask(__name__)

VAGA=[
    {
    'id':1,
      'titulo': 'Analista de Dados', 
      'local': 'Nampula',
      'salario': '35000 mt',
        'cantidados': '10', 
    },
    {
        'id':2,
          'titulo': 'Medicina', 
          'local': 'Beira',
          'salario': '1850 mt',
            'cantidados': '5', 
        },
    {
        'id':3,
          'titulo': 'licenciatura em Direito', 
          'local': 'Maputo',
          'salario': '25000 mt',
            'cantidados': '12', 
        },
    
        {
        'id':4,
          'titulo': 'Enfermagem geral', 
          'local': 'Nacala porto',
          'salario': '45000 mt',
            'cantidados': '8', 
        },

        {
            'id':5,
              'titulo': 'Engenhraria de dados', 
              'local': 'Pemba',
              'salario': '45000 mt',
                'cantidados': '3', 
            },
    {
        'id':6,
          'titulo': 'Engenhraria de softwere', 
          'local': 'Sofala',
          'salario': '55000 mt',
            'cantidados': '9', 
        }  
]



@app.route("/")
def home():
    vagas=VAGA
    return render_template("home.html", vagas=vagas)

@app.route("/vagas")
def lista_vagas():
    return jsonify(VAGA)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
