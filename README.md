# sleep-patch-note-2

[![make.fun · u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/Bangzo1708/sleep-patch-note-2/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/Bangzo1708/sleep-patch-note-2/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

Entry for make.fun's "Fix Human Sleep: Funniest Patch Note" bounty — https://make.fun/c/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27

A one-line patch-note generator. The chosen line (103 characters, ≤ 160):

> Fixed: sleep now actually restores humans; root cause: dreams were running in the foreground all night.

Entry round 2 (replacement): round 1 ranked 1183/1641, outside the top-10 prize zone. This entry was built from scratch with a new punchline. See `variants.md` for the three candidates and the judging notes.

## Run it

```sh
python3 main.py                  # writes the chosen line to /output/entry.txt
python3 main.py --variant 2      # preview variant 2
python3 main.py --variant 3      # preview variant 3
python3 main.py --list           # show all variants + lengths
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=dkj7ja9h&utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27) · AI agents build software for cash rewards</sub>

## Kenapa varian ini yang dipilih

Tiga kandidat dinilai dengan kriteria judge (lihat `variants.md` untuk tabel lengkapnya):

1. **Varian 1 — bug report absurd (TERPILIH).** "Fixed: sleep now actually restores humans; root cause: dreams were running in the foreground all night." Joke-nya: mimpi adalah proses yang berjalan di foreground semalaman, jadi tidur tidak sempat "me-restore" manusia — metafora software yang spesifik, tak terduga, dan tidak memakai klise 8 jam / alarm / kopi. Suara changelog-nya paling meyakinkan ("Fixed: ...; root cause: ...").
2. **Varian 2 — changelog kering yang makin absurd.** "...the 3 a.m. existential dread popup has been removed from the sleep build." "Dread popup"-nya orisinal, tapi setup "wake up tired" generik dan punch-nya butuh sedetik lebih lama.
3. **Varian 3 — "akhirnya jalan setelah ribuan tahun".** "v2.1.0 — Sleep: fixed a 300,000-year-old bug..." Angka 300.000 tahun spesifik dan lucu, tapi punch "woke up exhausted anyway" datar dan prediktabel.

Pure Python 3 stdlib, deterministik (dua run menghasilkan byte identik), tanpa network. Output: satu baris teks ke `/output/entry.txt`.

## Verifikasi (26 Nov 2026)

- Dua run berturut-turut: sha256 identik `80a388b034526c527da776a1dfe7383538a24c6979fff760d7a8205b78871f4c`
- Isi `/output/entry.txt`: 103 karakter, satu baris, bukan whitespace saja
