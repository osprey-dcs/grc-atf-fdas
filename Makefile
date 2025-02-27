DIA=dia
PYTHON=python3

all:
.PHONY: all

D-4-01_PROC_-_Functional_Checkout.md: D-4-01_PROC_-_Functional_Checkout.py
	$(PYTHON) $< > $@
all: D-4-01_PROC_-_Functional_Checkout.md

image/D-3-2_System_Block_Diagram.png: image/D-3-2_System_Block_Diagram.dia
all: image/D-3-2_System_Block_Diagram.png

%.png: %.dia Makefile
	$(DIA) --export=$@ $<
