CC = clang
CFLAGS = -Wall
LIBS = -lm

SRCS = $(wildcard *.c)

PROGS = $(patsubst %.c,%,$(SRCS))

all: $(PROGS)

%:%.c
	$(CC) $(CFLAGS) -o bin/$@ $<

clean:
	rm $(PROGS)
