import os
import re

# الگو برای شناسایی ایمیل‌ها
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# الگو برای شناسایی لینک‌ها
link_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

# مسیر پوشه‌ی اصلی
source_dir = 'sources'

# لیستی برای نگهداری ایمیل‌ها و لینک‌ها
emails_and_links = []

# پیمایش پوشه‌ها و فایل‌ها
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            # باز کردن فایل برای خواندن
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # استخراج ایمیل‌ها
                emails = re.findall(email_pattern, content)
                # استخراج لینک‌ها
                links = re.findall(link_pattern, content)
                # افزودن ایمیل‌ها و لینک‌ها به لیست
                emails_and_links.extend(emails)
                emails_and_links.extend(links)
        except Exception as e:
            print(f"خطا در خواندن فایل {file_path}: {e}")

# نوشتن ایمیل‌ها و لینک‌ها در فایل vahid.txt
with open('vahid.txt', 'w', encoding='utf-8') as output_file:
    for item in emails_and_links:
        output_file.write(item + '\n')

print("استخراج ایمیل‌ها و لینک‌ها تمام شد و در فایل vahid.txt ذخیره شدند.")
