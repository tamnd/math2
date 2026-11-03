---
tag: 6XV9EBX43B
kind: statement
role: theorem
name: Lenstra's algorithm for integer programming in fixed dimension
msc: [90C10, 68Q25, 11H06]
uses: [9GX3WH5EQF, WN9V7WSJKF, T00W8RQT8E]
about: [9GX3WH5EQF]
sources:
  - url: https://en.wikipedia.org/wiki/Integer_programming
---

## Statement

Let $n \ge 1$ be a fixed integer.
There is an algorithm with the following input and output.
The input is a rational $m \times n$ matrix $A$ and a vector $b \in \Q^m$.
The algorithm decides whether there is an $x \in \Z^n$ with $A x \le b$, and finds such an $x$ if there is one.
Its running time is bounded by a polynomial in the encoding length of $(A, b)$, where the polynomial depends on $n$.

## Remarks

Idea of the proof.
The polyhedron $P = \set{x : A x \le b}$ is first rounded, by an affine map, so that it lies between two balls whose radii differ by a factor depending only on $n$.
Lattice basis reduction then either finds an integer point in $P$ or finds a nonzero integer direction $d$ in which $P$ is thin.
Thin means that the number of integers in the range of $d^T x$ on $P$ is bounded in terms of $n$.
In the second case $P \cap \Z^n$ lies on a bounded number of hyperplanes $d^T x = k$, and each of them gives an integer feasibility problem in dimension $n - 1$, which is solved recursively.

The optimization version, maximizing $c^T x$ over $P \cap \Z^n$ with rational $c$, also runs in polynomial time for fixed $n$, by binary search on the objective value.

Without fixing $n$ the statement is believed false: the integer feasibility problem is [[NP-complete|JH780796ZP]], so a polynomial-time algorithm for all $n$ would give P $=$ NP.

Example: for $n = 1$ the problem is trivial: the constraints give an interval $[\ell, u]$, which contains an integer exactly when $\ceil{\ell} \le u$.

## Explanations

### L1 human

Integer programming is hard in general because the number of variables can grow.
Lenstra's theorem says that if the number of variables is kept fixed, the problem becomes easy.
It can then be solved in time that grows only polynomially with the size of the numbers and the number of constraints.
The idea is that a convex region with no grid point inside must be flat in some grid direction.
So it can be cut into a few slices of lower dimension.

### L2 human

Hendrik Lenstra proved the theorem in 1983, using the lattice basis reduction algorithm of Lenstra, Lenstra and Lovász.
The key geometric fact is the flatness theorem of Khinchine: a convex body with no point of the [[lattice|WN9V7WSJKF]] $\Z^n$ has lattice width bounded by a function of $n$ alone.
Later work by Kannan and others improved the dependence on $n$ of the [[running time|T00W8RQT8E]].
The result is used, for example, to show that some problems in parametrized complexity are fixed-parameter tractable when the parameter is the number of variables.
