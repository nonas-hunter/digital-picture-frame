# Digital Picture Frame
Repository for digital display using a raspberry pi.


### Setup Python Enviornment
For the python environment we are using [pyenv](https://github.com/pyenv/pyenv/#installation) so we can easily manage and upgrade our enviornment if needed.

We can begin the installation process by installing the required libraries:
```
sudo apt update; sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
Then we can install pyenv using the installer script from [pyenv-install](https://github.com/pyenv/pyenv-installer):
```
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```
Finally, we can run the following code to edit our .bashrc and add code to initalized pyenv when our terminal starts up:
```bash
echo -e '# set PATH so it includes PyEnv bin\nexport PYENV_ROOT="$HOME/.pyenv"\nexport PATH="$PYENV_ROOT/bin:$PATH"\n\n# initalized pyenv\neval "$(pyenv init --path)"\neval "$(pyenv init -)"\n' >> ~/.bashrc
```
Now that we've installed pyenv, we can begin installing python itself. We are currently using python 3.9.5 for this project. We can install python 3.9.5 using the code bellow:
```bash
pyenv install 3.9.5
pyenv global 3.9.5
```
Now that python3 is all setup, let's install pipx to manage our python packages. Run the following lines of code:
```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```
