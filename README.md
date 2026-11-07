# MOBA ni Joy

Laro sa browser na JavaScript ang code (Three.js). Pumili ng hero, bumili ng item, tapos sirain ang mga tower at ang Nexus ng Pula.

## Mga hero
- **Joy** (Mage): Kidlat at Starfall
- **Skeleton** (Tank): Slam at Rage
- **Behemoth** (Bruiser): Charge at Roar
- **Minotaur** (Assassin): Dive at Gale
- **Gunner** (Marksman): Cannon at Overdrive
- **Valkyrie** (Long-range): Burst at Volley. Umaatake mula sa malayo (10 yunit) gamit ang 3D na projectile na apoy na may buntot, at may sabog at apoy sa lupa kapag tumama.

## Mana, level, at gold
- **Mana**: gumagamit ng mana ang bawat skill (15 hanggang 30). Bumabalik ang mana ng **1 bawat segundo**, kaya piliin nang mabuti ang mga skill. Nagsisimula sa 60 mana at tumataas ng 10 sa bawat level.
- **Level at XP**: hanggang **level 20**. Tumataas ang kailangang XP sa bawat level. Nakakakuha ka ng XP sa mga napatay na kalaban malapit sa iyo (kawal 25, tower 150, hero 200) at 1.5 bawat segundo. Sa bawat level, lumalakas ang HP, atake, at magic, at gumagaling ka nang kaunti.
- **Panel sa ibaba-gitna** (tulad ng sa Dota): icon ng hero na may level, malapad na HP bar at mana bar na may numero (kasama ang +1.0 na regen ng mana), manipis na XP bar, mga slot ng **Recall** at **Heal**, at 6 na item slot. Nasa taas pa rin ang minimap.
- **Gold**: magsisimula ka sa $300. Dagdag na gold: +1 bawat segundo, +20 sa bawat kawal na mapatay, +150 sa tower, at +150 sa hero.

## Mga item
- Pindutin ang **Shop** (kanan-taas, sa tabi ng gold) para bumili. 6 na slot ang pwede, at isang beses lang kada item.
- Lumalabas ang mga nabili mong item sa 6 na slot ng panel sa ibaba. I-tap ang item na may asul na tuldok para gamitin ang Active nito (may cooldown na numero). I-tap ang ibang item para makita ang paliwanag.
- Mga item: Shadow Step Boots, Serpent Coil (Token), Serpent Coil (Orb), Crimson Heart, Curse Grimoire, Clockwork Spider, Lunar Aegis, Abyssal Trident, Phoenix Ash, Frostbitten Gauntlet, Windreaver Bow, Storm Caller's Staff, at Krristan Heart.

## Mga file
- `index.html`: ang mismong laro. May loading screen, pagpili ng hero, at walang editor.
- `editor.html`: ang Mini Game Editor (opsyonal), para makita at mabago ang script ng laro (kasama ang listahan ng `ITEMS`).

