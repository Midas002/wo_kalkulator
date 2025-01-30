import tkinter as tk

# Function to toggle the label value between 0 and 1
def toggle_label(label, index):
    current_value = label_values[index]
    new_value = 1 if current_value == 0 else 0
    label.config(text=str(new_value))
    label_values[index] = new_value

# Function to convert the list of values to a string
def convert_list_to_string():
    result_string = ''.join(map(str, label_values))
    print("Current values as string:", result_string)

# Initialize the main window
root = tk.Tk()
root.title("Clickable Labels")

# Create a list to store the values of the labels
label_values = [0] * 64

# Create a 8x8 grid of labels
for i in range(64):
    row = i // 8
    col = i % 8

    # Create a label with initial value 0
    label = tk.Label(root, text="0", width=4, height=2, relief="raised", bg="lightgray")
    label.grid(row=row, column=col, padx=5, pady=5)

    # Bind the label to a click event
    label.bind("<Button-1>", lambda event, idx=i, lbl=label: toggle_label(lbl, idx))

# Add a button to convert the list to a string
convert_button = tk.Button(root, text="Convert to String", command=convert_list_to_string)
convert_button.grid(row=8, column=0, columnspan=8, pady=10)

# Start the tkinter main loop
root.mainloop()