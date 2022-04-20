import socket
import tkinter
import threading



def scan():
    ip_address = entry_ip.get()
    time_out = float(entry_time.get())
    port_list=[20,21,22,23,25,53,80,110,143,443,1080,1433,1492,3128,3389,4000,8000,8080,8081,9098]

    for i in range(0,len(port_list)):

        try:
            s = socket.socket()
            s.settimeout(time_out)
            s.connect((ip_address, port_list[i]))
            s.send(b'Primal Security \n')
            result = s.recv(1024)
            if result != None:
                print('主机 ' + ip_address + ':' + str(port_list[i]) + ' 开放')

                listbox.insert(0, '主机 ' + ip_address + ':' + str(port_list[i]) + ' 开放')
                window.title(str(i+1)+'/'+str(len(port_list)) + '----端口----' +str(port_list[i]) + ' 开放')

            s.close()
        except:
            print('主机 ' + ip_address + ':' + str(port_list[i]) + ' 未开放')

            listbox.insert(0, '主机 ' + ip_address + ':' + str(port_list[i]) + ' 未开放')
            window.title(str(i+1)+'/'+str(len(port_list)) + '----端口----' + str(port_list[i]) + ' 未开放')
#按钮点击事件，执行run
def run():
    # 扫描线程
    scan_thread = threading.Thread(target=scan)
    scan_thread.start()






if __name__=='__main__':
    window = tkinter.Tk()
    # 进入消息循环
    window.title("端口扫描")
    window.geometry('350x300')
    # ip
    label_ip = tkinter.Label(window, text="IP地址，如127.0.0.1")
    label_ip.grid(column=0, row=0)

    entry_ip = tkinter.Entry(window, show=None)
    entry_ip.insert(0, "192.168.1.1")
    entry_ip.grid(column=1, row=0)

    # 响应时间
    label_time = tkinter.Label(window, text="超时时间（单位秒）")
    label_time.grid(column=0, row=4)

    entry_time = tkinter.Entry(window, show=None)
    entry_time.insert(0, "0.5")
    entry_time.grid(column=1, row=4)
    # 开始扫描
    button_start = tkinter.Button(window, text='开始扫描', command=run)  # 点击按钮式执行的命令,run函数
    button_start.grid(column=1, row=5)

    # 列表标签
    label_list = tkinter.Label(window, text="扫描结果")
    label_list.grid(column=0, row=6)
    # 列表
    listbox = tkinter.Listbox(window, width=30, height=10)
    listbox.grid(column=1, row=6)

    window.mainloop()


