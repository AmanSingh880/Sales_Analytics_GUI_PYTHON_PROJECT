import pickle
from tkinter import messagebox
#here we will add all modules
def Validate_password(password):
    #complete the module
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
    #complete the module
    def validate_password_reset(password):
        #complete the modue
        Upper_case=Num=Spec_char=False
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
            messagebox.showwarning("Sales Analytic","Not Valid")
            #changes required
            
    if(validate_password_reset(password)):
        file=open("binary.bin","wb")
        pickle.dump(password,file)
        file.close()
        messagebox.showwarning("Sales Analytic","Password Changed")
        return True
    else:
        return False


