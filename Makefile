DIA=dia

all:
.PHONY: all

image/system.png: image/system.dia
all: image/system.png

%.png: %.dia Makefile
	$(DIA) --export=$@ $<
