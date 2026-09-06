# Now Brief PT-BR

Projeto comunitário de pesquisa, localização e modificação do aplicativo **Now Brief** para português do Brasil.

> ⚠️ Este repositório não distribui o APK original. O trabalho parte de uma cópia legítima do APK obtida pelo próprio usuário e mantém as alterações como código, recursos, patches e documentação sempre que possível.

## Objetivos

- 🔎 Mapear a estrutura interna do APK
- 🇧🇷 Preparar uma localização pt-BR
- 🧩 Entender os componentes e recursos do aplicativo
- 🛠️ Desenvolver modificações e melhorias
- 📦 Automatizar desmontagem, reconstrução e assinatura de versões de teste
- 📝 Documentar cada alteração para facilitar reprodução e manutenção

## Estado atual

**Fase 1 — análise do APK**

- [x] APK de referência obtido
- [x] Inventário inicial dos arquivos
- [x] Identificação do package name
- [x] Identificação dos componentes principais no Manifest
- [x] Identificação dos DEX e bibliotecas nativas
- [ ] Descompilação completa
- [ ] Mapeamento das strings da aplicação
- [ ] Mapeamento das telas e fluxos
- [ ] Ambiente reproduzível de build
- [ ] Primeira tradução pt-BR
- [ ] Primeira versão modificada
- [ ] Testes em dispositivo

## Estrutura

```text
.
├── README.md
├── .gitignore
├── docs/
│   ├── analysis.md
│   └── changelog.md
├── patches/
│   ├── translation/
│   └── modifications/
├── resources/
│   └── pt-BR/
└── scripts/
    ├── decompile.sh
    ├── build.sh
    └── sign.sh
```

## APK analisado

A análise inicial encontrou:

- Package: `com.example.nowbrief`
- 7 arquivos DEX (`classes.dex` até `classes7.dex`, com a numeração presente no APK)
- `resources.arsc`
- 76 entradas em `assets/`
- bibliotecas nativas para `armeabi-v7a`, `arm64-v8a`, `x86` e `x86_64`
- recursos de clima em JSON
- fontes `OneUISans-Regular.ttf` e `OneUISans-Medium.ttf`
- áudios `jarvis_*`
- widgets Compact, Headline e Wide
- implementação baseada em Jetpack Compose/Material

## Licença e direitos

O aplicativo e seus componentes originais pertencem aos respectivos detentores de direitos. Este projeto é destinado a pesquisa, localização e desenvolvimento de modificações sobre uma cópia obtida legalmente. Não reivindicamos propriedade sobre código, marcas, imagens, áudios ou outros recursos originais do aplicativo.
