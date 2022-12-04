from tkinter import *
from mydb import Database
from myapi import API
from tkinter import messagebox


class App:

    def __init__(self):
        self.intent_result = None
        self.emotion_result = None
        self.api_obj = API()
        self.sentiment_result = None
        self.input_text = None
        self.db_obj = Database()
        self.name_input = None
        self.password_input = None
        self.email_input = None
        self.root = Tk()
        self.root.title('Flavour')
        self.root.iconbitmap('images/favicon.ico')
        self.root.geometry('455x600')
        self.root.configure(bg='#D6EAF8')
        self.login_panel()
        self.root.mainloop()

    def login_panel(self):
        self.clear()
        login_label = Label(self.root, text='LOGIN', bg='#D6EAF8', fg='#1B4F72')
        login_label.pack(pady=(40, 30))
        login_label.configure(font=('Big Caslon', 22, 'bold'))

        email_label = Label(self.root, text='EMAIL', font=('Candara', 10, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        email_label.pack(pady=(20, 3))
        self.email_input = Entry(self.root, font=('Century Gothic', 10, 'normal'), borderwidth=5, width=40,
                                 insertbackground='#1B4F72', fg='#21618C')
        self.email_input.pack(pady=(5, 20), ipady=4)

        password_label = Label(self.root, text='PASSWORD', font=('Candara', 10, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        password_label.pack(pady=(10, 3))
        self.password_input = Entry(self.root, font=('Century Gothic', 10, 'normal'), borderwidth=5, width=40,
                                    insertbackground='#1B4F72', fg='#21618C', show='*')
        self.password_input.pack(pady=(5, 20), ipady=4)

        login_btn = Button(self.root, text='LOGIN', font=('Candara', 10, 'bold'), bd=5, bg='#28B463',
                           fg='black', width=20, borderwidth=5, activeforeground='black',
                           activebackground='#D6EAF8', height=2, command=self.invoke_login_btn)
        login_btn.pack(pady=(10, 10))

        doRegister_label = Label(self.root, text='New to Flavour? Register Now', font=('Candara', 10, 'bold'),
                                 fg='#1B4F72', bg='#D6EAF8')
        doRegister_label.pack(pady=(20, 3))
        redirect_btn = Button(self.root, text='REGISTER NOW', font=('Candara', 10, 'bold'), bd=5, bg='#F1C40F',
                              fg='black', width=20, borderwidth=5, activeforeground='black',
                              activebackground='#D6EAF8', height=2, command=self.register_panel)
        redirect_btn.pack(pady=(10, 10))

    def register_panel(self):
        self.clear()
        register_label = Label(self.root, text='REGISTER', bg='#D6EAF8', fg='#1B4F72')
        register_label.pack(pady=(40, 30))
        register_label.configure(font=('Big Caslon', 22, 'bold'))

        name_label = Label(self.root, text='Enter Name', font=('Candara', 10, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        name_label.pack(pady=(5, 3))
        self.name_input = Entry(self.root, font=('Century Gothic', 10, 'normal'), borderwidth=5, width=40,
                                insertbackground='#1B4F72', fg='#21618C')
        self.name_input.pack(pady=(5, 20), ipady=4)

        email_label = Label(self.root, text='Enter Email', font=('Candara', 10, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        email_label.pack(pady=(10, 3))
        self.email_input = Entry(self.root, font=('Century Gothic', 10, 'normal'), borderwidth=5, width=40,
                                 insertbackground='#1B4F72', fg='#21618C')
        self.email_input.pack(pady=(5, 20), ipady=4)

        password_label = Label(self.root, text='Enter Password', font=('Candara', 10, 'bold'), fg='#1B4F72',
                               bg='#D6EAF8')
        password_label.pack(pady=(10, 3))
        self.password_input = Entry(self.root, font=('Century Gothic', 10, 'normal'), borderwidth=5, width=40,
                                    insertbackground='#1B4F72', fg='#21618C', show='*')
        self.password_input.pack(pady=(5, 20), ipady=4)

        register_btn = Button(self.root, text='REGISTER', font=('Candara', 10, 'bold'), bd=5, bg='#2E86C1',
                              fg='black', width=20, borderwidth=5, activeforeground='black',
                              activebackground='#D6EAF8', height=2, command=self.invoke_register_btn)
        register_btn.pack(pady=(10, 10))

        alreadyRegister_label = Label(self.root, text='Already a member? Login', font=('Candara', 10, 'bold'),
                                      fg='#1B4F72', bg='#D6EAF8')
        alreadyRegister_label.pack(pady=(10, 3))
        redirect_btn = Button(self.root, text='LOGIN HERE', font=('Candara', 10, 'bold'), bd=5, bg='#28B463',
                              fg='black', width=20, borderwidth=5, activeforeground='black',
                              activebackground='#D6EAF8', height=2, command=self.login_panel)
        redirect_btn.pack(pady=(10, 5))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def invoke_register_btn(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        user_data = self.db_obj.add_data(name, email, password)
        if user_data:
            messagebox.showinfo('Success', 'Successfully registered!. Login Now.')
        else:
            messagebox.showerror('Error', 'Email Already exists! Try different email.')

    def invoke_login_btn(self):
        email = self.email_input.get()
        password = self.password_input.get()

        credentials = self.db_obj.match(email, password)
        if credentials:
            self.main_panel()
        else:
            messagebox.showerror('Error', 'Incorrect credentials.')

    def main_panel(self):
        self.clear()
        app_label = Label(self.root, text='FLAVOUR', bg='#D6EAF8', fg='#1B4F72')
        app_label.pack(pady=(20, 10))
        app_label.configure(font=('Big Caslon', 22, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', font=('Candara', 10, 'bold'), bd=10, bg='#F1C40F',
                               fg='black', width=40, borderwidth=5, activeforeground='black',
                               activebackground='#D6EAF8', height=5, command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotions Analysis', font=('Candara', 10, 'bold'), bd=10, bg='#F1C40F',
                             fg='black', width=40, borderwidth=5, activeforeground='black',
                             activebackground='#D6EAF8', height=5, command=self.emotion_analysis)
        emotion_btn.pack(pady=(10, 10))

        intent_btn = Button(self.root, text='Intent Analysis', font=('Candara', 10, 'bold'), bd=10, bg='#F1C40F',
                            fg='black', width=40, borderwidth=5, activeforeground='black',
                            activebackground='#D6EAF8', height=5, command=self.intent_analysis)
        intent_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='LOGOUT', font=('Candara', 10, 'bold'), bd=10, bg='#E74C3C',
                            fg='black', width=20, borderwidth=5, activeforeground='black',
                            activebackground='#D6EAF8', height=3, command=self.login_panel)
        logout_btn.pack(pady=(10, 10))

    def sentiment_analysis(self):
        self.clear()
        sentiment_label = Label(self.root, text='SENTIMENT ANALYSIS', bg='#D6EAF8', fg='#1B4F72')
        sentiment_label.pack(pady=(30, 20))
        sentiment_label.configure(font=('Big Caslon', 22, 'bold'))

        text_label = Label(self.root, text='Enter Text', font=('Candara', 10, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        text_label.pack(pady=(5, 3))

        self.input_text = Text(self.root, width=40, height=10, font=('Century Gothic', 10, 'normal'), borderwidth=5,
                               insertbackground='#1B4F72', fg='#21618C')
        self.input_text.pack(pady=(2, 1))

        sentiment_btn = Button(self.root, text='Analyze', font=('Candara', 10, 'bold'), bd=5, bg='#28B463',
                               fg='black', width=15, borderwidth=5, activeforeground='black',
                               activebackground='#D6EAF8', height=2, command=self.invoke_sentiment_btn)
        sentiment_btn.pack(pady=(1, 2))

        self.sentiment_result = Label(self.root, text='', font=('Candara', 15, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        self.sentiment_result.pack(pady=(10, 5))

        goback_btn = Button(self.root, text='Back', font=('Candara', 10, 'bold'), bd=5, bg='#E74C3C',
                            fg='black', width=15, borderwidth=5, activeforeground='black',
                            activebackground='#D6EAF8', height=2, command=self.main_panel)
        goback_btn.pack(pady=(1, 2))

    def invoke_sentiment_btn(self):
        text = self.input_text.get(1.0, END)
        sentiment_analysis_result = self.api_obj.sentiment_analysis(text)

        txt = ''
        for i in sentiment_analysis_result['sentiment']:
            txt = txt + i + ' : ' + str(sentiment_analysis_result['sentiment'][i]) + '\n'

        self.sentiment_result['text'] = txt

    def emotion_analysis(self):
        self.clear()
        emotion_label = Label(self.root, text='EMOTIONS ANALYSIS', bg='#D6EAF8', fg='#1B4F72')
        emotion_label.pack(pady=(30, 20))
        emotion_label.configure(font=('Big Caslon', 22, 'bold'))

        text_label = Label(self.root, text='Enter Text', font=('Candara', 10, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        text_label.pack(pady=(5, 3))

        self.input_text = Text(self.root, width=40, height=10, font=('Century Gothic', 10, 'normal'), borderwidth=5,
                               insertbackground='#1B4F72', fg='#21618C')
        self.input_text.pack(pady=(2, 1))

        emotion_btn = Button(self.root, text='Analyze', font=('Candara', 10, 'bold'), bd=5, bg='#28B463',
                             fg='black', width=15, borderwidth=5, activeforeground='black',
                             activebackground='#D6EAF8', height=2, command=self.invoke_emotion_btn)
        emotion_btn.pack(pady=(1, 2))

        self.emotion_result = Label(self.root, text='', font=('Candara', 15, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        self.emotion_result.pack(pady=(10, 2))

        goback_btn = Button(self.root, text='Back', font=('Candara', 10, 'bold'), bd=5, bg='#E74C3C',
                            fg='black', width=15, borderwidth=5, activeforeground='black',
                            activebackground='#D6EAF8', height=2, command=self.main_panel)
        goback_btn.pack(pady=(1, 1))

    def invoke_emotion_btn(self):
        text = self.input_text.get(1.0, END)
        emotion_analysis_result = self.api_obj.emotions_analysis(text)

        txt = ''
        for i in emotion_analysis_result['emotion']:
            txt = txt + i + ' : ' + str(emotion_analysis_result['emotion'][i]) + '\n'

        self.emotion_result['text'] = txt

    def intent_analysis(self):
        self.clear()
        intent_label = Label(self.root, text='INTENT ANALYSIS', bg='#D6EAF8', fg='#1B4F72')
        intent_label.pack(pady=(30, 20))
        intent_label.configure(font=('Big Caslon', 22, 'bold'))

        text_label = Label(self.root, text='Enter Text', font=('Candara', 10, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        text_label.pack(pady=(5, 3))

        self.input_text = Text(self.root, width=40, height=10, font=('Century Gothic', 10, 'normal'), borderwidth=5,
                               insertbackground='#1B4F72', fg='#21618C')
        self.input_text.pack(pady=(2, 1))

        intent_btn = Button(self.root, text='Analyze', font=('Candara', 10, 'bold'), bd=5, bg='#28B463',
                            fg='black', width=15, borderwidth=5, activeforeground='black',
                            activebackground='#D6EAF8', height=2, command=self.invoke_intent_btn)
        intent_btn.pack(pady=(1, 2))

        self.intent_result = Label(self.root, text='', font=('Candara', 15, 'bold'), fg='#1B4F72', bg='#D6EAF8')
        self.intent_result.pack(pady=(10, 5))

        goback_btn = Button(self.root, text='Back', font=('Candara', 10, 'bold'), bd=5, bg='#E74C3C',
                            fg='black', width=15, borderwidth=5, activeforeground='black',
                            activebackground='#D6EAF8', height=2, command=self.main_panel)
        goback_btn.pack(pady=(1, 2))

    def invoke_intent_btn(self):
        text = self.input_text.get(1.0, END)
        intent_analysis_result = self.api_obj.intent_analysis(text)

        txt = ''

        for i in intent_analysis_result['intent']:
            txt = txt + i + ' : ' + str(intent_analysis_result['intent'][i]) + '\n'

        self.intent_result['text'] = txt


application = App()
