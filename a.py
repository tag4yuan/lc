import subprocess
import time

def start_project():
    try:
        # 使用 subprocess.Popen 启动外部脚本
        process = subprocess.Popen(
            ['python', '-u', 'b.py'],  # 执行 b.py 脚本
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1  # 启用行缓冲，实时获取输出
        )

        # 实时捕获标准输出
        output_lines = []
        print("Real-time Output:")
        # 使用逐行读取的方法来实时显示输出
        while True:
            line = process.stdout.readline()
            if line:  # 如果有输出，则打印
                line = line.strip()
                output_lines.append(line)
                print(line)
            elif process.poll() is not None:  # 当进程结束时，退出循环
                break

        # 等待进程结束，并获取标准错误
        process.stdout.close()  # 关闭标准输出管道
        error_output = process.stderr.read().strip()  # 捕获所有错误输出
        process.stderr.close()  # 关闭标准错误管道

        result = {
            "status": "success",
            "message": "started successfully",
            "stdout": "\n".join(output_lines),  # 合并所有输出
            "stderr": error_output  # 错误输出
        }

        if result["stderr"]:
            print("\nErrors:\n", result["stderr"])

    except Exception as e:
        result = {
            "status": "error",
            "message": str(e)
        }
        print("An error occurred:", result["message"])

# 直接调用函数
if __name__ == "__main__":
    start_project()
