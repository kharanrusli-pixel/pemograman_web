from flask import Flask, render_template, url_for

app = Flask(__name__)

# Data untuk dikirim ke HTML
data = {
    "nama": "KHARAN RUSLI",
    "ringkasan": "Biodata : saya mahasiswa unidayan (Universitas Dayanu Ikhsanuddin).",
    "minat": "Coding, Artificial Intelligence, Web Development dan desain proyek.",
    "foto_url": "kharan.jpeg", 
    "pendidikan": [
        {"tahun": "2012 - 2019", "instansi": "MIN 1 BUTON"},
        {"tahun": "2019 - 2021", "instansi": "MTsN 1 Buton"},
        {"tahun": "2021 - 2024", "instansi": "MAN 1 BUTON"},
        {"tahun": "2024 - Sekarang", "instansi": "Univ Dayanu Ikhsanuddin - TI"}
    ],
    "pengalaman": "Magang di wabula sport, menjual barang barang di pasar dan organisasi Remasj Laburunci",
    "kontak": {"email": "kharanrusli@gmail.com"}
}

@app.route('/')
@app.route('/beranda')
def beranda():
    return render_template('beranda.html', profil=data)

@app.route('/tentang')
def tentang():
    return render_template('tentang.html', profil=data)

@app.route('/pendidikan')
def pendidikan():
    return render_template('pendidikan.html', profil=data)

@app.route('/pengalaman')
def pengalaman():
    return render_template('pengalaman.html', profil=data)

@app.route('/kontak')
def kontak():
    return render_template('kontak.html', profil=data)

if __name__ == '__main__':
    app.run(debug=True)