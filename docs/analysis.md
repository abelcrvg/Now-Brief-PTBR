# Análise inicial do APK

## Arquivo de referência

`Now.Brief.apk` — analisado localmente em 2026-09-06.

Tamanho observado: aproximadamente **92 MiB**.

## Estrutura do pacote

O APK contém **628 entradas** no ZIP.

### DEX

Foram encontrados 7 arquivos DEX:

| Arquivo | Tamanho aproximado |
|---|---:|
| `classes.dex` | 40.2 MiB |
| `classes2.dex` | 162 KiB |
| `classes3.dex` | 1.58 MiB |
| `classes4.dex` | 9.6 KiB |
| `classes5.dex` | 15.0 MiB |
| `classes6.dex` | 10.5 MiB |
| `classes7.dex` | 543 KiB |

Os DEX usam formato `dex\n039`, compatível com a família de formatos DEX observada no APK.

### Package name

O Manifest binário contém referências a:

`com.example.nowbrief`

Componentes próprios identificados:

- `com.example.nowbrief.MainActivity`
- `com.example.nowbrief.NowBriefCompactWidgetProvider`
- `com.example.nowbrief.NowBriefHeadlineWidgetProvider`
- `com.example.nowbrief.NowBriefWideWidgetProvider`
- `com.example.nowbrief.NowBriefLiveUpdateService`
- `com.example.nowbrief.NowBriefLiveUpdateTapReceiver`
- `com.example.nowbrief.NowBriefNotificationReceiver`

Também foi identificado o provider interno relacionado ao AndroidX Startup.

## Permissões observadas

Entre as permissões/referências do Manifest estão:

- `ACCESS_COARSE_LOCATION`
- `ACCESS_NETWORK_STATE`
- `ACCESS_WIFI_STATE`
- `DUMP`
- `FOREGROUND_SERVICE`
- `FOREGROUND_SERVICE_DATA_SYNC`
- `FOREGROUND_SERVICE_SHORT_DURATION`
- `INTERNET`
- `POST_NOTIFICATIONS`
- `READ_CALENDAR`
- `READ_CONTACTS`
- `READ_EXTERNAL_STORAGE`
- `READ_MEDIA_IMAGES`
- `RECEIVE_BOOT_COMPLETED`
- `health.READ_ACTIVE_CALORIES_BURNED`
- `health.READ_EXERCISE`
- `health.READ_STEPS`

Essas permissões ainda precisam ser relacionadas aos respectivos fluxos da aplicação antes de qualquer modificação.

## Tecnologias identificadas

Há evidências fortes de uso de:

- Kotlin
- Jetpack Compose
- Material / Material 3
- AndroidX
- Lifecycle
- Navigation
- Health Connect
- OkHttp
- Haze / efeitos visuais
- componentes de blur e liquid glass

Os metadados de compilação encontrados nos DEX também indicam `min-api 31` em artefatos gerados pelo compilador. Isso **não deve ser tratado ainda como substituto do `minSdkVersion` do Manifest**; precisamos decodificar o Manifest para confirmar os valores oficiais.

## Recursos interessantes

### Assets

O APK possui 76 entradas em `assets/`, incluindo:

- `OneUISans-Regular.ttf`
- `OneUISans-Medium.ttf`
- fundos de manhã, meio-dia, notícias e noite
- animação `brief-stars-real.gif`
- animações de configuração em modo claro/escuro
- recursos de clima em JSON
- imagens relacionadas a energia e sono

### Áudio

Foram encontrados arquivos como:

- `jarvis_morning_header.wav`
- `jarvis_afternoon_header.wav`
- `jarvis_evening_header.wav`
- `jarvis_night_header.wav`
- `jarvis_now_brief.wav`
- `jarvis_schedule.wav`
- `jarvis_sleep.wav`
- `jarvis_weather.wav`
- `jarvis_location.wav`

### Widgets

O APK inclui definições para três variantes:

- Compact
- Headline
- Wide

## Código da aplicação

Os metadados de debug/Compose encontrados em `classes3.dex` expõem nomes de arquivos-fonte e composables, incluindo referências a `MainActivity.kt`. Entre os componentes identificados aparecem:

- `BriefHeader`
- `BriefScreen`
- `ContentToggleRow`
- `EditPencilButton`
- `FitnessMetricRow`
- `MemoryStackPhoto`
- `PlanRow`
- `PlaylistSwatch`
- `ShimmerSweepText`
- `ShinyTextOnce`
- `WeatherGlyphIcon`
- `WeatherGlyphLottieIcon`

Isso é particularmente útil porque indica que parte importante da UI foi compilada com informações de origem suficientes para orientar a engenharia reversa.

## Próxima etapa técnica

1. Decodificar `AndroidManifest.xml` completamente.
2. Extrair o `resources.arsc` e identificar strings/recursos por configuração de idioma.
3. Obter uma ferramenta de análise DEX/Java/Smali adequada.
4. Separar código próprio de bibliotecas de terceiros.
5. Mapear strings realmente utilizadas pela aplicação.
6. Identificar o fluxo da `MainActivity`.
7. Criar a primeira alteração mínima e reproduzível.
8. Recompilar e validar a assinatura/instalação.

**Importante:** não devemos editar os DEX manualmente antes de termos um baseline decompilado e uma forma reproduzível de reconstruir o APK.
