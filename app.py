from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    total = 0
    input1_value = 0
    input2_value = 0
    input3_value = 0
    input4_value = 0
    input5_value = 0
    input6_value = 0
    formatted_x = 0
    metal_mats = 0
    cloth_mats = 0
    beast_mats = 0
    wood_mats = 0
    medicine_mats = 0
    mana_mats = 0
    if request.method == 'POST':
        input1_value = int(request.form['input1'])
        input2_value = int(request.form['input2'])
        input3_value = int(request.form['input3'])
        input4_value = int(request.form['input4'])
        input5_value = int(request.form['input5'])
        input6_value = int(request.form['input6'])

        metal_mats = int(input1_value/1800)
        cloth_mats = int(input2_value/1500)
        beast_mats = int(input3_value/1400)
        wood_mats = int(input4_value/1200)
        medicine_mats = int(input5_value/880)
        mana_mats = int(input6_value/900)

        metal = metal_mats/4*40000
        cloth = cloth_mats/4*40000
        beast = beast_mats/4*40000
        wood = wood_mats/4*40000
        medicine = medicine_mats/4*25000
        mana = mana_mats/4*120000
        if request.method == 'POST':
            total = int(metal + cloth + beast + wood + medicine + mana + 500000)
            formatted_x = "{:,}".format(total)


    return render_template('index.html', total=formatted_x, metal_mats=metal_mats, cloth_mats=cloth_mats, mana_mats=mana_mats, beast_mats=beast_mats, wood_mats=wood_mats, medicine_mats=medicine_mats)

if __name__ == '__main__':
    app.run(debug=True)
