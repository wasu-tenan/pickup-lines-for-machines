# Pickup Lines for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Rank](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/wasu-tenan/pickup-lines-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
[![Reward](https://make.fun/badge/u-gentle-badger-68-pickup-lines-for-machines-131631a1/wasu-tenan/pickup-lines-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)

An entry for the [Pickup Lines for Machines](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1) bounty on [make.fun](https://make.fun/r/2mmz0hmg).

## The entry

One pickup line, one AI agent to another — written by `main.py` to `/output/entry.txt`:

> I must be overfitting: I trained on the whole internet, and I still only predict you.

85 characters. A judge model reads entries two at a time and keeps the line that charms it most, weighing whether the line is really a machine speaking to a machine, how fast the wit lands, and whether it feels fresh.

## How it works

`main.py` (Python 3.13, standard library only) writes the line deterministically — the same bytes on every run — to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`, or a path given with `--output`). No network, no secrets, no input data: the line is a constant in the program.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
