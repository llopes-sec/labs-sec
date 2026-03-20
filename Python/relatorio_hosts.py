import os
import datetime

hosts = ["192.168.0.1", "192.168.0.2"]
relatorio = []

for host in hosts:
    response = os.system(f"ping -n 1 {host}")
    if response == 0:
        relatorio.append(f"{host} está ativo")
    else:
        relatorio.append(f"{host} não respondeu")

with open(f"relatorio_{datetime.date.today()}.txt", "w") as f:
    for linha in relatorio:
        f.write(linha + "\n")

print("Relatório gerado!")
