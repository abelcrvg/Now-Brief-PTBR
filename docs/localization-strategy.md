# Estratégia de localização pt-BR

## O que já foi confirmado

A análise inicial do APK mostra que o aplicativo contém texto de interface diretamente nos DEX, além de recursos Android. Há evidências de Jetpack Compose/Kotlin e de uma concentração relevante da UI em `MainActivity.kt`.

Isso significa que a tradução não deve assumir que todos os textos estão em `res/values/strings.xml`. Parte do trabalho provavelmente será localizar strings embutidas no código/bytecode e, quando possível, convertê-las para recursos traduzíveis.

## Estratégia

1. **Mapear** todas as strings de usuário em inglês.
2. **Separar** strings do aplicativo das strings de bibliotecas Android/Compose.
3. **Classificar** cada string por tela/componente.
4. **Traduzir** para português do Brasil preservando placeholders, pontuação e capitalização quando relevantes.
5. **Priorizar** telas principais: Brief, Settings, Weather, News, Calendar, Contacts, Fitness e Sleep.
6. **Só depois** alterar comportamento ou aparência.
7. **Compilar e assinar** uma cópia modificada para testes locais.

## Regras de tradução

- `Brief` será tratado como **Resumo** quando representar o conteúdo apresentado ao usuário.
- `Briefing` será tratado como **Boletim** quando representar uma edição/notificação agendada.
- `Feed` será mantido como **Feed** quando representar uma lista contínua de conteúdo.
- `Check-in` será mantido quando tiver sentido de acompanhamento/status.
- Termos de Android, APIs, classes e nomes técnicos não devem ser traduzidos.
- Placeholders como `%s`, `%d`, `{name}` etc. devem permanecer exatamente iguais.

## Arquivos

- `localization/pt-BR.csv`: mapa inicial de traduções, ainda marcado para revisão.
- `scripts/extract_strings.sh`: extrator simples dos pools de strings dos DEX.

## Próxima etapa técnica

A próxima etapa é obter uma decodificação completa do APK com Apktool/JADX e cruzar os textos encontrados com os componentes `MainActivity`, widgets e recursos. A tradução final só deve ser marcada como concluída depois de recompilar e testar a instalação.
