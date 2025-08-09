import re

def extract_phone_numbers(input_file, output_file):
    # الگوی regex برای شناسایی شماره‌های تلفن
    phone_pattern = re.compile(r'(\+98|0098|0)?9\d{9}')

    # باز کردن فایل ورودی و خواندن محتوا
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # استخراج شماره‌های تلفن با استفاده از الگوی regex
    phone_numbers = phone_pattern.finditer(content)

    # نوشتن شماره‌های تلفن در فایل خروجی
    with open(output_file, 'w', encoding='utf-8') as file:
        for match in phone_numbers:
            # کل شماره تلفن را از match بگیرید
            full_number = match.group(0)
            file.write(full_number + '\n')

    print(f"تعداد شماره‌های تلفن استخراج شده: {len(list(phone_numbers))}")

# نام فایل‌های ورودی و خروجی
input_file = 'number.txt'
output_file = 'vahid.txt'

# فراخوانی تابع برای استخراج شماره‌های تلفن
extract_phone_numbers(input_file, output_file)