import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow

from LogInPage import Ui_LogInPage
from SignUpPage import Ui_SignUpPage
from MainPage import Ui_MainPage
from RecomendationsPage import Ui_RecPage
from BookTheTicketPage import Ui_BookTheTicketPage
from BeyoncePage import Ui_BeyoncePage
from LanaPage import Ui_LanaPage
from WeekendPage import Ui_WeekendPage
from BilliePage import Ui_BilleiPage
from AccountPage import Ui_AccountPage
from TheBillPage import Ui_TheBillPage
from AAA import recommend_songs_from_db


conn = sqlite3.connect('UserInfo.sqlite3')
conn.row_factory = sqlite3.Row
c = conn.cursor()

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # LOGIN
        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = Ui_LogInPage()
        self.login_ui.setupUi(self.login_window)
        self.login_ui.AgreementCheckBox.setEnabled(False)
        self.login_ui.LogInBtn.setEnabled(False)
        self.login_ui.UsernameInput.textChanged.connect(self.check_inputs)
        self.login_ui.PasswordInput.textChanged.connect(self.check_inputs)
        self.login_ui.AgreementCheckBox.stateChanged.connect(self.toggle_login_btn)
        self.username = self.login_ui.LogInBtn.clicked.connect(self.Login)
        self.login_ui.SignUpPagebtn.clicked.connect(self.showSignup)

        # SIGNUP
        self.signup_window = QtWidgets.QMainWindow()
        self.signup_ui = Ui_SignUpPage()
        self.signup_ui.setupUi(self.signup_window)
        self.signup_ui.AgreementCheckBox.stateChanged.connect(self.toggle_signup_btn)
        self.signup_ui.SignUpBtn.clicked.connect(self.SignUp)
        self.signup_ui.LogInbtn.clicked.connect(self.showLogin)
        self.signup_ui.AgreementCheckBox.stateChanged.connect(self.toggle_signup_btn)
        self.signup_ui.SignUpBtn.setEnabled(False)
        self.login_window.show()

        # MAIN PAGE

        self.main_window = QtWidgets.QMainWindow()
        self.main_ui = Ui_MainPage()
        self.main_ui.setupUi(self.main_window)
        self.main_ui.BookBtn.clicked.connect(self.OpenBooking)
        self.main_ui.RecBtn.clicked.connect(self.OpenRecs)
        self.main_ui.RecBtn.clicked.connect(self.Top5)
        self.main_ui.RecBtn.clicked.connect(self.Recs)
        self.main_ui.SignOutbtn.clicked.connect(self.Signout)
        self.main_ui.AccountBtn.clicked.connect(self.OpenAccount)
        self.main_ui.AccountBtn.clicked.connect(self.UserStuff)


        # BOOKTHETICKETS

        self.BookTheTicket_window = QtWidgets.QMainWindow()
        self.book_ui = Ui_BookTheTicketPage()
        self.book_ui.setupUi(self.BookTheTicket_window)
        self.book_ui.HMHASbtn.clicked.connect(self.BillEyelash_btt)
        self.book_ui.LDRUKBtn.clicked.connect(self.CrossedLegs_btt)
        self.book_ui.AHTDBtn.clicked.connect(self.EyeGuy_btt)
        self.book_ui.CCBtn.clicked.connect(self.LowPolyNPCLookinAhh_btt)
        self.book_ui.BTTBackBtn.clicked.connect(self.BTTbackBtn)


        # BEYONCE

        self.Beyonce_window = QtWidgets.QMainWindow()
        self.Beyonce_ui = Ui_BeyoncePage()
        self.Beyonce_ui.setupUi(self.Beyonce_window)
        self.Beyonce_ui.BeyonceBackBtn.clicked.connect(self.BeyonceBackBtn)
        self.Beyonce_ui.QuantityCheckBtn.clicked.connect(self.setup_Beyonce_checkbox_counter)
        self.Beyonce_ui.ConfirmBeyonceBtn.setEnabled(False)
        self.Beyonce_ui.QuantityCheckBtn.clicked.connect(lambda : self.Beyonce_ui.ConfirmBeyonceBtn.setEnabled(True))
        self.Beyonce_ui.ConfirmBeyonceBtn.clicked.connect(self.confirmBeyonce)
        self.Beyonce_ui.PayBeyonceBtn.clicked.connect(self.BuyBeyonce)
        self.Beyonce_ui.PayBeyonceBtn.setEnabled(False)
        self.Beyonce_ui.BalanceNotEnoughMessage.setHidden(True)


        # BILLIE

        self.Billie_window = QtWidgets.QMainWindow()
        self.Billie_ui = Ui_BilleiPage()
        self.Billie_ui.setupUi(self.Billie_window)
        self.Billie_ui.BillieBackBtn.clicked.connect(self.BillieBackBtn)
        self.Billie_ui.QuantityCheckBtn.clicked.connect(self.setup_Billie_checkbox_counter)
        self.Billie_ui.ConfirmBillieBtn.setEnabled(False)
        self.Billie_ui.QuantityCheckBtn.clicked.connect(lambda : self.Billie_ui.ConfirmBillieBtn.setEnabled(True))
        self.Billie_ui.ConfirmBillieBtn.clicked.connect(self.confirmBillie)
        self.Billie_ui.PayBillieBtn.clicked.connect(self.BuyBillie)
        self.Billie_ui.PayBillieBtn.setEnabled(False)
        self.Billie_ui.BalanceNotEnoughMessage.setHidden(True)


        # LANA

        self.Lana_window = QtWidgets.QMainWindow()
        self.Lana_ui = Ui_LanaPage()
        self.Lana_ui.setupUi(self.Lana_window)
        self.Lana_ui.LanaBackBtn.clicked.connect(self.LanaBackBtn)
        self.Lana_ui.QuantityCheckBtn.clicked.connect(self.setup_Lana_checkbox_counter)
        self.Lana_ui.ConfirmLanaBtn.setEnabled(False)
        self.Lana_ui.QuantityCheckBtn.clicked.connect(lambda: self.Lana_ui.ConfirmLanaBtn.setEnabled(True))
        self.Lana_ui.ConfirmLanaBtn.clicked.connect(self.confirmLana)
        self.Lana_ui.PayLanaBtn.clicked.connect(self.BuyLana)
        self.Lana_ui.PayLanaBtn.setEnabled(False)
        self.Lana_ui.BalanceNotEnoughMessage.setHidden(True)


        # WEEKEND

        self.Weekend_window = QtWidgets.QMainWindow()
        self.Weekend_ui = Ui_WeekendPage()
        self.Weekend_ui.setupUi(self.Weekend_window)
        self.Weekend_ui.WeekendBackBtn.clicked.connect(self.WeekendBackBtn)
        self.Weekend_ui.QuantityCheckBtn.clicked.connect(self.setup_Weekend_checkbox_counter)
        self.Weekend_ui.ConfirmWeekendBtn.setEnabled(False)
        self.Weekend_ui.QuantityCheckBtn.clicked.connect(lambda: self.Weekend_ui.ConfirmWeekendBtn.setEnabled(True))
        self.Weekend_ui.ConfirmWeekendBtn.clicked.connect(self.confirmWeekend)
        self.Weekend_ui.PayWeekendBtn.clicked.connect(self.BuyWeekend)
        self.Weekend_ui.PayWeekendBtn.setEnabled(False)
        self.Weekend_ui.BalanceNotEnoughMessage.setHidden(True)


        # THEBILLPAGE

        self.Bill_window = QtWidgets.QMainWindow()
        self.Bill_ui = Ui_TheBillPage()
        self.Bill_ui.setupUi(self.Bill_window)
        self.Bill_ui.TheBillBackBtn.clicked.connect(self.BillBackBtn)


        # ACCOUNT

        self.Account_window = QtWidgets.QMainWindow()
        self.Account_ui = Ui_AccountPage()
        self.Account_ui.setupUi(self.Account_window)
        self.Account_ui.AccountBackBtn.clicked.connect(self.ACCBack)
        self.Account_ui.EYERadio.clicked.connect(self.toggled)
        self.Account_ui.ChangeUsernameBtn.clicked.connect(self.NameChange)
        self.Account_ui.ChangePasswordBtn.clicked.connect(self.PasswordChange)
        self.Account_ui.NewUsername.setHidden(True)
        self.Account_ui.KeepNewUsernameBtn.setHidden(True)
        self.Account_ui.NewPassword.setHidden(True)
        self.Account_ui.KeepNewPasswordBtn.setHidden(True)
        self.Account_ui.NewBalance.setHidden(True)
        self.Account_ui.KeepNewBalanceBtn.setHidden(True)
        self.Account_ui.ChangeBalanceBtn.clicked.connect(self.BalanceChange)
        self.Account_ui.YesBtn.clicked.connect(self.DelUser)


        # RECOMENDATIONS

        self.Rec_window = QtWidgets.QMainWindow()
        self.Rec_ui = Ui_RecPage()
        self.Rec_ui.setupUi(self.Rec_window)
        self.Rec_ui.RecBackBtn.clicked.connect(self.RECBackBtn)
        self.Rec_ui.GenerateBtn.clicked.connect(self.Recs)

    #### ბალანსის ამოღება DB დან
    def BalanceCheck(self):     
        return c.execute(f'SELECT Balance FROM UserInformation WHERE UserName="{self.username}"').fetchone()

    #### ყველგან აახლებს Balance label
    def BalanceUpdate(self):
        Balance = c.execute(f'SELECT Balance FROM UserInformation WHERE UserName="{self.username}"').fetchone()[0]
        print(Balance)
        self.main_ui.MainBalanceLabel.setText(f"Balance:{str(Balance)}$")
        self.Account_ui.AccountBalanceLabel.setText(f"Balance:{str(Balance)}$")
        self.Billie_ui.BillieBalanceLabel.setText(f"Balance:{str(Balance)}$")
        self.Beyonce_ui.BeyonceBalanceLabel.setText(f"Balance:{str(Balance)}$")
        self.Lana_ui.LanaBalanceLabel.setText(f"Balance:{str(Balance)}$")
        self.Weekend_ui.WeekendBalanceLabel.setText(f"Balance:{str(Balance)}$")
        self.book_ui.BTTBalanceLabel.setText(f"Balance:{str(Balance)}$")








    ####                        LOGIN

    #### ამოწმებს შეყვანილია თუ არა საკმარისი ინფორმაციაა 
    def check_inputs(self):
        username = self.login_ui.UsernameInput.text()
        password = self.login_ui.PasswordInput.text()
        enable = bool(username and password)
        self.login_ui.AgreementCheckBox.setEnabled(enable)
        if not enable:
            self.login_ui.LogInBtn.setEnabled(False)
            self.login_ui.AgreementCheckBox.blockSignals(True)
            self.login_ui.AgreementCheckBox.setChecked(False)
            self.login_ui.AgreementCheckBox.blockSignals(False)

    #### login btn ჩართვა
    def toggle_login_btn(self, state):
        self.login_ui.LogInBtn.setEnabled(state == QtCore.Qt.Checked)
        
    #### არასწორი პაროლის დროს გამოიყენება. ათავისუფლებს პაროლის ველს.
    def passwordReset(self):
        self.login_ui.PasswordInput.clear()
        
    #### არესტარტებს login page ს
    def loginPageReset(self, wrong_type):
        if wrong_type == "username":
            self.login_ui.ErrorLabel.setText("Wrong username")
        else:
            self.login_ui.ErrorLabel.setText("Wrong password")
        self.login_ui.AgreementCheckBox.setEnabled(False)
        self.login_ui.LogInBtn.setEnabled(False)
        self.login_ui.UsernameInput.setText("")
        self.login_ui.PasswordInput.setText("")
    
    #### Login ფუნქცია სადაც რეგისტრაციის მაგია ხდება
    def Login(self):
        username1 = self.login_ui.UsernameInput.text()
        password = self.login_ui.PasswordInput.text()
        try:
            result = c.execute('SELECT Password FROM UserInformation WHERE Username = ?', (username1,)).fetchone()
            if result:
                if password == result['Password']:
                    print(f"{username1} login successful")
                    self.username = username1
                    self.login_window.close()
                    self.main_window.show()
                    self.login_ui.PasswordInput.clear()
                    self.BalanceUpdate()
                    self.main_ui.UsernameLabel.setText(self.username)
                else:
                    print("wrong password")
                    self.loginPageReset("password")
            else:
                print("wrong username")
                self.loginPageReset("username")
        except Exception as e:
            print(f"Login error: {e}")
            self.login_ui.ErrorLabel.setText("An error occurred")
        return username1



