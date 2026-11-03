---
tag: YXGCA9NJMP
kind: definition
name: Sorting network
msc: [68P10, 68Q06]
defines: G854V12EC7
uses: [0FRXBVVR03, MGKDQAM7K3]
sources:
  - url: https://en.wikipedia.org/wiki/Sorting_network
---

## Definition

Let $n \ge 1$ and let $(X, \le)$ be a [[totally ordered set|0FRXBVVR03]].
A *comparator* $[i, j]$ with $1 \le i < j \le n$ is a map $X^n \to X^n$.
It replaces the entries $x_i, x_j$ by $\min(x_i, x_j)$ and $\max(x_i, x_j)$ respectively and leaves the other entries unchanged.
A *comparator network* on $n$ wires is a finite sequence of comparators $c_1, \dots, c_s$; it acts on $X^n$ by the composition $c_s \circ \dots \circ c_1$.
It is a *sorting network* if for every $x \in X^n$ the output $y$ satisfies $y_1 \le y_2 \le \dots \le y_n$.
The *size* of the network is $s$.
Its *depth* is the largest $r$ with indices $a_1 < \dots < a_r$ such that $c_{a_l}$ and $c_{a_{l+1}}$ share a wire for each $l < r$.
The depth is the number of rounds needed when comparators on disjoint wires work at the same time.

## Remarks

Example: $[1,2], [2,3], [1,2]$ on $3$ wires is a sorting network.
After $[1,2]$ and $[2,3]$, the largest entry is on wire $3$, and the last $[1,2]$ orders the other two.
Non-example: $[1,2], [2,3]$ alone is not a sorting network, since it sends $(3, 2, 1)$ to $(2, 3, 1)$ and then to $(2, 1, 3)$.
Whether a sorting property holds does not depend on the ordered set $X$, by the [[zero–one principle|FMR0TZ9Z88]].
Known constructions include Batcher's odd–even mergesort and the bitonic sorter, of depth $O(\log^2 n)$; the AKS network has depth $O(\log n)$.
