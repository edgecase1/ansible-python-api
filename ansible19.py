

from ansible.playbook import PlayBook
from ansible import callbacks, utils

import jinja2
from tempfile import NamedTemporaryFile
import os



playbook_callback = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
stats = callbacks.AggregateStats()
runner_callback = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

HOST_LIST_TEMPLATE = """
[local]
localhost

[{{group_name}}]
{{ip_address}}
"""

template = jinja2.Template(HOST_LIST_TEMPLATE)
temp = NamedTemporaryFile(delete=False)
temp.write(template.render({'group_name': 'ansible', 'ip_address': "192.168.56.212"}))
temp.close()

playbook = PlayBook(remote_user='ansible',
                    private_key_file='/etc/ansible/ansible.key.pem',
                    playbook='playbook.yml',
                    callbacks=playbook_callback,
                    runner_callbacks=runner_callback,
                    stats=stats,
                    host_list=temp.name
                    )

results = playbook.run()


