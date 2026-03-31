# DimSum - Serving up embedding models by dimensionality, no weights needed
# Usage: python dimsum.py --dims 384 --limit 50

import argparse
import warnings
import requests
from huggingface_hub import list_models

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description="Find embedding models by output dimensionality")
parser.add_argument("--dims", type=int, default=384, help="Target embedding dimensionality")
parser.add_argument("--limit", type=int, default=None, help="Max number of models to check")
args = parser.parse_args()

candidates = list(list_models(filter="sentence-transformers"))
if args.limit:
    candidates = candidates[:args.limit]

for model in candidates:
    try:
        url = f"https://huggingface.co/{model.modelId}/resolve/main/1_Pooling/config.json"
        config = requests.get(url, timeout=5).json()
        dim = config.get("word_embedding_dimension")
        if dim == args.dims:
            print(model.modelId)
    except Exception:
        continue
        