####                                                                    SIGNUP
    
    ####signup button ს ჩართვა 
    def toggleSignupBtn(self, state):
        self.signup_ui.SignUpBtn.setEnabled(state == QtCore.Qt.Checked)

    ####
    def SignupPageReset(self):
        self.signup_ui.AgreementCheckBox.setEnabled(False)
        self.signup_ui.SignUpBtn.setEnabled(False)
        self.signup_ui.NewUsernameInput.setText("")
        self.signup_ui.NewPasswordInput.setText("")
        self.signup_ui.RetypePasswordInput.setText("")

    #### signup page ჩვენება
    def showSignup(self):
        self.login_window.close()
        self.signup_window.show()

    #### login page show
    def showLogin(self):
        self.signup_window.close()
        self.login_window.show()

    #### ჯადოსნური ფუნქიცა Signup
    def SignUp(self):
        username = self.signup_ui.NewUsernameInput.text()
        password = self.signup_ui.NewPasswordInput.text()
        retype = self.signup_ui.RetypePasswordInput.text()
        existing = c.execute('SELECT Username FROM UserInformation WHERE Username = ?', (username,)).fetchone()
        if not username or not password:
            self.signup_ui.ErrorLabel.setText("Please fill all fields")


        elif password != retype:
            self.signup_ui.ErrorLabel.setText("Passwords do not match")
            self.signup_ui.NewPasswordInput.setText("")
            self.signup_ui.RetypePasswordInput.setText("")


        elif existing:
            self.signup_ui.ErrorLabel.setText("User already exists")
            # self.SignUpPageReset()
        else:
            try:
                c.execute('INSERT INTO UserInformation (Username, Password) VALUES (?, ?)', (username, password))
                conn.commit()
                self.signup_ui.ErrorLabel.setText("Registration successful!")
                self.signup_window.close()
                self.login_window.show()
            except Exception as e:
                self.signup_ui.ErrorLabel.setText("Error during registration")
                print(f"SignUp error: {e}")


