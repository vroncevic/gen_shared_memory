#
# Makefile
# Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# latest_pro is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# latest_pro is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

CC = gcc
CFLAGS = -Wall -Wextra -pedantic -lrt

BINARIES = server client

all: $(BINARIES)

server: server.o
	$(CC) $(CFLAGS) -o $@ $^

client: client.o
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c shared_memory.h
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(BINARIES) *.o

.PHONY: all clean
