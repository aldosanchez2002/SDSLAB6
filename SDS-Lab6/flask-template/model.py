import answers
from collections import defaultdict

def grade(guesses):
  output=defaultdict(bool)
  total=0
  for key in guesses:
    if guesses[key]=="":
      continue
    output[key]= guesses[key] == answers.capital_dic[key]
    if guesses[key] == answers.capital_dic[key]:
      total+=2
  return (output,str(total)+"%")