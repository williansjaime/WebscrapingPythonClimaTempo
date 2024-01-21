from datetime import datetime

# String original
string_original = "05:29h18:41h"

# Dividir a string usando "h" como delimitador
partes = string_original.split("h")

# Obter as duas partes
parte1 = partes[0].strip()  # "05:29"
parte2 = partes[1].strip()  # "18:41"

print("Parte 1:", parte1)
print("Parte 2:", parte2)

# Horas de início e fim
hora_inicio_str = "05:29"
hora_fim_str = "18:41"

# Criar objetos datetime para as duas horas
hora_inicio = datetime.strptime(hora_inicio_str, "%H:%M")
hora_fim = datetime.strptime(hora_fim_str, "%H:%M")

# Calcular a diferença
diferenca = hora_fim - hora_inicio

# Extrair horas e minutos da diferença
horas = diferenca.seconds // 3600
minutos = (diferenca.seconds % 3600) // 60

print(f"A diferença é de {horas} horas e {minutos} minutos.")