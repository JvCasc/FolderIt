import mimetypes

# Pega a categoria do arquivo e a extensão dele
def filetype(file):
    mime, _ = mimetypes.guess_type(file)
    extensao_arquivo = mime.split("/")[0]
    extensao_expecifica = mime.split("/")[1]
    return extensao_arquivo, extensao_expecifica