import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile


URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"


PASTA_ANEXOS = "teste_01_web_scraping/anexos"

os.makedirs(PASTA_ANEXOS, exist_ok=True)


def baixar_pdf(url_pdf, nome_arquivo):
    print(f"Baixando: {nome_arquivo}")
    resposta = requests.get(url_pdf, stream=True)
    print(f"a resposta da requisição é : {resposta}")
    caminho = os.path.join(PASTA_ANEXOS, nome_arquivo)
    with open(caminho, "wb") as f:
        f.write(resposta.content)
    print(f"Salvo em: {caminho}")
    return caminho


print(f"Acessando {URL}...")
resposta = requests.get(URL)
soup = BeautifulSoup(resposta.content, "html.parser")


links_pdf = soup.find_all("a", href=True)


pdfs_encontrados = {}

for link in links_pdf:
    texto = link.get_text(strip=True)
    href = link["href"]
    if any(nome in texto for nome in ["Anexo I", "Anexo II"]) and href.endswith(".pdf"):
        for nome in ["Anexo I", "Anexo II"]:
            if nome in texto:
                url_completa = href if href.startswith("http") else f"https://www.gov.br{href}"
                pdfs_encontrados[nome] = url_completa


arquivos_salvos = []

for nome, url in pdfs_encontrados.items():
    nome_arquivo = f"{nome.replace(' ', '_')}.pdf"
    caminho = baixar_pdf(url, nome_arquivo)
    arquivos_salvos.append(caminho)
    print(arquivos_salvos)

ZIP_SAIDA = "teste_01_web_scraping/anexos.zip"
with ZipFile(ZIP_SAIDA, "w") as zipf:
    for caminho in arquivos_salvos:
        zipf.write(caminho, arcname=os.path.basename(caminho))

print(f"\n✅ Compactação finalizada. Arquivo criado: {ZIP_SAIDA}")
