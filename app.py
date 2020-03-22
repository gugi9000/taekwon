from flask import Flask, redirect, render_template
import poomsae

app = Flask(__name__)


@app.route('/poom')
@app.route('/poom/<int:max_poomsae>')
def show_poomsae(max_poomsae=8):
    poomsae_list = poomsae.poomsae_list
    if max_poomsae > len(poomsae_list):
        max_poomsae = len(poomsae_list)
    selected = poomsae.random_poomsae_list(max_poomsae)
    print(selected)
    total_moves = sum([poomsae[2] for poomsae in selected])
    return render_template('index.html', poomsae_list=poomsae_list, random_list=selected, total_moves=total_moves)


@app.route('/')
def index():

    return render_template('index.html', poomsae_list=poomsae.poomsae_list)


if __name__ == '__main__':
    app.run(port=5002, debug=True)
