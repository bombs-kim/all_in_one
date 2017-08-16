from django.shortcuts import render
import esm

def get_neworder(account):
    if account.site in ('ESM', 'GMKT', 'AUC'):
        esm.get_neworder(account.username, account.password)

def neworders(request):
    master = request.user.master
    accounts = master.accounts.all()


    master.neworders.all()
