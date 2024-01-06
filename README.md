# 租屋好朋友 ApartmentFriend

# 一、系統說明

coming soon~

# 二、系統架構

coming soon~

# 三、Build With

1. Django
2. HTML5
3. Bootstrap4
4. Python
5. Celery
6. Docker
7. Mysql

# 四、建立環境
- with poetry：

```shell
poetry install
```

- with pip：

```shell
pip install -r ./requirements.txt
```

# 五、部屬方式 (Shell)

1. 建立資料表 
    ```shell
    python ./manage.py makemigrations
    ```
    ```shell
    python ./manage.py migrate
    ```

2. 執行 Django

    ```shell
    python ./manage.py runserver
    ```

# 六、其他指令
1. 資料表異動

    當今天各個 app 底下的 model 有修改時，亦即針對資料表有異動時，須按照順序執行下方步驟
    
    ```shell
    python ./manage.py makemigrations
    ```
    ```shell
    python ./manage.py migrate
    ```

2. poetry 輸出 requirements.txt

    ```shell
    poetry export --without-hashes --format=requirements.txt > requirements.txt
    ```