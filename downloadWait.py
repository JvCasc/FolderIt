import time
import os

def aguardar_conclusao(caminho_arquivo):
    tamanho_antigo = -1
    while True:
        try:
            tamanho_atual = os.path.getsize(caminho_arquivo)
            if tamanho_atual == tamanho_antigo:
                return True # O tamanho parou de mudar, download terminou
            tamanho_antigo = tamanho_atual
            time.sleep(1)
        except OSError:
            # Arquivo ainda pode estar inacessível
            return False