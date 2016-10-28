from plan import Plan
import os


if __name__ == "__main__":
  ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
  cron = Plan("commands")
  # online
  cron.command('/usr/local/bin/node %s/ghost/online.js'%ROOT_PATH, every='1.day', at="hour.21 minute.30", output=
               dict(stdout='%s/log/online_stdout.log'%ROOT_PATH,
                    stderr='%s/log/online_stderr.log'%ROOT_PATH))
  # offline
  cron.command('/usr/local/bin/node %s/ghost/offline.js'%ROOT_PATH, every='1.day', at="hour.7", output=
               dict(stdout='%s/log/offline_stdout.log'%ROOT_PATH,
                    stderr='%s/log/offline_stderr.log'%ROOT_PATH))

  cron.run("check")
  cron.run("write")