# Nível 2 — Regras de Firewall

## Objetivo
Criar regras de controle de tráfego no OPNsense, entendendo
como o firewall decide o que bloquear e o que permitir.

## Regras criadas
- Block ICMP (ping) — bloqueia pacotes ICMP saindo da LAN

## Prints
- `prints/opn-rules.png` → Regras da interface LAN
- `prints/opn-ping-icmprule.png` → Teste de ping via Diagnostics
- `prints/opn-log-ping.png` → Log do firewall

## O que eu aprendi
As regras de firewall são processadas de cima pra baixo,
 a primeira regra que bater no tráfego é a que vale.

Aprendi também que regras da LAN controlam tráfego originado
dentro da rede interna. Em um ambiente de lab com recursos
limitados, sem uma VM cliente separada na LAN, os testes
foram validados via logs e diagnósticos do próprio OPNsense.

Isso me mostrou que entender o escopo de cada regra
(em qual interface ela atua e em qual direção) é fundamental
para configurar um firewall corretamente.
