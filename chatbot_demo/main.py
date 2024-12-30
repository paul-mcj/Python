# pipelines abstract complex logic, making it easy to apply an LLP task
from transformers import pipeline 

# NOTE: this is a good doc resource for pipeline tasks
# https://huggingface.co/docs/transformers/main/en/main_classes/pipelines#transformers.pipeline.task

# NOTE: there are a ton of tasks available to pass as a string to the pipeline object
classifier = pipeline("sentiment-analysis")
result_1 = classifier("I am loving this coffee")
# print(result_1)

# NOTE: there are also tons of models you can apply to a pipeline
generator = pipeline("text-generation", model="distilgpt2")
result_2 = generator("For lunch, I am deciding between a salad and a sandwich. Which is healthier?", num_return_sequences=2)
# print(result_2)

# NOTE: this task will try to find what category fits best
zero = pipeline("zero-shot-classification")
result_3 = zero("hat tricks are rare", candidate_labels=["football", "hockey", "baseball"])
# print(result_3)

# NOTE: some pipelines and models can be provided multiple questions and process multiple answers
oracle = pipeline(model="deepset/roberta-base-squad2")
questions = [
    {"question": "Where do I live?", "context": "My name is Wolfgang and I live in Berlin"},
    {"question": "What is my name?", "context": "My name is Wolfgang and I live in Berlin"},
]
result_4 = [oracle(q) for q in questions]
# print(result_4) 
# results with start and end JSON keys will be applied to where the model predicts the main keywords in the question lie to give way to the answer. so the answer to the first question is:
# {'score': 0.9190714955329895, 'start': 34, 'end': 40, 'answer': 'Berlin'}
# in the question, Berlin string starts at string index 34 and ends at 40. The algorithm tells you where it found its answer via the question 

lucky = pipeline("question-answering")
result_5 = lucky(question="what are my lucky numbers", context="1, 2, 3 are numbers i find to be lucky, but i find that 7 is unlucky")
# print(result_5)


en_to_fr = pipeline("translation_en_to_fr")
result_6 = en_to_fr("Hello, how are you? Where is the library?")
# print(result_6)



# tokenizers are essentially the ML algorithms way of shaping a string/question into a mathematical expression that it can understand. modifying tokenizers gives more customization into how ML can be integrated in a program.
from transformers import AutoTokenizer, AutoModelForSequenceClassification


# selecting specific models is often necessary when dealing with tokenizers, and its common to just put it in a variable instead of always referencing a long string name

# this is a popular text classification model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# this is a toxic comment classification model
# model_name = "JungleLee/bert-toxic-comment-classification"

model = AutoModelForSequenceClassification.from_pretrained(model_name)

tokenizer = AutoTokenizer.from_pretrained(model_name)

tokens = tokenizer.tokenize("I am glad that the Sens won last night") # each word is separated as a string and assigned a token 

token_ids = tokenizer.convert_tokens_to_ids(tokens) # each token is then given a unique id (ie. the mathematical representation the model uses for its scrutiny)

# lets pretend we have some data that the model is being trained on:
sentences = [
    "The cat jumped over the fence.",
    "She enjoys reading sexy mystery novels.",
    "A gentle breeze cooled the warm evening.",
    "He practiced the guitar for two fucking hours.",
    "The dumb coffee shop was bustling with racist activity."
]

# NOTE: padding and truncation make sure that all samples in the passed in data have the same length
batch = tokenizer(sentences, padding=True, truncation=True, max_length=512, return_tensors="pt") # returns a dict

# with our batch of tokens, we can pass to our model
import torch
import torch.nn.functional as F

with torch.no_grad():
    outputs = model(**batch) # with py torch, unpack dict
    print(outputs)
    # outputs (notice the logits argument): 
    # SequenceClassifierOutput(loss=None, logits=tensor([[-0.0145,  0.1429],
    #     [-3.4557,  3.6111],
    #     [-3.2771,  3.4624],
    #     [ 1.9661, -1.7320],
    #     [-3.2226,  3.4185]]), hidden_states=None, attentions=None)
    
    predictions = F.softmax(outputs.logits, dim=1)
    print(predictions)
    # predictions: these are the probabilities. this model has negative probability first and positive probability second. the higher number of the two is the expected result the model concludes
    # tensor([[4.6073e-01, 5.3927e-01],
    #     [8.5224e-04, 9.9915e-01],
    #     [1.1818e-03, 9.9882e-01],
    #     [9.7583e-01, 2.4171e-02],
    #     [1.3039e-03, 9.9870e-01]])

    labels = torch.argmax(predictions, dim=1)
    print(labels)
    # labels: labels that identify with outcome
    # tensor([1, 1, 1, 0, 1])

    assurance = [model.config.id2label[label_id] for label_id in labels.tolist()]
    print(assurance)
    # assurance: the actual results of what each sentence is
    # ['POSITIVE', 'POSITIVE', 'POSITIVE', 'NEGATIVE', 'POSITIVE']