from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)


df = pd.read_csv("teste_03_banco_de_dados/dados/Relatorio_cadop.csv", sep=";", encoding="latin1")
df = df.apply(lambda col: col.str.encode('latin1').str.decode('utf-8') if col.dtype == 'object' else col)


df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")

df = df.astype(str).apply(lambda col: col.str.upper())

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("query", "").strip().upper()

    if not termo:
        resposta = df.head(100).to_dict(orient="records")
        return jsonify(resposta)

    
    resultados = df[df["REGISTRO_ANS"] == termo]

    if resultados.empty:
        resultados = df[
            df["RAZAO_SOCIAL"].str.contains(termo, na=False) |
            df["NOME_FANTASIA"].str.contains(termo, na=False)
        ]

    resposta = resultados.to_dict(orient="records")  # 🔄 remove head(10) aqui
    return jsonify(resposta)

if __name__ == "__main__":
    app.run(debug=True)
