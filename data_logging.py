import csv

def log_results(image_name, result):
    with open("quality_control_log.csv", mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([image_name, result])
