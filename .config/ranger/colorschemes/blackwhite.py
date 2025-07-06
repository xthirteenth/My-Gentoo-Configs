# Black and White colorscheme for ranger
# Minimalistic monochrome theme

from __future__ import absolute_import, division, print_function

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import (
    black,
    white,
    default,
    normal,
    bold,
    reverse,
    default_colors,
)


class BlackWhite(ColorScheme):
    progress_bar_color = 15

    def verify_browser(self, context, fg, bg, attr):
        if context.selected:
            attr = reverse
        else:
            attr = normal
        if context.empty or context.error:
            bg = 8
            fg = 0
        if context.border:
            fg = default
        if context.document:
            attr |= normal
            fg = 15
        if context.media:
            if context.image:
                attr |= normal
                fg = 15
            elif context.video:
                fg = 15
            elif context.audio:
                fg = 15
            else:
                fg = 15
        if context.container:
            attr |= bold
            fg = 15
        if context.directory:
            attr |= bold
            fg = 15
        elif context.executable and not any(
            (context.media, context.container, context.fifo, context.socket)
        ):
            attr |= bold
            fg = 15
        if context.socket:
            fg = 8
            attr |= bold
        if context.fifo or context.device:
            fg = 8
            if context.device:
                attr |= bold
        if context.link:
            fg = 15 if context.good else 8
        if context.tag_marker and not context.selected:
            attr |= bold
            fg = 15
        if not context.selected and (context.cut or context.copied):
            fg = 8
            attr |= bold
        if context.main_column:
            if context.selected:
                attr |= bold
            if context.marked:
                attr |= bold
                fg = 15
        if context.badinfo:
            if attr & reverse:
                bg = 8
            else:
                fg = 8

        if context.inactive_pane:
            fg = 8

        return fg, bg, attr

    def verify_titlebar(self, context, fg, bg, attr):
        attr |= bold
        if context.hostname:
            fg = 8 if context.bad else 15
        elif context.directory:
            fg = 15
        elif context.tab:
            if context.good:
                bg = 15
                fg = 0
        elif context.link:
            fg = 15

        return fg, bg, attr

    def verify_statusbar(self, context, fg, bg, attr):
        if context.permissions:
            if context.good:
                fg = 15
            elif context.bad:
                bg = 8
                fg = 0
        if context.marked:
            attr |= bold | reverse
            fg = 15
        if context.frozen:
            attr |= bold | reverse
            fg = 8
        if context.message:
            if context.bad:
                attr |= bold
                fg = 8
        if context.loaded:
            bg = self.progress_bar_color
        if context.vcsinfo:
            fg = 15
            attr &= ~bold
        if context.vcscommit:
            fg = 15
            attr &= ~bold
        if context.vcsdate:
            fg = 8
            attr &= ~bold

        return fg, bg, attr

    def verify_taskview(self, context, fg, bg, attr):
        if context.title:
            fg = 15

        if context.selected:
            attr |= reverse

        if context.loaded:
            if context.selected:
                fg = self.progress_bar_color
            else:
                bg = self.progress_bar_color

        return fg, bg, attr

    def verify_vcsfile(self, context, fg, bg, attr):
        attr &= ~bold
        if context.vcsconflict:
            fg = 8
        elif context.vcschanged:
            fg = 8
        elif context.vcsunknown:
            fg = 8
        elif context.vcsstaged:
            fg = 15
        elif context.vcssync:
            fg = 15
        elif context.vcsignored:
            fg = default

        return fg, bg, attr

    def verify_vcsremote(self, context, fg, bg, attr):
        attr &= ~bold
        if context.vcssync or context.vcsnone:
            fg = 15
        elif context.vcsbehind:
            fg = 8
        elif context.vcsahead:
            fg = 15
        elif context.vcsdiverged:
            fg = 8
        elif context.vcsunknown:
            fg = 8

        return fg, bg, attr

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            fg, bg, attr = self.verify_browser(context, fg, bg, attr)

        elif context.in_titlebar:
            fg, bg, attr = self.verify_titlebar(context, fg, bg, attr)

        elif context.in_statusbar:
            fg, bg, attr = self.verify_statusbar(context, fg, bg, attr)

        elif context.in_taskview:
            fg, bg, attr = self.verify_taskview(context, fg, bg, attr)

        if context.vcsfile:
            fg, bg, attr = self.verify_vcsfile(context, fg, bg, attr)

        elif context.vcsremote:
            fg, bg, attr = self.verify_vcsremote(context, fg, bg, attr)

        return fg, bg, attr 