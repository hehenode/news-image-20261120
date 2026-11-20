# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/hehenode/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/hehenode/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world news of **Friday 20 November 2026**: a dated
masthead over six labelled panels. `main.py` copies `entry.png` to the output
directory; the artwork was generated as a flat editorial collage
(`build/art-source.webp`) and composited with the date, headlines and source
line by `build/compose.py` (Pillow), so every word in the image is rendered
type, not generated pixels.

The six stories depicted, as reported on 20 November 2026:

1. **Shenzhen summit** — Presidents Trump, Xi and Putin held their first
   three-way summit in Shenzhen and signed a joint peace declaration.
   (Reuters; One Turn News; Open Chronicle)
2. **Genocide ruling** — The International Court of Justice ruled that
   Myanmar committed genocide against the Rohingya, the court's first such
   finding against a state. (One Turn News; Open Chronicle)
3. **Kyiv under fire** — Russia launched a major overnight missile strike on
   Kyiv, targeting bridges and killing residents; Ukraine's allies met in
   Berlin. (Just Security Early Edition; AP via Euronews)
4. **Record IPO, markets fall** — Anthropic raised a record $81bn in its
   Nasdaq debut while global stocks slid for a fifth day; Japan's Nikkei fell
   4.8% in an AI sell-off. (Reuters; One Turn News)
5. **Riyadh tower struck** — A Houthi missile damaged Saudi Arabia's Public
   Investment Fund tower in Riyadh's financial district. (Reuters; One Turn News)
6. **Ebola over in Kenya** — Kenya discharged its last Ebola patient, 37 days
   after its first case. (One Turn News)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=jwjdm10j&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
