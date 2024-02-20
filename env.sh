export PATH="~/.pyenv/bin: $PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

export MINARD_SETTINGS=`pwd`/settings.conf
