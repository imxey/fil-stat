from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    total = None
    input1_value = None
    input2_value = None
    input3_value = None
    input4_value = None
    input5_value = None
    input6_value = None
    if request.method == 'POST':
        input1_value = int(request.form['input1'])
        input2_value = int(request.form['input2'])
        input3_value = int(request.form['input3'])
        input4_value = int(request.form['input4'])
        input5_value = int(request.form['input5'])
        input6_value = int(request.form['input6'])
        metal = input1_value/1800/4*40000
        cloth = input2_value/1500/4*40000
        beast = input3_value/1400/4*40000
        wood = input4_value/1200/4*40000
        medicine = input5_value/880/4*25000
        mana = input6_value/900/4*120000
        total = metal + cloth + beast + wood + medicine + mana + 500000
        formatted_x = "{:,}".format(total)


    return render_template('index.html', total=formatted_x)

if __name__ == '__main__':
    app.run(debug=True)
