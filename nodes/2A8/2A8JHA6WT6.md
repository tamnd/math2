---
tag: 2A8JHA6WT6
kind: definition
name: Barker code
msc: [94A55, 05B20, 94A12]
defines: 2D88FYZ3DZ
sources:
  - url: https://en.wikipedia.org/wiki/Barker_code
---

## Definition

Let $N \ge 2$ and let $a = (a_1, \dots, a_N)$ be a sequence with every $a_j \in \set{+1, -1}$.
For $0 \le v \le N - 1$, the aperiodic autocorrelation of $a$ at shift $v$ is
$$c_v = \sum_{j=1}^{N - v} a_j \, a_{j+v}.$$
The sequence $a$ is a *Barker code* (or Barker sequence) of length $N$ if $\abs{c_v} \le 1$ for every $v$ with $1 \le v \le N - 1$.

## Remarks

Always $c_0 = N$, so a Barker code has a peak of height $N$ and side values of size at most $1$.

Example: $a = (+1, +1, -1)$ has $c_1 = a_1 a_2 + a_2 a_3 = 1 - 1 = 0$ and $c_2 = a_1 a_3 = -1$, so it is a Barker code of length $3$.

Non-example: $a = (+1, +1, +1)$ has $c_1 = 2$, so it is not a Barker code.

Barker codes exist for the lengths $2, 3, 4, 5, 7, 11$ and $13$.
Turyn and Storer proved that there is none of odd length greater than $13$.
It is conjectured that there is none of any length greater than $13$; for even lengths this is open.
Changing every sign, reversing the order, or negating every second entry turns a Barker code into another one.
