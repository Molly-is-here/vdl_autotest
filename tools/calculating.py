import statistics
import csv
import pandas as pd
import os


def calculate_data(file_name):
    with open(file_name, 'r', newline='', errors='replace') as read_f:
        read_file = pd.read_csv(read_f)
        columns = ['GPU利用率/%', '显存使用量/Mib','CPU利用率/%','内存使用量/MB','磁盘使用量/GB']

        result_df = pd.DataFrame(columns=columns) 

        for column in columns:
            column_total = {}
            if column not in read_file.columns:
                print(f"Column '{column}' not found in the CSV file.")
                continue

            max_value = read_file[column].max()
            min_value = read_file[column].min()
            avg_value = read_file[column].mean()
            avg = round(avg_value,2)
            variance_value = statistics.variance(read_file[column])
            van_value = round(variance_value,2)
            range_value = max_value - min_value
            ran_value = round(range_value,2)

            column_total[column] = {
                    'max': max_value,
                    'min': min_value,
                    'avg': round(avg_value,2),
                    'van': round(van_value,2),
                    'ran' :round(range_value,2)
                }


            new_row = pd.DataFrame({'GPU利用率/%': ['max:'+ str(max_value)], '显存使用量/Mib': ['min:'+str(min_value)], 'CPU利用率/%': ['avg:'+str(avg)], '内存使用量/MB': ['van:'+str(van_value)], '磁盘使用量/GB': ['ran:'+str(ran_value)]})
            result_df = pd.concat([result_df, new_row], ignore_index=True)

        result_df = result_df.T

        result_df.reset_index(drop=True, inplace=True)

        # 设置新的列名
        result_df.columns = ['GPU利用率/%', '显存使用量/Mib', 'CPU利用率/%', '内存使用量/MB', '磁盘使用量/GB']

        result_df.to_csv(file_name, mode='a', index=True, encoding='gbk', header=True)


if __name__ == "__main__":
    path = r"C:\Users\yunli\Desktop\ly_autotest\2060\test" 
    files = os.listdir(path)
    for file in files:
        file_name = path + "\\" + file
        calculate_data(file_name)