import random
from game.terminal_service import TerminalService

class Word:

  def __init__(self):

    self.terminalservice = TerminalService()
    self._word_list = ["zebra", "lion", "wolf", "bear"]
    self._chosen_word = random.choice(self._word_list)
    self._word_guess = " _ " * len(self._chosen_word)
    



  def draw_word_guess(self):

    self.terminalservice.write_text(self._word_guess)


  def process_guess(self, guess_letter):

    for i in range(len(self._chosen_word)):
      if guess_letter == self._chosen_word[i]:
        # correct_guess = True
        self._word_guess[i] = guess_letter



  

        
