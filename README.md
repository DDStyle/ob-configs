# ob-configs
Openbox configurations I used in my Arch

![Screenshot](https://i.ibb.co/9ZmH1nP/2020-07-16-01-38.png)

## Packets for installing

+ Xorg  ***Graphical Server***
+ Openbox ***Window Manager***
+ [Polybar](https://aur.archlinux.org/packages/polybar/) (aur) ***Top and bottom panels***
+ Tint2 ***Right panel***
+ Jgmenu ***Start menu***
+ Trayer ***System Tray***
+ Conky ***System Monitor***
+ mpd ***Music Player***
+ Nitrogen ***Desktop wallpapers Manager***
+ Pcmanfm ***GUI File Manager***
+ Kitty ***Terminal Emulator***
+ Zsh ***Shell***
+ Glava ***Desktop Visualizer***
+ Neofetch ***CLI System Monitor***
+ Ranger ***CLI File Manager***
+ Picom ***Composite Manager***
+ Lxappearance ***GTK Manager***
+ Gvim/Vim ***Text Editor***
+ Qt5ct ***QT Manager***

-----------------

If you want install my configs, you may be required edit files `~/.config/openbox/rc.xml, autostart, menu.xml` to setup your applications in menus and for hotkeys.

## Installing

In ob-configs folder:
```bash 
chmod a+x install.sh
./install.sh
```

### (!) If you open install script, you can notice that some files won't be copied automatically. You can copy them manually.
