import logging
from salt._logging import *
import sys

setup_console_handler(LOG_LEVELS["trace"])

# Configure the root logger to output to the console.
#logging.basicConfig(
#    level=salt._logging.TRACE,  # Set the desired level (DEBUG, INFO, etc.)
#    stream=sys.stdout,    # Explicitly log to stdout; by default it goes to stderr.
#    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#)

import salt.config
import salt.client

logging.info("Salt API logging initialized.")

overrides = {"file_client": "local", "log_level_logfile": "info", "providers": {"winrepo": "winrepo"},  "root_dir": "/tmp/salt"} 
__opts__ = salt.config.apply_minion_config(overrides | {"grains": {"cpuarch": "AMD64"}})

caller = salt.client.Caller(mopts=__opts__)

print(caller.cmd("test.ping"))


print(caller.cmd("test.get_opts"))

print(caller.cmd("grains.items"))

print(caller.cmd("winrepo.show_sls", "arduino-ide.sls"))
print(caller.cmd("winrepo.show_sls", "vscode.sls"))
print(caller.cmd("winrepo.show_sls", "openvpn.sls"))