####                                                        MAIN PAGE
    #### ხსნიან შესაბამის ფანჯრებს/გვერდებს
    def OpenBooking(self):
        self.main_window.close()
        self.BookTheTicket_window.show()
    def OpenRecs(self):
        self.main_window.close()
        self.Rec_window.show()
    def OpenAccount(self):
        self.main_window.close()
        self.Account_window.show()

    #### self-explanatory
    def Signout(self):
        self.main_window.close()
        self.login_window.show()



####                                                            BOOKTHETICKET

####ხსნიან შესაბამის ფანჯრებს
    def BillEyelash_btt(self):
        self.BookTheTicket_window.close()
        self.Billie_window.show()
        ArtistName = "Billie Eilish"
        DateA = ""
        self.Bill_ui.BillArtistLabel.setText(ArtistName)
        self.Bill_ui.BillDateLabel.setText(DateA)
    def CrossedLegs_btt(self):
        self.BookTheTicket_window.close()
        self.Lana_window.show()
        ArtistName = "Lana"
        DateA = ""
        self.Bill_ui.BillArtistLabel.setText(ArtistName)
        self.Bill_ui.BillDateLabel.setText(DateA)
    def EyeGuy_btt(self):
        self.BookTheTicket_window.close()
        self.Weekend_window.show()
        ArtistName = "Weekend"
        DateA = ""
        self.Bill_ui.BillArtistLabel.setText(ArtistName)
        self.Bill_ui.BillDateLabel.setText(DateA)
    def LowPolyNPCLookinAhh_btt(self):
        self.BookTheTicket_window.close()
        self.Beyonce_window.show()
        ArtistName = "Beyonce"
        DateA = ""
        self.Bill_ui.BillArtistLabel.setText(ArtistName)
        self.Bill_ui.BillDateLabel.setText(DateA)

    ####go back button(return to main page),  ყველა ანალოგიური button სგავსი სახელითაა
    def BTTbackBtn(self):
        self.BookTheTicket_window.close()
        self.main_window.show()

