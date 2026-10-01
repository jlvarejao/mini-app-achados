from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "chave-secreta"

DATABASE = "achados.db"


def conectar():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def criar_banco():
    conn = conectar()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            nome TEXT NOT NULL,
            descricao TEXT NOT NULL,
            local TEXT NOT NULL,
            contato TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pendente'
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def index():
    filtro = request.args.get("filtro", "todos")
    busca = request.args.get("busca", "")

    conn = conectar()

    query = "SELECT * FROM itens WHERE 1=1"
    parametros = []

    if filtro in ["perdido", "encontrado"]:
        query += " AND tipo = ?"
        parametros.append(filtro)

    if busca:
        query += """
            AND (
                nome LIKE ?
                OR descricao LIKE ?
                OR local LIKE ?
            )
        """
        palavra = f"%{busca}%"
        parametros.extend([palavra, palavra, palavra])

    query += " ORDER BY id DESC"

    itens = conn.execute(query, parametros).fetchall()

    conn.close()

    return render_template(
        "index.html",
        itens=itens,
        filtro=filtro,
        busca=busca
    )


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        tipo = request.form["tipo"]
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        local = request.form["local"]
        contato = request.form["contato"]

        conn = conectar()

        conn.execute("""
            INSERT INTO itens
            (tipo, nome, descricao, local, contato)
            VALUES (?, ?, ?, ?, ?)
        """, (tipo, nome, descricao, local, contato))

        conn.commit()
        conn.close()

        flash("Item cadastrado com sucesso!")

        return redirect(url_for("index"))

    return render_template("cadastrar.html")


@app.route("/resolver/<int:id>")
def resolver(id):
    conn = conectar()

    conn.execute("""
        UPDATE itens
        SET status = 'Resolvido'
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    flash("Item marcado como resolvido!")

    return redirect(url_for("index"))


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)