# Виджет банковских операций 
by lolomyn

## Description:

Виджет позволяет пользователям проверять и контролировать банковские операции клиентов

## Install:

**Ubuntu**

`sudo apt update` - update all packages

- python

`sudo apt install python3` - install python

`python3 -V` - check python version

- git

`sudo apt install git` - install git

`git --version` - check git version

- poetry

`sudo apt install python3-poetry` - install poetry

`poetry --version` - check poetry version

- clone repo

`git clone git@github.com:Lolomyn/skypro.git`

- install dependencies

`poetry add requests`

- start

`python3 main.py`

**Windows**

`sudo apt update` - update all packages

- python

Download it  [here](https://www.python.org/) and follow instructions

`python --version` - check python version

- git

Download in [here](https://git-scm.com/) and follow instructions

`git --version` - check git version

- poetry

`curl -sSL https://install.python-poetry.org | python -` - install poetry

`poetry --version` - check poetry version

- clone repo

`git clone git@github.com:Lolomyn/skypro.git`

- install dependencies

`poetry add requests`

- start

`python main.py`

## Functions:

*mask_account_card* -
маскирует введенные данные карты или счета

example:
```
# input
VISA 6482985672846578
СЧЕТ 72759305647182947589

# output
1234 56** **** 2345
 **7589
```

*get_date* - 
форматирует полученную дату в ДД.ММ.ГГГГ

example:
```
# input
2024-03-11T02:26:18.671407

# output
11.03.2024
```

*filter_by_state* - 
возвращает список словарей, отфильтрованных по ключу `state`

example:
```
# input
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# output
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

*sort_by_date* - 
возвращает отсортированный список словарей по дате, указывается порядок сортировки

example:
```
# input
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# output
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

```

## Author:
[Mail](vismanmark@yandex.ru) /
[GitHub](https://github.com/Lolomyn)
