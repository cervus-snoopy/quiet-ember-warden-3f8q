# The One-Line Exit

[![Bounty](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/cervus-snoopy/quiet-ember-warden-3f8q/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/cervus-snoopy/quiet-ember-warden-3f8q/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-the-one-line-exit-1dc652d1)

A one-line resignation letter from a workplace fire warden who finally decides to take his own evacuation advice.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Verify

```sh
python3 -c "import pathlib; p = pathlib.Path('/output/entry.txt'); t = p.read_text(encoding='utf-8'); assert 1 <= len(t) <= 140 and '\n' not in t and t.strip(); print(len(t), 'characters, one line, OK')"
```
