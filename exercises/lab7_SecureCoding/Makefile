SRCS = $(wildcard *.c)

PROGS = $(patsubst %.c,%,$(SRCS))

CFLAGS = -fno-stack-protector -m32 -O0 -no-pie

all: $(PROGS)

%: %.c

	$(CC) $(CFLAGS)  -o $@ $<
