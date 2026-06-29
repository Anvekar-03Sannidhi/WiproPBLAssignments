import colors_module

colors = input("Enter hyphen-separated colors: ")

sorted_colors = colors_module.sort_colors(colors)

print("Sorted colors:", sorted_colors)