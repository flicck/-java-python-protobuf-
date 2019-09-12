import six
#注意：Msg_pb2替换成你的用protobuf生成的文件
import Msg_pb2
import socket
address = ('127.0.0.1',8765)
s = socket.socket()
s.connect(address)

def startparse():
    reply = b''
    count = 0
    flag = True
    while True:
        len_buffer = b""
        data_buffer = b""

        if flag:
            reply = reply+s.recv(1024)

        len_buffer = len_buffer + six.int2byte(reply[0])+six.int2byte(reply[1])
        len = DecodeVarint(len_buffer)

        # print(len)
        for i in range(2,len+2):
            #长度不够，说明半包,把flag改为True，继续接收
            if(reply.__len__()<len+2):
                flag =True
            #长度足够，说明整包或粘包
            else:
                data_buffer = data_buffer + six.int2byte(reply[i])
                #取出data_buffer后需要去除在reply里面的这一部分内容
        reply1 = b''
        if reply.__len__()>=len+2:
            for j in range(len+2,reply.__len__()):
                reply1 = reply1 + six.int2byte(reply[j])

            reply = reply1
            # print(b'xxxx' + reply1)
            #大于等于2且实际长度大于指示长度加2说明足够获取下一个数据，将flag改为False,小于则改为True
        if reply.__len__()>=2:
            len_buffer1 = six.int2byte(reply[0]) + six.int2byte(reply[1])
            len1 = DecodeVarint(len_buffer1)
            if reply.__len__()>=len1+2:
                flag = False
        else:
            flag = True
        # print(data_buffer)
        if  data_buffer != b"":
    #注意:这里根据自己protobuf生成文件改一下
            msg3 = Msg_pb2.Msg.FromString(data_buffer)
            print(msg3.name)
            count = count +1
        print (count)

def DecodeVarint(buffer):
    mask = (1 << 32) - 1
    result_type = int
    result = 0
    shift = 0
    for b in buffer:
        result |= ((b & 0x7f) << shift)
        shift += 7
        if shift >= 64:
            raise Exception('Too many bytes when decoding varint.')
    result &= mask
    result = result_type(result)
    return result

startparse()