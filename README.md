示例;投票系统应用
地址：https://docs.djangoproject.com/zh-hans/3.0/

使用
默认数据库sqlite3
中文显示admin
时区上海
自定义模板
setuptools打包应用

激活model >python manage.py makemigrations polls
查看表 >python manage.py sqlmigrate polls 0001
创建表 >python manage.py migrate

交互式命令行 >python manage.py shell

创建管理员账号 >python manage.py createsuperuser

运行
python manage.py runserver


内容
1.models
    1.列表展示
    2.关联投票项展示
2.urls
   使用include,引入polls路由地址

3.views
    使用对象模板化view,简化代码

4.页面优化
    增加文字显示颜色
    增加背景图片
    自定义admin base_site站点文件，默认
    
5.TestCase示例

6.打包应用
    django-polls 目录下执行  python setup.py sdist
    安装包 >python -m pip install --user ./dist/django-polls-0.1.tar.gz
    卸载 >python -m pip uninstall django-polls
    
    