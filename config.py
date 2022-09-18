#                   _      __         
#  ____ _____ ___  (_)    / /_  ____ _
# / __ `/ __ `__ \/ /    / __ \/ __ `/
#/ /_/ / / / / / / /    / /_/ / /_/ / 
#\__,_/_/ /_/ /_/_/____/_.___/\__,_/  
#                /_____/              

#### Custom Qtile Config by ami_ba ####

import os
#os.system("xrandr -s 1920x1080")
#os.system("xrandr --output HDMI-1 --scale 0.89x0.89")
#if(os.system("xrandr | grep 'HDMI-A-0 connected'")):
os.system("xrandr --output HDMI-A-0 --mode 1920x1080 --left-of eDP")
os.system("xinput --map-to-output 'Wacom HID 5218 Finger' eDP")
#os.system("picom -b")
os.system("picom -b --config ~/.config/picom.conf")
os.system("nm-applet &")
os.system("blueman-applet &")
os.system("/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &")
from typing import List  # noqa: F401
from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
#terminal = guess_terminal()

keys = [
    
    Key([mod], "a", lazy.spawn("alacritty"), desc="Open Alacritty"),
    #File Manager
    Key([mod], "f", lazy.spawn("thunar"), desc="Open Nautilus File Manager"),

    #brave
    Key([mod], "b", lazy.spawn("brave"), desc="Open Brave Browser"),

    #dmenu 
    Key([mod], "d", lazy.spawn("dmenu_run  -l 6 -nb '#191919' -nf '#2aa198' -sb '#2aa198' -sf '#191919' -fn 'Hurmit Nerd Font-10'"), desc="Open dmenu"),

    #custom keys
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle floating"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key(["control"], "Tab", lazy.next_screen(), desc="move to next screen")

]

#groups = [Group(i) for i in "123456789"]

#groups = [Group("sfds")]

#for i in groups:
#    keys.extend([
#        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
#            desc="Switch to group {}".format(i.name)),
#
#        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#            desc="Switch to & move focused window to group {}".format(i.name)),
#        # Or, use below if you prefer not to switch to that group.
#        # # mod1 + shift + letter of group = move focused window to group
#        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#        #     desc="move focused window to group {}".format(i.name)),
#    ])



