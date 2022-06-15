# ktmm (Keep That Mouse Moving!)

Thanks to [Andrew Odendaal](https://github.com/ao/ktmm)

## Use pyenv and pyenv-virtualenv (my method of running this tool)

1. Prepare the env
    ```zsh
    brew install pyenv-virtualenv
    ```

1. Add below to your `~/.zprofile`:
    ```zsh
    # pyenv
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH=$PYENV_ROOT/shims:$PATH
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```

1. Install virtualenv
    ```zsh
    pyenv install 3.10.4 # if you don't know the exact version, use TAB to show the hints
    pyenv virtualenv 3.10.4 ktmm
    ```

1. Final preparation
    ```zsh
    # git clone https://github.com/bougenville/ktmm.git ~/Code/ktmm
    gh repo clone bougenville/ktmm ~/Code/ktmm
    cd ~/Code/ktmm
    penv shell ktmm
    python -m pip install -U pip -i https://pypi.douban.com/simple
    pip install -r requirements.txt -i https://pypi.douban.com/simple
    ```

1. Make the command alias, Run `ktmm` thereafter.
    ```zsh
    alias ktmm="cd ~/Code/ktmm && pyenv shell ktmm && python ktmm.py"
    ```
