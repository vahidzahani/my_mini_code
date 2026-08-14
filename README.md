# 🧰 My Mini Code Collection

Welcome to the `my_mini_code` folder — a collection of small Python scripts created for automation, data extraction, file handling, and GUI development. Below you'll find a summary of each file and its purpose.

---

## 🔊 `boogh.py`
Plays beeps using the `winsound` module with customizable frequency and duration.  
Useful for creating sound notifications or alerts.

---

## 🔗 `extract_links.py`
Extracts all hyperlinks from HTML content using `requests` and `BeautifulSoup`.  
Great for basic web scraping tasks.

---

## 🔢 `extract_Number.py`
Uses regular expressions to extract numbers from text or files.  
Perfect for parsing numerical data from mixed content.

---

## 📂 `file_list_move.py`
Moves files based on a predefined list of filenames.  
Uses `os` and `shutil` to handle file transfers between folders.

---

## 📄 `get children.txt`
A plain text file, most likely containing a list of child file paths or filenames.  
Used in conjunction with `file_list_move.py`.

---

## 🖼️ `my svg gallery.py`
A simple script to build and display a gallery of SVG files.  
Can be used for previewing icons, illustrations, or assets.

---

## 🖥️ `svg_gallery_gui.py`
A GUI version of the SVG gallery built with `Tkinter`.  
Provides a user-friendly visual interface to browse SVG files.

---

## ⏱️ `timer.py`
Implements a timer or delay mechanism using `datetime` and `time.sleep()`.  
Can be combined with sound alerts from `boogh.py`.

---

## 📊 `vahid_log_analyzer.py`
Analyzes log files to extract key information such as events, timestamps, or errors.  
A basic log parser for quick data inspection and diagnostics.

---

## 📘 `README.md`
You're reading it 😊 — this file explains the purpose of each script in the folder.

---


---

## 🌐 `ip_country_alert.py`

Monitors the system's public IP address every 30 seconds and checks its country.
If the public IP is detected as belonging to Iran (`IR`), the script displays an alert and plays a Ding sound using the `winsound` module.

---



## ✅ Usage Tips
- All scripts are written in **Python 3**.
- Make sure to install external dependencies such as `beautifulsoup4` if needed:
  ```bash
  pip install beautifulsoup4
