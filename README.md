# DimSum 🥟

Find embedding models by output dimensionality without downloading weights.

## Install

### pipx (recommended)
```bash
pipx install git+https://github.com/thestrawh4t/dimsum.git
```

### pip / venv
```bash
git clone https://github.com/thestrawh4t/dimsum.git
cd dimsum
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
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

## How it works

DimSum queries the `1_Pooling/config.json` of each sentence-transformer model on Hugging Face — no weights are downloaded. Fast and lightweight.

## License

MIT
