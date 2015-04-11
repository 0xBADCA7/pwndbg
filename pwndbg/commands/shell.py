import gdb
import os
import pwndbg.commands

shellcmds = [
    "awk",
    "bash",
    "cat",
    "chattr",
    "chmod",
    "chown",
    "clear",
    "cp",
    "date",
    "dd",
    "diff",
    "egrep",
    "find",
    "grep",
    "htop",
    "id",
    "kill",
    "killall",
    "less",
    "ln",
    "ls",
    "man",
    "mkdir",
    "mktemp",
    "more",
    "mv",
    "nano",
    "nc",
    "ping",
    "pkill",
    "ps",
    "pstree",
    "pwd",
    "rm",
    "sed",
    "sh",
    "sort",
    "sort",
    "ssh",
    "sudo",
    "tail",
    "top",
    "touch",
    "uniq",
    "vi",
    "vim",
    "w",
    "wc",
    "wget",
    "who",
    "whoami",
    "zsh",
]

print "RELOADED"

def register_shell_function(cmd):
    def handler(*a):
        """Invokes %s""" % cmd
        if os.fork() == 0:
            os.execvp(cmd, (cmd,) + a)
        os.wait()
    handler.__name__ = cmd
    pwndbg.commands.Command(handler)

for cmd in shellcmds:
    register_shell_function(cmd)
