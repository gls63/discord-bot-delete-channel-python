## Установка зависимостей

Установите все необходимые библиотеки одной командой в Visual Studio code или  terminal:
```bash
pip install -r requirements.txt
```

В проекте используется:
- [disnake](https://pypi.org/project/disnake/) — библиотека для работы с Discord API
- logging — стандартный модуль Python для логирования событий

## Конфиг: параметры и управление
В файле `config.py`:


```python
admin_id = "1354758424491196487"  # Discord User ID администратора, кто может запускать /dora
token = "ВАШ_ТОКЕН_БОТА"           # Discord Bot Token
config_channel_name = "by-discord-com"    # Название создаваемых каналов
config_alert_message = "@everyone @here ПЕРЕЕЗД НА https://discord.gg/" # Текст для спама
channel_create_delay = 0.01         # Задержка между созданием каналов (секунды, например: 0.01 — быстро, 1 — 1 секунда, 60 — минута)
spam_delay = 0.0                    # Задержка между сообщениями (секунды, например: 0 — без задержки, 1 — 1 секунда, 60 — минута)
```
**channel_create_delay** — задержка между созданием новых каналов (в секундах, можно указать 0 для максимальной скорости, 1 — секунда, 60 — минута)

**spam_delay** — задержка между отправкой сообщений в каждом канале (в секундах, можно указать 0 для максимального спама, 1 — секунда, 60 — минута)

**admin_id** — Discord User ID, кто может запускать команду `/dora` (узнать свой ID можно через Discord: Настройки → Расширенные → Включить режим разработчика → ПКМ по себе → Копировать ID)

**token** — токен вашего Discord-бота, получить на [Discord Developer Portal](https://discord.com/developers/applications)

**config_channel_name** — название для новых каналов

**config_alert_message** — текст, который бот будет спамить


## Как создать Discord-бота
- Перейдите на [Discord Developer Portal](https://discord.com/developers/applications)
- Создайте новое приложение и бот-аккаунт ([инструкция](https://discordpy.readthedocs.io/en/stable/discord.html))
- Скопируйте токен и вставьте в `config.py`
- Добавьте бота на сервер с правами администратора ([инструкция](https://support.discord.com/hc/ru/articles/360040720412))

### Установка Python и pip
- [Python (официальный сайт)](https://www.python.org/downloads/)
- [pip (установка)](https://pip.pypa.io/en/stable/installation/)

### Установка pm2
- [pm2 (официальный сайт)](https://pm2.keymetrics.io/)



### Запуск на Ubuntu (через pm2)
```bash
sudo apt update
sudo apt install python3-pip
pip3 install disnake
pm2 start main.py --interpreter=python3
```

### Запуск на Windows
- Установите [Python 3.x](https://www.python.org/downloads/windows/)
- Установите [pip](https://pip.pypa.io/en/stable/installation/)
- В терминале:
```bash
pip install disnake
python main.py
```

### Запуск в Visual Studio Code
- [Visual Studio Code](https://code.visualstudio.com/)
- Откройте проект
- Установите зависимости:
```bash
pip install disnake
```
- Запустите `main.py`

## Как изменить задержки (asyncio)

Чтобы управлять скоростью создания каналов и отправки сообщений, откройте файл `config.py` и измените параметры:

```python
channel_create_delay = 0.01  # Задержка между созданием каналов (секунды)
spam_delay = 0.0             # Задержка между сообщениями (секунды)
```

Примеры:
- `channel_create_delay = 1` — пауза 1 секунда между созданием каналов
- `channel_create_delay = 60` — пауза 1 минута между созданием каналов
- `spam_delay = 0` — сообщения отправляются без задержки
- `spam_delay = 10` — пауза 10 секунд между сообщениями

После изменения параметров сохраните файл и перезапустите — бот будет использовать новые значения при следующем запуске.

---

Если проект был полезен — поставьте ⭐ на этот репозиторий!
