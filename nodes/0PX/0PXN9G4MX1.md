---
tag: 0PXN9G4MX1
kind: statement
role: theorem
name: Double orthogonal complement
msc: [46C05, 15A63]
topics: [8GQVME4SZZ]
audience: ug1
about: [0XJXTBCB2T]
uses: [079D68S3AW, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Finite dimensions
  - book: isbn:9783031410253
    locator: Section 6C
---

## Statement

In finite dimension, taking the orthogonal complement twice gives back the subspace you started with.
Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $U$ be a subspace of $V$.
Let $U^\perp$ be the [[orthogonal complement|079D68S3AW]] of $U$.
Then
$$(U^\perp)^\perp = U.$$
The inclusion $U \subseteq (U^\perp)^\perp$ holds in every inner product space, and the [[proof|FZEF1XYTVB]] gets equality from a count of [[dimensions|05G2G0P224]].

## Remarks

### A check with numbers

Take $U = \R(1, 1, 0)$ in $\R^3$.
Its complement is the plane $x_1 + x_2 = 0$, with basis $(1, -1, 0)$ and $(0, 0, 1)$.
The complement of that plane is the null space of the matrix with these two rows, so we solve
$$x_1 - x_2 = 0, \qquad x_3 = 0.$$
The solutions are $t(1, 1, 0)$, so $(U^\perp)^\perp = \R(1, 1, 0) = U$.

### Why each hypothesis is needed

The space must be finite-dimensional, or $U$ must be closed.
In $\ell^2$, the subspace $c_{00}$ of finitely supported sequences has $c_{00}^\perp = \{0\}$, so $(c_{00}^\perp)^\perp = \ell^2 \ne c_{00}$, by [[the counterexample in l2|DNZF0R4VMZ]].

The set $U$ must be a subspace, since $(U^\perp)^\perp$ is always one.
For a subset $S$, the double complement in finite dimension is the span of $S$.
For $S = \{(1, 0)\}$ in $\R^2$, it is the whole $x$-axis, not $S$.

The form must be positive.
For $\langle x, y \rangle = x_1 y_1$ on $\R^2$ and $U = \{0\}$, we get $U^\perp = \R^2$, and then $(U^\perp)^\perp = \{x : x_1 = 0\} = \R(0, 1)$, which is not $U$.

### What it gives you

For subspaces $U$ and $W$ of $V$, the theorem gives $U \subseteq W$ if and only if $W^\perp \subseteq U^\perp$.
One direction is part 2 of the [[basic properties|T5Q51M5BAK]].
For the other, apply that part to $W^\perp \subseteq U^\perp$ and use the theorem on both sides.
In particular $U^\perp = W^\perp$ implies $U = W$, so a subspace is determined by its orthogonal complement.

The theorem also turns the sum rule into an intersection rule.
The sum rule for $U^\perp$ and $W^\perp$ gives $(U^\perp + W^\perp)^\perp = U \cap W$, and taking complements gives $(U \cap W)^\perp = U^\perp + W^\perp$.
For a real matrix $A$, it turns $\operatorname{Nul}(A) = \operatorname{Row}(A)^\perp$ into $\operatorname{Row}(A) = \operatorname{Nul}(A)^\perp$, as in the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]].

### The converse

Which subspaces satisfy $(U^\perp)^\perp = U$ in an infinite-dimensional space?
In a [[Hilbert space|HM2HHE3J51]], $(U^\perp)^\perp$ is the [[closure|0QEAJB91GZ]] of $U$, so the equality holds exactly for the closed subspaces.
We only name this fact here, and the counterexample above shows a subspace where the two sides differ.

## Explanations

### L1 human

Taking the orthogonal complement twice brings you back to where you started.
In space, the complement of a line is a plane, and the complement of that plane is the same line again.

### L2 human

The typical use is to prove that two subspaces are equal by showing that they have the same complement.
For example, let $U$ be the plane in $\R^3$ spanned by $(1, 0, -1)$ and $(0, 1, -1)$, and let $W$ be the plane $x_1 + x_2 + x_3 = 0$.
The complement of $U$ is cut out by $x_1 - x_3 = 0$ and $x_2 - x_3 = 0$, so it is $\R(1, 1, 1)$.
The plane $W$ is the set of vectors orthogonal to $(1, 1, 1)$, so $W = \R(1, 1, 1)^\perp$, and the theorem gives $W^\perp = \R(1, 1, 1)$.
The complements agree, so $U = (U^\perp)^\perp = (W^\perp)^\perp = W$.
Watch out: in an infinite-dimensional space, check that the subspaces are closed before you use this argument.

### L3 human

The map $U \mapsto U^\perp$ is an inclusion-reversing bijection of the lattice of subspaces of $V$ onto itself, and it is its own inverse.
So the subspaces of a finite-dimensional inner product space form an orthocomplemented lattice.
Without an inner product, the same statement uses the [[annihilator|0ASHNYF7AG]] in the dual space: $U^{00} = U$ under the identification of $V$ with $V^{**}$.
For the [[adjoint|0R9NMSM1ZP]], the theorem turns $\ker T^* = (\im T)^\perp$ into $\im T = (\ker T^*)^\perp$.
