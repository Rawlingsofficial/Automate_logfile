import os
import re
from datetime import datetime
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# path to the log file and the output directory for visualizations
log_file_path = 'dataset/Hadoop_2k.log'
output_dir = 'result'  # Change to the existing result directory

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def analyze_logs(file_path):
    log_counts = {'ERROR': 0, 'WARN': 0, 'INFO': 0}
    log_messages = {'ERROR': []}
    log_timestamps = {'ERROR': [], 'WARN': [], 'INFO': []}

    # Read the log file
    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                log_counts['ERROR'] += 1
                log_messages['ERROR'].append(line.strip())
                timestamp = extract_timestamp(line)
                if timestamp:
                    log_timestamps['ERROR'].append(timestamp)
            elif 'WARN' in line:
                log_counts['WARN'] += 1
                timestamp = extract_timestamp(line)
                if timestamp:
                    log_timestamps['WARN'].append(timestamp)
            elif 'INFO' in line:
                log_counts['INFO'] += 1
                timestamp = extract_timestamp(line)
                if timestamp:
                    log_timestamps['INFO'].append(timestamp)

    # Print the results
    print(f"Total ERROR entries: {log_counts['ERROR']}")
    print(f"Total WARN entries: {log_counts['WARN']}")
    print(f"Total INFO entries: {log_counts['INFO']}")

    # Save ERROR messages to PDF and TXT
    save_errors_to_pdf(log_messages['ERROR'])
    save_errors_to_txt(log_messages['ERROR'])

    # Perform some basic analytics
    print("\nBasic Analytics:")
    total_entries = sum(log_counts.values())
    print(f"Total log entries: {total_entries}")

    # Frequency of logs over time
    analyze_time_series(log_counts)

def extract_timestamp(log_line):
    """Extract timestamp from the log line."""
    match = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', log_line)
    if match:
        return datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
    return None

def analyze_time_series(log_counts):
    """Analyze frequency of logs and create a single visualization."""
    # Prepare data for plotting
    labels = list(log_counts.keys())
    counts = list(log_counts.values())

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.bar(labels, counts, color=['red', 'orange', 'green'], alpha=0.6)
    plt.xlabel('Log Level')
    plt.ylabel('Count')
    plt.title('Frequency of Logs (ERROR, WARN, INFO)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(os.path.join(output_dir, 'log_frequency.png'))
    plt.close()

def save_errors_to_pdf(error_messages):
    """Save ERROR messages to a PDF file."""
    pdf_file_path = os.path.join(output_dir, 'error_logs.pdf')
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    c.setFont("Helvetica", 10)
    
    # Add title
    c.drawString(50, 750, "ERROR Logs")
    
    # Add each error message to the PDF
    y_position = 730
    for msg in error_messages:
        c.drawString(50, y_position, msg)
        y_position -= 12  # Move down for the next line
        if y_position < 50:  # Check if we need a new page
            c.showPage()
            c.setFont("Helvetica", 10)
            y_position = 750

    c.save()
    print(f"\nERROR logs saved to {pdf_file_path}")

def save_errors_to_txt(error_messages):
    """Save ERROR messages to a TXT file."""
    txt_file_path = os.path.join(output_dir, 'error_logs.txt')
    with open(txt_file_path, 'w') as file:
        file.write("ERROR Logs\n")
        file.write("=" * 40 + "\n")
        for msg in error_messages:
            file.write(msg + "\n")
    print(f"ERROR logs saved to {txt_file_path}")

if __name__ == "__main__":
    analyze_logs(log_file_path)