####                                                            BILL PAGE

    def BillBackBtn(self):
        self.Bill_window.close()
        self.BookTheTicket_window.show()

####                                                            ACCOUNT
    def ACCBack(self):
        self.Account_window.close()
        self.main_window.show()

    #### ავსებს Account page ს შესაბამისი ინფორმაციით.
    def UserStuff(self):

        self.main_ui.UsernameLabel.setText(self.username)
        self.Account_ui.AccountUsernameLabel.setText(self.username)

        password_row = c.execute(f"SELECT Password FROM UserInformation WHERE Username = ?", (self.username,)).fetchone()
        password = password_row["Password"] if password_row else ""
        self.Account_ui.AccountPasswordLabel.setText("*"*len(password))


        self.BalanceUpdate()

    #### პაროლს აქცევს ფიფქებად პაროლის ველში Account Page ზე.
    #### Toggle ის გამოყენებით შეგიძლია გამოაჩინო ეს პაროლი
    def PasswordEncriotonRadio(self):
        password_row = c.execute(f"SELECT Password FROM UserInformation WHERE Username = ?",
                                 (self.username,)).fetchone()
        password = password_row["Password"] if password_row else ""
        self.Account_ui.AccountPasswordLabel.setText("*"*len(password))
    def PasswordDecryption(self):
        password_row = c.execute(f"SELECT Password FROM UserInformation WHERE Username = ?",
                                 (self.username,)).fetchone()
        password = password_row["Password"] if password_row else ""
        self.Account_ui.AccountPasswordLabel.setText(password)
    def toggled(self):
        if self.Account_ui.EYERadio.isChecked():
            self.PasswordDecryption()
        else:
            self.PasswordEncriotonRadio()

    #### name change and the helper funciton. same for password and Balance change
    def NameChange(self):
        self.Account_ui.NewUsername.setHidden(False)
        self.Account_ui.KeepNewUsernameBtn.setHidden(False)
        self.Account_ui.NewUsername.setEnabled(True)
        self.Account_ui.KeepNewUsernameBtn.setEnabled(True)
        self.Account_ui.KeepNewUsernameBtn.clicked.connect(self.DoIt)
    def DoIt(self):
        NewUserName = self.Account_ui.NewUsername.text()
        c.execute('UPDATE UserInformation SET UserName = ? WHERE UserName = ?', (NewUserName, self.username))
        conn.commit()
        self.username = NewUserName
        self.Account_window.close()
        self.Account_window.show()
        self.Account_ui.AccountUsernameLabel.setText(NewUserName)
        self.Account_ui.NewUsername.setHidden(True)
        self.Account_ui.KeepNewUsernameBtn.setHidden(True)

    def PasswordChange(self):
        self.Account_ui.NewPassword.setHidden(False)
        self.Account_ui.KeepNewPasswordBtn.setHidden(False)
        self.Account_ui.NewPassword.setEnabled(True)
        self.Account_ui.KeepNewPasswordBtn.setEnabled(True)
        self.Account_ui.KeepNewPasswordBtn.clicked.connect(self.PasswordDoIt)
    def PasswordDoIt(self):
        NewPassword = self.Account_ui.NewPassword.text()
        c.execute('UPDATE UserInformation SET Password = ? WHERE UserName = ?', (NewPassword, self.username))
        conn.commit()
        self.Account_window.close()
        self.Account_window.show()
        self.Account_ui.NewPassword.setHidden(True)
        self.Account_ui.KeepNewPasswordBtn.setHidden(True)
        self.Account_ui.AccountPasswordLabel.setText(NewPassword)

    def BalanceChange(self):
        self.Account_ui.NewBalance.setHidden(False)
        self.Account_ui.KeepNewBalanceBtn.setHidden(False)
        self.Account_ui.NewBalance.setEnabled(True)
        self.Account_ui.KeepNewBalanceBtn.setEnabled(True)
        self.Account_ui.KeepNewBalanceBtn.clicked.connect(self.BalanceDoIt)
    def BalanceDoIt(self):
        NewBalance = self.Account_ui.NewBalance.text()
        c.execute('UPDATE UserInformation SET Balance = ? WHERE UserName = ?', (NewBalance, self.username))
        conn.commit()

        self.BalanceUpdate()
        self.Account_window.close()
        self.Account_window.show()
        self.Account_ui.NewBalance.setHidden(True)
        self.Account_ui.KeepNewBalanceBtn.setHidden(True)

    #### Self explanatory
    def DelUser(self):
        c.execute('DELETE FROM UserInformation WHERE UserName = ?', (self.username,))
        conn.commit()
        self.Account_window.close()
        self.login_window.show()

