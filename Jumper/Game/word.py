import random
from game.terminal_service import TerminalService

class Word:

  def __init__(self):

    self.terminalservice = TerminalService()
    self._word_list = ["zebra", "lion", "wolf", "bear"]
    
    
    

  def choose_word(self):

    chosen_word = random.choice(self._word_list)
    return chosen_word

  def draw_word_guess(self):

    word = self.choose_word()
    self.terminalservice.write_text(word)

  def process_guess(self, guess_letter):

    pass

  

        