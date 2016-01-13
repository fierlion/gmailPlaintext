import smtplib
import sys
import getopt

def main(argv):
    toAddress = ''
    fromAddress = ''
    messageSubject = ''
    messageText = ''
    username = 'fierlion' #insert gmail username
    password = 'Three!=3216' #insert gmail password
    hMess = "'test.py -t <toAddress> -f <fromAddress> -s <messageSubject> -m " \
            "<messageText>'"
    try:
        opts, args = getopt.getopt(argv,"ht:f:s:m:",
        ["to=","from=","subj=","mess="])
    except getopt.GetoptError:
        print(hMess)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(hMess)
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
              "MIME-Version: 1.0\r\nContent-Type: text/plain;\r\n" \
              % (fromAddress, toAddress, messageSubject)
    message = header1 + messageText
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(toAddress, fromAddress, message)
        print('email successfully sent')
    except Exception as e:
        print('error: unable to send email; errortext: ' + str(e))

if __name__ == "__main__":
    main(sys.argv[1:])
