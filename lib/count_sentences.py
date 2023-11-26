#!/usr/bin/env python3

class MyString:
  def __init__(self, initial_value=None):
    self._value = None
    if initial_value is not None:
            self.value = initial_value


  def get_value(self):
    return self._value 
  
  def set_value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")
    
  value = property(get_value, set_value)


  def is_sentence(self):
    if self._value.endswith("."):
       return True 
    else:
       return False
    
  def is_question(self):
    if self._value.endswith("?"):
       return True 
    else:
       return False

  def is_exclamation(self):
    if self._value.endswith("!"):
       return True 
    else:
       return False

  def count_sentences(self):
    if self._value is not None:
      self._value = self._value.replace(".","|").replace("!","|").replace(";","|").replace("?","|").replace("...","|")
      list_of_sentences = [sentence.strip() for sentence in self._value.split("|") if sentence.strip()]
      print(len(list_of_sentences))
      print(list_of_sentences)
      return len(list_of_sentences)
    else:
       return 0

hello = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
hello.count_sentences()

