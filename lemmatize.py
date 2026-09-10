from nltk.stem import WordNetLemmatizer
lemmatizier=WordNetLemmatizer()
print(lemmatizier.lemmatize("cats"))
print(lemmatizier.lemmatize("cacti"))
print(lemmatizier.lemmatize("geese"))
print(lemmatizier.lemmatize("rocks"))
print(lemmatizier.lemmatize("python"))
print(lemmatizier.lemmatize("better",pos="a"))
print(lemmatizier.lemmatize("happy",pos="a"))           




import spacy
nlp=spacy.load("en_core_web_sm")
text=input("Enter a sentence:")
doc=nlp(text)
print("nNamed Entities")
print("_"*40)
for ent in doc.ents:
    print("Entity:(ent.text)")
    print("label:(ent.label_)")
    print("_"*40)

