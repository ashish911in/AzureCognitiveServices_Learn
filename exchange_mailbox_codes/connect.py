from exchangelib import Credentials, Account

password = ''
email = ''
shared_email = ''
credentials = Credentials(email, password)
account = Account(shared_email, credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)