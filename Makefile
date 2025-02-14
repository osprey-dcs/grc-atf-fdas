DIA=dia

all:
.PHONY: all

image/system.png: image/D.3.2%20System%20Block%20Diagram.dia
all: image/D.3.2%20System%20Block%20Diagram.png

%.png: %.dia Makefile
	$(DIA) --export=$@ $<
