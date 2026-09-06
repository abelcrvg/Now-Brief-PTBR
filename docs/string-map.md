# Mapa de strings por tela — pt-BR

Esta etapa cruza os literais observados no `classes3.dex` com os métodos principais de `MainActivityKt`. A análise foi feita em nível DEX; strings de bibliotecas Compose/Android e dados auxiliares são tratadas como não traduzíveis até confirmação.

## 1. BriefScreen

**Método:** `com.example.nowbrief.MainActivityKt.BriefScreen`  
**Origem indicada no DEX:** `MainActivity.kt:3463`

Strings associadas diretamente ao método:

| English | pt-BR | Status |
|---|---|---|
| Traffic updates | Atualizações do trânsito | confirmar |
| Routine | Rotina | confirmar |
| Health and wellness | Saúde e bem-estar | confirmar |
| Events and tasks | Eventos e tarefas | confirmar |
| Daily activity | Atividade diária | confirmar |
| Here's how you're tracking today. | Veja como você está hoje. | confirmar |
| Alarms | Alarmes | confirmar |
| Travel | Viagens | confirmar |
| Digital Wellbeing | Bem-estar digital | confirmar |
| Here's your connected briefing. | Aqui está seu boletim conectado. | confirmar |
| News | Notícias | confirmada |
| Moments | Momentos | confirmar |
| Smart home | Casa inteligente | confirmar |
| Info | Informações | confirmar |
| Settings | Configurações | confirmar |
| Audio brief | Resumo em áudio | confirmada |

Há também referências de ambiente Compose e nomes internos de estado; esses itens não devem ser traduzidos.

## 2. SettingsScreen

**Método:** `com.example.nowbrief.MainActivityKt.SettingsScreen`  
**Região de origem:** `MainActivity.kt:5107`–`5288`

O método recebe callbacks para áudio, conteúdo, personalização, opções de desenvolvedor e navegação. O vocabulário prioritário é:

| English | pt-BR | Status |
|---|---|---|
| Customize Now Brief | Personalizar o Now Brief | confirmada |
| Audio brief | Resumo em áudio | confirmada |
| Schedule | Programação | confirmada |
| Edit schedule | Editar programação | confirmada |
| Dark mode for settings | Modo escuro das configurações | candidata |
| Compact widget | Widget compacto | candidata |
| Large Home widget | Widget grande da tela inicial | candidata |
| Compact Home widget | Widget compacto da tela inicial | candidata |
| Lock-style pill widget | Widget em formato de cápsula para a tela de bloqueio | candidata |
| Always show lockscreen widget | Sempre mostrar o widget na tela de bloqueio | candidata |
| Weather-reactive backgrounds | Planos de fundo reativos ao clima | candidata |
| Weather always first | O clima sempre primeiro | candidata |
| Memories and News above Weather | Memórias e Notícias acima do Clima | candidata |

## 3. AudioBriefSettingsScreen

**Método:** `com.example.nowbrief.MainActivityKt.AudioBriefSettingsScreen`  
**Origem indicada no DEX:** `MainActivity.kt:5478`

Estado observado no método:

- `selectedVoice`
- `onEnabledChange`
- `onVoiceChange`
- `onBack`

Strings de trabalho:

| English | pt-BR | Status |
|---|---|---|
| Audio brief | Resumo em áudio | confirmada |
| Voice | Voz | candidata |
| Enable audio brief | Ativar resumo em áudio | candidata |
| Voice style | Estilo de voz | candidata |

Os três últimos itens precisam ser validados após reconstrução/decompilação.

## 4. ContentScreen

**Método:** `com.example.nowbrief.MainActivityKt.ContentScreen`  
**Origem indicada no DEX:** `MainActivity.kt:5320`

Callbacks observados:

- `items`
- `onToggleChange`
- `onBack`
- `onOpenPersonalization`

Categorias de conteúdo já identificadas:

| English | pt-BR |
|---|---|
| News | Notícias |
| Traffic updates | Atualizações do trânsito |
| Routine | Rotina |
| Health and wellness | Saúde e bem-estar |
| Events and tasks | Eventos e tarefas |
| Daily activity | Atividade diária |
| Alarms | Alarmes |
| Travel | Viagens |
| Digital Wellbeing | Bem-estar digital |
| Smart home | Casa inteligente |
| Moments | Momentos |

## 5. NewsCard

