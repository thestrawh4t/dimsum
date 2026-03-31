# DimSum 🥟

Find embedding models by output dimensionality without downloading weights.

## Install
```bash
pipx install git+https://github.com/thestrawh4t/dimsum.git
```

## Usage
```bash
dimsum --dims 384
dimsum --dims 768 --limit 50
```

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--dims` | 384 | Target embedding dimensionality |
| `--limit` | None | Max number of models to check |

## Manual Install
```bash
git clone https://github.com/thestrawh4t/dimsum.git
cd dimsum
pip install -r requirements.txt
python dimsum.py --dims 384
```

## How it works

DimSum queries the `1_Pooling/config.json` of each sentence-transformer model on Hugging Face — no weights are downloaded. Fast and lightweight.

## License

MIT
