import spacy

nlp = spacy.load("en_core_web_md")

# Define three objects: cat, monkey, and banana
cat = nlp("cat")
monkey = nlp("monkey")
banana = nlp("banana")

# Calculate the similarity between cat and monkey, and cat and banana
cat_monkey_similarity = cat.similarity(monkey)
cat_banana_similarity = cat.similarity(banana)

# Print the results
print("Similarity between cat and monkey:", cat_monkey_similarity)
print("Similarity between cat and banana:", cat_banana_similarity)


# Finding interesting similarities between cat, monkey, and banana:
# What I find interesting about the similarities between cat, monkey, and banana is that they can be related through their properties and attributes, 
# such as being living organisms and having specific physical features. 
# However, they also differ in various ways, such as their type of food consumption, behavior, and natural habitats.

#For example, a cat is a carnivorous animal that is often kept as a pet, 
# while a monkey is an omnivorous animal that lives in the wild and has a more complex social behavior.
#  A banana is a fruit that is consumed by both animals and humans and is often used as a source of energy.

# When I run a file using "en_core_web_sm", spaCy will load the smaller and 
# faster English model which includes the core features like tokenization, part-of-speech tagging, 
# dependency parsing, and named entity recognition. 
# This model is designed to be used for smaller-scale projects where speed is a priority.

# On the other hand, when you run a file using "en_core_web_md", spaCy will load a 
# larger English model which includes all the core features and additionally includes word vectors. 
# These word vectors are pre-trained and can provide useful context to the model. 
# This model is designed to be used for larger-scale projects where accuracy and context are more important than speed.