####                                                            BEYONCE
    def BeyonceBackBtn(self):
        self.Beyonce_window.close()
        self.BookTheTicket_window.show()

    #### beyonce ს page ის სტრუქტურის ფუნქციები და მისი დამხმარე ფუნქციები
    def count_checked_Beyonce_checkboxes(self):
        count = 0
        seats = []
        for i in range(1, 31):
            checkbox = getattr(self.Beyonce_ui, f"checkBox{i}", None)
            if checkbox and checkbox.isChecked():
                count += 1
                seats.append(i)
        return [count, seats]
    def setup_Beyonce_checkbox_counter(self):
        for i in range(1, 31):
            checkbox = getattr(self.Beyonce_ui, f"checkBox{i}", None)
            if checkbox:
                checkbox.stateChanged.connect(
                    lambda: self.Beyonce_ui.lineEdit.setText(str(self.count_checked_Beyonce_checkboxes()[0])))
        self.Beyonce_ui.TotalBeyonceLabelValue.setText(f'{self.count_checked_Beyonce_checkboxes()[0]*300} $')
        self.Beyonce_ui.lineEdit.setText(f'{self.count_checked_Beyonce_checkboxes()[0]}')
    def confirmBeyonce(self):
        if self.Beyonce_ui.lineEdit.text() is not None:
            print(self.Beyonce_ui.QuantityBeyonceLabel.text())
            self.Beyonce_ui.PayBeyonceBtn.setEnabled(True)
            self.Beyonce_ui.PayBeyonceBtn.setText("BUY")

    def BuyBeyonce(self):
        Balance = c.execute(f'SELECT Balance FROM UserInformation WHERE UserName = "{self.username}"').fetchone()[0]

        if Balance >= int(self.count_checked_Beyonce_checkboxes()[0] * 300):
            Balance -= int(self.count_checked_Beyonce_checkboxes()[0] * 300)
            c.execute(f'UPDATE UserInformation SET Balance = {Balance} WHERE UserName = "{self.username}"')
            conn.commit()
            self.BalanceUpdate()
            self.Bill_ui.BillDateLabel.setText(self.Beyonce_ui.DateBeyonceComboBox.currentText())
            self.Beyonce_ui.DateBeyonceComboBox.setCurrentIndex(0)
            self.Bill_ui.BillArtistLabel.setText('Beyonce')
            self.Bill_ui.BillRowLabel.setText(self.Beyonce_ui.RowBeyonceComboBox.currentText())
            self.Beyonce_ui.RowBeyonceComboBox.setCurrentIndex(0)
            self.Bill_ui.BillSeatLabel.setText(', '.join(str(x) for x in self.count_checked_Beyonce_checkboxes()[1]))
            self.Bill_ui.BillTotalLabel.setText(self.Beyonce_ui.TotalBeyonceLabelValue.text())
            self.Beyonce_ui.lineEdit.setText("")
            self.Beyonce_ui.ConfirmBeyonceBtn.setDisabled(True)
            self.Beyonce_ui.PayBeyonceBtn.setText("Check the Quantity first")
            self.Beyonce_ui.PayBeyonceBtn.setDisabled(True)
            self.Beyonce_window.close()
            self.Bill_window.show()
            for i in range(1, 31):
                checkbox = getattr(self.Beyonce_ui, f"checkBox{i}", None)
                if checkbox and checkbox.isChecked():
                    checkbox.setChecked(False)
                    checkbox.setDisabled(True)
                    checkbox.setHidden(True)
        else:
            self.Beyonce_ui.BalanceNotEnoughMessage.show()
            self.Beyonce_ui.BalanceNotEnoughMessage.setEnabled(True)
            self.Beyonce_ui.BalanceNotEnoughMessage.setText("Not Enough Balance")