## Laruin
- **Pahalang agad ang screen**: kapag patayo ang phone, nakapahalang na ang laro. Iikot mo lang ang phone sa gilid para tumayo ang larawan. Sa Android Chrome, susubukan din nitong i-lock ang screen sa pahalang kapag pinindot ang **Maglaro**. Kung gusto mong ibalik sa patayo, pindutin ang **⟳** (kanan-taas).
- Hintaying matapos ang loading, pindutin ang **Maglaro**, pumili ng hero, at pindutin ang **Simulan**.
- Joystick (kaliwa-baba) o tap sa lupa para maglakad.
- Kanan-baba: malaking button ang atake, at sa paligid nito ang mga skill. Sa ilalim, **Recall** at **Heal**.
- **Fog of war**: madilim ang lugar na hindi pa napupuntahan, at nakatago ang mga kalaban na malayo sa mga kakampi mo. Nasa kaliwa-taas ang minimap na may ilog, damo, lane, at camp.
- **Mapa na hango sa Dota**: malawak na parisukat na mapa. Nasa kaliwa-baba ang base ng Asul at kanan-taas ang sa Pula. May tatlong lane (taas, gitna, baba) at diagonal na ilog mula kaliwa-taas hanggang kanan-baba. Sa panig natin, **damo** ang sahig at **kayumangging batong tile** ang mga lane. **Kulay-abong batong tile** ang sahig ng kabilang panig (panig ng kalaban), at **kulay-kahel na tile** ang mga lane doon.
- **Damo**: parihabang damo (hango sa modelo mo) sa gubat, sa gilid ng mga lane at sa pagitan ng mga guho. Wala ito sa mismong daanan. Pumasok para magtago: hindi ka makikita o matatarget ng mga kalaban, tower, at kawal, maliban kung nasa parehong damo rin sila, o kapag kakaatake o kaka-skill mo lang (1.5 segundo). Naglalabo ang hero mo kapag nakatago.
- **Jungle camp**: may 12 camp (dilaw na tatsulok sa minimap), tig-2 neutral. May **sanctuary** (guho ng bato) sa likod ng bawat camp, na may banggaan. Lumalaban lang sila kapag may lumapit, at bumabalik sila sa pwesto nila. Bawat napatay: +25 gold, +30 XP. Bumabalik ang camp pagkalipas ng 60 segundo.
- **Dragon (boss)**: nasa dalawang sanctuary (isa sa kaliwang gubat ng Asul at isa sa kanang gubat ng Pula) ang dragon na may 3 ulo at pumapagaspas na pakpak. 2500 HP, malakas ang atake at sumisigaw ng apoy. Kapag napatay mo: +150 gold, +200 XP, at gumagaling ka ng 30% HP. Bumabalik pagkalipas ng 3 minuto. Orange na malaking tatsulok ito sa minimap.
- **Ahas at Reaper**: dalawa pang 3D monster, tig-isa sa bawat panig, sa mga sanctuary na walang dragon. Ang **ahas** (sungay, pulang-itim) ay may lason: 500 HP, bawat kagat ay may lason na 6 damage kada segundo sa loob ng 3 segundo (+$40, +50 XP, bumabalik pagkalipas ng 90 segundo). Ang **Reaper** (may sandata at katawan ng ahas) ay 700 HP at nagpapabagal sa tinamaan ng 1.5 segundo (+$60, +80 XP, bumabalik pagkalipas ng 2 minuto). Lilang tatsulok sila sa minimap. Ang natitirang 6 na sanctuary ay may tig-2 maliit na neutral pa rin.
- May banggaan ang mga tower, Nexus, at mga unit.
- Pindutin ang **Ulit** (kanan-taas) para bumalik sa pagpili ng hero.
- Pinch (o scroll) para mag-zoom ng camera. Katamtaman ang taas ng camera sa simula (hindi masyadong mataas).

## I-deploy sa GitHub Pages
1. Gumawa ng bagong repository sa GitHub.
2. Add file > Upload files. I-upload ang `index.html`, `editor.html`, at `README.md`. Commit changes.
3. Settings > Pages > Source: **Deploy from a branch** > Branch: `main`, folder `/ (root)` > Save.
4. Maghintay ng ilang minuto. Ang laro ay nasa link ng Pages mo, at ang editor ay sa dulo ng link na `/editor.html`.

## Para i-upload ang sarili mong laro
1. Buksan ang editor at gawin ang laro. Ilagay ang pangalan ng laro sa kahon sa taas.
2. Pindutin ang **I-export ang Laro**. Makukuha mo ang `laro.html`: may loading screen at walang editor.
3. Palitan ang pangalan nito ng `index.html` at i-upload sa GitHub.
4. Hindi kasama sa export ang mga na-import na GLB. Pero pwede mong gamitin sa script ang `Spawn("joy")`, `Spawn("skeleton")`, `Spawn("beast")`, `Spawn("minotaur")`, `Spawn("gunner")`, at `Spawn("valkyrie")`, na naka-embed na.

## Paalala
- Kailangan ng internet dahil kinukuha ang Three.js mula sa CDN.
- Mabigat ang file (mga 4 MB) dahil naka-embed ang mga 3D model at texture.
- Auto-rig ang galaw ng mga character (hula batay sa hugis), kaya hindi ito kasing-ayos ng totoong animation.
- **Bumabagal ang laro?** Awtomatikong ibinababa ng laro ang linaw ng larawan kapag mabagal ang phone, at itinataas ulit kapag gumaan.
- Wala pang physics na kumpleto at multiplayer. AI lang ang kalaban.
