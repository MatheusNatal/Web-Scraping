import requests
from bs4 import BeautifulSoup
from time import sleep

def extract_elements(resposta, elemento_selecionado):
    soupe = BeautifulSoup(resposta.text, 'html.parser')
    elementos_encontrados = soupe.find_all(elemento_selecionado)
    return elementos_encontrados

def main():
    while True:
        url = input('Digite a URL do site (ou "sair" para encerrar): ')

        if url.lower() == "sair":
            break

        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            sleep(0.7)
            
            print('''Opções de elementos:
                    1) Links
                    2) Botões
                    3) Textos e Conteúdo
                    4) Imagens e Mídia''')
            
            elementos = {
                1: ('a', 'link'),
                2: 'button',
                3: ('h1', 'h2', 'h3', 'p'),
                4: ('img', 'video')
            }
            
            try:
                opcao = int(input('Escolha uma opção: '))
                elemento_selecionado = elementos.get(opcao)
                
                if elemento_selecionado:
                    elementos_encontrados = extract_elements(resposta, elemento_selecionado)
                    
                    if elementos_encontrados:
                        for elemento in elementos_encontrados:
                            print(elemento)
                    else:
                        print("Nenhum elemento encontrado.")
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        else:
            print(f"Erro ao acessar o site. Código de status: {resposta.status_code}")

if __name__ == "__main__":
    main()
