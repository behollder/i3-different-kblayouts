# i3-different-kblayouts
i3wm python script for different keyboard layouts for each window

## Use it
```
exec --no-startup-id "python ~/.i3/different_keyboard_layout_i3_windows.py"
```

## Require
xkb-switch
i3ipc

## Some
I'm new in python and start learn it with start of create this script. All comments are welcome.

I use it with(change keyboard layout by press capslock):
```
exec_always --no-startup-id setxkbmap "us,ru" ",winkeys" "grp:caps_toggle,grp_led:caps"
```
