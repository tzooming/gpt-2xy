import torch
from torch.nn import functional as F
from pytorch_transformers import GPT2Tokenizer, GPT2Model, GPT2LMHeadModel
torch.set_grad_enabled(False)

tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')
model = GPT2LMHeadModel.from_pretrained('gpt2-large').eval()


def extend(text, size=20):
    tokens = tokenizer.encode(text)
    prediction, past = torch.tensor([tokens]), None
    for i in range(size):
        prediction, past = model(prediction, past=past)
        prediction = torch.multinomial(F.softmax(prediction[:, -1]), 1)
        tokens.append(prediction.item())
    return tokenizer.decode(tokens)


if __name__ == "__main__":
    test_text = 'Microsoft and Google'
    extended = extend(test_text, 25)
    print(extended)
