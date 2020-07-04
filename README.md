## Setup

### Linux 
```bash
# Requires python 3.8
git clone https://github.com/uncojohnco/test-jc--dd-2019 lsseq-jc && \
cd lsseq-jc  && \
python -m venv venv-lss && \
source ./venv-lss/bin/activate && \
pip install .


# Example usage
> lss ./tests/files/ex1
1 elem.info
46 sd_fx29.%04d.rgb 101-121 123-147
1 strange.xml

## doc
> lss --help
usage: lss [OPTION] [DIRECTORY]...

.

positional arguments:
  directory             the directory to work on. Leave empty to work on the cwd

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

debug:
  -v, --verbose         set logging level to 'debug'
  -d, --debug           enable 'pycharm' debugger
  --host DEBUGGER_HOST  set 'host' for debug server
  --port DEBUGGER_PORT  set 'port' for debug server
```
