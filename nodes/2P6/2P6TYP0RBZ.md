---
tag: 2P6TYP0RBZ
kind: definition
name: Kendall's notation
msc: [60K25, 90B22]
defines: 9HTFATQNJ2
uses: [P64V0HTE78, 0E99F51GVB, 0XB9GQTN9G]
sources:
  - url: https://en.wikipedia.org/wiki/Kendall%27s_notation
---

## Definition

*Kendall's notation* describes a queueing system with independent interarrival times and independent service times by a code $A/S/c/K/N/D$ where:

1. $A$ is the law of the times between consecutive arrivals, which are independent and identically distributed;
2. $S$ is the law of the service times, which are independent and identically distributed and independent of the arrivals;
3. $c \ge 1$ is the number of identical servers;
4. $K$, with $c \le K \le \infty$, is the capacity, the largest number of customers in the system; arrivals that find $K$ customers are lost;
5. $N \le \infty$ is the size of the population from which customers come;
6. $D$ is the service discipline, such as FIFO (first in, first out), LIFO or processor sharing.

For $A$ and $S$, the symbol $M$ means the [[exponential distribution|0E99F51GVB]], so arrivals of type $M$ form a Poisson process.
The symbol $D$ means a deterministic constant, and $E_k$ means the Erlang law with $k$ phases.
The symbol $G$ means a general law, and $GI$ means general independent interarrival times.
When the last three fields are omitted, they are $K = \infty$, $N = \infty$ and FIFO, and the code is written $A/S/c$.

## Remarks

Example: the [[M/M/1 queue|GTFRPF5J2K]] has Poisson arrivals, exponential service times and one server; all six clauses hold with $K = \infty$, $N = \infty$ and FIFO.
Similarly $M/M/c/c$ is the Erlang loss system with $c$ servers and no waiting room.

Non-example: suppose long service times tend to follow long gaps between arrivals.
Then the service times depend on the arrivals, which fails clause 2, so no code $A/S/c$ describes the system.

Some authors write $G$ for general arrivals as well, and $GI$ only to stress independence.
Some put the discipline in a different position, but the meaning of each letter is the same.
