import mechanize
br = mechanize.Browser()
to = raw_input("Recipient address: ")
subject = raw_input("Subject: ")
print "Message: "
message = raw_input("Enter the message and press enter> ")
url = "http://anonymouse.org/anonemail.html"
headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
br.addheaders = [('User-agent', headers)]
br.open(url)
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_debug_http(False)
br.set_debug_redirects(False)
br.select_form(nr=0)
br.form['to'] = to
br.form['subject'] = subject
br.form['text'] = message
result = br.submit()
response = br.response().read()
response
if "The e-mail has been sent anonymously!" in response:
    print "The email has been sent successfully :)"
else:
    print "Sending email failed"