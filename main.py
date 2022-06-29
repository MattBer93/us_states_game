import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 - States",
                                    prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state in all_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    elif answer_state == 'Exit':
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        missed_data = pandas.DataFrame(missed_states)
        csv_data = missed_data.to_csv("states_to_learn.csv")
        break


#states_to_learn.csv




