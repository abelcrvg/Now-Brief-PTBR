# Mapa de strings — pt-BR

Esta etapa registra strings encontradas diretamente no `classes3.dex`, com foco no vocabulário visível do Now Brief. A extração foi feita em nível DEX porque o ambiente atual ainda não possui JADX/Apktool disponíveis.

## Critério

- **confirmada**: string claramente voltada à interface, notificação, permissão ou conteúdo apresentado ao usuário.
- **candidata**: string plausivelmente visível, mas que ainda precisa ser associada ao ponto exato da UI antes de substituir.
- Placeholders, nomes de APIs, classes e strings de bibliotecas não devem ser traduzidos.

## Strings prioritárias

| English | pt-BR | Status |
|---|---|---|
| Now Brief | Now Brief | manter |
| Morning Brief | Resumo da manhã | confirmada |
| Morning briefing | Boletim da manhã | confirmada |
| Morning check-in | Check-in da manhã | confirmada |
| Morning overview | Visão geral da manhã | confirmada |
| Morning summary | Resumo da manhã | confirmada |
| Morning update | Atualização da manhã | confirmada |
| Afternoon Brief | Resumo da tarde | confirmada |
| Afternoon briefing | Boletim da tarde | confirmada |
| Afternoon check-in | Check-in da tarde | confirmada |
| Afternoon overview | Visão geral da tarde | confirmada |
| Afternoon summary | Resumo da tarde | confirmada |
| Afternoon update | Atualização da tarde | confirmada |
| Evening Brief | Resumo da noite | confirmada |
| Evening briefing | Boletim da noite | confirmada |
| Evening check-in | Check-in da noite | confirmada |
| Evening overview | Visão geral da noite | confirmada |
| Evening summary | Resumo da noite | confirmada |
| Evening update | Atualização da noite | confirmada |
| Late night briefing | Boletim da madrugada | confirmada |
| Late night recap | Resumo da madrugada | confirmada |
| Night briefing | Boletim da noite | confirmada |
| Night check-in | Check-in da noite | confirmada |
| Night summary | Resumo da noite | confirmada |
| Audio brief | Resumo em áudio | confirmada |
| Current weather | Clima atual | confirmada |
| Weather always first | O clima sempre primeiro | candidata |
| Refreshing weather | Atualizando o clima | candidata |
| Calendar | Calendário | confirmada |
| Calendar event | Evento do calendário | confirmada |
| Contacts | Contatos | confirmada |
| News | Notícias | confirmada |
| Sleep | Sono | confirmada |
| Sleep mode | Modo de sono | candidata |
| Sleep graph | Gráfico do sono | candidata |
| Sleep score | Pontuação do sono | candidata |
| Energy mascot | Mascote de energia | confirmada |
| Energy score | Pontuação de energia | confirmada |
| Fitness goals | Metas de atividade física | confirmada |
| Calories goal | Meta de calorias | confirmada |
| Customize Now Brief | Personalizar o Now Brief | confirmada |
| Edit schedule | Editar programação | confirmada |
| Schedule | Programação | confirmada |
| Saved schedule | Programação salva | candidata |
| Schedule editor | Editor de programação | candidata |
| Compact widget | Widget compacto | candidata |
| Compact Home widget | Widget compacto da tela inicial | candidata |
| Large Home widget | Widget grande da tela inicial | candidata |
| Your Location | Sua localização | candidata |
| Briefing unavailable. | Boletim indisponível. | confirmada |
| Good morning | Bom dia | confirmada |
| Good afternoon | Boa tarde | confirmada |
| Good evening | Boa noite | confirmada |
| Allow all | Permitir tudo | candidata |
| Don't allow | Não permitir | candidata |

## Notificações e mensagens

Estas strings foram encontradas no DEX e são fortes candidatas a textos de notificação/estado:

- `Now brief is ready` → `O Now Brief está pronto`
- `Your briefing is ready` → `Seu boletim está pronto`
- `Last briefing available` → `Último boletim disponível`
- `Now Brief available` → `Now Brief disponível`
- `Now Brief Is Ready To View` → `O Now Brief está pronto para visualização`
- `Now Brief Ready To View!` → `Now Brief pronto para visualização!`
- `Evening Brief Is Ready To View` → `O resumo da noite está pronto para visualização`
- `Midday briefing available` → `Boletim do meio-dia disponível`
- `Evening summary available` → `Resumo da noite disponível`
- `Your morning briefing is ready` → `Seu boletim da manhã está pronto`
- `Welcome To Your New Now Briefing` → `Bem-vindo ao seu novo Now Brief`
- `You Now Brief Has Been Generated` → `Seu Now Brief foi gerado`

## Permissões

Strings de permissão que podem precisar de tratamento específico no fluxo de primeira execução:

- `Allow Now Brief to send you notifications?` → `Permitir que o Now Brief envie notificações?`
- `Allow Now Brief to access your calendar?` → `Permitir que o Now Brief acesse seu calendário?`
- `Allow Now Brief to access your contacts?` → `Permitir que o Now Brief acesse seus contatos?`
- `Allow Now Brief to access your photos?` → `Permitir que o Now Brief acesse suas fotos?`
- `Allow Now Brief to access smart home devices?` → `Permitir que o Now Brief acesse dispositivos de casa inteligente?`
- `Allow Now Brief to access usage data?` → `Permitir que o Now Brief acesse dados de uso?`
- `Allow Health Connect` → `Permitir o Health Connect`

## Próxima etapa técnica

O próximo passo é associar cada string a referências `const-string`/`const-string/jumbo` e aos métodos de `MainActivityKt`. Isso permite separar strings realmente exibidas pela UI das strings de teste, logs ou geração dinâmica. Depois disso, a substituição deve ser feita preferencialmente no ponto de origem dos textos, preservando placeholders e evitando alterar bibliotecas.
