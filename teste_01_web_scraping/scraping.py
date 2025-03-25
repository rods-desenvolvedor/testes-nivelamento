import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile


URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

NOMES_ANEXOS = ["Anexo I", "Anexo II"]


PASTA_ANEXOS = "teste_01_web_scraping/anexos"
ZIP_SAIDA = "teste_01_web_scraping/anexos.zip"


os.makedirs(PASTA_ANEXOS, exist_ok=True)

if os.path.exists(ZIP_SAIDA):  # Para facilitar a visualização do programa rodando, 
    os.remove(ZIP_SAIDA)       # vou apagar o arquivo zip gerado na ultima execução do programa 
    print(f"Arquivo zip anterior removido: {ZIP_SAIDA}")


for arquivo in os.listdir(PASTA_ANEXOS):
    caminho_arquivo = os.path.join(PASTA_ANEXOS, arquivo)  # Para facilitar a visualização do programa rodando,
    os.remove(caminho_arquivo)                             # vou limpar a pasta anexos gerada na ultima execução do programa 

print(f"Pasta '{PASTA_ANEXOS}' limpa.")

def baixar_pdf(url_pdf, nome_arquivo):

    print(f"Baixando: {nome_arquivo}")
    try:
        resposta = requests.get(url_pdf, stream=True)
        resposta.raise_for_status()
        caminho = os.path.join(PASTA_ANEXOS, nome_arquivo)
        with open(caminho, "wb") as f:
            f.write(resposta.content)
        print(f"Arquivo salvo em: {caminho}")
        return caminho
    except Exception as e:
        print(f"Erro ao baixar {nome_arquivo}: {e}")
        return None

def main():
    print(f"Acessando {URL}...")
    resposta = requests.get(URL)
    
    if resposta.status_code != 200:
        print(f"Erro ao acessar a página. Status: {resposta.status_code}")
        return
    
    soup = BeautifulSoup(resposta.content, "html.parser")

    print("Buscando links dos anexos...")
    links_pdf = soup.find_all("a", href=True)

    pdfs_encontrados = {}

    for link in links_pdf:
        texto = link.get_text(strip=True)
        href = link["href"]
        if any(nome in texto for nome in NOMES_ANEXOS) and href.endswith(".pdf"):
            for nome in NOMES_ANEXOS:
                if nome in texto:
                    url_completa = href if href.startswith("http") else f"https://www.gov.br{href}"
                    pdfs_encontrados[nome] = url_completa

    if not pdfs_encontrados:
        print("Nenhum anexo foi encontrado.")
        return
    elif len(pdfs_encontrados) < len(NOMES_ANEXOS):
        print("Apenas parte dos anexos foi encontrada:")
        for nome in pdfs_encontrados:
            print(f"- {nome}")

    arquivos_salvos = []

    for nome, url in pdfs_encontrados.items():
        nome_arquivo = f"{nome.replace(' ', '_')}.pdf"
        caminho = baixar_pdf(url, nome_arquivo)
        if caminho and os.path.getsize(caminho) > 0:
            arquivos_salvos.append(caminho)
        else:
            print(f"O arquivo {nome_arquivo} está vazio ou não foi baixado corretamente.")

    if not arquivos_salvos:
        print("Nenhum arquivo foi salvo. Cancelando compactação.")
        return

    with ZipFile(ZIP_SAIDA, "w") as zipf:
        for caminho in arquivos_salvos:
            zipf.write(caminho, arcname=os.path.basename(caminho))

    print(f"\nCompactação finalizada. Arquivo criado foi salvo em: {ZIP_SAIDA}")

if __name__ == "__main__":
    main()
