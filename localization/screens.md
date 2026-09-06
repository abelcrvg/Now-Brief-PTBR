# Plano de localização por tela — pt-BR

Este arquivo transforma o inventário DEX em uma ordem prática de implementação. As traduções abaixo são propostas para uso no APK; antes da substituição definitiva, cada literal deve ser confirmado no ponto de renderização.

## 1. BriefScreen — prioridade máxima

| Original | pt-BR |
|---|---|
| Gallery stories | Histórias da galeria |
| Traffic updates | Atualizações do trânsito |
| Routine | Rotina |
| Health and wellness | Saúde e bem-estar |
| Events and tasks | Eventos e tarefas |
| Daily activity | Atividade diária |
| Alarms | Alarmes |
| Travel | Viagens |
| News | Notícias |
| Moments | Momentos |
| Smart home | Casa inteligente |
| Digital Wellbeing | Bem-estar digital |
| Here's some news you may be interested in. | Aqui estão algumas notícias que podem interessar a você. |
| Here's your energy score for today. | Aqui está sua pontuação de energia de hoje. |
| Here's what tomorrow is already shaping into. | Veja como o dia de amanhã já está se desenhando. |
| Stay up to date with Now brief. | Mantenha-se atualizado com o Now Brief. |

## 2. SettingsScreen

| Original | pt-BR |
|---|---|
| Customize Now Brief | Personalizar o Now Brief |
| Audio brief | Resumo em áudio |
| Compact widget | Widget compacto |
| Edit schedule | Editar programação |
| Schedule | Programação |
| Current weather | Clima atual |
| Calendar | Calendário |
| Contacts | Contatos |
| News | Notícias |
| Sleep | Sono |
| Fitness goals | Metas de atividade física |
| Calories goal | Meta de calorias |
| Energy score | Pontuação de energia |
| Weather always first | O clima sempre primeiro |
| Memories and News above Weather | Memórias e Notícias acima do Clima |
| Dark mode for settings | Modo escuro das configurações |

## 3. AudioBriefSettingsScreen

| Original | pt-BR |
|---|---|
| Audio brief | Resumo em áudio |
| Morning | Manhã |
| Afternoon | Tarde |
| Evening | Noite |
| Night | Madrugada |
| Voice | Voz |
| Schedule | Programação |

Os nomes de vozes e referências a arquivos JARVIS devem ser preservados até confirmar se são nomes próprios da configuração.

## 4. WeatherCard

| Original | pt-BR |
|---|---|
| Current weather | Clima atual |
| Your Location | Sua localização |
| Refreshing weather | Atualizando o clima |
| Clear tonight | Céu limpo esta noite |
| Weather always first | O clima sempre primeiro |
| Weather-reactive backgrounds | Planos de fundo reativos ao clima |

Códigos meteorológicos, nomes de APIs, unidades e nomes de assets não devem ser traduzidos.

## 5. NewsCard

| Original | pt-BR |
|---|---|
| News | Notícias |
| Here's some news you may be interested in. | Aqui estão algumas notícias que podem interessar a você. |
| Read more in Samsung News | Leia mais no Samsung News |
| Stay up to date with Now brief | Mantenha-se atualizado com o Now Brief |

## 6. PermissionIntroDialog / primeiro uso

| Original | pt-BR |
|---|---|
| Allow all | Permitir tudo |
| Don't allow | Não permitir |
| Allow Now Brief to send you notifications? | Permitir que o Now Brief envie notificações? |
| Allow Now Brief to access your calendar? | Permitir que o Now Brief acesse seu calendário? |
| Allow Now Brief to access your contacts? | Permitir que o Now Brief acesse seus contatos? |
| Allow Now Brief to access your photos? | Permitir que o Now Brief acesse suas fotos? |
| Allow Now Brief to access smart home devices? | Permitir que o Now Brief acesse dispositivos de casa inteligente? |
| Allow Now Brief to access usage data? | Permitir que o Now Brief acesse dados de uso? |
| Allow Health Connect | Permitir o Health Connect |

## 7. Notificações

| Original | pt-BR |
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

## 8. Períodos do dia

| Original | pt-BR |
|---|---|
| Good morning | Bom dia |
| Good afternoon | Boa tarde |
| Good evening | Boa noite |
| Morning Brief | Resumo da manhã |
| Afternoon Brief | Resumo da tarde |
| Evening Brief | Resumo da noite |
| Late night briefing | Boletim da madrugada |
| Late night recap | Resumo da madrugada |
| Night briefing | Boletim da madrugada |

## Regra de implementação

1. Primeiro substituir strings claramente visíveis e confirmadas.
2. Depois substituir mensagens de notificação.
3. Em seguida tratar permissões e onboarding.
4. Só depois alterar strings candidatas.
5. Não substituir nomes de classes, métodos, APIs, assets, chaves JSON ou strings de bibliotecas.
6. Preservar placeholders e formatação exatamente como no original.
7. Após cada grupo, reconstruir, assinar e instalar uma versão de teste antes de continuar.
