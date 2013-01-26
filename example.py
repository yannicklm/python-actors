import actor

@actor.actor
def Input():
    stdin = input()
    Output.push(stdin)

@actor.actor
def Output():
    print(Output.pop())

if __name__ == "__main__":
    actor.run(Input, Output)
