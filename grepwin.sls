{% set arch = {'AMD64': '-x64', 'x86': ''}[grains['cpuarch']] %}

grepwin:
{% for version in ['2.0.3'] %}
  '{{ version }}':
    full_name: 'grepWin{{ arch | replace("-", " ") }}'
    installer: 'https://github.com/stefankueng/grepWin/releases/download/{{ version }}/grepWin-{{ version }}{{ arch }}.msi'
    uninstaller: 'https://github.com/stefankueng/grepWin/releases/download/{{ version }}/grepWin-{{ version }}{{ arch }}.msi'
    install_flags: '/qn ALLUSERS=1 /norestart'
    uninstall_flags: '/qn /norestart'
    msiexec: True
    locale: en_US
    reboot: False
{% endfor %} 
