 zmq

使用的zmq模式为`zmq.REP`。在这种模式下，我们的程序必须要遵守`recv()`和`send()`配对使用的编程模式。

也就是说，在服务程序中，必须要有完整的`recv()`和`send()`成对出现。同理，在客户端程序中，`send()`后，也要有`recv()`。





服务端收到信息以后，会 send 一个“World”给客户端。值得注意的是一定是 client 连接上来以后，send 消息给 Server，然后 Server 再 rev 然后响应 client，这种一问一答式的。如果 Server 先 send，client 先 rev 是会报错的。



作者：零一间
链接：https://www.jianshu.com/p/a8b657472518
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





[201710472292.2 - 一种基于多Kinect的实时三维人体绘制方法 - SooPAT专利搜索](http://www.soopat.com/Patent/201710472292#this)



[201810922979.6 - 基于平面镜的Kinect标定方法及装置 - SooPAT专利搜索](http://www.soopat.com/Patent/201810922979?lx=FMSQ)



[201510237341.5 - 基于Kinect实现室内人体跌倒检测的系统及方法 - SooPAT专利搜索](http://www.soopat.com/Patent/201510237341?lx=FMSQ)





[201610075712.9 - 一种基于多台Kinect的3D人体姿态数据库构建方法 - SooPAT专利搜索](http://www.soopat.com/Patent/201610075712)



CV2图片转字节流

\# 将数组转成 图片的二进制数据
 img_data = np.linspace(0,255,100*100*3).reshape(100,100,-1).astype(np.uint8)
 ret,buf = cv2.imencode(".jpg",img_data)
 img_bin = Image.fromarray(np.uint8(buf)).tobytes()

\# 将图片二进制数据 转为数组
 img_data = plt.imread(BytesIO(img_bin),"jpg")
 print(type(img_data))
 print(img_data.shape)