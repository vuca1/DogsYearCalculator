import tkinter as tk

def main():

    # create main window
    window = tk.Tk()
    window.title("Dog Year Calculator 🐕")
    window.geometry("300x150")
    window.resizable(False, False)

    # add entry and label from user for age
    year_label = tk.Label(window, text="Enter your age: ")
    year_label.pack(pady=5)
    year_entry = tk.Entry(window, width=20)
    year_entry.pack(pady=5)

    # get information from the entry and return it after button event
    output_label = tk.Label(window, text="")
    output_label.pack(pady=5)

    # transfer human age to dog age
    def calculate_to_dog():
        try:
            entry = (int(year_entry.get()))/7
            entry = str(entry)
            output_label.config(text=entry)
        except ValueError as e:
            output_label.config(text="Wrong input!")

    # transfer dog age to human age
    def calculate_to_human():
        try:
            entry = (int(year_entry.get()))*7
            entry = str(entry)
            output_label.config(text=entry)
        except ValueError as e:
            output_label.config(text="Wrong input!")

    # buttons frame
    button_frame = tk.Frame(window)
    button_frame.pack(pady=5)

    # buttons to trigger calculation dog age <-> human age
    human_to_dog = tk.Button(button_frame, text="Human to Dog", command= calculate_to_dog)
    human_to_dog.grid(row=0, column= 0, padx=5, pady=5)

    dog_to_human = tk.Button(button_frame, text="Dog to Human", command=calculate_to_human)
    dog_to_human.grid(row=0, column=1, padx=5, pady=5)

    # todo - make buttons next to each other

    window.mainloop()

if __name__ == "__main__":
    main()