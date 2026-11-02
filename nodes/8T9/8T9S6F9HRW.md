---
tag: 8T9S6F9HRW
kind: example
name: Fence
msc: [06A07, 05A05]
instance_of: [0QV2JS9RJ3]
illustrates: [W8DZ5KGGHN]
uses: [W8DZ5KGGHN]
sources:
  - url: https://en.wikipedia.org/wiki/Fence_(mathematics)
---

## Example

Let $n \ge 1$.
The fence $Z_n$ is the [[partially ordered set|0QV2JS9RJ3]] on $x_1, \ldots, x_n$ with these covering relations:
$$x_1 < x_2 > x_3 < x_4 > \cdots.$$
That is, $x_i < x_{i+1}$ for odd $i$ and $x_i > x_{i+1}$ for even $i$, with $1 \le i < n$.
It is also called a zigzag poset.
Its Hasse diagram is a path that goes up and down in turn.

A [[linear extension|W8DZ5KGGHN]] of $Z_n$ is a bijection $f \colon \set{x_1, \ldots, x_n} \to \set{1, \ldots, n}$ with $f(x_1) < f(x_2) > f(x_3) < \cdots$.
So the linear extensions of $Z_n$ correspond to the alternating permutations of $\set{1, \ldots, n}$, and their number is the Euler zigzag number $E_n$.
Check for $n = 3$: the poset $x_1 < x_2 > x_3$ has the two linear extensions $x_1, x_3, x_2$ and $x_3, x_1, x_2$, and $E_3 = 2$.

## Remarks

The number of down-sets of $Z_n$ is the Fibonacci number $F_{n+2}$, with $F_1 = F_2 = 1$.
For $n = 3$ the down-sets are $\varnothing$, $\set{x_1}$, $\set{x_3}$, $\set{x_1, x_3}$ and $\set{x_1, x_2, x_3}$, which makes $5 = F_5$.
Every fence has height at most $2$.

## Explanations

### L1 human

A fence is a zigzag: up, down, up, down.
Putting its elements in a row that respects the zigzag is the same as writing the numbers $1$ to $n$ so that they go up, down, up, down.
This links a simple poset with a classical counting problem.
