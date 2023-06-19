SHELL=/bin/bash

all: out.pdf

%.pdf: %.svg
	svgtopdf $<

out.svg: out.dat plot.py
	python3 plot.py

out.dat: calc.jl
	julia calc.jl

.PHONY: clean

clean: 
	\rm -f *.eps *.pdf out.dat *svg