**Método:** `com.example.nowbrief.MainActivityKt.NewsCard`  
**Origem indicada no DEX:** `MainActivity.kt:9360`

O método principal tem poucas referências textuais diretas; a UI de notícias usa lambdas/componentes Compose auxiliares. Portanto, a análise deve continuar pelos métodos gerados associados ao `NewsCard`.

| English | pt-BR | Status |
|---|---|---|
| News | Notícias | confirmada |
| Here's some news you may be interested in. | Aqui estão algumas notícias que podem interessar a você. | candidata |

## 6. WeatherCard

**Método:** `com.example.nowbrief.MainActivityKt.WeatherCard`  
**Origem indicada no DEX:** `MainActivity.kt:4171`

O método referencia diretamente o estado `weather`. A produção de texto meteorológico passa por funções auxiliares:

- `weatherCodeToLabel`
- `weatherGlyphForCode`
- `weatherGlyphForSummary`
- `weatherIconAssetName`
- `normalizeWeatherLocation`
- `fetchLiveWeatherUi`
- `fetchOpenMeteoWeatherUi`
- `fetchWeatherApiWeatherUi`

| English | pt-BR | Status |
|---|---|---|
| Current weather | Clima atual | confirmada |
| Your Location | Sua localização | candidata |
| Refreshing weather | Atualizando o clima | candidata |
| Here's your weather update. | Aqui está sua atualização do clima. | candidata |
| Clear tonight | Céu limpo esta noite | candidata |

## 7. PermissionIntroDialog

**Método:** `com.example.nowbrief.MainActivityKt.PermissionIntroDialog`  
**Origem indicada no DEX:** `MainActivity.kt:4668`

Callbacks observados: `onDismiss` e `onAllowAll`.

| English | pt-BR | Status |
|---|---|---|
| Allow all | Permitir tudo | candidata |
| Don't allow | Não permitir | candidata |
| Allow Now Brief to send you notifications? | Permitir que o Now Brief envie notificações? | candidata |
| Allow Now Brief to access your calendar? | Permitir que o Now Brief acesse seu calendário? | candidata |
| Allow Now Brief to access your contacts? | Permitir que o Now Brief acesse seus contatos? | candidata |
| Allow Now Brief to access your photos? | Permitir que o Now Brief acesse suas fotos? | candidata |
| Allow Now Brief to access smart home devices? | Permitir que o Now Brief acesse dispositivos de casa inteligente? | candidata |
| Allow Now Brief to access usage data? | Permitir que o Now Brief acesse dados de uso? | candidata |
| Allow Health Connect | Permitir o Health Connect | candidata |

**Atenção:** caixas de diálogo de permissão nativas do Android podem ignorar essas strings e usar a localização do próprio sistema.

## 8. Notificações

### `notificationBody`

String diretamente encontrada:

| English | pt-BR |
|---|---|
| Tap to see what's new in your briefing. | Toque para ver o que há de novo no seu boletim. |

### `notificationTitleFor`

A análise inicial não encontrou literal textual direto neste método. Os títulos parecem ser derivados por lógica/constantes ou métodos auxiliares.

Títulos encontrados no conjunto geral do DEX:

| English | pt-BR |
|---|---|
| Now brief is ready | O Now Brief está pronto |
| Your briefing is ready | Seu boletim está pronto |
| Last briefing available | Último boletim disponível |
| Now Brief available | Now Brief disponível |
| Now Brief Is Ready To View | O Now Brief está pronto para visualização |
| Now Brief Ready To View! | Now Brief pronto para visualização! |
| Evening Brief Is Ready To View | O resumo da noite está pronto para visualização |
| Midday briefing available | Boletim do meio-dia disponível |
| Evening summary available | Resumo da noite disponível |
| Your morning briefing is ready | Seu boletim da manhã está pronto |
| Your Late Night Brief Is Ready To View | Seu boletim da madrugada está pronto para visualização |
| Your Evening Brief Is Ready To View! | Seu resumo da noite está pronto para visualização! |
| Good Morning, Now Brief Is Ready To View | Bom dia, o Now Brief está pronto para visualização |
| Early Riser! Your Now Brief Is Ready To View | Cedo! Seu Now Brief está pronto para visualização |

## 9. Períodos do dia

