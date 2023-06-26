from exchangelib import Credentials, Account

credentials = Credentials('Firstname.Lastname@someenterprise.com', 'Your_Password_Here')
account = Account('shared_mail_box_name@someenterprise.com', credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)