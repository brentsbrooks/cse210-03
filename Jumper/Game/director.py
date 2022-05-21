from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.guesser import Guesser


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


  def start_game(self):
    """Starts the game by running the main game loop.
        
    Args:
      self (Director): an instance of Director.
    """
    while self._is_playing:
      self._get_inputs()
      self._do_updates()
      self._do_outputs()


  def _get_inputs(self):
  


  def _do_updates(self):



  def _do_outputs(self):