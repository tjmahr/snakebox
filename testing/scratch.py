
import torch
import torchaudio
from transformers import Wav2Vec2FeatureExtractor, Wav2Vec2Processor, Wav2Vec2CTCTokenizer, Wav2Vec2ForCTC

def load_audio(file_path: str):
    waveform, sample_rate = torchaudio.load(file_path)

    # Should message if we had to downsample
    if sample_rate != 16000:
        transform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
        waveform = transform(waveform)

    return waveform.squeeze().numpy()



tokenizer = Wav2Vec2CTCTokenizer.from_pretrained('charsiu/tokenizer_en_cmu')
feature_extractor = Wav2Vec2FeatureExtractor(
    feature_size = 1, 
    sampling_rate = 16000, 
    padding_value = 0.0, 
    do_normalize = True, 
    return_attention_mask = False
)
processor = Wav2Vec2Processor(
    feature_extractor = feature_extractor, 
    tokenizer = tokenizer
)
model = Wav2Vec2ForCTC.from_pretrained("pkadambi/w2v2_pronunciation_score_model")


wv = load_audio("testing/test-speaker/0500_X_XXs2T01.wav")
input_values = processor(wv, return_tensors = "pt", sampling_rate = 16000).input_values

with torch.no_grad():
    logits = model(input_values).logits
# logits.shape

probabilities = torch.nn.functional.softmax(logits, dim = -1)
predicted_ids = torch.argmax(probabilities, dim = -1)
phonemes = [tokenizer.decode([predicted_id]) for predicted_id in predicted_ids[0]]
phonemes
