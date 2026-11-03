---
tag: ZJNDYVZV9K
kind: definition
name: Gomory's fractional cut
msc: [90C10]
defines: AZJMC8A93H
uses: [9GX3WH5EQF, PR7VMJN5BH, 957S7V3JW8, 08GR54CKEA]
sources:
  - url: https://en.wikipedia.org/wiki/Cutting-plane_method
---

## Definition

Consider a pure [[integer program|9GX3WH5EQF]] in standard form: maximize $c^T x$ subject to $A x = b$, $x \ge 0$, $x \in \Z^n$, with $A$ and $b$ integral.
Let $B$ be the set of basic indices of a [[basic feasible solution|957S7V3JW8]] of its linear relaxation and $N$ the set of nonbasic indices.
Suppose a row of the simplex tableau reads
$$x_i + \sum_{j \in N} \bar a_{j} x_j = \bar b, \qquad i \in B,$$
with $\bar b \notin \Z$.
For $t \in \R$ write $\set{t} = t - \floor{t}$ for the fractional part, where $\floor{t}$ is the [[floor|08GR54CKEA]] of $t$.
*Gomory's fractional cut* from this row is the inequality
$$\sum_{j \in N} \set{\bar a_j} x_j \ge \set{\bar b}.$$

## Remarks

The cut is valid for every $x \ge 0$ in $\Z^n$ that satisfies the tableau row.
Indeed, subtracting $x_i + \sum_{j} \floor{\bar a_j} x_j$, an integer, from both sides shows that $\sum_j \set{\bar a_j} x_j - \set{\bar b}$ is an integer.
It is greater than $-1$, because $\sum_j \set{\bar a_j} x_j \ge 0$ and $\set{\bar b} < 1$, so it is at least $0$.
The cut is violated by the current basic solution, since all $x_j$ with $j \in N$ are $0$ there and $\set{\bar b} > 0$.

Example: the row $x_1 + \tfrac{1}{2} x_3 - \tfrac{3}{2} x_4 = \tfrac{5}{2}$ gives the cut $\tfrac{1}{2} x_3 + \tfrac{1}{2} x_4 \ge \tfrac{1}{2}$, that is, $x_3 + x_4 \ge 1$, because $\set{-3/2} = 1/2$.

Non-example: the inequality $\sum_{j \in N} \bar a_j x_j \ge \set{\bar b}$, with the full coefficients, is not valid in general.
In the row above, $x_1 = 4$, $x_3 = 0$, $x_4 = 1$ is a nonnegative integer solution.
At this point the inequality reads $-3/2 \ge 1/2$, which is false.

After adding the cut with a new slack variable, the dual simplex method reoptimizes; Gomory showed that with a lexicographic rule this terminates after finitely many cuts.
