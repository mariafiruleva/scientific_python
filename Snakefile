rule all:
  input: "input/input.txt"
  output: "output/output.txt"
  shell: "wc -w {input} > {output}"
