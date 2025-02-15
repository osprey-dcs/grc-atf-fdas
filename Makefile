DIA=dia

all:
.PHONY: all

image/D-3-2_System_Block_Diagram.png: image/D-3-2_System_Block_Diagram.dia
all: image/D-3-2_System_Block_Diagram.png

%.png: %.dia Makefile
	$(DIA) --export=$@ $<
