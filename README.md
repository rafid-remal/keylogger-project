# Keylogger Project

## ⚠️ Disclaimer

This project is created **strictly for educational and ethical cybersecurity research purposes only**.

- It demonstrates input logging concepts in a safe environment  
- Do NOT use it on any system without explicit permission  
- Unauthorized use may violate privacy laws and regulations  

---

## 📌 Overview

This is a **safe input logging demo project** designed for learning purposes:

- Python file handling  
- Logging with timestamps  
- Modular project structure  
- Basic CLI interaction  

---

## 🛠️ Features

- User input logging (safe simulation)  
- Timestamped entries  
- File-based log storage  
- Simple and clean Python structure  

---

## 📂 Project Structure

```text
keylogger-project/
├── src/
│   ├── main.py
│   ├── logger.py
│   ├── crypto.py
│   ├── webapp.py
│
├── logs/
│   ├── encrypted.log
│
├── templates/
│   ├── index.html
│
├── README.md
├── requirements.txt
```
---


## ⚙️ Setup (Linux)

### 1. Clone repository

```bash
git clone https://github.com/rafid-remal/keylogger-project.git
cd keylogger-project
```
### 2. Install dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### 3. Run project

```bash
python3 src/main.py
```

### ▶️ Usage

- Run the program and type input:

```bash
> hello
> test input
> exit
```

Logs are stored in:
```bash
logs/keystrokes.log
```

## 🔒 Ethical Notice

- This project is a learning-only simulation and does NOT capture real system keystrokes.

## 🚀 Future Improvements

Add encryption for logs
Web dashboard interface
Log analytics system

## 📜 License

MIT License

---

