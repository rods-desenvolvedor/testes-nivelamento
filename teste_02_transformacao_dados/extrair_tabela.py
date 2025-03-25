import pdfplumber
import pandas as pd
import os
import zipfile

CAMINHO_PDF = "teste_01_web_scraping/anexos/Anexo_I.pdf"
CSV_SAIDA = "teste_02_transformacao_dados/saida/tabela_extraida.csv"
ZIP_SAIDA = "teste_02_transformacao_dados/saida/Teste_Rodolfo.zip"



PASTA_SAIDA = "teste_02_transformacao_dados/saida"

print("Conferindo pasta de saida...")


if os.path.exists(PASTA_SAIDA):
    for arquivo in os.listdir(PASTA_SAIDA):
        caminho = os.path.join(PASTA_SAIDA, arquivo)
        os.remove(caminho)
    print(f"Pasta '{PASTA_SAIDA}' limpa.")
else:
    os.makedirs(PASTA_SAIDA)
    print("Pasta de saida criada!!")


linhas = []

print("Abrindo o PDF...")

with pdfplumber.open(CAMINHO_PDF) as pdf:
    for pagina in pdf.pages:
        tabelas = pagina.extract_tables()
        for tabela in tabelas:
            for linha in tabela:
                linhas.append(linha)


linhas = [linha for linha in linhas if any(campo for campo in linha)]


df = pd.DataFrame(linhas[1:], columns=linhas[0])


df.replace({
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}, inplace=True)


df.to_csv(CSV_SAIDA, index=False, encoding="utf-8-sig")
print(f"CSV salvo em: {CSV_SAIDA}")


with zipfile.ZipFile(ZIP_SAIDA, "w") as zipf:
    zipf.write(CSV_SAIDA, arcname=os.path.basename(CSV_SAIDA))

print(f"Arquivo zip criado em: {ZIP_SAIDA}")
