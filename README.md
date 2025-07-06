# 🐧 My Gentoo Configs

[![Gentoo](https://img.shields.io/badge/Gentoo-54487A?style=for-the-badge&logo=gentoo&logoColor=white)](https://www.gentoo.org/)
[![Hyprland](https://img.shields.io/badge/Hyprland-58E1FF?style=for-the-badge&logo=wayland&logoColor=black)](https://hyprland.org/)
[![DWM](https://img.shields.io/badge/DWM-1177AA?style=for-the-badge&logo=dwm&logoColor=white)](https://dwm.suckless.org/)
[![License](https://img.shields.io/badge/License-Custom-red?style=for-the-badge)](LICENSE)
[![Development](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)](https://github.com/your-username/My-Gentoo-Configs)

> 💎 **Продвинутые конфигурации Gentoo Linux от skreamer (mvko)**  
> Полнофункциональная система с Wayland/X11, оптимизированная для производительности и удобства

## ⚠️ **ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ**

> 🚧 **Данные конфигурации находятся в стадии активной разработки и тестирования!**
>
> - ❌ **НЕ рекомендуется** для использования в производственных системах
> - 🔧 **Требует доработки** и настройки под конкретное оборудование
> - 🐛 **Может содержать ошибки** и несовместимости
> - 💥 **Использование на свой страх и риск** - автор не несёт ответственности за возможные повреждения системы
> - 📋 **Обязательно делайте резервные копии** перед применением конфигураций

## 📋 Обзор системы

| Компонент                  | Значение                |
| -------------------------- | ----------------------- |
| 🏗️ **Дистрибутив**         | Gentoo Linux            |
| 🪟 **WM (основной)**       | Hyprland (Wayland)      |
| 🪟 **WM (альтернативный)** | DWM + 100+ патчей (X11) |
| 🔧 **Init система**        | systemd                 |
| 🗂️ **Файловая система**    | ext4                    |
| 🔊 **Аудиосистема**        | PipeWire + PulseAudio   |
| 🖥️ **Display сервер**      | Wayland + XWayland      |
| 🐚 **Shell**               | Zsh + плагины           |

## 🚀 Особенности

### 🎨 **Окружение рабочего стола**

- **Hyprland** - современный композитор Wayland с анимациями и эффектами
- **DWM Flexipatch** - легковесный тайлинговый WM с множеством патчей
- **Waybar** - настраиваемая панель для Wayland
- **SwayNC** - центр уведомлений
- **Rofi** - лаунчер приложений

### ⚡ **Оптимизация производительности**

- Флаги компиляции `march=native -O2`
- 13-поточная сборка (`MAKEOPTS="-j13"`)
- ccache для ускорения пересборки (50GB кэш)
- Rust оптимизация `target-cpu=native`

### 🛠️ **Инструменты разработки**

- **VSCode** с темой Absolute Black
- **Neovim** - продвинутый текстовый редактор
- **Docker** + Docker Compose
- **Git** с автодополнением и подсветкой
- **Kitty** терминал

### 📦 **Менеджер пакетов**

- Тонко настроенный Portage
- Подключен репозиторий GURU
- Оптимизированные USE флаги
- Автоматическое принятие лицензий

## 📁 Структура проекта

```
My-Gentoo-Configs/
├── 🏗️ dwm/                     # DWM конфигурации и скрипты
│   ├── main/dwm-flexipatch/    # DWM с патчами
│   └── dwm-scripts/            # Скрипты статус-бара
├── ⚙️ etc/                     # Системные конфигурации
│   ├── portage/                # Настройки Portage
│   │   ├── make.conf          # Основные флаги компиляции
│   │   ├── package.use/       # USE флаги для пакетов
│   │   └── package.accept_keywords/ # Нестабильные пакеты
│   └── modprobe.d/            # Модули ядра
├── 🔤 fonts/                   # JetBrains Mono Nerd Font
├── 🎨 icons/                   # Иконки и скриншоты
├── 🐚 zsh-syntax-highlighting/ # Подсветка синтаксиса Zsh
├── 📋 *.packages              # Списки пакетов
└── 🔧 usr/share/applications/ # Desktop файлы
```

## 🛠️ Установка

### 📋 Предварительные требования

- Установленная базовая система Gentoo Linux
- Доступ root или doas/sudo
- Активное интернет-соединение

### 🚀 Быстрая установка

> ⚠️ **Перед началом установки:**
>
> - Сделайте полную резервную копию системы
> - Убедитесь, что у вас есть способ восстановления системы
> - Тестируйте на виртуальной машине перед установкой на основную систему

```bash
# Клонируем репозиторий
git clone https://github.com/your-username/My-Gentoo-Configs.git
cd My-Gentoo-Configs

# ВАЖНО: Проверьте и адаптируйте конфигурации под ваше оборудование
# Особенно обратите внимание на:
# - etc/portage/make.conf (флаги процессора)
# - etc/portage/package.use/* (USE флаги)
# - dwm/main/dwm-flexipatch/config.h (настройки DWM)

# Копируем конфигурации Portage (ОСТОРОЖНО!)
doas cp -r etc/portage/* /etc/portage/

# Включаем репозиторий GURU
doas eselect repository enable guru

# Обновляем Portage
doas emerge --sync

# Устанавливаем основные пакеты (может занять много времени)
doas emerge --ask $(cat gentoo.packages | grep -v '^#' | grep -v '^$')

# Копируем шрифты
cp -r fonts/* ~/.local/share/fonts/
fc-cache -fv

# Настраиваем Zsh
cp -r zsh-syntax-highlighting ~/.config/
echo 'source ~/.config/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh' >> ~/.zshrc
```

### 🪟 Установка DWM

```bash
cd dwm/main/dwm-flexipatch/
# Редактируем config.h под свои нужды
$EDITOR config.h
# Собираем и устанавливаем
doas make install
```

### 🎨 Установка Hyprland

```bash
# Устанавливаем Hyprland и дополнения
doas emerge --ask gui-wm/hyprland gui-apps/waybar gui-apps/swaync gui-apps/rofi-wayland

# Копируем конфигурации (создайте их отдельно)
# mkdir -p ~/.config/{hypr,waybar,swaync}
```

## 📊 Мониторинг системы

В проекте включены инструменты для мониторинга:

- **htop** - монитор процессов
- **dust** - анализатор дискового пространства
- **fastfetch** - информация о системе
- **Grafana + Prometheus** - веб-мониторинг

## 🎯 USE флаги

Система настроена с акцентом на Wayland:

```bash
USE="wayland xwayland mesa opengl pipewire egl drm alsa X -kde -gnome -dvd"
```

## 🔧 Дополнительные компоненты

### 📱 Приложения

- **Firefox** - веб-браузер
- **Telegram Desktop** - мессенджер
- **Ranger** - файловый менеджер
- **VSCode** - редактор кода

### 🔊 Аудио

- **PipeWire** - современная аудиосистема
- **PulseAudio** - совместимость
- **pavucontrol** - графический микшер
- **pamixer** - CLI микшер

### 🖼️ Графика и медиа

- **Mesa** - OpenGL драйверы
- **Hyprpaper** - обои для Wayland
- **grim + slurp** - скриншоты

## 🚧 Статус разработки

### 📊 Текущее состояние

| Компонент                   | Статус          | Описание                                       |
| --------------------------- | --------------- | ---------------------------------------------- |
| 🏗️ **Portage конфигурации** | 🟡 Тестирование | Основные настройки работают, требуют адаптации |
| 🪟 **DWM setup**            | 🟢 Стабильно    | Проверено на нескольких системах               |
| 🎨 **Hyprland config**      | 🔴 В разработке | Базовая конфигурация, много TODO               |
| 🔤 **Шрифты**               | 🟢 Готово       | Полный набор JetBrains Mono                    |
| 📦 **Списки пакетов**       | 🟡 Частично     | Основные пакеты, может не хватать зависимостей |
| 🐚 **Zsh настройки**        | 🟡 Базовые      | Только подсветка синтаксиса                    |

### 🔄 Планы развития

- [ ] Добавить полные конфигурации Hyprland
- [ ] Создать скрипты автоматической установки
- [ ] Добавить конфигурации для различных DE
- [ ] Расширить документацию
- [ ] Создать Docker образы для тестирования
- [ ] Добавить CI/CD для проверки конфигураций

### 🧪 Тестирование

Конфигурации тестируются на:

- **Основная система:** Gentoo Linux с systemd
- **Виртуальные машины:** VirtualBox, QEMU
- **Железо:** AMD Ryzen, Intel Core i-series

**Не тестировалось на:**

- ARM архитектуре
- OpenRC init системе
- Экзотическом оборудовании

## 🐛 Решение проблем

### 🔧 Распространенные проблемы

**Проблемы с компиляцией:**

```bash
# Очистить кэш ccache
ccache -C
# Пересобрать пакет без ccache
FEATURES="-ccache" emerge --ask package-name
```

**Проблемы с Wayland:**

```bash
# Проверить переменные окружения
echo $XDG_SESSION_TYPE
echo $WAYLAND_DISPLAY
```

**Проблемы с DWM:**

```bash
# Пересобрать DWM
cd dwm/main/dwm-flexipatch/
make clean && doas make install
```

**Проблемы с конфигурациями:**

```bash
# Откатить изменения Portage
doas cp -r /etc/portage /etc/portage.backup.$(date +%Y%m%d)
# Восстановить из резервной копии
doas cp -r /etc/portage.backup.YYYYMMDD/* /etc/portage/
```

**Системные проблемы:**

```bash
# Проверить целостность системы
doas emerge --ask --depclean
doas emerge --ask --newuse --deep --with-bdeps=y @world
doas revdep-rebuild
```

### ⚠️ Критические предупреждения

- **Не применяйте make.conf** без адаптации под ваш процессор
- **Проверьте USE флаги** - они могут конфликтовать с вашими пакетами
- **Делайте snapshot'ы** перед большими изменениями
- **Тестируйте на виртуалках** перед применением на основной системе

## 🤝 Участие в разработке

1. Fork репозитория
2. Создайте feature branch (`git checkout -b feature/amazing-feature`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing-feature`)
5. Создайте Pull Request

## 📜 Лицензия

Этот проект распространяется под **кастомной лицензией** с следующими условиями:

- ✅ **Разрешено:** Личное использование, изучение, модификация, распространение
- ❌ **Запрещено:** Коммерческое использование, патентные претензии, закрытие производных работ
- 🔒 **Требования:** Все производные работы должны быть открытыми и распространяться под той же лицензией
- 🛡️ **Защита:** Встроенная защита от патентных претензий

**Для коммерческого использования требуется письменное разрешение автора.**

См. файл [`LICENSE`](LICENSE) для полного текста лицензии.

## 📞 Контакты

- **Автор:** skreamer (mvko)
- **GitHub:** [your-profile](https://github.com/your-username)

---

<div align="center">

**⭐ Понравился проект? Поставьте звездочку! ⭐**

_Создано с ❤️ для сообщества Gentoo Linux_

</div>
