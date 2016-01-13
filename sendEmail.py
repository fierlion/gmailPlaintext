import smtplib
import sys
import getopt

def main(argv):
    toAddress = ''
    fromAddress = ''
    messageSubject = ''
    messageText = ''
    username = '' #insert gmail username
    password = '' #insert gmail password
    try:
        opts, args = getopt.getopt(argv,"ht:f:s:m:", ["to=","from=","subj=","mess="])
    except getopt.GetoptError:
        print 'test.py -t <toAddress> -f <fromAddress> -s <messageSubject> -m <messageText>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -t <toAddress> -f <fromAddress> -s <messageSubject> -m <messageText>'
            sys.exit()
        elif opt in ("-t", "--to"):
            toAddress = arg
        elif opt in ("-f", "--from"):
            fromAddress = arg
        elif opt in ("-s", "--subject"):
            messageSubject = arg
        elif opt in ("-m", "--message"):
            messageText = arg

    #send email
    header1 = "From: From person <%s>\r\nTo: To Person <%s>\r\nSubject: %s\r\n" \
              "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=\"utf-8\"\r\n" % (fromAddress, toAddress, messageSubject)
    message = header1 + messageText
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(toAddress, fromAddress, message)
        print 'email successfully sent'
    except Exception as e:
        print 'error: unable to send email; errortext: ' + str(e)

if __name__ == "__main__":
    main(sys.argv[1:])
