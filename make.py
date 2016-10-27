from plan import Plan

cron = Plan("commands")

cron.command('node /home/cps/dev/my/shadow/ghost/schemel.js', every='5.minute', output=
             dict(stdout='/tmp/top_stdout.log',
                  stderr='/tmp/top_stderr.log'))

if __name__ == "__main__":
    cron.run("check")
    cron.run("write")