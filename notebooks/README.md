jupyter notebooks for prototyping...

https://jupyter.org/
> JupyterLab is a web-based interactive development environment for Jupyter notebooks, code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range of workflows in data science, scientific computing, and machine learning. JupyterLab is extensible and modular: write plugins that add new components and integrate with existing ones.

```bash
git clone https://github.com/uncojohnco/test-jc--dd-2019 lss-jc
cd lss-jc

# Setup venv
python3 -m venv env.lss-jc
source env.lss-jc/bin/activate

# install requirements
python3 -m pip install -r requirements-dev.txt

# launch Jupyter instance
jupyter-lab # A browser tab should open up to connect to the instance
```
