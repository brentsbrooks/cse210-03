from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.word import Word


class Director:
  """A person who directs the game. 
    
  The responsibility of a Director is to control the sequence of play.

    Attributes:
        
  """

  def __init__(self):
    """Constructs a new Director.
        
    Args:
      self (Director): an instance of Director.
    """
    self._word = Word()
    self._is_playing = True
    self._jumper = Jumper()
    self._terminal_service = TerminalService()


  def start_game(self):
    """Starts the game by running the main game loop.
        
    Args:
      self (Director): an instance of Director.
    """
    while self._is_playing:
      self._do_outputs()
      self._get_inputs()
      self._do_updates()
      self._is_playing = False
      

  def _do_outputs(self):
    self._word.draw_word_guess()
    self._jumper.draw_jumper()



  def _get_inputs(self):
    pass
  


  def _do_updates(self):
    pass



 
