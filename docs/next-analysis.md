# Next analysis targets

## Phase 1 — completed
- APK inventory
- DEX inventory
- application class inventory
- initial pt-BR string map
- build/decompile/sign helper scripts

## Phase 2 — current
Prioritize these symbols in `classes3.dex`:

1. `MainActivityKt.AppRoot`
2. `MainActivityKt.BriefScreen`
3. `MainActivityKt.BriefHeader_p9gR_Fk`
4. `MainActivityKt.SettingsScreen`
5. `MainActivityKt.AudioBriefSettingsScreen`
6. `MainActivityKt.ContentScreen`
7. weather settings components
8. notification title/body functions

## Phase 3 — translation patch

For every user-visible literal:

- identify its originating method/class;
- determine whether it is a resource lookup or a code literal;
- preserve format placeholders and pluralization behavior;
- add the pt-BR mapping;
- avoid modifying third-party/library strings;
- keep English fallback behavior where appropriate.

## Phase 4 — functional modifications

After translation is stable, implement requested behavior changes one at a time and test each change independently.

## Phase 5 — rebuild/test

- decode/rebuild resources with Apktool;
- rebuild DEX/code patch;
- sign with a development key;
- install on a test Android device/emulator;
- verify startup, permissions, widgets, notifications, audio, weather, calendar and Health Connect flows.

## Important constraint

Do not commit the original APK or a full proprietary decompilation to the public repository. Commit scripts, analysis, mappings and original-code-independent patches instead.
