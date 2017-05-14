基于 django 1.11 和 Python 3.6 的 django 博客开发入门教程，带领你从零开始一步步开发属于自己的个人博客，让你以最快的速度掌握 django 开发的技巧。

项目演示地址

http://blog.wangyouyu.com/

项目教程

本项目配有完整的教程说明，教程阅读地址：django 博客开发入门教程。

每篇教程的代码都位于项目相应的分支中，点击上方的 Branch 按钮可以查看到，例如分支 Step1_build-development-environment 对应第 2 篇教程 2. 搭建开发环境。

master 主分支是整个项目的完整代码。

在本地运行项目

克隆项目到本地

打开命令行，进入到保存项目的文件夹，输入如下命令：

git clone https://github.com/xia0sheng/DjangoByExample.git
创建并激活虚拟环境

在命令行进入到保存虚拟环境的文件夹，输入如下命令创建并激活虚拟环境：

virtualenv blogproject_env

# windows
blogproject_env\Scripts\activate

# linux
source blogproject_env/bin/activate
关于如何使用虚拟环境，参阅：2. 搭建开发环境的 Virtualenv 部分。

如果不想使用虚拟环境，可以跳过这一步。

安装项目依赖

如果使用了虚拟环境，确保激活并进入了虚拟环境，在命令行进入项目所在的 django-blog-tutorial 文件夹，运行如下命令：

pip install -r requirements.txt
迁移数据库

在上一步所在的位置运行如下命令迁移数据库：

python manage.py migrate
创建后台管理员账户

在上一步所在的位置运行如下命令创建后台管理员账户

python manage.py createsuperuser
具体请参阅：8. 在 django admin 后台发布我们的文章

运行开发服务器

在上一步所在的位置运行如下命令开启开发服务器：

python manage.py runserver
在浏览器输入：127.0.0.1:8000

进入后台发布文章

在浏览器输入：127.0.0.1:8000/admin

使用第 5 步创建的后台管理员账户登录

具体请参阅：8. 在 django admin 后台发布我们的文章
