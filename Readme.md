# Recruit_web

这是web招聘的数据分析网站 2018-11-11

## Getting start

首先确认您使用 Python3 并已经安装了 conda 或者 virtualenv

```
git clone https://github.com/MasterFishfish/recruit_web.git
cd ai-writing/mysite
virtualenv venv # 假设您使用 virtualenv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver 
```