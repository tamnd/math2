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

Let $V$ be a finite-dimensional inner product space over $\R$ or $\C$, and let $U$ be a subspace of $V$.
Let $U^\perp$ be the [[orthogonal complement|079D68S3AW]] of $U$.
Then
$$(U^\perp)^\perp = U.$$
The inclusion $U \subseteq (U^\perp)^\perp$ holds in every inner product space; the [[proof|FZEF1XYTVB]] gets equality from a count of [[dimensions|05G2G0P224]].

## Remarks

### Why each hypothesis is needed

- Finite dimension: in $\ell^2$, the subspace $c_{00}$ of finitely supported sequences has $(c_{00}^\perp)^\perp = \ell^2 \ne c_{00}$, by [[the counterexample in l2|DNZF0R4VMZ]].
- Subspace: for a subset $S$ that is not a subspace, $(S^\perp)^\perp$ is the span of $S$. For $S = \set{(1, 0)}$ in $\R^2$, $(S^\perp)^\perp$ is the whole $x$-axis, not $S$.
- Positivity: for the form $\langle x, y \rangle = x_1 y_1$ on $\R^2$ and $U = \set{0}$, we get $U^\perp = \R^2$ and $(U^\perp)^\perp = \R(0, 1) \ne U$.

### Consequences

- For subspaces $U, W$ of $V$: $U \subseteq W$ if and only if $W^\perp \subseteq U^\perp$. One direction is part 2 of the [[basic properties|T5Q51M5BAK]]; for the other, apply that part to $W^\perp \subseteq U^\perp$ and use the theorem twice.
- $U^\perp = W^\perp$ implies $U = W$. So a subspace is determined by its orthogonal complement.
- $(U \cap W)^\perp = U^\perp + W^\perp$: the sum rule for $U^\perp$ and $W^\perp$ gives $(U^\perp + W^\perp)^\perp = U \cap W$, and then we take complements.
- For a real matrix $A$, $\operatorname{Row}(A) = \operatorname{Nul}(A)^\perp$ follows from $\operatorname{Nul}(A) = \operatorname{Row}(A)^\perp$, as in the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]].

### Converse

The converse question is which subspaces satisfy $(U^\perp)^\perp = U$ in an infinite-dimensional space.
In a [[Hilbert space|HM2HHE3J51]], $(U^\perp)^\perp$ is the [[closure|0QEAJB91GZ]] of $U$, so the equality holds exactly for the closed subspaces.
We name this fact here and do not prove it; the counterexample above shows the gap.

## Explanations

### L1 human

Taking the orthogonal complement twice gives back the subspace you started with.
In space, the complement of a line is a plane, and the complement of that plane is the same line again.

### L2 human

We check the theorem for $U = \R(1, 1, 0)$ in $\R^3$.

1. $U^\perp$ is the plane $x_1 + x_2 = 0$, with basis $(1, -1, 0)$ and $(0, 0, 1)$.
2. $(U^\perp)^\perp$ is the null space of the matrix with rows $(1, -1, 0)$ and $(0, 0, 1)$.
3. Its equations are $x_1 - x_2 = 0$ and $x_3 = 0$, so the solutions are $t(1, 1, 0)$.
4. Hence $(U^\perp)^\perp = \R(1, 1, 0) = U$.

The typical use is to prove that two subspaces are equal by showing that they have the same complement.
The trap is to use the theorem in an infinite-dimensional space without checking that $U$ is closed.

### L3 human

The map $U \mapsto U^\perp$ is an inclusion-reversing bijection of the lattice of subspaces of $V$ onto itself, and it is its own inverse.
So the subspaces of a finite-dimensional inner product space form an orthocomplemented lattice.
The same statement for a vector space without an inner product uses the [[annihilator|0ASHNYF7AG]] in the dual space: $U^{00} = U$ under the identification $V = V^{**}$.
For the [[adjoint|0R9NMSM1ZP]], it turns $\ker T^* = (\im T)^\perp$ into $\im T = (\ker T^*)^\perp$.
