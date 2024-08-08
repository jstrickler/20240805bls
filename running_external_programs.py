from subprocess import run, PIPE, CalledProcessError

# run("notepad")

CMD = "netstat -n"

proc = run(CMD, stdout=PIPE)
# print(proc.stdout.decode())  # decode UTF-8 encoded string into python str

netstat_lines = proc.stdout.decode().splitlines()  # split lines on EOL

# print(netstat_lines)
for line in netstat_lines:
    if "ESTAB" in line:
        print(line)
