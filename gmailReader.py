import poplib
from getpass import getpass
import email
from email import parser

mailServer = poplib.POP3_SSL('pop.gmail.com')
mailServer.user('stevenmoleskin@gmail.com')
mailServer.pass_('secret@@089')
(mailCount,size)=mailServer.stat()

print('Mails: {0}'.format(mailCount))

print('第{0}封邮件'.format(1))
(hdr,messages,octet)=mailServer.retr(1)
#messages = [message.decode('utf-8') for message in messages]
mail=email.message_from_bytes('\n'.encode('utf-8').join(messages))
subject = email.header.decode_header(mail.get('subject'))
if type(subject[0][0]) in (type(b' '),):
    print("邮件标题：" + subject[0][0].decode(subject[0][1]))
else:
    print("邮件标题：" + subject[0][0])

for par in mail.walk():
    if not par.is_multipart():
        # 附件
        name = par.get_param('name')
        if name:
            dh = email.header.decode_header(name)
            if type(dh[0][0]) in (type(b' '),):
                if dh[0][1] == None:
                    fname = dh[0][0].decode()
                else:
                    fname = dh[0][0].decode(dh[0][1])
            else:
                fname = dh[0][0]
            print('附件名：' + fname)
            data = par.get_payload(decode=True)

            try:
                f = open(fname, 'wb')
            except:
                print('附件名有非法字符')
            f.write(data)
            f.close()
        else:
            # 邮件内容
            ch = par.get_content_charset()
            if ch == None:
                print(par.get_payload(decode=True).decode())
            else:
                print(par.get_payload(decode=True).decode(ch))

print("=================================")