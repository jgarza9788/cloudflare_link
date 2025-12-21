import os, sys, subprocess, time, re

DIR = os.path.dirname(os.path.abspath(__file__))


def run_cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def main():
    try:
        os.remove('log')
    except FileNotFoundError:
        pass

    # start cloudflared
    proc = run_cmd('cloudflared tunnel --url http://192.168.1.250:5055 --logfile ./log')

    # give it time to start
    time.sleep(10)

    with open('log', 'r') as file:
        nlog = file.read()

    # grab first https:// link
    link = re.findall(r'"message":"\|  https://.*.com', nlog)[0]
    link = link.replace('"message":"|  ',"")
    print(link)

    ffpath = os.path.join(DIR,'overseerr_link.txt')

    with open(ffpath,'w') as file:
        file.write(link)

    run_cmd(f'rclone copy {ffpath} drive_202508:temp/ ')


    # keep cloudflared alive
    proc.wait()


if __name__ == "__main__":
    main()
