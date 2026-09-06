# Application class inventory

Generated from the uploaded `Now.Brief.apk` for analysis. The original APK is not included in this repository.

## DEX layout

- `classes3.dex` contains the main `com.example.nowbrief` application implementation.
- `classes2.dex` contains generated Android `R` resource classes.
- `classes4.dex` contains Compose theme classes.
- Other DEX files are primarily dependency/runtime code.

## High-value entry points

### MainActivity
`com.example.nowbrief.MainActivity`

Methods observed:
- `<init>`
- `onCreate`

### MainActivityKt
`com.example.nowbrief.MainActivityKt`

Important Compose/UI functions observed:
- `AppRoot`
- `BriefScreen`
- `BriefHeader_p9gR_Fk`
- `ContentScreen`
- `SettingsScreen`
- `AudioBriefSettingsScreen`
- `DeveloperOptionsScreen`
- `WidgetsScreen`
- `AppearanceOption`
- `ContentToggleRow`
- `ContentToggleListCard`
- `WeatherFirstModeOption`
- `WeatherFirstExceptionSettingsCard`
- `WidgetInstallCard`
- `FitnessCard`
- `SleepCard`
- `WeatherCard`
- `CommuteCard`
- `ConnectedBriefCard`
- `SmartHomeCard`
- `TomorrowCard`
- `WalletCard`
- `NewsCard` / news-related UI symbols
- `PermissionIntroDialog` / permission-related UI symbols
- `StartupIntroOverlay`

## Functional symbols worth modifying later

### Notifications / scheduling
- `createBriefNotificationChannel`
- `notificationTitleFor`
- `notificationBody`
- `notificationTitles`
- `scheduleNextBriefNotification`
- `syncBriefNotificationSchedule`
- `cancelBriefNotifications`
- `showBriefReadyNotification`

### Weather
- `fetchLiveWeatherUi`
- `fetchOpenMeteoWeatherUi`
- `fetchWeatherApiWeatherUi`
- `weatherCodeToLabel`
- `weatherGlyphForCode`
- `weatherGlyphForSummary`
- `weatherIconAssetName`
- `normalizeWeatherLocation`
- `rememberWeatherQuery`
- `rememberWeatherUi`

### Calendar / fitness
- `fetchCalendarSchedule`
- `HealthConnectFitnessReader`
- `FitnessDaySnapshot`

### Audio briefing
- `AudioBriefSpeaker`
- `AudioBriefSettingsScreen`
- `audioBriefLinesForPhase`

### App/settings integration
- `samsungBriefSettingsIntent`
- `openSamsungBriefSettings`
- `openGalaxyAiSettings`
- `isSamsungBriefSettingsAvailable`
- `launchAppOrStore`

## Translation implication

The UI is substantially implemented in Kotlin/Jetpack Compose rather than relying exclusively on Android XML resources. Therefore, a complete pt-BR translation will require patching application-level constants/code in addition to `resources.arsc`/`R$string` values.

## Current blocker

JADX 1.5.6 is the intended decompiler. It is the current upstream release as of this analysis, but the execution environment cannot resolve GitHub DNS, so the release archive cannot currently be downloaded from inside the container. The APK itself is fully available locally, allowing continued static DEX/string/class-table analysis without inventing decompiled source.
