---
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Setup instuctions
## Introduction

These instructions cover how to install Python and other supporting software to your laptop in the department suggested way.

+++ {"tags": ["mac"]}

This version assumes you are installing software on a 2022 16GB Macbook Air laptop with an Apple Silicon M1 chip, as supplied by the department. If you are installing on a Dell Latitude machine, please see the instructions [here](windows_setup.html)

+++ {"tags": ["windows"]}

This version assumes you are installing software on a 2022 16GB Dell Latitude laptop, as supplied by the department. If you are installing on an Apple Macbook machine, please see the instructions [here](mac_setup.html)

+++

Please work through the sections in order. At the end of each part are instructions to test that stage of your installation.


+++ {"tags": ["mac"]}


## Initial bootup

When the laptop first boots, it will ask you to select the macine's language and the country in which you it is operating. You will then be asked to connect to a wifi network. If you are in college, then you can connect to the ImperialWPA identity using your college username which has been sent to you (it will look something like `abc22` or `ab622`) and your college password. The laptop will then download and install an automatic profile from Imperial. Once this is complete, you will be able to log in using your college ID (this time in the form `abc22@ic.ac.uk`).

When your account is created, you will be given the option to set up Screen Time limits, the ability to log in via Touch ID (you can skip both these if you want) and to choose the default colour palette for your user interface.

After all that, you will finally be able to log in, but will have a short wait (probably less than 15 minutes) while supporting software is installed and you are asked to restart your machine.

When the reboot finishes you'll be able to log in (with your username in the `abc22` format) and access the desktop.

![Desktop](images/mac/desktop.png)

 You are now ready to move on to the next section.

### Homebrew - a unix package manager

[Homebrew](https://brew.sh) is a [package manager]() for useful tools, particularly unix command line tools which are not available on MacOS via the app store. It can be installed by opening a Terminal app install(from the Utilities folder inside the Applications tab) and then typing the commands below.
![]()

```{code-cell}
:tags: [mac]
sudo echo "hello"
echo |/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

+++ {"tags": ["mac"]}

You will be asked to enter your password after the first command. Homebrew will install after the second.


You may be asked to access the Terminal on other occasions during the course, so it's work spending a second or two to remember where it lives. You can also secondary click (using two fingers, or the Option key) on the icon in the dock and select `Options > Keep in Dock` from the menu bar so that it is always readily available. 

When Homebrew finishes installing it recommends you run two commands to activate it, and to ensure it's automatically available whenever you open a Terminal window.

```{code-cell}
:tags: [mac]
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> $HOME/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"

```

+++ {"tags": ["mac"]}

Now that `brew` is installed and set up, we can use it to install some useful packages:

```{code-cell}
:tags: [mac]
brew install miniconda
brew install --cask visual-studio-code
brew install --cask microsoft-teams
```

```{code-cell}
:tags: [mac, windows]
conda init zsh
source ~/.zshrc
yes '' | conda update conda
```

+++ {"tags": ["mac"]}

```{code-cell}
:tags: [mac]
brew install miniconda visual-studio-code
```


+++ {"tags": ["mac", "windows"]}

## Docker Desktop

```{code-cell}
:tags: [mac]
brew install --cask docker
open -a docker
```

```{code-cell}
:tags: [mac, windows]
docker run hello-world
```
+++ {"tags": ["mac", "windows"]} 

If your Docker installation is successful you should see an output something like

> Hello from Docker!
> This message shows that your installation appears to be working correctly.
>
> To generate this message, Docker took the following steps:
>  1. The Docker client contacted the Docker daemon.
>  2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
>  3. The Docker daemon created a new container from that image which runs the
>    executable that produces the output you are currently reading.
>  4. The Docker daemon streamed that output to the Docker client, which sent it
>    to your terminal.
>
> To try something more ambitious, you can run an Ubuntu container with:
>  $ docker run -it ubuntu bash
>
> Share images, automate workflows, and more with a free Docker ID:
>  https://hub.docker.com/
>
> For more examples and ideas, visit:
>  https://docs.docker.com/get-started/

If you see anything else, especially an error  please ask for help.

+++ {"tags": ["mac", "windows"]}

## Visual Studio Code

Visual Studio code is a lightweight text editor with multiple features which make it suitable for inspecting & editing code. VS code offers a range of Microsoft & third-party extensions to support additional functionality. We will install a selection to improve the experience when coding with Python

```{code-cell}
:tags: [mac, windows]

code --install-extension ms-python.python
code --install-extension vscode.cpptools 
code --install-extension ms-vscode-remote.vscode-remote-extensionpack
code --install-extension ms-vsliveshare.vsliveshare-pack
```
