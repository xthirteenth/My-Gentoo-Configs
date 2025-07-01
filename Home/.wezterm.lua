local wezterm = require("wezterm")

local config = wezterm.config_builder()

config.font = wezterm.font("MesloLGS Nerd Font Mono")
config.font_size = 16

config.enable_tab_bar = true

config.window_background_opacity = 0.90
config.text_background_opacity = 0.90
config.window_background_gradient = {
	orientation = "Vertical",
	colors = {
		"#1a1b26",
		"#2a1a40",
	},
	interpolation = "Linear",
	blend = "Rgb",
}

config.colors = {
	foreground = "#dcd7ff", -- светло-фиолетовый
	background = "#0d0b1a", -- почти чёрный с фиолетовым оттенком
	cursor_bg = "#bb9af7",
	cursor_border = "#bb9af7",
	cursor_fg = "#0d0b1a",
	selection_bg = "#3e2d5c",
	selection_fg = "#ffffff",
	ansi = {
		"#1a1a1a", -- black
		"#ff5c8f", -- red
		"#8aff80", -- green
		"#f5c2e7", -- yellow (розово-фиолетовый)
		"#9580ff", -- blue
		"#cba6f7", -- magenta (фиолетовый)
		"#94e2d5", -- cyan
		"#dcd7ff", -- white
	},
	brights = {
		"#2c2c2c",
		"#ff75a0",
		"#a6ff99",
		"#fad6f7",
		"#a9a1ff",
		"#e0b3ff",
		"#b5f0e5",
		"#ffffff",
	},
}

config.default_prog = { "tmux" }

return config
