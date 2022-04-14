import smtplib,time

import tkinter as tk 
from  tkinter.constants import *  
import tkinter.messagebox as tkmessagebox

import  email.mime.multipart 
import  email.mime.text


class SendEmail(tk.Tk):
    #Version 0.15
    def __init__(self):
        super().__init__()
        self.reciveid_email()
        self.proprieter_email()
        self.password_email()
        self.subject_email()
        self.message_to_send_for_email()

        self.btn_send_email = tk.Button(self, text="envoyez l'email", command=self.send_email)
        self.btn_send_email.grid(row=5,column=1)

    def reciveid_email(self): 
        self.label_receveid = tk.Label(self,text="Destinateur:",bg="#1EE") 
        self.entry_r = tk.Entry(self, width=98)

        self.label_receveid.grid(row=0,column=0)
        self.entry_r.grid(row=0,column=1,pady=10)

    def proprieter_email(self): 
        self.label_proprieter = tk.Label(self,text="De:",bg="#1EE")
        self.entry_p = tk.Entry(self, width=98)

        self.label_proprieter.grid(row=1,column=0)
        self.entry_p.grid(row=1,column=1,pady=10)

    def password_email(self):
        self.label_password = tk.Label(self,text="Mot de passe:",bg="#1EE")
        self.entry_pass = tk.Entry(self,show="*",width=98)

        self.label_password.grid(row=2,column=0)
        self.entry_pass.grid(row=2,column=1,pady=10)

    def subject_email(self): 
        self.label_subject = tk.Label(self, text="Object: ", bg="#1EE")
        self.entry_subject = tk.Entry(self,width=98)

        self.label_subject.grid(row=3, column=0)
        self.entry_subject.grid(row=3, column=1, pady=10)

    def message_to_send_for_email(self):
        self.entry_message = tk.Text(self)
        self.entry_message.grid(row=4, column=1, ipadx=10, ipady=10)

    def send_email(self):
        msg = email.mime.multipart.MIMEMultipart()

        msg["Subject"] = self.entry_subject.get()
        msg["From"] = self.entry_p.get()
        msg["To"] =  self.entry_r.get()

        self.password_d =  self.entry_pass.get()
        msgText = email.mime.text.MIMEText(self.entry_message.get("1.0","end"))
        msg.attach(msgText)
         
        with  smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            try: 
                server.login(self.entry_p.get(),self.password_d)
            
            except smtplib.SMTPAuthenticationError: 
                tkmessagebox.showerror("Attention","Le mot de passe ou email incorrect")
            
            except TypeError: 
                tkmessagebox.showinfo("Titre d'info","Entrez un email pour le destinataire (Destinateur), l'email de l'envoyeur (De) avec le mot de passe saisie.")
            
            else: 
                server.sendmail(self.entry_p.get(),self.entry_r.get(),msg.as_string())
        time.sleep(2)



if __name__ == "__main__":
    app = SendEmail()
    app.geometry("850x600")
    app.title("SENDER EMAIL")
    app.config(bg="#1EE")
    app.mainloop()