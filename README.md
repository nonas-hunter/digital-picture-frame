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
Finally, we can make the following changes to our .profile so pyenv is initialized when the terminal is opened: 
```bash
# set PATH so it includes PyEnv bin
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

# start PyEnv
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```
