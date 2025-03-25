from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


df = pd.read_csv("teste_03_banco_de_dados/dados/Relatorio_cadop.csv", sep=";", encoding="latin1")


df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")

df = df.astype(str).apply(lambda col: col.str.upper())

@app.route("/buscar", methods=["GET"])
def buscar():
    termo = request.args.get("query", "").strip().upper()

    if not termo:
        return jsonify({"erro": "Parâmetro 'query' é obrigatório."}), 400


    if "RAZAO_SOCIAL" not in df.columns or "NOME_FANTASIA" not in df.columns:
        return jsonify({"erro": "Colunas necessárias não encontradas no CSV."}), 500


    resultados = df[
        df["RAZAO_SOCIAL"].str.contains(termo, na=False) |
        df["NOME_FANTASIA"].str.contains(termo, na=False)
    ]

    resposta = resultados.head(10).to_dict(orient="records")
    return jsonify(resposta)

if __name__ == "__main__":
    app.run(debug=True)
