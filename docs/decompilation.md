# Decompilação

## Estado

O APK original contém múltiplos DEX e código Kotlin/Jetpack Compose. A análise inicial identificou sete arquivos DEX e componentes como `MainActivity`, `BriefScreen`, widgets e serviços de atualização.

## Ferramenta recomendada

Usamos **JADX 1.5.6 ou superior** para obter uma visão de alto nível do código Java/Kotlin descompilado. A versão 1.5.6 é a versão estável atual utilizada neste projeto e inclui melhorias importantes no tratamento de Kotlin e no export de projetos.

## Execução local

Com o APK original disponível localmente:

```bash
./scripts/decompile-jadx.sh /caminho/Now.Brief.apk build/jadx
```

Ou, se o executável não estiver no `PATH`:

```bash
JADX_BIN=/caminho/jadx ./scripts/decompile-jadx.sh /caminho/Now.Brief.apk build/jadx
```

## O que procurar primeiro

1. `com.example.nowbrief.MainActivity`
2. `BriefScreen`
3. telas de configurações/personalização
4. componentes relacionados a notícias e clima
5. widgets Compact, Headline e Wide
6. `NowBriefLiveUpdateService`
7. chamadas que constroem `Text(...)` no Jetpack Compose
8. strings que correspondam a `localization/pt-BR.csv`

## Regra de tradução

Não traduzir nomes de classes, métodos, chaves internas, URLs, identificadores de recursos ou textos pertencentes a bibliotecas. Primeiro localizar o ponto em que a string chega à UI; depois criar uma substituição mínima e testável.

## Observação de segurança

O APK original não é armazenado no repositório. O projeto mantém scripts, documentação, mapas de tradução e alterações necessárias para reproduzir o trabalho sem redistribuir o binário original.
