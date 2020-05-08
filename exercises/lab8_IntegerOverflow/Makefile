SRCS = $(wildcard *.c)

PROGS = $(patsubst %.c,%,$(SRCS))

CFLAGS = -fno-stack-protector -m32 -O0 -g

all: $(PROGS)

%: %.c

	$(CC) $(CFLAGS)  -o $@ $<
