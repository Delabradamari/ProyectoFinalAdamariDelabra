from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_aguinaldo(salario_diario, meses_trabajados):
    aguinaldo_base = 15
    bono_antiguedad = 0.5

    sueldo_mensual = salario_diario * 30
    aguinaldo_total = (aguinaldo_base * sueldo_mensual) + (bono_antiguedad * meses_trabajados * sueldo_mensual)
    return aguinaldo_total

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            salario_diario = float(request.form['salario_diario'])
            meses_trabajados = int(request.form['meses_trabajados'])

            if salario_diario < 0 or meses_trabajados < 0:
                raise ValueError("El salario diario y la cantidad de meses no pueden ser negativos.")
            
            aguinaldo = calcular_aguinaldo(salario_diario, meses_trabajados)
            return render_template('resultado.html', aguinaldo=aguinaldo)
        except ValueError as e:
            error_message = f"Error: {e}. Por favor, ingresa valores válidos."
            return render_template('index.html', error_message=error_message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
