#### Linux / Ubuntu

###### **Bash shell**

All Ubuntu and other Linux distros come with Bash as the default shell, so no need to download it! Some versions of Linux may require that you type bash inside the terminal to access it. To verify if this is the case, follow these steps:

Open a terminal and type `echo $SHELL`. If it reads `/bin/bash` then you are all set! If it does not, then for all parts of the subsequent instructions, whenever the instructions read “open a terminal,” please assume you are to open a terminal, type bash, and the proceed with the instructions as specified.

###### **Git**

You most likely already have Git installed. To check if you do:

*   On Debian - type `sudo apt-get install git` inside the terminal
*   On Fedora - type `sudo yum install git` inside the terminal.

###### **VSCode**

Go to the [visual studio code website](https://code.visualstudio.com/) and click the download button for either the .deb (Ubuntu, Debian) or the .rpm (Fedora, CentOS) file.

Double-click the downloaded file to install VSCode. (You may be prompted to type your administrator password during the install).

###### **VSCode extensions**

1.  Open the Ubuntu application.
2.  Type `code .` into the terminal and press `Enter`. You should see a message reading “Installing VS Code Server” and then a new windows will open up.
3.  Press `Ctrl+Shift+P` in the new window that opens and type “Extensions: Install extensions” into the search bar that appears at the top of the screen. Select the appropriate entry from the dropdown menu that appears (there should be four entries; simply select the one that reads “Extensions: Install extensions”).
4.  A new panel should appear on the left-hand side of the screen with a search bar. Search for each of the following extensions and press `Install` for the first entry that appears. (The author listed for all of these extensions should be “Microsoft”.)
    *   Python (n.b., you will need to reload VSCode after installing this)
    *   Live Share (n.b., you may need to press “Ctrl/Cmd+Shift+P” and type “install extensions” again after installing this)
    *   Live Share Extension Pack
    *   Docker
    *   Remote - WSL

###### **Python**

1.  Open a new terminal and type the following lines (separately) into the terminal, pressing `Enter` after each one:
    
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
        bash Miniconda3-latest-Linux-x86_64.sh
        
    
2.  A license agreement will be displayed and the bottom of the terminal will read `--More--`. Press `Enter` or the space bar until you are prompted with “Do you accept the license terms? \[yes|no\].” Type `yes` and then press `Enter`
3.  The installation script will inform you that it is going to install into a default directory (e.g., `/home/$USER/miniconda3`). Leave this default and press `Enter`.
4.  When you are asked “Do you wish the installer to initialize Miniconda3 by running conda init? \[yes|no\],” type `yes` and press `Enter`. Exit the terminal once the installation has finished.
5.  Re-open a new terminal. Type `which python` into the terminal and it should return a path (e.g., `/home/$USER/miniconda3/bin/python`).
    *   If you do not see a path like this then please try typing `conda init`, closing your terminal, and repeating this step. If your issue is still not resolved skip the following step and contact an instructor on the #help-installation channel of the BHS Slack.
6.  Type the following to remove the installation script that was downloaded:
    
        rm ./Miniconda3-latest-Linux-x86_64.sh
        
    

###### **Python packages**

Open a terminal and type the following commands:

    conda config --append channels conda-forge
    conda config --set channel_priority strict
    conda install -y flake8 ipython jupyter jupyterlab matplotlib nibabel nilearn numpy pandas scipy seaborn
    

#### MacOS

###### **Bash shell**

You already have it! Depending on which version of Mac OS you’re running you may need to type `bash` inside the terminal to access it. To check whether this is necessary, follow these steps:

1.  Open a terminal and type `echo $SHELL`. If it reads `/bin/bash` then you are all set!

Note: If you are using Mac Catalina (10.15.X) then it is possible your default shell is NOT CORRECT. To set the default to bash, type `chsh -s /bin/bash` in the terminal, enter your password when prompted, and then close + re-open the terminal.

###### **Git**

You may already have it! Try opening a terminal and typing `git --version`. If you do not see something like “git version X.XX.X” printed out, then follow these steps:

1.  Follow [this link](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect) to automatically download an installer.
2.  Double click the downloaded file (`git-2.23.0-intel-universal-mavericks.dmg`) and then double click the `git-2.23.0-intel-universal-mavericks.pkg` icon inside the dmg that is opened.
3.  Follow the on-screen instructions to install the package.

###### **VSCode**

1.  Go to the [visual studio code website](https://code.visualstudio.com/) and click the download button.
2.  Unzip the downloaded file (e.g., `VSCode-darwin-stable.zip`) and moving the resulting `Visual Studio Code` file to your Applications directory.

###### **VSCode extensions**

1.  Open the Visual Studio Code application
2.  Type `Cmd+Shift+P` and then enter “Shell command: Install ‘code’ command in PATH” into the search bar that appears at the top of the screen. Select the highlighted entry. A notification box should appear in the bottom-right corner indicating that the command was installed successfully.
3.  Type `Cmd+Shift+P` again and then enter “Extensions: Install extensions” into the search bar. Select the appropriate entry from the dropdown menu that appears (there should be four entries; simply select the one that reads “Extensions: Install extensions”).
4.  A new panel should appear on the left-hand side of the screen with a search bar. Search for each of the following extensions and press `Install` for the first entry that appears. (The author listed for all of these extensions should be “Microsoft”.)
    *   Python (n.b., you will need to reload VSCode after installing this)
    *   Live Share (n.b., you may need to press “Ctrl/Cmd+Shift+P” and type “install extensions” again after installing this)
    *   Live Share Extension Pack
    *   Docker

###### **Python**

1.  Open a new terminal and type the following lines (separately) into the terminal, pressing `Enter` after each one:
    
        curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
        bash Miniconda3-latest-MacOSX-x86_64.sh
        
    
2.  A license agreement will be displayed and the bottom of the terminal will read `--More--`. Press `Enter` or the space bar until you are prompted with “Do you accept the license terms? \[yes|no\].” Type `yes` and then press `Enter`
3.  The installation script will inform you that it is going to install into a default directory (e.g., `/home/$USER/miniconda3`). Leave this default and press `Enter`.
4.  When you are asked “Do you wish the installer to initialize Miniconda3 by running conda init? \[yes|no\],” type `yes` and press `Enter`. Exit the terminal once the installation has finished.
5.  Re-open a terminal. Type `which python` into the terminal and it should return a path (e.g., `/home/$USER/miniconda3/bin/python`).
    *   If you do not see a path like this then please try typing `conda init`, closing your terminal, and repeating this step. If your issue is still not resolved skip the following step and contact an instructor on the #help-installation channel of the BHS Slack.
6.  Type the following to remove the installation script that was downloaded:
    
        rm ./Miniconda3-latest-MacOSX-x86_64.sh
        
    

###### **Python packages**

Open a terminal and type the following commands:

    conda config --append channels conda-forge
    conda config --set channel_priority strict
    conda install -y flake8 ipython jupyter jupyterlab matplotlib nibabel nilearn numpy pandas scipy seaborn
    

#### Windows

###### **Windows Subsystem for Linux (WSL)**

1.  Search for `Windows Powershell` in your applications; right click and select `Run as administrator`. Select `Yes` on the prompt that appears asking if you want to allow the app to make changes to your device.
2.  Type the following into the Powershell and then press `Enter`:
    
        Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
        
    
3.  Press `Enter` again when prompted to reboot your computer.
4.  Once your computer has rebooted, open the Microsoft Store and search for “Ubuntu.” Install the program labelled “Ubuntu 18.04” (NOT “Ubuntu 20.04” (bug in gpg that makes git clone from https fail) NOT “Ubuntu 16.04” NOT “Ubuntu”) by clicking the tile, pressing `Get`, and then `Install`.
5.  Search for and open Ubuntu from your applications. There will be a slight delay (of a few minutes) while it finishes installing.
6.  You will be prompted to `Enter new UNIX username`. You can use any combination of alphanumeric characters here for your username, but a good choice is `<first_initial><last_name>` (e.g., `jsmith` for John Smith). You will then be prompted to enter a new password. (Choose something easy to remember as you will find yourself using it frequently.)
7.  Right click on the top bar of the Ubuntu application and select “Properties”. Under the “Options” tab, under the “Edit Options” heading, make sure the box reading “Use Ctrl+Shift+C/V as Copy/Paste” is checked. Under the “Terminal” tab, under the “Cursor Shape” heading, make sure the box reading “Vertical Bar” is checked. Press “Okay” to save these settings and then exit the application.

(The above step-by-step WSL instructions are distilled from [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and [here](https://docs.microsoft.com/en-us/windows/wsl/initialize-distro). If you have questions during the installation procedure those resources may have answers!)

From this point on whenever the instructions specify to “open a terminal” please assume you are supposed to open the Ubuntu application.

###### **Bash shell**

You already have it, now that you’ve installed the WSL!

###### **Git**

You already have it, now that you’ve installed the WSL!

###### **VSCode**

1.  Go to the [visual studio code website](https://code.visualstudio.com/) and click the download button, then run the `.exe` file.
2.  Leave all the defaults during the installation with the following exception:
    *   Please make sure the box labelled “Register Code as an editor for supported file types” is selected

###### **VSCode extensions**

1.  Open the Ubuntu application.
2.  Type `code .` into the terminal and press `Enter`. You should see a message reading “Installing VS Code Server” and then a new windows will open up.
3.  Press `Ctrl+Shift+P` in the new window that opens and type “Extensions: Install extensions” into the search bar that appears at the top of the screen. Select the appropriate entry from the dropdown menu that appears (there should be four entries; simply select the one that reads “Extensions: Install extensions”).
4.  A new panel should appear on the left-hand side of the screen with a search bar. Search for each of the following extensions and press `Install` for the first entry that appears. (The author listed for all of these extensions should be “Microsoft”.)
    *   Python (n.b., you will need to reload VSCode after installing this)
    *   Live Share (n.b., you may need to press “Ctrl/Cmd+Shift+P” and type “install extensions” again after installing this)
    *   Live Share Extension Pack
    *   Docker
    *   Remote - WSL

###### **Python**

1.  Open a new terminal and type the following lines (separately) into the terminal, pressing `Enter` after each one:
    
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
        bash Miniconda3-latest-Linux-x86_64.sh
        
    
2.  A license agreement will be displayed and the bottom of the terminal will read `--More--`. Press `Enter` or the space bar until you are prompted with “Do you accept the license terms? \[yes|no\].” Type `yes` and then press `Enter`
3.  The installation script will inform you that it is going to install into a default directory (e.g., `/home/$USER/miniconda3`). Leave this default and press `Enter`.
4.  When you are asked “Do you wish the installer to initialize Miniconda3 by running conda init? \[yes|no\],” type `yes` and press `Enter`. Exit the terminal once the installation has finished.
5.  Re-open the Ubuntu application. Type `which python` into the terminal and it should return a path (e.g., `/home/$USER/miniconda3/bin/python`).
    *   If you do not see a path like this then please try typing `conda init`, closing your terminal, and repeating this step. If your issue is still not resolved skip the following step and contact an instructor on the #help-installation channel on the BHS Slack.
6.  Type the following to remove the installation script that was downloaded:
    
        rm ./Miniconda3-latest-Linux-x86_64.sh
        
    

###### **Python packages**

Open a terminal and type the following commands:

    conda config --append channels conda-forge
    conda config --set channel_priority strict
    conda install -y flake8 ipython jupyter jupyterlab matplotlib nibabel nilearn numpy pandas scipy seaborn
    
