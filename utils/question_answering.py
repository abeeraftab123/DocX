from transformers import pipeline

qa_pipeline = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

def answer_question(context, question):
    return qa_pipeline({'context': context, 'question': question})['answer']