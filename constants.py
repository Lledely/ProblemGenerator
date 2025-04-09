default_latex_headers = r"""\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{mathabx}
\usepackage[utf8]{inputenc}
\usepackage[T1,T2A]{fontenc}
\usepackage[russian]{babel}
\usepackage{amsfonts}
\usepackage{gensymb}
\usepackage{listings}
\usepackage{titlesec}
\usepackage{color}
\usepackage[dvipsnames]{xcolor}
\usepackage{soul}
\usepackage{xfrac}
\usepackage{hyperref}
\usepackage[margin=0.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{decorations.pathreplacing,calligraphy,patterns}
\usepackage{stackengine} 
\usepackage{enumitem}
\usepackage{blindtext}
"""

default_latex_problems_file_name = "problems.tex"
default_latex_solutions_file_name = "solutions.tex"
default_number_of_variants = 3

constraints_lower_bound = 1
constraints_upper_bound = 10
third_point_max_shift = 5