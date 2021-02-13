from emailrep import EmailRep
import sys

# uses modules emailrep from https://emailrep.io
# sign up for an API key https://emailrep.io/key
# docs: https://docs.emailrep.io

# have to create an EmailRep object to use query() function below
# api key allows for 1500 queries a month and 50 queries a day
email_rep = EmailRep("YOUR API KEY")
email_to_check = ''

# results get sent back in json format
# better to store json in variable to work with later

if len(sys.argv) > 1:
    if sys.argv[1] == '-e':
        email_to_check = str(sys.argv[2])
        results = email_rep.query(email_to_check)
        print('\n')
        print('=' * 55)
        print('\t\tEmail Reputation Report\t\t\n')
        print('Email: {}'.format(results['email']))
        print('Reputation Score: {}'.format(results['reputation']).title())
        print('Is Suspicious: {}'.format(results['suspicious']))    
        print('Is Blacklisted: {}'.format(results['details']['blacklisted']))
        print('Has Credentials Leaked: {}'.format(results['details']['credentials_leaked']))
        print('Has Credentials Leaked Recently: {}'.format(results['details']['credentials_leaked_recent']))
        print('Domain Reputation Score: {}'.format(results['details']['domain_reputation']).title())
        print('Is Email a Spam Address: {}'.format(results['details']['spam']))
        print('Days Since Domain Creation: {}'.format(results['details']['days_since_domain_creation']))
        print('New Domain: {}'.format(results['details']['new_domain']))
        print('=' * 55)
        print('\n')
else:
    print('\n')
    print('=' * 45)
    print('\t\tUsage Section:\t\t\n')
    print('-e\t\temail to query reputaton')
    print('=' * 45)
    print('\n')
