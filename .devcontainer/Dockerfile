FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Instalar dependências do sistema
RUN apt update && \
    apt install -y software-properties-common && \
    add-apt-repository -y ppa:neovim-ppa/unstable && \
    apt update && \
    apt upgrade -y && \
    apt -y install --no-install-recommends \
    build-essential \
    curl \
    git \
    tmux \
    zsh \
    libssl-dev \
    libffi-dev \
    python3-dev \
    pkg-config \
    gcc \
    g++ \
    make \
    cmake \
    libcurl4-openssl-dev \
    libsqlite3-dev \
    default-libmysqlclient-dev && \
    apt install -y neovim && \
    apt clean -y && \
    rm -rf /var/lib/apt/lists/* && \
    chsh -s /bin/zsh

# Configurar o usuário vscode
USER vscode
WORKDIR /home/vscode

# Instalar uv e ferramentas Python
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/home/vscode/.local/bin:$PATH" && \
    . "/home/vscode/.local/bin/env" && \
    echo 'export PATH="/home/vscode/.local/bin:$PATH"' >> ~/.zshrc && \
    echo 'source "/home/vscode/.local/bin/env"' >> ~/.zshrc

# Instalar versões do Python e ferramentas
RUN export PATH="/home/vscode/.local/bin:$PATH" && \
    . "/home/vscode/.local/bin/env" && \
    uv python install 3.11 3.12 3.13 && \
    uv tool install ruff && \
    uv tool install tox --with tox-uv

# Configurar Git
RUN git config --global user.name "Emerson Delatorre" && \
    git config --global user.email "38289677+fazedordecodigo@users.noreply.github.com"

# Instalar fontes Nerd Fonts
RUN git clone --depth 1 https://github.com/ryanoasis/nerd-fonts.git && \
    cd nerd-fonts && \
    ./install.sh FiraCode && \
    ./install.sh JetBrainsMono && \
    cd .. && \
    rm -rf nerd-fonts

# Instalar e configurar fzf
RUN git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf && \
    ~/.fzf/install --all

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Adicionar binários Rust ao PATH
ENV PATH="/home/vscode/.cargo/bin:${PATH}"
ENV RUSTUP_HOME=/home/vscode/.rustup
ENV CARGO_HOME=/home/vscode/.cargo

# Instalar EZA
RUN . "$HOME/.cargo/env" && cargo install eza

# Instalar plugins do ZSH
RUN mkdir -p ~/.zsh && \
    git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.zsh/zsh-syntax-highlighting && \
    git clone https://github.com/zsh-users/zsh-history-substring-search.git ~/.zsh/zsh-history-substring-search

# Instalar Oh My Zsh e tema
RUN rm -rf ~/.oh-my-zsh && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended && \
    mkdir -p ~/.oh-my-zsh/custom/themes && \
    git clone --depth=1 https://github.com/spaceship-prompt/spaceship-prompt.git ~/.oh-my-zsh/custom/themes/spaceship-prompt && \
    ln -s ~/.oh-my-zsh/custom/themes/spaceship-prompt/spaceship.zsh-theme ~/.oh-my-zsh/custom/themes/spaceship.zsh-theme

RUN echo 'export GPG_TTY=$(tty)' >> ~/.zshrc && \
    echo '' >> ~/.zshrc && \
    echo 'ZSH_THEME="spaceship"' >> ~/.zshrc && \
    echo '' >> ~/.zshrc && \
    echo '#plugins:' >> ~/.zshrc && \
    echo 'source ~/.cargo/env' >> ~/.zshrc && \
    echo 'source ~/.oh-my-zsh/oh-my-zsh.sh' >> ~/.zshrc && \
    echo 'source ~/.local/bin/env' >> ~/.zshrc && \
    echo 'source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh' >> ~/.zshrc && \
    echo 'source ~/.zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh' >> ~/.zshrc && \
    echo 'source ~/.zsh/zsh-history-substring-search/zsh-history-substring-search.zsh' >> ~/.zshrc && \
    echo '' >> ~/.zshrc && \
    echo '[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh' >> ~/.zshrc && \
    echo '' >> ~/.zshrc && \
    echo 'plugins=(' >> ~/.zshrc && \
    echo '  dircycle' >> ~/.zshrc && \
    echo '  git' >> ~/.zshrc && \
    echo '  gitignore' >> ~/.zshrc && \
    echo '  pip' >> ~/.zshrc && \
    echo '  pre-commit' >> ~/.zshrc && \
    echo '  python' >> ~/.zshrc && \
    echo '  poetry' >> ~/.zshrc && \
    echo '  ssh-agent' >> ~/.zshrc && \
    echo '  ubuntu' >> ~/.zshrc && \
    echo '  vscode' >> ~/.zshrc && \
    echo ')' >> ~/.zshrc && \
    echo '' >> ~/.zshrc && \
    echo 'zstyle :omz:plugins:ssh-agent identities id_ed25519' >> ~/.zshrc && \
    echo 'zstyle '\'':completion:*:*:docker:*'\'' option-stacking yes' >> ~/.zshrc && \
    echo 'zstyle '\'':completion:*:*:docker-*:*'\'' option-stacking yes' >> ~/.zshrc && \
    echo '' >> ~/.zshrc && \
    echo '#settings for zsh-history-substring-search' >> ~/.zshrc && \
    echo 'bindkey '\''^[[A'\'' history-substring-search-up' >> ~/.zshrc && \
    echo 'bindkey '\''^[[B'\'' history-substring-search-down' >> ~/.zshrc && \
    echo 'bindkey '\''^[[1;4D'\'' insert-cycledleft' >> ~/.zshrc && \
    echo 'bindkey '\''^[[1;4C'\'' insert-cycledright' >> ~/.zshrc && \
    echo '' >> ~/.zshrc && \
    echo '#alias:' >> ~/.zshrc && \
    echo 'alias zshconfig="code ~/.zshrc"' >> ~/.zshrc && \
    echo 'alias ohmyzsh="code ~/.oh-my-zsh"' >> ~/.zshrc && \
    echo 'alias pbcopy="xclip -selection clipboard"' >> ~/.zshrc && \
    echo 'alias pbpaste="xclip -selection clipboard -o"' >> ~/.zshrc && \
    echo 'alias cls="clear"' >> ~/.zshrc && \
    echo 'alias ls="eza -la"' >> ~/.zshrc

# Configurar o PATH permanentemente
ENV PATH="/home/vscode/.local/bin:$PATH"

# ... rest of the file remains unchanged ...
