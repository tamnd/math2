---
tag: QZCYFGT9DP
kind: example
name: The natural numbers with multiplication are not a residuated lattice
msc: ["06F05"]
topics: [QYA4H5Y7VR]
audience: research
not_instance_of:
  - target: E337A6WVH3
    note: the residual of 0 by 0 does not exist, since 0 times every number is 0
uses: [S9Z6PKTXAS]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_lattice
    locator: Definition
---

## Example

Take $\mathbb{N} = \set{0, 1, 2, \dots}$ with its usual order, $\min$, $\max$, multiplication and unit $1$.

1. Lattice. $\mathbb{N}$ is a chain, so $\min$ and $\max$ are the meet and the join.
2. Monoid. $(\mathbb{N}, \cdot, 1)$ is a commutative [[monoid|0N6R902FG1]].
3. Monotonicity. If $y \le y'$, then $xy \le xy'$, since $x \ge 0$.
4. Residuals for $x \ge 1$. The largest $y$ with $xy \le z$ is $\lfloor z / x \rfloor$, so $x \backslash z$ exists.
5. Residual for $x = 0$. Every $y$ satisfies $0 \cdot y = 0 \le 0$. So the set $\set{y : 0 \cdot y \le 0}$ is all of $\mathbb{N}$, and it has no largest element.

So $0 \backslash 0$ does not exist, and $\mathbb{N}$ is not a [[residuated lattice|E337A6WVH3]].

## Remarks

1. The failure comes from the missing top: a residual must be the largest element of a set, and $\mathbb{N}$ has no largest element.
2. Removing $0$ does not help. In $\set{1, 2, \dots}$ no $y$ satisfies $2y \le 1$, so $2 \backslash 1$ does not exist.
3. Adding a top $\infty$ with $0 \cdot \infty = 0$ and $x \cdot \infty = \infty$ for $x \ge 1$ repairs the failure. Then $0 \backslash z = \infty$, and $\infty \backslash z = 0$ for finite $z$.
4. The integers with multiplication fail at an earlier point: multiplication by $-1$ reverses the order.

## Explanations

### L1 human

For ordinary numbers, $3 \cdot y \le 10$ has the best answer $y = 3$.
For $0 \cdot y \le 0$, every number $y$ works.
There is no largest natural number, so there is no best answer.
A residuated lattice needs a best answer in every case.

### L2 human

1. Compute $3 \backslash 10$: the products $3 \cdot 3 = 9 \le 10$ and $3 \cdot 4 = 12 > 10$ give $3 \backslash 10 = 3$.
2. Try $0 \backslash 0$: the products $0 \cdot y$ are all $0$, so all $y$ qualify.
3. A largest element of $\mathbb{N}$ does not exist, so $0 \backslash 0$ does not exist.

The typical use: the example shows why complete or bounded models are common in this theory.
The trap: monotonicity of multiplication is necessary for residuation, but it is not sufficient.
