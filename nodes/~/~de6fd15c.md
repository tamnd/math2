---
tag: ~de6fd15c
kind: definition
name: Partition of an interval
msc: [26A42]
defines: ~b38cc789
sources:
  - url: https://en.wikipedia.org/wiki/Partition_of_an_interval
    locator: lead section
---

## Definition

Let $a < b$ be real numbers.
A partition of $[a, b]$ is a finite sequence of real numbers $P = (x_0, x_1, \dots, x_n)$ with
$$a = x_0 < x_1 < \cdots < x_n = b.$$
The intervals $[x_{i-1}, x_i]$ for $i = 1, \dots, n$ are the subintervals of $P$.

## Remarks

Partitions are the basis of [[Darboux sums|~fb054658]] and [[Riemann sums|~3a724e5e]].
A [[refinement|~af3ee3d9]] of $P$ adds more points. The [[mesh|~c4b15e64]] of $P$ is the length of its longest subinterval.
A tagged partition also chooses a point $t_i$ in each subinterval $[x_{i-1}, x_i]$.

## Explanations

### L1 human

A partition cuts the interval $[a, b]$ into finitely many pieces.
The cut points are listed from left to right.
