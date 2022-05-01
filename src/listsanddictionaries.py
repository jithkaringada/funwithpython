# movie schedule
movieschedule = {
    'Batman': ["10:00am", "1:00pm", "5:00pm", "10:00pm"],
    'Spiderman': ["9:00am", "1:00pm", "4:00pm", "6:30pm", "9:00pm"],
    'Home Alone': ["3:00pm", "6:00pm"]
}

print('We are showing the following movies:\n')
for k in movieschedule:
    print('The', k, ' movie is showing at ', movieschedule.get(k))