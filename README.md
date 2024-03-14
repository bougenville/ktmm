# ktmm (Keep That Mouse Moving!)

Thanks to [Andrew Odendaal](https://github.com/ao/ktmm)

## Use pyenv and pyenv-virtualenv (my method of running this tool)

1. Prepare the env
    - macOS
    ```zsh
    brew install pyenv-virtualenv
    ```
    - Linux
    ```bash
    gh repo clone pyenv/pyenv ~/.pyenv
    gh repo clone pyenv/pyenv-virtualenv ~/.pyenv/plugins/pyenv-virtualenv
    ```

1. Add below to your `~/.zprofile` or `~/.bash_profile`:
    ```zsh
    # pyenv
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH=$PYENV_ROOT/shims:$PATH
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```

1. Install virtualenv
    ```zsh
    pyenv install 3.12.2 # if you don't know the exact version, use TAB to show the hints
    pyenv virtualenv 3.12.2 ktmm
    ```

    If you want to download the Python package by using another mirror site instead of the [official ftp site](https://www.python.org/ftp/python/), here is the solution:

    ```bash
    mkdir -p ~/.pyenv/cache
    export v=x.y.z; wget https://repo.huaweicloud.com/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/; pyenv install $v
    ```

    You shall also use the script provided by this repo, with the following:
    ```bash
    sudo mv -v `pwd`/pyenv-install /usr/local/bin
    ```

1. Final preparation
    ```zsh
    # git clone https://github.com/kalabsha/ktmm.git ~/Code/ktmm
    gh repo clone kalabsha/ktmm ~/Code/ktmm
    cd ~/Code/ktmm
    penv shell ktmm
    python -m pip install -U pip -i https://pypi.douban.com/simple
    pip install -r requirements.txt -i https://pypi.douban.com/simple
    ```

    > Update: I forgot something when migrate this script to macOS,
    > now try `pip install -r requirements.macOS.txt` instead.
    > But usually, try to run `python ktmm.py` first,
    > you might want to install the packages needed only and
    > let `pip` do the rest. Here in this case, it is `pynput`.

1. Make the command alias, Run `ktmm` thereafter.
    ```zsh
    alias ktmm="cd ~/Code/ktmm && pyenv shell ktmm && python ktmm.py"
    ```
