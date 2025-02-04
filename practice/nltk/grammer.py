import os
import IPython

from nltk.parse.stanford import StanfordDependencyParser
path = '/home/harshhindocha/nlp/stanford-corenlp-full-2018-10-05/'
# Set this to where you have downloaded the JAR file to
path_to_jar = path + 'stanford-corenlp-3.9.2-models.jar'
path_to_models_jar = path + 'stanford-corenlp-3.9.2-models.jar'

dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
os.environ['JAVAHOME'] = '/usr/bin/'
# Set this to where the JDK is 

"""result = dependency_parser.raw_parse('I shot an elephant in my pajamas')
dep = next(result)
# get next item from the iterator result
for t in dep.triples():
    print(t)

dep.root["word"]
list(dep.tree())

# dep.tree().draw()  # alternative NLTK native method
IPython.core.display.display(dep.tree())"""

import re
regexpSubj = re.compile(r'subj')
regexpObj = re.compile(r'obj')
regexNouns = re.compile("^N.*|^PR.*")
#root = dep.root["word"]

# A random selection of sentences with different styles, domains etc
sentences = ["He watched the dark eyeslits narrowing with greed till her eyes were green stones",
             "When will the Oracle 12.2 database be released?",
             "Coherence is an in-memory grid cluster for Java code",
             "Oracle 12.2 will be released in March 2017",
             "PyData community gathers to discuss how best to apply languages and tools to continuously evolving challenges in data management, processing, analytics, and visualization.",
             "Arsenal are a football team in North London",
             "When will Arsenal ever win a match?",
             "Harsh is playing cricket with bat",
             "Putin and Modi spoke for about three hours over dinner on Thursday, and again for one-and-a-half hours on Friday, before the delegation-level talks took place."
            ]

def get_compounds(triples, word):
    compound = []
    for t in triples:
        if t[0][0] == word:
            if regexNouns.search(t[2][1]):
                compound.append(t[2][0])
    return compound

for sentence in sentences:
    
    result = dependency_parser.raw_parse(sentence)
    dep = next(result)
    root = [dep.root["word"]]
    root.append(get_compounds(dep.triples(), root))
    subj = []
    obj = []
    
    for t in dep.triples():
        if regexpSubj.search(t[1]):
            subj.append(t[2][0])
            subj.append(get_compounds(dep.triples(),t[2][0]))
        if regexpObj.search(t[1]):
            obj.append(t[2][0])
            obj.append(get_compounds(dep.triples(),t[2][0]))
    print("\n",sentence)
    print("Subject:",subj, "\nTopic:", root, "\nObject:",obj)
