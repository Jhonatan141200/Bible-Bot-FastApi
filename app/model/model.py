from transformers import pipeline

# Use Bert Model
def get_model():
    qa = pipeline('bible-model-bert', 
              model="/BibleModelBert/chkp/1/saved_model.pb", 
              tokenizer="/BibleModelBert/tokenizer/tokenizer_config.json")
    return qa