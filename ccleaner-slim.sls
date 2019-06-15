{% set PROGRAM_FILES = "%ProgramFiles%" %}
ccleaner-slim:
  {% for version in ['5.57', '5.58'] %}
  '{{ version }}':
    {% set dl_version = version | replace(".","") %}
    full_name: 'CCleaner'
    installer: 'https://download.ccleaner.com/slim/ccsetup{{ dl_version }}_slim.exe'
    install_flags: '/S'
    uninstaller: '{{ PROGRAM_FILES }}\CCleaner\uninst.exe'
    uninstall_flags: '/S'
    msiexec: False
    locale: en_US
    reboot: False
  {% endfor %}
