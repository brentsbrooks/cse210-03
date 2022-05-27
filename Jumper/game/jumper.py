from game.terminal_service import TerminalService
from game.terminal_service import TerminalService


class Jumper:




  def __init__(self):

    self.terminalservice = TerminalService()

    self._jumper = [
      "  ____",
      " /____\\",
      " \\   /",
      "  \\ /",
      "   O",
      "  /|\\",
      "  / \\",
      "",
      "^^^^^^^^",
    ]

  
  def draw_jumper(self):
    for line in self._jumper:
      self.terminalservice.write_text(line)


  def cut_line(self):
    self._jumper.pop(0)







  
