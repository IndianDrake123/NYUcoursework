def find_part(msg):
    for char in msg[0:]:
        if char.isdigit():
            beg = msg.find(char)

    for char in msg[beg + 1:]:
        if char.isdigit():
            print(char)
            end = msg.find(char)


    #return msg[beg:end]
#def decode_entire_msg(msg, ):


def main():
    msg = "3Gn.olwo pd/Q gh5l!d pulAk c_kosk an2 moPn! .y\oausr? 3mqei,sd+ktcbe.KrkcmOpsne!se odYpqo>kulq fag pozrtks dftpqh /ipaslk!dp4vm fkofwolp9 mjcnre"
    #print(decode_entire_msg(msg))
    print(find_part(msg))

main()