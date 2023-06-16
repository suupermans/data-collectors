# data-collectors
基于python开发的可以采集b站，微博，快手，小红书评论的GUI软件 
<h2>使用教程</h2>
1.首先运行main.py,将图形界面窗口运行出。  

<img width="392" alt="image" src="https://github.com/suupermans/data-collectors/assets/99522395/4f23ce51-9f19-482e-9570-a9a33db5f525">
2.再次在图形界面窗口中点击需要爬取的类型网站。  
3.具体操作指南。  

## b站程序使用教程

1. 找到视频网址（点击b站上面你想要看的任何一个视频）

   ![image-20221221211811867](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221211811867.png)

2. F12键打开开发者工具，找到红色标识的一栏

   **第一步，找到network工具栏**

   ![image-20221221212701612](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221212701612.png)

   **第二步，找到可以输入aid号的白色框**

   ![image-20221221211948228](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221211948228.png)

3. 程序的oid号就是这里的aid号，每个视频都会分配一个号（叫做oid号）

   ![image-20221221212135441](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221212135441.png)

4. 输入aid号（oid）

   ![image-20221221212233205](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221212233205.png)

5. 输入oid

   ![image-20221221212354036](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221212354036.png)

6. 评论开始爬取

   ![image-20221221212413298](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221212413298.png)

7. 程序结束之后，会在这个程序的同一级目录下成csv文件

   ![image-20221221212542835](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221212542835.png)

8. 点击这个文件，就可以看到爬取的内容

   ![image-20221221212621357](C:\Users\李小宝\AppData\Roaming\Typora\typora-user-images\image-20221221212621357.png)

   

