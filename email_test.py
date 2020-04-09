import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def gui():
    
    def sendmail():
        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465
        username = 'temp.mail.mca@gmail.com'
        password = 'qwerty@1234'
        sender = 'temp.mail.mca@gmail.com'
        targets = to_ent.get()
        msg = MIMEMultipart()
        msg = MIMEText(body_text.get("1.0",'end-1c'))
        msg['To'] = to_ent.get()
        msg['From'] = sender
        msg['CC'] = cc_ent.get()
        msg['BCC'] = bcc_ent.get()
        msg['Subject'] = sub_ent.get()
        
              
        try:
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            server.sendmail(sender, targets, msg.as_string())
        except Exception as e:
            print("error is: ", e)
        
    root = tk.Tk()
    root.title("Compose Mail")
   
    to_lbl = tk.Label(root,text="To:")
    cc_lbl = tk.Label(root,text="CC:")
    bcc_lbl = tk.Label(root,text="BCC:")
    sub_lbl = tk.Label(root,text="Subject:")
    body_lbl = tk.Label(root,text="Message:")
    to_ent = tk.Entry(root, width = 40)
    cc_ent = tk.Entry(root, width = 40)
    bcc_ent = tk.Entry(root, width = 40)
    sub_ent = tk.Entry(root, width = 40)
    body_text = tk.Text(root, wrap = 'word', height = 16, width = 60)
    submit_btn = tk.Button(root, text = "Submit", command = sendmail)
    att_btn = tk.Button(root, text = "Attach File")
    
    to_lbl.place(x = 5,y = 5)
    to_ent.place(x = 35,y = 5)
    cc_lbl.place(x = 5,y = 35)
    cc_ent.place(x = 35,y = 35)
    bcc_lbl.place(x = 5,y = 65)
    bcc_ent.place(x = 40,y = 65)
    sub_lbl.place(x = 5,y = 95)
    sub_ent.place(x = 55,y = 95)
    att_btn.place(x = 5,y = 125)
    body_lbl.place(x = 5,y = 155)
    body_text.place(x = 5,y = 175)
    submit_btn.place(x = 5,y = 440)
        
    root.geometry("500x500")
    
    root.mainloop()

if __name__=="__main__":
    gui()