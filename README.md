# -java-python-protobuf-
这个是解决java和python互联时python接收java信息时，使用protobuf的半包、粘包问题的工具类。  
使用场景：java开启new ProtobufVarint32LengthFieldPrepender()  
因为我在java客户端向python发送消息时，发现出现了半包、粘包问题，网上找不到相关解决方案，就写了一个工具类解决。如果大家遇到相关问题，可以使用这个工具类
