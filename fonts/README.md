# 🔤 JetBrains Mono Nerd Font

## 📖 Описание

**JetBrains Mono** - это бесплатный и открытый моноширинный шрифт, разработанный JetBrains специально для разработчиков. **Nerd Font** версия включает дополнительные глифы и иконки для улучшения внешнего вида терминала и редакторов кода.

## ✨ Особенности

- 🔤 **Моноширинный** - все символы имеют одинаковую ширину
- 👁️ **Читаемость** - оптимизирован для длительного чтения кода
- 🔗 **Лигатуры** - красивые соединения символов (=>, !=, >=, etc.)
- 🎨 **Nerd Font глифы** - иконки для файлов, git статусов, и т.д.
- 🎯 **Множество стилей** - от Thin до ExtraBold
- 📐 **Пропорциональные варианты** - Propo версии для UI

## 📦 Включенные варианты

### 🔤 Стандартные (JetBrainsMonoNerdFont)

- Regular, Bold, Italic, BoldItalic
- Light, Medium, SemiBold
- Thin, ExtraLight, ExtraBold
- - соответствующие Italic версии

### 🔧 Моно (JetBrainsMonoNerdFontMono)

- Только моноширинные символы
- Те же стили что и стандартные

### 📐 Пропорциональные (JetBrainsMonoNerdFontPropo)

- Переменная ширина символов
- Для UI элементов

### 🚫 Без лигатур (JetBrainsMonoNLNerdFont)

- Версии без автоматических лигатур
- Все варианты: стандартный, моно, пропорциональный

## 🛠️ Установка

### 🐧 Linux (пользователь)

```bash
# Копировать в домашнюю директорию
cp -r jetbrainsmono-nerd-font ~/.local/share/fonts/
fc-cache -fv
```

### 🐧 Linux (системно)

```bash
# Копировать системно (требует root)
sudo cp -r jetbrainsmono-nerd-font /usr/share/fonts/
sudo fc-cache -fv
```

### 📱 Проверка установки

```bash
# Проверить доступные шрифты
fc-list | grep "JetBrains"
```

## 🎨 Настройка в приложениях

### 💻 Терминалы

```bash
# Kitty
font_family JetBrains Mono Nerd Font

# Alacritty
font:
  normal:
    family: "JetBrains Mono Nerd Font"

# Terminator
font = JetBrains Mono Nerd Font 12
```

### 🖊️ Редакторы кода

```json
// VSCode
{
  "editor.fontFamily": "JetBrains Mono Nerd Font",
  "editor.fontLigatures": true
}

// Neovim
set guifont=JetBrains\ Mono\ Nerd\ Font:h12
```

### 🎯 DWM/i3status

```c
// config.h
static const char *fonts[] = {
    "JetBrains Mono Nerd Font:size=10:antialias=true:autohint=true"
};
```

## 🔍 Тестирование

Для проверки корректности отображения шрифта используйте эти символы:

```
📁 📄 📊 🔧 ⚡ 🐧 🔒 🌐 💾 🎯

λ ≡ ≠ ≤ ≥ → ← ↑ ↓ ∞

Лигатуры: != == => -> <- >= <= :: .. ...
```

## 📜 Лицензия

JetBrains Mono распространяется под лицензией **SIL Open Font License 1.1**.
Подробности в файле `OFL.txt`.

## 🔗 Ссылки

- [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
- [Nerd Fonts](https://www.nerdfonts.com/)
- [GitHub: JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)
- [GitHub: Nerd Fonts](https://github.com/ryanoasis/nerd-fonts)
