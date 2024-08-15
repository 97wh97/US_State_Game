import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# This is a way to get the (x,y) of the state by clicking on it.
# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

pd = pandas.read_csv("50_states.csv")
all_states = pd.state.to_list()

answer = screen.textinput(title = "Guess the state", prompt = "What is another state's name?").title()

correct = []
correct_num = 0

missing_states = []

while correct_num < 50:
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in correct]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        # missing_states = []
        # for state in all_states:
        #     if state not in correct:
        #         missing_states.append(state)
        # new_data = pandas.DataFrame(missing_states)
        # new_data.to_csv("states_to_learn.csv")

        break
    if answer in all_states and answer not in correct:
        state_data = pd[pd.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)
        correct.append(answer)
        correct_num += 1

    answer = screen.textinput(title= f"{correct_num}/50 States Correct", prompt="What is another state's name?").title()





