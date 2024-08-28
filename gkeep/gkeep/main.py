import click
import gpsoauth

master_token = None

@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        master_token = auth()
        print(master_token)
    
def auth():
    email = input("Enter email of your google keep: ")
    android_id = input("Enter android id of your device which has google keep installed: ")
    oauth_token = input("Enter oauth token of your google account (See how to get a oauth token https://github.com/rukins/gpsoauth-java/blob/b74ebca999d0f5bd38a2eafe3c0d50be552f6385/README.md#receiving-an-authentication-token ): ")
    master_token = get_master_token(email, oauth_token, android_id)
    while master_token == None:
        print("Please enter correct information")
        auth()
    return master_token

def get_master_token(email, oauth_token, android_id):
    master_response = gpsoauth.exchange_token(email, oauth_token, android_id)
    master_token = master_response['Token']
    return master_token


    

@click.command(help="Have your new program say Hi to you!")
@click.argument('name')
def hello(name):
    print(f'Hi, {name}!')


