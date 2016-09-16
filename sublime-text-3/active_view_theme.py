import sublime
import sublime_plugin


class ActiveViewThemeListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        view_settings = view.settings()
        plugin_settings = sublime.load_settings(
            "ActiveViewTheme.sublime-settings")
        preference_settings = sublime.load_settings(
            "Preferences.sublime-settings")
        active_theme = plugin_settings.get("active_theme")

        # and preference_settings.get("color_scheme") ==
        # view_settings.get("color_scheme")
        if active_theme != "":
            view_settings.set("color_scheme", active_theme)

        else:
            print ("No active theme specified")

    def on_deactivated(self, view):
        preference_settings = sublime.load_settings(
            "Preferences.sublime-settings")
        plugin_settings = sublime.load_settings(
            "ActiveViewTheme.sublime-settings")
        view_settings = view.settings()
        if plugin_settings.get("active_theme") == view_settings.get("color_scheme"):
            view_settings.set(
                "color_scheme", preference_settings.get("color_scheme"))
