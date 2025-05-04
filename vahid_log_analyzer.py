import re
import os
from collections import Counter, defaultdict

# Log file
log_file = 'allog'  # Replace with your actual log file

# Suspicious user agents
suspicious_agents_keywords = [
    'python-requests',
    'GRequests',
    '-',  # empty user-agent
]

# Counters for tracking IPs, user agents, dates, etc.
date_ip_counter = Counter()
agent_ip_counter = Counter()
date_counter = Counter()
user_agent_counter = Counter()
ip_per_day = defaultdict(Counter)  # To count IPs per day

# Regular expression pattern to parse log file
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<datetime>\d{2}/\w{3}/\d{4}):[^\]]+\] '
    r'"(?:GET|POST) (?P<path>[^ ]+)[^"]*" \d+ \d+ "-" "(?P<agent>[^"]+)"'
)

# Get the directory of the log file
log_dir = os.path.dirname(os.path.abspath(log_file))

# Create a folder with the name of the log file (without extension)
log_folder_name = os.path.basename(log_file) + "_"
output_dir = os.path.join(log_dir, log_folder_name)

# Create the directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open and read the log file
with open(log_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = log_pattern.search(line)
        if match:
            ip = match.group('ip')
            date = match.group('datetime')
            agent = match.group('agent').strip()

            # Count IPs based on suspicious user agents
            for keyword in suspicious_agents_keywords:
                if agent.lower().startswith(keyword.lower()):
                    agent_ip_counter[ip] += 1
                    break

            # Count requests for each date
            date_counter[date] += 1
            ip_per_day[date][ip] += 1  # Count the number of requests for each IP on a given day

            # Count the user agents
            user_agent_counter[agent] += 1

# Identify suspicious dates (more than 400 requests)
suspicious_dates = {date for date, count in date_counter.items() if count > 400}

# Save IPs based on suspicious user agents
with open(os.path.join(output_dir, 'ips_by_useragent.txt'), 'w', encoding='utf-8') as f:
    for ip in sorted(agent_ip_counter):
        f.write(ip + '\n')

# Save request counts based on suspicious user agents
with open(os.path.join(output_dir, 'ips_by_useragent_count.txt'), 'w', encoding='utf-8') as f:
    for ip, count in agent_ip_counter.most_common():
        f.write(f"{ip} => {count} requests\n")

# Save top dates (more than 400 requests)
with open(os.path.join(output_dir, 'top_days.txt'), 'w', encoding='utf-8') as f:
    for date, count in date_counter.items():
        if count > 400:
            f.write(f"{date} => {count} requests\n")

# Save output of Top User Agents and Top Dates
with open(os.path.join(output_dir, 'top_user_agents_and_dates.txt'), 'w', encoding='utf-8') as f:
    # Save Top User Agents
    f.write("=== Top User Agents ===\n")
    for agent, count in user_agent_counter.most_common():
        f.write(f"{agent} => {count}\n")
    
    # Save Top Dates
    f.write("\n=== Top Dates ===\n")
    for date, count in date_counter.most_common():
        f.write(f"{date} => {count}\n")

# Find the most requested IP on the most active days
with open(os.path.join(output_dir, 'top_day_and_ip.txt'), 'w', encoding='utf-8') as f:
    # Identify days with more than 400 requests
    for date in suspicious_dates:
        f.write(f"\n=== Most Requests on {date} ===\n")
        # Find the IP with the most requests on that day
        most_requested_ip = ip_per_day[date].most_common(1)[0]  # IP with the most requests
        f.write(f"Most Requested IP: {most_requested_ip[0]} with {most_requested_ip[1]} requests\n")

print("✅ Extraction completed. All files have been saved.")
