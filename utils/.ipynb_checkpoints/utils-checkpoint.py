hello = 'hello world'


RC_FOLDER = '/mnt/c/Users/PLour/OneDrive - Universidade Federal de Minas Gerais/01_Estudos/Faculdade/RI/rc'
CORPUS = RC_FOLDER + '/corpus/corpus.jsonl'
INDEX_FOLDER = RC_FOLDER + '/index'

def file_nlines (file):
  with open(file, 'r') as corpus:
    for line, _ in enumerate(corpus):
      pass
    pass
  return line + 1