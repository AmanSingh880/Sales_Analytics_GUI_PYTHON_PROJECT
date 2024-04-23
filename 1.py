import pickle
from tkinter import messagebox
from tkinter import messagebox

def Validate_password(password):
    try:
        file=open("binary.bin","rb")
        original_password=pickle.load(file)
        if(original_password==password):
            file.close()
            return True
        else:
            messagebox.showwarning("Sales Analytic","Incorrect Password")
            file.close()
            return False
    except:
        messagebox.showwarning("Sales Analytic","Data not Found")
    finally:
        return False
        
def reset_password(password):
    def validate_password_reset(password):
        Upper_case=Num=Spec_char=False
        if(len(password)<8):
            messagebox.showwarning("Sales Analytic","Password must have 8 characters")
            return False
        for i in password:
            if(i.isupper()):
                Upper_case=True
            elif(not(i.isalnum())):
                Spec_char=True
            elif(i.isdigit()):
                Num=True
        if(Upper_case and Num and Spec_char):
            return True
        else:
            if(Upper_case):
                if(Num):
                    messagebox.showwarning("Sales Analytic","Password must have special character")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have digits(0-9)")
            elif(Num):
                if(Upper_case):
                    messagebox.showwarning("Sales Analytic","Password must have special character(@-#)")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have Uppercase character(A-Z)")
            else:
                if(Num):
                    messagebox.showwarning("Sales Analytic","Password must have Uppercase character(A-Z)")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have digits(0-9)")
            return False

    
    if(validate_password_reset(password)):
        file=open("binary.bin","wb")
        pickle.dump(password,file)
        file.close()
        messagebox.showwarning("Sales Analytic","Password Changed")
        return True
    else:
        return False
