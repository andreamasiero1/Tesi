import re

with open('example.tex', 'r') as f:
    content = f.read()

# Replace \begin{center} \huge{...} \end{center} with \vfill {\centering \huge{...} \par} \vspace{0.5em}
# This removes the extra vertical space from the center environment and adds a top \vfill
pattern_title = r"\\begin\{center\}\s*\\huge\{\\textbf\{\\textcolor\{rossoPantano\}\{(.*?)\}\}\}\s*\\end\{center\}"
replacement_title = r"\\vfill\n\t\t{\\centering \\huge{\\textbf{\\textcolor{rossoPantano}{\1}}} \\par}\n\t\t\\vspace{0.5em}"
content = re.sub(pattern_title, replacement_title, content)

# Add \vfill right before \end{frame} for those frames that had the title.
# To safely add \vfill to the end of ALL frames (except the first two and the last one which don't have the subtitle):
# Actually, it's easier to just add \vfill before \end{frame} everywhere it is safe, 
# or just do a generic replacement: if a frame has \vfill at the start (from our replacement), it needs \vfill at the end.
# Let's just do a regex that finds \vfill ... \end{frame} and inserts \vfill.

# We can split by \begin{frame} and process each frame
frames = content.split("\\begin{frame}")
new_frames = [frames[0]]
for frame in frames[1:]:
    if "rossoPantano" in frame and "\\vfill" in frame:
        # It's one of our modified frames
        # Replace the last occurrence of \end{frame} with \vfill \n \end{frame}
        # Be careful, frame might not end with \end{frame} if we split by \begin{frame}, it ends with \end{frame} somewhere inside it.
        # Let's split frame by \end{frame}
        parts = frame.split("\\end{frame}")
        parts[0] = parts[0].rstrip() + "\n\t\t\\vfill\n\t"
        frame = "\\end{frame}".join(parts)
    new_frames.append(frame)

new_content = "\\begin{frame}".join(new_frames)

with open('example.tex', 'w') as f:
    f.write(new_content)

print("Done")
