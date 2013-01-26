Silly actor library for Python
===============================

Inspired by `Talk #86 on destroyallsoftware.com <https://www.destroyallsoftware.com/screencasts/catalog/actor-syntax-from-scratch>`_

Python is a flexible language too!

::

  import actor

  @actor.actor
  def Input():
      stdin = input()
      Output.push(stdin)

  @actor.actor
  def Output():
      print(Output.pop())

  actor.run(Input, Output)