####                                                            BILLIE

    def BillieBackBtn(self):
        self.Billie_window.close()
        self.BookTheTicket_window.show()
    def count_checked_Billie_checkboxes(self):
        count = 0
        seats = []
        for i in range(1, 31):
            checkbox = getattr(self.Billie_ui, f"checkBox{i}", None)
            if checkbox and checkbox.isChecked():
                count += 1
                seats.append(i)
        return [count, seats]
    def setup_Billie_checkbox_counter(self):
        for i in range(1, 31):
            checkbox = getattr(self.Billie_ui, f"checkBox{i}", None)
            if checkbox:
                checkbox.stateChanged.connect(
                    lambda: self.Billie_ui.BillieQuantityLabel.setText(str(self.count_checked_Billie_checkboxes()[0])))
        self.Billie_ui.TotalBillieLabelValue.setText(f'{self.count_checked_Billie_checkboxes()[0] * 300} $')
        self.Billie_ui.BillieQuantityLabel.setText(f'{self.count_checked_Billie_checkboxes()[0]}')
    def confirmBillie(self):
        if self.Billie_ui.BillieQuantityLabel.text() is not None:
            print(self.Billie_ui.QuantityBillieLabel.text())
            self.Billie_ui.PayBillieBtn.setEnabled(True)
            self.Billie_ui.PayBillieBtn.setText("BUY")
    def BuyBillie(self):
        Balance = c.execute(f'SELECT Balance FROM UserInformation WHERE UserName = "{self.username}"').fetchone()[0]

        if Balance >= int(self.count_checked_Billie_checkboxes()[0]*300):
            Balance -= int(self.count_checked_Billie_checkboxes()[0]*300)
            c.execute(f'UPDATE UserInformation SET Balance = {Balance} WHERE UserName = "{self.username}"')
            conn.commit()
            self.BalanceUpdate()
            self.Bill_ui.BillDateLabel.setText(self.Billie_ui.DateBillieComboBox.currentText())
            self.Billie_ui.DateBillieComboBox.setCurrentIndex(0)
            self.Bill_ui.BillArtistLabel.setText('Billie')
            self.Bill_ui.BillRowLabel.setText(self.Billie_ui.RowBillieComboBox.currentText())
            self.Billie_ui.RowBillieComboBox.setCurrentIndex(0)
            self.Bill_ui.BillSeatLabel.setText(', '.join(str(x) for x in self.count_checked_Billie_checkboxes()[1]))
            self.Bill_ui.BillTotalLabel.setText(self.Billie_ui.TotalBillieLabelValue.text())
            self.Billie_ui.BillieQuantityLabel.setText("")
            self.Billie_ui.ConfirmBillieBtn.setDisabled(True)
            self.Billie_ui.PayBillieBtn.setText("Check the Quantity first")
            self.Billie_ui.PayBillieBtn.setDisabled(True)
            self.Billie_window.close()
            self.Bill_window.show()
            for i in range(1, 31):
                checkbox = getattr(self.Billie_ui, f"checkBox{i}", None)
                if checkbox and checkbox.isChecked():
                    checkbox.setChecked(False)
                    checkbox.setDisabled(True)
                    checkbox.setHidden(True)
        else:
            self.Billie_ui.BalanceNotEnoughMessage.show()
            self.Billie_ui.BalanceNotEnoughMessage.setEnabled(True)
            self.Billie_ui.BalanceNotEnoughMessage.setText("Not Enough Balance")

    ####                                                            LANA

    def LanaBackBtn(self):
        self.Lana_window.close()
        self.BookTheTicket_window.show()
    def count_checked_Lana_checkboxes(self):
        count = 0
        seats = []
        for i in range(1, 31):
            checkbox = getattr(self.Lana_ui, f"checkBox{i}", None)
            if checkbox and checkbox.isChecked():
                count += 1
                seats.append(i)
        return [count, seats]
    def setup_Lana_checkbox_counter(self):
        for i in range(1, 31):
            checkbox = getattr(self.Lana_ui, f"checkBox{i}", None)
            if checkbox:
                checkbox.stateChanged.connect(
                    lambda: self.Lana_ui.lineEdit.setText(str(self.count_checked_Lana_checkboxes()[0])))
        self.Lana_ui.TotalLanaLabelValue.setText(f'{self.count_checked_Lana_checkboxes()[0] * 300} $')
        self.Lana_ui.lineEdit.setText(f'{self.count_checked_Lana_checkboxes()[0]}')
    def confirmLana(self):
        if self.Lana_ui.lineEdit.text() is not None:
            print(self.Lana_ui.QuantityLanaLabel.text())
            self.Lana_ui.PayLanaBtn.setEnabled(True)
            self.Lana_ui.PayLanaBtn.setText("BUY")
    def BuyLana(self):
        Balance = c.execute(f'SELECT Balance FROM UserInformation WHERE UserName = "{self.username}"').fetchone()[0]

        if Balance >= int(self.count_checked_Lana_checkboxes()[0] * 300):
            Balance -= int(self.count_checked_Lana_checkboxes()[0] * 300)
            c.execute(f'UPDATE UserInformation SET Balance = {Balance} WHERE UserName = "{self.username}"')
            conn.commit()
            self.BalanceUpdate()
            self.Bill_ui.BillDateLabel.setText(self.Lana_ui.DateLanaComboBox.currentText())
            self.Lana_ui.DateLanaComboBox.setCurrentIndex(0)
            self.Bill_ui.BillArtistLabel.setText('Lana')
            self.Bill_ui.BillRowLabel.setText(self.Lana_ui.RowLanaComboBox.currentText())
            self.Lana_ui.RowLanaComboBox.setCurrentIndex(0)
            self.Bill_ui.BillSeatLabel.setText(', '.join(str(x) for x in self.count_checked_Lana_checkboxes()[1]))
            self.Bill_ui.BillTotalLabel.setText(self.Lana_ui.TotalLanaLabelValue.text())
            self.Lana_ui.lineEdit.setText("")
            self.Lana_ui.ConfirmLanaBtn.setDisabled(True)
            self.Lana_ui.PayLanaBtn.setText("Check the Quantity first")
            self.Lana_ui.PayLanaBtn.setDisabled(True)
            self.Lana_window.close()
            self.Bill_window.show()
            for i in range(1, 31):
                checkbox = getattr(self.Lana_ui, f"checkBox{i}", None)
                if checkbox and checkbox.isChecked():
                    checkbox.setChecked(False)
                    checkbox.setDisabled(True)
                    checkbox.setHidden(True)
        else:
            self.Lana_ui.BalanceNotEnoughMessage.show()
            self.Lana_ui.BalanceNotEnoughMessage.setEnabled(True)
            self.Lana_ui.BalanceNotEnoughMessage.setText("Not Enough Balance")


    ####                                                            WEEKEND

    def WeekendBackBtn(self):
        self.Weekend_window.close()
        self.BookTheTicket_window.show()
    def count_checked_Weekend_checkboxes(self):
        count = 0
        seats = []
        for i in range(1, 31):
            checkbox = getattr(self.Weekend_ui, f"checkBox{i}", None)
            if checkbox and checkbox.isChecked():
                count += 1
                seats.append(i)
        return [count, seats]
    def setup_Weekend_checkbox_counter(self):
        for i in range(1, 31):
            checkbox = getattr(self.Weekend_ui, f"checkBox{i}", None)
            if checkbox:
                checkbox.stateChanged.connect(
                    lambda: self.Weekend_ui.lineEdit.setText(str(self.count_checked_Weekend_checkboxes()[0])))
        self.Weekend_ui.TotalWeekendLabelValue.setText(f'{self.count_checked_Weekend_checkboxes()[0] * 300} $')
        self.Weekend_ui.lineEdit.setText(f'{self.count_checked_Weekend_checkboxes()[0]}')
    def confirmWeekend(self):
        if self.Weekend_ui.lineEdit.text() is not None:
            print(self.Weekend_ui.QuantityWeekendLabel.text())
            self.Weekend_ui.PayWeekendBtn.setEnabled(True)
            self.Weekend_ui.PayWeekendBtn.setText("BUY")
    def BuyWeekend(self):
        Balance = c.execute(f'SELECT Balance FROM UserInformation WHERE UserName = "{self.username}"').fetchone()[0]

        if Balance >= int(self.count_checked_Weekend_checkboxes()[0] * 300):
            Balance -= int(self.count_checked_Weekend_checkboxes()[0] * 300)
            c.execute(f'UPDATE UserInformation SET Balance = {Balance} WHERE UserName = "{self.username}"')
            conn.commit()
            self.BalanceUpdate()
            self.Bill_ui.BillDateLabel.setText(self.Weekend_ui.DateWeekendComboBox.currentText())
            self.Weekend_ui.DateWeekendComboBox.setCurrentIndex(0)
            self.Bill_ui.BillArtistLabel.setText('Weekend')
            self.Bill_ui.BillRowLabel.setText(self.Weekend_ui.RowWeekendComboBox.currentText())
            self.Weekend_ui.RowWeekendComboBox.setCurrentIndex(0)
            self.Bill_ui.BillSeatLabel.setText(', '.join(str(x) for x in self.count_checked_Weekend_checkboxes()[1]))
            self.Bill_ui.BillTotalLabel.setText(self.Weekend_ui.TotalWeekendLabelValue.text())
            self.Weekend_ui.lineEdit.setText("")
            self.Weekend_ui.ConfirmWeekendBtn.setDisabled(True)
            self.Weekend_ui.PayWeekendBtn.setText("Check the Quantity first")
            self.Weekend_ui.PayWeekendBtn.setDisabled(True)
            self.Weekend_window.close()
            self.Bill_window.show()
            for i in range(1, 31):
                checkbox = getattr(self.Weekend_ui, f"checkBox{i}", None)
                if checkbox and checkbox.isChecked():
                    checkbox.setChecked(False)
                    checkbox.setDisabled(True)
                    checkbox.setHidden(True)
        else:
            self.Weekend_ui.BalanceNotEnoughMessage.show()
            self.Weekend_ui.BalanceNotEnoughMessage.setEnabled(True)
            self.Weekend_ui.BalanceNotEnoughMessage.setText("Not Enough Balance")