| English | pt-BR |
|---|---|
| Good morning | Bom dia |
| Good afternoon | Boa tarde |
| Good evening | Boa noite |
| Morning | Manhã |
| Morning Brief | Resumo da manhã |
| Morning briefing | Boletim da manhã |
| Morning check-in | Check-in da manhã |
| Morning feed | Feed da manhã |
| Morning overview | Visão geral da manhã |
| Morning report | Relatório da manhã |
| Morning status | Status da manhã |
| Morning summary | Resumo da manhã |
| Morning update | Atualização da manhã |
| Midday brief | Resumo do meio-dia |
| Midday briefing available | Boletim do meio-dia disponível |
| Afternoon Brief | Resumo da tarde |
| Afternoon briefing | Boletim da tarde |
| Afternoon check-in | Check-in da tarde |
| Afternoon feed | Feed da tarde |
| Afternoon overview | Visão geral da tarde |
| Afternoon report | Relatório da tarde |
| Afternoon status | Status da tarde |
| Afternoon summary | Resumo da tarde |
| Afternoon update | Atualização da tarde |
| Evening Brief | Resumo da noite |
| Evening briefing | Boletim da noite |
| Evening check-in | Check-in da noite |
| Evening feed | Feed da noite |
| Evening overview | Visão geral da noite |
| Evening report | Relatório da noite |
| Evening status | Status da noite |
| Evening summary | Resumo da noite |
| Evening update | Atualização da noite |
| Late night | De madrugada |
| Late night briefing | Boletim da madrugada |
| Late night recap | Resumo da madrugada |
| Late night update | Atualização da madrugada |
| Night briefing | Boletim da noite |
| Night check-in | Check-in da noite |
| Night summary | Resumo da noite |

## 10. Onboarding e mensagens gerais

| English | pt-BR |
|---|---|
| Welcome To Your New Now Briefing | Bem-vindo ao seu novo Now Brief |
| You Now Brief Has Been Generated | Seu Now Brief foi gerado |
| Learn about your Now brief. | Saiba mais sobre o Now Brief. |
| Stay up to date with Now brief | Mantenha-se atualizado com o Now Brief |
| Start your day with this briefing. | Comece seu dia com este boletim. |
| Your morning briefing is ready | Seu boletim da manhã está pronto |
| Enjoy a peaceful and restful night. | Tenha uma noite tranquila e revigorante. |
| Nothing Scheduled, Enjoy Your Free Time! | Nada programado. Aproveite seu tempo livre! |
| Here's your connected brief. | Aqui está seu boletim conectado. |
| Here's your connected briefing. | Aqui está seu boletim conectado. |
| Open your latest morning update. | Abra sua atualização mais recente da manhã. |
| Open your evening summary and suggestions. | Abra seu resumo e suas sugestões da noite. |
| Here's what tomorrow is already shaping into. | Veja como o dia de amanhã já está se desenhando. |
| Briefing unavailable. | Boletim indisponível. |

## 11. Sono e energia

| English | pt-BR |
|---|---|
| Sleep | Sono |
| Sleep soon | Hora de dormir |
| Almost sleep | Quase na hora de dormir |
| Rest mode | Modo de descanso |
| Sleep mode | Modo de sono |
| Sleep graph | Gráfico do sono |
| Sleep score | Pontuação do sono |
| Energy mascot | Mascote de energia |
| Energy score | Pontuação de energia |
| Calories goal | Meta de calorias |
| Fitness goals | Metas de atividade física |
| Daily activity goals | Metas diárias de atividade |
| Protect your energy | Proteja sua energia |
| Save energy while away | Economize energia enquanto estiver fora |

## 12. Regras para a implementação

1. Traduzir primeiro strings controladas pelo aplicativo.
2. Não alterar strings de bibliotecas Compose/Android sem evidência de que são da UI do app.
3. Preservar placeholders, URLs, nomes de APIs, classes e identificadores.
4. Manter `Now Brief` como nome do produto.
5. Separar textos próprios do aplicativo de diálogos nativos do Android.
6. Após a decompilação, registrar para cada string a origem: `resources`, `DEX literal`, `Android framework` ou `dependência`.
7. A substituição definitiva só deve ocorrer depois que o APK puder ser reconstruído e instalado para validação.

## 13. Próximo alvo

Rastrear os lambdas gerados por Compose associados a `BriefScreen`, `SettingsScreen`, `NewsCard` e `WeatherCard`. Esses métodos auxiliares devem revelar os textos que não aparecem diretamente no método principal e permitir uma tradução muito mais completa sem substituir código de terceiros.