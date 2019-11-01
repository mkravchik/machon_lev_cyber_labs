SRCS = $(wildcard *.c)

PROGS = $(patsubst %.c,%,$(SRCS))

CFLAGS = -fno-stack-protector -m32 -O0

all: $(PROGS)

%: %.c

	$(CC) $(CFLAGS)  -o $@ $<
