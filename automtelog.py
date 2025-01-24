import os

# Define paths
log_file_path = 'dataset/Hadoop_2k.log'  # Existing dataset
output_dir = 'result'  # Output directory for results

# Ensure the result directory exists
os.makedirs(output_dir, exist_ok=True)

def analyze_logs(file_path):
    error_exception_logs = []

    # Read the existing log file
    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line or "EXCEPTION" in line:
                error_exception_logs.append(line.strip())

    # Save results to TXT file
    save_to_txt(error_exception_logs)

def save_to_txt(logs):
    """Save logs to a TXT file."""
    txt_file_path = os.path.join(output_dir, "log_analysis.txt")
    with open(txt_file_path, "w") as file:
        file.write("ERROR and EXCEPTION Logs\n")
        file.write("=" * 40 + "\n")
        for log in logs:
            file.write(log + "\n")
    print(f"Logs saved to TXT file: {txt_file_path}")

if __name__ == "__main__":
    if os.path.exists(log_file_path):
        analyze_logs(log_file_path)
    else:
        print(f"Log file not found: {log_file_path}")
