from flask import Flask, render_template, request, redirect, url_for, session, abort, flash

app = Flask(__name__)
app.secret_key = "secret123"

users = [
    {"id": 1,"username":"kharan", "password":"1234", "role":"admin"},
    {"id": 2,"username":"budi", "password":"1234", "role":"mahasiswa"},
    {"id": 3,"username":"Mr.Andi", "password":"1234", "role":"dosen"}
]

@app.route("/")
def home():
    return render_template(
        "home.html",
        users=users,
        current_user=session.get("username")
    )

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    for u in users:
        if u["username"] == username:
            flash("Username sudah dipakai")
            return redirect("/")
    role = request.form["role"]
    users.append({
        "id": len(users) + 1,
        "username": username,
        "password": password,
        "role": role
    })

    return redirect("/")

@app.route("/delete/<int:user_id>")
def delete(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return redirect("/")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_aktif' in session:
        role = session.get('role')
        if role == 'mahasiswa':
            return redirect(url_for('dashboard_mahasiswa'))
        elif role == 'admin':
            return redirect(url_for('dashboard_admin'))
        elif role == 'dosen':
            return redirect(url_for('dashboard_dosen'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        for user in users:
            if user['username'] == username and user['password'] == password:
                session['user_aktif'] = username
                session['role'] = user['role']
                
                if user['role'] == 'mahasiswa':
                    return redirect(url_for('dashboard_mahasiswa'))
                elif user['role'] == 'admin':
                    return redirect(url_for('dashboard_admin'))
                elif user['role'] == 'dosen':
                    return redirect(url_for('dashboard_dosen'))
        
        return "Login Gagal! Username atau Password salah."
    
    return render_template('index2.html')

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard/admin")
def dashboard_admin():
    if session.get("role") != "admin":
        abort(403)
    return render_template("dashboard_admin.html",
        current_user=session.get("username")
    )

@app.route("/dashboard/dosen")
def dashboard_dosen():
    if session.get("role") != "dosen":
        abort(403)
    return render_template("dashboard_dosen.html",
        current_user=session.get("username")
    )

@app.route("/dashboard/mahasiswa")
def dashboard_mahasiswa():
    if session.get("role") != "mahasiswa":
        abort(403)
    return render_template("dashboard_mahasiswa.html",
        current_user=session.get("username")
    )

if __name__ == "__main__":
    app.run(debug=True)
