from datetime import datetime

def CalcularHoras(string_original):
    # Dividir a string usando "h" como delimitador
    partes = string_original.split("h")
    parte1 = partes[0].strip()  # "05:29"
    parte2 = partes[1].strip()  # "18:41"
    hora_inicio = datetime.strptime(parte1, "%H:%M")
    hora_fim = datetime.strptime(parte2, "%H:%M")
    diferenca = hora_fim - hora_inicio
    horas = diferenca.seconds // 3600
    return horas
