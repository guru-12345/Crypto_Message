#Run the code and observe the x and y coordinates.
#Task: Create a new `label3` with text 'bottom-right corner' and place it at the bottom-right.
# Refer the image given in the SRM

import customtkinter as ctk

# Create the main window
root = ctk.CTk()
root.geometry("600x450")  # Window size 600x450

# Adding a label at the top-left corner (0, 0)
label1 = ctk.CTkLabel(root, text="Top-left Corner")
label1.place(x=0, y=0)  #place() is used to position widgets at exact coordinates (x, y).

# Adding a label at the center of the window (300, 225)
label2 = ctk.CTkLabel(root, text="Center of the Window")
label2.place(x=300, y=225)

#Add the new label3 here

# Run the application
root.mainloop()
