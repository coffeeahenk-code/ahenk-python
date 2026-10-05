from flask import Flask, request
from veritabani import get_connection

app = Flask(__name__)


@app.route("/saglik-durumu")
def saglik_durumu():
    return {
        "durum": "ok",
        "mesaj": "Ahenk API çalışıyor!"
    }


@app.route("/kahve-kaydet", methods=["POST"])
def kahve_kaydet():
    data = request.get_json()

    name = data.get("name")
    country = data.get("country")
    description = data.get("description")
    price = data.get("price")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO coffee_products
        (name, country, description, price)
        VALUES (?, ?, ?, ?)
        """,
        (name, country, description, price)
    )

    connection.commit()
    connection.close()

    return {
        "durum": "ok",
        "mesaj": "Kahve başarıyla kaydedildi!"
    }


if __name__ == "__main__":
    app.run(debug=True)