def criaCodigo(e):
    e.sort(key=ordena)
    codigo = []
    for x in e:
        code = x['tipo']
        if code == "print":
            codigo.append('print('+x['valor']+')\n')
        elif code == "for" or code == "if" or code == "while" or code == "elif":
            codigo.append(code+' ('+x['valor']+'):\n')
        elif code == "true":
            codigo.append('else:\n')
        elif code == "var":
            codigo.append(x['valor']+' = entrada\n')

    arquivoCodigo = open("codigoMissao1.py", "w")
    for linha in codigo:
        arquivoCodigo.write(linha)
    return codigo

def ordena(e):
  return e['index']