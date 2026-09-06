# Patching pt-BR

## Objetivo

Transformar o mapa de localização em uma etapa reproduzível de patch, sem armazenar o APK original no repositório.

## Fluxo

1. Obter uma cópia local do APK que você tem autorização para modificar.
2. Rodar `scripts/decompile.sh` com a ferramenta de engenharia reversa disponível.
3. Gerar um dump UTF-8 das strings efetivamente presentes no APK.
4. Rodar:

```bash
python3 scripts/patch_strings.py --strings build/strings.txt
```

5. Revisar `build/pt-BR-patch.json`.
6. Aplicar somente as entradas aprovadas usando o toolchain de APK/DEX escolhido.
7. Recompilar.
8. Assinar o APK com uma chave própria de teste.
9. Instalar em um dispositivo/emulador de teste e validar permissões, Compose, notificações, widgets, áudio e clima.

## Regra importante

`patch_strings.py` gera um **plano de patch**; ele não faz substituição cega de bytes. Isso evita corromper offsets/estruturas do DEX quando uma tradução tiver tamanho diferente da string original.

## Estado atual

O projeto já possui o mapa pt-BR e a análise por tela. A aplicação efetiva no DEX ainda depende de um toolchain de reconstrução (por exemplo, APK/DEX tooling) disponível no ambiente de build.
