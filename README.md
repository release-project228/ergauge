# ergauge

Free, no-login toolset around public Instagram content: profile previews,
story viewing, an engagement-rate calculator and account comparison.

**Website: [https://ergauge.com](https://ergauge.com)**

## What's inside

- `er_calc.py` — engagement-rate calculator: feed it a CSV of your own post
  metrics and it prints per-post ER plus the account average.

```bash
python er_calc.py posts.csv
```

CSV columns: `followers,likes,comments` (one post per line).

## Why this repo

`er_calc.py` is a small, dependency-free example of the kind of utility ergauge
runs as a web tool. The full product lives at
[https://ergauge.com](https://ergauge.com).

## License

MIT
