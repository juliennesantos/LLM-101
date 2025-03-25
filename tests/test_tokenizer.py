from transformers import AutoTokenizer

def test_tokenizer():
  # Load the pre-trained tokenizer
  tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", force_download=False)

  # Define input test and expected tokenization output
  input_text = "Hello, world!"
  tokens = tokenizer.tokenize(input_text)

  # Assert expected tokens
  assert tokens == ["hello",",","world","!"]