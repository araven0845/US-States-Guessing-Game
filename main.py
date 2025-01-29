import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. 50 States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guesses = []


while len(guesses) < 50:
    ans_state = screen.textinput(title=f"{len(guesses)}/50",
                                 prompt="What's another states name?").title()
    if ans_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if ans_state in all_states:
        guesses.append(ans_state)
        t = turtle.Turtle()
        t.pu()
        t.hideturtle()
        state_data = data[data.state == ans_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(ans_state)

turtle.mainloop()