import torch
from INF.models import InferSent

# From infersent documentation
# You can find more at https://github.com/facebookresearch/InferSent
MODEL_PATH = 'INF/encoder/infersent2.pkl'
params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': 2}

# Create infersent object
infersent = InferSent(params_model)
infersent.load_state_dict(torch.load(MODEL_PATH))

# Path to word embeddings
W2V_PATH = 'INF/fastText/crawl-300d-2M.vec'
infersent.set_w2v_path(W2V_PATH)

# Only use vectors that are of the 100,000 most used words in the English language
infersent.build_vocab_k_words(K=100000)

print("InferSent Loaded")

def get_infersent(sentences):
        """
        Returns the array of InferSent vectors associated with the sentences
        """
        embeddings = infersent.encode(sentences, tokenize=True)
        return embeddings