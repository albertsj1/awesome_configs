#!/usr/bin/python

import imaplib
import mypasswords # mypasswords.py must exist in the same directory as this script.

#first field is imap server, second - port (993 for gmail SSL IMAP)
M=imaplib.IMAP4_SSL("imap.gmail.com", 993)
#first field is imap login (gmail uses login with domain and '@' character), second - password
M.login("john.m.alberts@gmail.com",mypasswords.gmail_password)

status, counts = M.status("[Gmail]/Important","(MESSAGES UNSEEN)")
#status, counts = M.status("Inbox","(MESSAGES UNSEEN)")

unread = counts[0].split()[4][:-1]
if unread == "0":
    print " no gmail "
else:
#red bg color when you have unseen mail
    #print "<bg color=\"red\" style='font-size: 25px;'>  <b>"+unread+"</b>  </bg>"
    print "<span color=\"red\">"+unread+" gmail </span>"
M.logout()
