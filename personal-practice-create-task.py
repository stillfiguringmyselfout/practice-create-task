state_fish_list = {"Hawaii": "rectangular triggerfish" , "California": "garibaldi", "The Moon": "anglerfish", "Colorado": "greenback cutthroat trout"}


def define(dictionary, q, printmsg1, printmsg2):

  c = "y"
  
  while c == "y":
    word = input(q)
    if dictionary.get(word, 0) != 0:
      print(printmsg1, word, printmsg2, dictionary[word] + ".")
      c = input("Search again? y/n ")
    else:
      print("ERROR")

define(state_fish_list, "Enter state: ", "The state fish of", "is the")