import subprocess
prin = subprocess.run(["zippyshare-dl","https://www62.zippyshare.com/v/ZMHll2Qa/file.html"], capture_output=True, text=True).stdout.strip("\n")
print(prin)