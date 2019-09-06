import requests
from tkinter import *
import smtplib
weather=''
q=''

def tkinter():
    api = ''
    def query():
        string = entry.get()
        f = string.split(',')
        global q
        if f[0].isalpha():
            q = 'q'
        else:
            q = 'zip'

        try:

            # get weather through API

            url = f'https://api.openweathermap.org/data/2.5/weather?{q}={f[0]},{f[-1]}&appid={api_box.get()}'
            json = requests.get(url).json()
            count = ','.join([json['name'], json['sys']['country']])
            temp = int(json['main']['temp'])
            condition = json['weather'][0]['main']
            global weather
            weather = ('Name: ' + count + '\n' + 'Temp (F): ' + str(temp) + '\n' + 'Condition: ' + condition)
            label['text'] = weather
        except Exception as e:
            label['text'] = f"There was something wrong.\n{e}\nUse zip_code,IN"


    #send email
    def send_weather():
        to_email = str(mail_input.get())
        msg= str(f'Subject:Greeting from ROHIT MAIL SERVICES:\n\n{weather}')
        log = str(log_in.get())
        pas = str(password.get())
        if int(var1.get())==1:
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                label['text'] = 'Log in........'
                server.login(log, pas)
                label['text'] = 'sending email.......'
                server.sendmail(log, to_email, msg)
                label['email'] = 'Sent email!'
                server.quit()
                # mail('pijej@doc-mail.net', 'Subject:Greeting from ROHIT MAIL SERVICE,\n\n')
            except ConnectionError as e:
                label['text'] = str(e)
        else:
            pass



    tk = Tk()
    # title of app
    tk.title('AccWeather')
    tk.geometry('900x600')



    # main canvas with image
    background_image = PhotoImage(file='C:\\Users\\ABC\\Desktop\\Unsplash_photos\\forest.png')
    canvas = Label(tk, image = background_image)
    canvas.place(x=0, y=0, relwidth=1, relheight=1)

    # button and input
    entry = Entry(canvas, bd=0, font=5, fg='black')
    entry.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.6)
    Button(canvas, text='Get Weather',bg='Tomato',font=5, bd=0, command=lambda: query()).place(relx=0.7, rely=.1, relheight=0.1,relwidth=0.2)

    # API box
    Label(canvas, bg='white', text='API key: ').place(relx=0.1, rely=0)
    api_box = Entry(canvas, bd=2, font=3)
    api_box.place(relx=0.2, rely=0, relwidth=.7)
    api_box.insert(0, str(api))


    # output label
    Label(canvas, text='OUTPUT:', fg='black',bg='white', font=5).place(relx=.1, rely=.3)
    # output box
    label = Label(canvas, font=20, anchor='nw', bg='white', justify='left', bd=5)  # border = bd
    label.place(relx=.1, rely=.4, relwidth=.4, relheight=.5)

    # email frame
    mail_frame=Frame(canvas, bg='white')
    mail_frame.place(relx=.6, rely=.4, relwidth=0.3, relheight=0.5)



    var1 = IntVar()  # This is important to access value
    #check box
    email_check=Checkbutton(mail_frame, variable=var1, text='Check to send weather.', bg='white')
    email_check.place(relx=.1, rely=0, relwidth=.8)
    # label and  log in
    log_in = Entry(mail_frame, font=4, bg='white', bd=2, width=25)
    log_in.place(relx=.1, rely=.1, relwidth=.8, relheight=.1)
    log_in.insert(0, 'Email id:')

    # label and password for log in
    password = Entry(mail_frame, font=4, bg='white', bd=2, width=25)
    password.place(relx=.1, rely=.2, relwidth=.8, relheight=.1)
    password.insert(0, 'password:')
    # send email input, whom you wanna send email
    mail_input = Entry(mail_frame, font=5, bg='white', bd=2, width=25)
    mail_input.place(relx=.1, rely=0.4, relwidth=.8, relheight=0.1)
    mail_input.insert(0, 'To:')
    # button to send email
    mail_button = Button(mail_frame, bg='Tomato', text='Send email', command=lambda: send_weather())
    mail_button.place(relx=.3, rely=.5, relwidth=.4, relheight=.1)


    tk.mainloop()

tkinter()








