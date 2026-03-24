import tkinter as tk

root = tk.Tk()



def main_login():
   login= input("Login Required: ")
   if login == "Zac":
        print("Login Success!")



root.title("OTR Mobile Database")
root.configure(background= "black")
root.minsize(500, 500)
root.maxsize(1920, 1080)

main_window_h1= tk.Label(root, text="Dashboard").pack()

main_window_heroimage= tk.PhotoImage(file= "OTR_Social_Sharing_Logo.PNG")
tk.Label(root, image= main_window_heroimage).pack()


login_textbox= tk.Label(root, text="Login Required: ", anchor= tk.W)
login_textbox.pack()

main_window_button1= tk.Entry(root, text= "Login:")
main_window_button1.pack()
main_window_button1.get()

main_window_button1_entry= print(main_window_button1.get)

root.mainloop()