####                                                            RECS

    def RECBackBtn(self):
        self.Rec_window.close()
        self.main_window.show()

    #### რეკომენდაციების window ს რეკომენდაციების ველის სკრიპტი, რომელის მთავარი ფუნქციაც იმპორტდება AAA.py დან
    #### random ის დახმარებით, პოპულარობის ფარდობებით,
    #### აკეთებს მუსიკების შემოთავაზებებს. მაღალი პოპულარობა = მაღალი შანსი
    def Recs(self):
        db_path = "Top1KTracks.sqlite3"
        List = recommend_songs_from_db(db_path)
        print(List)
        self.Rec_ui.Rec1LabelSong.setText(str(List[0][0]))
        self.Rec_ui.Rec2LabelSong.setText(str(List[1][0]))
        self.Rec_ui.Rec3LabelSong.setText(str(List[2][0]))
        self.Rec_ui.Rec4LabelSong.setText(str(List[3][0]))
        self.Rec_ui.Rec5LabelSong.setText(str(List[4][0]))
        self.Rec_ui.Rec1Labelartist.setText(f'by {str(List[0][1])}')
        self.Rec_ui.Rec2Labelartist.setText(f'by {str(List[1][1])}')
        self.Rec_ui.Rec3Labelartist.setText(f'by {str(List[2][1])}')
        self.Rec_ui.Rec4Labelartist.setText(f'by {str(List[3][1])}')
        self.Rec_ui.Rec5Labelartist.setText(f'by {str(List[4][1])}')

    #### DB დან ამოარჩევეს TOP 5 ს
    def Top5(self):
        conne = sqlite3.connect("Top1KTracks.sqlite3")
        ca = conne.cursor()
        ca.execute('''SELECT track_name, artist FROM spotify_top_1000_tracks 
        ORDER BY popularity DESC LIMIT 5''')

        List = [list(row) for row in ca.fetchall()]

        self.Rec_ui.Top1LabelSong.setText(str(List[0][0]))
        self.Rec_ui.Top2LabelSong.setText(str(List[1][0]))
        self.Rec_ui.Top3LabelSong.setText(str(List[2][0]))
        self.Rec_ui.Top4LabelSong.setText(str(List[3][0]))
        self.Rec_ui.Top5LabelSong.setText(str(List[4][0]))
        self.Rec_ui.Top1Labelartist.setText(f'by {str(List[0][1])}')
        self.Rec_ui.Top2Labelartist.setText(f'by {str(List[1][1])}')
        self.Rec_ui.Top3Labelartist.setText(f'by {str(List[2][1])}')
        self.Rec_ui.Top4Labelartist.setText(f'by {str(List[3][1])}')
        self.Rec_ui.Top5Labelartist.setText(f'by {str(List[4][1])}')
        conne.close()








if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())

conn.close()








