'''
Application main file written in Python.
It ties the flow of the application togheter
'''

from markov_python.cc_markov import MarkovChain
from fetch_data import html

mc = MarkovChain()

mc.add_string(html)

text = mc.generate_text()
text = " ".join(text)

print text
