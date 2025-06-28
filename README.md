# ✨ hypr-windowrulex ✨

**Dynamic window rules script for Hyprland**  
![Preview](assets/preview.gif)

---

## 🌟 Motivation

Some windows update their title shortly after they open (like Firefox popups or Picture-in-Picture). Because of this, Hyprland's `windowrulev2` can't set rules on them correctly.

This tool fixes that by listening for title changes right after a window appears and applying rules (**floating**, **move**, **resize**) when they match.

Currently supports **floating**, **move**, and **size**, with more options planned.

---

## 📦 Installation

<!--
### 🐧 From AUR (Arch Linux)

```bash
yay -S hypr-windowrulex
# or
paru -S hypr-windowrulex
```
-->

### 🛠️ From GitHub

1. **Clone the repo:**

   ```bash
   git clone https://github.com/xeyossr/hypr-windowrulex.git
   cd hypr-windowrulex
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pip install nuitka
   ```

3. **Compile with Nuitka:**

   ```bash
   python -m nuitka \
       --onefile \
       --follow-imports \
       --standalone \
       --lto=yes \
       --enable-plugin=upx \
       --show-progress \
       --assume-yes-for-downloads \
       --remove-output \
       hypr_windowrulex.py
   ```

4. **Move the compiled binary to `/usr/bin`:**

   ```bash
   sudo mv hypr_windowrulex.bin /usr/bin/hypr-windowrulex
   ```

---

## ⚙️ Configuration

**See the [Wiki](https://github.com/xeyossr/hypr-windowrulex/wiki) for advanced config options 📚**

---

## 🚀 Usage

Simply run:

```bash
hypr-windowrulex --daemon
```

- By default, it will use `~/.config/hypr/windowrulex.conf`.
- For custom config path:
  ```bash
  hypr-windowrulex --config /path/to/your.conf --daemon
  ```
- Add it to your Hyprland autostart for seamless experience!

---

## 🤝 Contributing

PRs and issues are **very welcome**!  
If you hit a bug, have a feature request, or want to improve the docs, please open an [issue](https://github.com/xeyossr/hypr-windowrulex/issues) or [pull request](https://github.com/xeyossr/hypr-windowrulex/pulls).  
Let's make Hyprland even more awesome together! ✨

---

## 📜 License

hypr-windowrulex is licensed under the [GNU GPL-3.0](LICENSE).

---

## 📚 More

For advanced configuration, troubleshooting, or extra tips,  
**check out the [Wiki](https://github.com/xeyossr/hypr-windowrulex/wiki)!**
