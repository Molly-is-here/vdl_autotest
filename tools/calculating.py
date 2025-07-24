import os
import pandas as pd

folder_path = r"C:\Users\user\Desktop\0724_V1.7.2测试数据"
columns = ['GPU利用率/%', '显存使用量/Mib', 'CPU利用率/%', '内存使用量/MB', '磁盘使用量/MB']

results = []

for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        filepath = os.path.join(folder_path, filename)
        try:
            df = pd.read_excel(filepath)
            df.columns = [col.strip() for col in df.columns]

            if not all(col in df.columns for col in columns):
                print(f"⚠️ 文件 {filename} 缺少必要列，跳过。实际列名：{df.columns.tolist()}")
                continue

            # 过滤条件：GPU利用率≥10，且所有指标≥0
            df_filtered = df[df['GPU利用率/%'] >= 10]
            for col in columns:
                df_filtered = df_filtered[df_filtered[col] >= 0]

            if df_filtered.empty:
                print(f"⚠️ 文件 {filename} 中符合条件的数据为空，跳过。")
                continue

            max_vals = df_filtered[columns].max().round(2)
            min_vals = df_filtered[columns].min().round(2)
            mean_vals = df_filtered[columns].mean().round(2)

            result = {
                '文件名': filename,
                'GPU利用率MAX/%': max_vals['GPU利用率/%'],
                'GPU利用率MIN/%': min_vals['GPU利用率/%'],
                'GPU利用率AVG/%': mean_vals['GPU利用率/%'],

                '显存使用量MAX/Mib': max_vals['显存使用量/Mib'],
                '显存使用量MIN/Mib': min_vals['显存使用量/Mib'],
                '显存使用量AVG/Mib': mean_vals['显存使用量/Mib'],

                'CPU利用率MAX/%': max_vals['CPU利用率/%'],
                'CPU利用率MIN/%': min_vals['CPU利用率/%'],
                'CPU利用率AVG/%': mean_vals['CPU利用率/%'],

                '内存使用量MAX/MB': max_vals['内存使用量/MB'],
                '内存使用量MIN/MB': min_vals['内存使用量/MB'],
                '内存使用量AVG/MB': mean_vals['内存使用量/MB'],

                '磁盘使用量MAX/MB': max_vals['磁盘使用量/MB'],
                '磁盘使用量MIN/MB': min_vals['磁盘使用量/MB'],
                '磁盘使用量AVG/MB': mean_vals['磁盘使用量/MB'],
            }

            results.append(result)

        except Exception as e:
            print(f"❌ 处理文件 {filepath} 时出错：{e}")

if results:
    result_df = pd.DataFrame(results)
    output_path = os.path.join(folder_path, '汇总结果.xlsx')
    result_df.to_excel(output_path, index=False)
    print(f"\n✅ 汇总完成，结果保存在：{output_path}")
else:
    print("❗ 没有成功处理的数据。")
