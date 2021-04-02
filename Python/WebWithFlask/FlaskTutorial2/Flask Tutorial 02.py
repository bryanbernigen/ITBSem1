from flask import Flask, render_template, url_for
app = Flask(__name__)

data = [
    {
        'nama': 'Andi',
        'tanggal': '18 Jan 2018',
        'judul': 'AADCC',
        'konten': 'Ini konten 1'
    },
    {
        'nama': 'Budi',
        'umur': '19 April 2019',
        'judul': 'Gigi Berlubang',
        'konten': 'Ini konten berguna'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',data=data)

@app.route('/owner')
def about():
    return render_template('owner.html', title='Owner')

if __name__ == '__main__':
    app.run(debug=True)
