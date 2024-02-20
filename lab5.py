import nltk


def tokenize_sentence(sentence):
    return nltk.word_tokenize(sentence)

def tag_tokens(tokens):
    return nltk.pos_tag(tokens)

def print_tags(tags):
    for tag in tags:
        print(f'Token: ``{tag[0]}`` Tag: ``{tag[1]}``')


if __name__ == '__main__':
    
    sentence = input("Enter the sentence you want to tokenize and tag: ")
    tokens = tokenize_sentence(sentence)
    tags = tag_tokens(tokens)
    print_tags(tags)
    