group_names = [("一", {'layout': 'monadtall'}),
               ("二", {'layout': 'monadtall'}),
               ("三", {'layout': 'monadtall'}),
               ("四", {'layout': 'monadtall'}),
               ("五", {'layout': 'monadtall'}),
               ("六", {'layout': 'monadtall'}),
               ("七", {'layout': 'monadtall'}),
               ("八", {'layout': 'monadtall'}),
               ("九", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group



layouts = [
    layout.Columns(border_width=3, border_on_single="True", border_normal ="#928374", border_focus="#458588", border_focus_stack='#928374', border_normal_stack="#928374", margin=6),
    layout.Max(border_focus ="#928374"),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    #layout.MonadTall(border_width=3, border_on_single="True", border_normal ="#928374", border_focus="#458588", border_focus_stack='#928374', border_normal_stack="#928374", margin=6),
    #layout.MonadWide(),
    #layout.RatioTile(),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
    #layout.Slice(),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

#Custom mouse callbacks
def dmenu_start():
    qtile.cmd_spawn("instantmenu_run -c -i  -l 5 -g 5  -nb '#191919' -nf '#2aa198' -sb '#2aa198' -sf '#191919' -fn 'Hurmit Nerd Font-10'")

def htop_start():
    qtile.cmd_spawn("alacritty -e htop");

def clock_start():
    qtile.cmd_spawn("alacritty -e tty-clock");

def systemd_suspend():
    os.system("systemctl suspend")

def shutdown_trigger():
    os.system("shutdown now")

def slock_run():
    os.system("slock")

def reboot_trigger():
    os.system("reboot")

screens = [
    Screen(
        wallpaper='~/.config/qtile/wallpapers/Astro.jpg',
        wallpaper_mode='fill',
        bottom=bar.Bar([widget.Notify(font="Hurmit Nerd Font Bold", background="#282828", fontsize=14),], opacity=1.0, size=16, background="282828"),
        top=bar.Bar(
            [
                widget.Spacer(length=3, background="#282828"),
                widget.Image(
                    filename = "~/.config/qtile/icons/python.png",
                    scale = "False",
                    background="#282828",
                    mouse_callbacks={'Button1': dmenu_start}
                ),
                widget.Spacer(length=2, background="#282828"),
                widget.CurrentLayout(
                    font="Hurmit Nerd Font Bold",
                    fontsize=16,
                    #active="#d3869b",
                    foreground = "#d3869b",
                    background = "#282828",
                    padding = 5
                ),
                widget.GroupBox(
                    font="URW Gothic:style=Demi Oblique Bold",
                    fontsize=19,
                    hide_unused="True",
                    active="#fe8019",
                    foreground="#b8bb26",
                    background="#282828",
                ),
                widget.Spacer(length =6, background="#282828"),
                #widget.Prompt(),
                widget.WindowName(
                    font="Hurmit Nerd Font Bold",
                    fontsize=15,
                    foreground="#d5c4a1",
                    background="#282828"
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                #widget.Spacer(length=12, background="#282828"),
                #widget.Systray(background="#282828"),
                widget.Spacer(length=12, background="#282828"),
                widget.NetGraph(
                    interface="auto",
                    background="282828",
                    graph_color="fabd2f",
                    border_color="#282828",
                    fill_color="#282828",
                ),
                widget.Net(
                    #interface="enp6s0",
                    background="#282828",
                    font="Ubuntu Bold",
                    fontsize=15,
                    foreground="#fabd2f"
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.CPUGraph(
                    background="#282828",
                    graph_color="#d3869b",
                    fill_color="282828",
                    border_color="282828",
                    mouse_callbacks={'Button1': htop_start},
                ),
                widget.CPU(
                    padding=5,
                    foreground="#d3869b",
                    background="#282828",
                    font="Ubuntu Bold",
                    fontsize=15,
                    mouse_callbacks={'Button1': htop_start}
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.Memory(
                    background="282828",
                    font="Ubuntu Bold",
                    fontsize=15,
                    foreground="#b8bb26",
                    mouse_callbacks={'Button1': htop_start},
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.Clock(
                    mouse_callbacks={'Button1': clock_start},
                    font="Ubuntu Bold",
                    fontsize=15,
                    foreground =  "#2aa198",
                    #foreground="#458588",
                    background =  "#282828",

                    format='%Y-%m-%d %a %I:%M %p'
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.Battery(
                    background="#282828",
                    foreground='#fb4934',
                    font="Ubuntu Bold",
                    fontsize=15
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.Systray(background="#282828"),
                widget.Spacer(length=12, background="#282828"),
                widget.Image(
                    filename='~/.config/qtile/icons/lock.png',
                    scale="True",
                    background="#282828",
                    mouse_callbacks={'Button1': slock_run},
                ),
                widget.Spacer(length=2, background="#282828"),
                widget.Image(
                    filename='~/.config/qtile/icons/suspend2.png',
                    scale="False",
                    background="#282828",
                    mouse_callbacks={'Button1': systemd_suspend},
                ),
                widget.Spacer(length=2, background="#282828"),
                widget.Image(filename='~/.config/qtile/icons/reboot.png',
                    scale="False",
                    background="#282828",
                    mouse_callbacks={'Button1': reboot_trigger}
                ),
                widget.Spacer(length=2, background="#282828"),
                widget.Image(
                    filename='~/.config/qtile/icons/shutdown2.png',
                    scale="False",
                    background="282828",
                    mouse_callbacks={'Button1': shutdown_trigger},
                ),
                #widget.Notify(),

                #widget.QuickExit(),
            ],
            31,
        ),
    ),
    Screen(
        wallpaper='~/.config/qtile/wallpapers/Astro.jpg',
        wallpaper_mode='fill',
        bottom=bar.Bar([widget.Notify(font="Hurmit Nerd Font Bold", background="#282828", fontsize=14),], opacity=1.0, size=16, background="282828"),
        top=bar.Bar(
            [
                widget.Spacer(length=3, background="#282828"),
                widget.Image(
                    filename = "~/.config/qtile/icons/python.png",
                    scale = "False",
                    background="#282828",
                    mouse_callbacks={'Button1': dmenu_start}
                ),
                widget.Spacer(length=2, background="#282828"),
                widget.CurrentLayout(
                    font="Hurmit Nerd Font Bold",
                    fontsize=16,
                    #active="#d3869b",
                    foreground = "#d3869b",
                    background = "#282828",
                    padding = 5
                ),
                widget.GroupBox(
                    font="URW Gothic:style=Demi Oblique Bold",
                    fontsize=19,
                    hide_unused="True",
                    active="#fe8019",
                    foreground="#b8bb26",
                    background="#282828",
                ),
                widget.Spacer(length =6, background="#282828"),
                #widget.Prompt(),
                widget.WindowName(
                    font="Hurmit Nerd Font Bold",
                    fontsize=15,
                    foreground="#d5c4a1",
                    background="#282828"
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                #widget.Spacer(length=12, background="#282828"),
                #widget.Systray(background="#282828"),
                widget.Spacer(length=12, background="#282828"),
                widget.NetGraph(
                    interface="auto",
                    background="282828",
                    graph_color="fabd2f",
                    border_color="#282828",
                    fill_color="#282828",
                ),
                widget.Net(
                    #interface="enp6s0",
                    background="#282828",
                    font="Ubuntu Bold",
                    fontsize=15,
                    foreground="#fabd2f"
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.CPUGraph(
                    background="#282828",
                    graph_color="#d3869b",
                    fill_color="282828",
                    border_color="282828",
                    mouse_callbacks={'Button1': htop_start},
                ),
                widget.CPU(
                    padding=5,
                    foreground="#d3869b",
                    background="#282828",
                    font="Ubuntu Bold",
                    fontsize=15,
                    mouse_callbacks={'Button1': htop_start}
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.Memory(
                    background="282828",
                    font="Ubuntu Bold",
                    fontsize=14,
                    foreground="#b8bb26",
                    mouse_callbacks={'Button1': htop_start},
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.Clock(
                    mouse_callbacks={'Button1': clock_start},
                    font="Ubuntu Bold",
                    fontsize=15,
                    foreground =  "#2aa198",
                    #foreground="#458588",
                    background =  "#282828",

                    format='%Y-%m-%d %a %I:%M %p'
                ),
                widget.Spacer(length=10, background="#282828"),
                widget.Battery(
                    background="#282828",
                    foreground='#fb4934',
                    font="Ubuntu Bold",
                    fontsize=15
                ),
                widget.Spacer(length=10, background="#282828"),
                #widget.Systray(background="#282828"),
                widget.Spacer(length=12, background="#282828"),
                widget.Image(
                    filename='~/.config/qtile/icons/lock.png',
                    scale="True",
                    background="#282828",
                    mouse_callbacks={'Button1': slock_run},
                ),
                widget.Spacer(length=2, background="#282828"),
                widget.Image(
                    filename='~/.config/qtile/icons/suspend2.png',
                    scale="False",
                    background="#282828",
                    mouse_callbacks={'Button1': systemd_suspend},
                ),
                widget.Spacer(length=2, background="#282828"),
                widget.Image(filename='~/.config/qtile/icons/reboot.png',
                    scale="False",
                    background="#282828",
                    mouse_callbacks={'Button1': reboot_trigger}
                ),
                widget.Spacer(length=2, background="#282828"),
                widget.Image(
                    filename='~/.config/qtile/icons/shutdown2.png',
                    scale="False",
                    background="282828",
                    mouse_callbacks={'Button1': shutdown_trigger},
                ),
                #widget.Notify(),

                #widget.QuickExit(),
            ],
            30,
        ),
    ),

]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


wmname = "Qtile"

