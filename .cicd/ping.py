import salt.config
import salt.loader

overrides = {"root_dir": "/tmp/salt"} 
__opts__ = salt.config.apply_minion_config(overrides | {"grains": {"cpuarch": "AMD64"}})

__utils__ = salt.loader.utils(__opts__)
__salt__ = salt.loader.minion_mods(__opts__)

testmod = salt.loader.raw_mod(__opts__, 'test', None)
print(testmod['test.ping']())
print(testmod['test.get_opts']())

grainsmod = salt.loader.raw_mod(__opts__, "grains", None)
print(grainsmod["grains.items"]())

winrepomod = salt.loader.raw_mod(__opts__, 'winrepo', __salt__)
print(winrepomod["winrepo.show_sls"]("arduino-ide.sls"))
print(winrepomod["winrepo.show_sls"]("vscode.sls"))
print(winrepomod["winrepo.show_sls"]("openvpn.sls"))
