# data-collectors
基于python开发的可以采集b站，微博，快手，小红书评论的GUI软件 
<h2>使用教程</h2>
1.首先运行main.py,将图形界面窗口运行出。  
<br/>
<img width="392" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/4f23ce51-9f19-482e-9570-a9a33db5f525">
<br/>
2.再次在图形界面窗口中点击需要爬取的类型网站。  
<br/>
3.具体操作指南。  

## b站程序使用教程

1. 找到视频网址（点击b站上面你想要看的任何一个视频）

<img width="416" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/ed04dc1c-392e-42df-ac2d-3b05ed9aaf23">

2. F12键打开开发者工具，找到红色标识的一栏

   **第一步，找到network工具栏**

<img width="416" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/1009b611-30f1-4b33-ad5b-8acfcee6b8c2">


   **第二步，找到可以输入aid号的白色框**
   
<img width="415" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/2db29415-75cc-413c-bf2d-2398eb1cc97a">


3. 程序的oid号就是这里的aid号，每个视频都会分配一个号（叫做oid号）

  <img width="416" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/345cf197-f705-4f41-93ae-879c5ed48ecb">


4. 输入aid号（oid）

  <img width="416" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/2bb222f3-1a84-468c-b06f-b7aa024cc82f">


5. 输入oid
<img width="416" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/24a5842c-de8f-47a3-bb60-e1b9037f56c1">


6. 评论开始爬取

  ![image](https://github.com/suupermans/data-collectors/assets/99522395/36d31374-7967-48a0-a785-898fc4a23063)


7. 程序结束之后，会在这个程序的同一级目录下成csv文件

<img width="416" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/d25e53c6-f384-4168-adf1-574ace869688">


8. 点击这个文件，就可以看到爬取的内容

![image](https://github.com/suupermans/data-collectors/assets/99522395/9cc50b18-a813-45b1-8027-37d0d356f5cb)

<h2>爬取结果图</h2>
   
![image](https://github.com/suupermans/data-collectors/assets/99522395/714dca6b-5f56-4345-b630-d1147c153e87)

