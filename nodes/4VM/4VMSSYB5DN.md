---
tag: 4VMSSYB5DN
kind: statement
role: theorem
name: Nevanlinna–Pick interpolation
msc: ["30E05", 47A57]
uses: [8G5ABXRK85, 0DG0Z72CQD, TSPTN464CM, 0880F9EQCP, 9N6R5ADJXT]
about: [TSPTN464CM, 8G5ABXRK85]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna–Pick_interpolation
same_as:
  wikidata: Q7190737
  wikipedia: Nevanlinna–Pick interpolation
---

## Statement

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]].
Let $n \ge 1$, let $z_1, \ldots, z_n \in \mathbb{D}$ be distinct, and let $w_1, \ldots, w_n \in \mathbb{D}$.
Let $P$ be the [[Pick matrix|TSPTN464CM]] with entries $P_{ij} = \frac{1 - w_i \overline{w_j}}{1 - z_i \overline{z_j}}$.

1. There is a [[holomorphic function|0DG0Z72CQD]] $f \colon \mathbb{D} \to \mathbb{D}$ with $f(z_i) = w_i$ for $i = 1, \ldots, n$ if and only if $P$ is [[positive semidefinite|0880F9EQCP]].
2. Let $P$ be positive semidefinite and singular, of rank $m$.
Then such an $f$ is unique, and it is a constant of modulus $1$ times a [[Blaschke product|9N6R5ADJXT]] of degree $m$.

## Remarks

Proof idea for necessity: if $\abs{f} \le 1$, the multiplication operator by $f$ on the [[Hardy space|PNNNFJVF6W]] $H^2$ has norm at most $1$.
Its adjoint sends the reproducing kernel $k_{z_i}(z) = \frac{1}{1 - \overline{z_i} z}$ to $\overline{w_i} k_{z_i}$, and the condition $\norm{M_f^* g} \le \norm{g}$ on combinations of these kernels is exactly $P \ge 0$.
Sufficiency can be proved by Pick's original induction, which reduces $n$ points to $n - 1$ points with a Möbius change of variables, or by the commutant lifting theorem.

Example: for $n = 2$ with $z_1 = w_1 = 0$, $z_2 = a \ne 0$ and $w_2 = b$, the matrix is positive semidefinite exactly when $\abs{b} \le \abs{a}$.
This is the [[Schwarz lemma|0MB48XDBY3]]; when $\abs{b} = \abs{a}$, the matrix has rank $1$ and the unique solution is $f(z) = (b/a) z$.

## Explanations

### L1 human

You choose some points in the disc and where you want them to go.
The question is whether a holomorphic map of the disc into itself can do this.
The theorem gives a test: build the Pick matrix and check that it has no negative eigenvalue.
When the test passes only just, the map is forced and is a finite Blaschke product.

### L2 human

The theorem generalises the Schwarz–Pick lemma from one pair of points to any finite set.
Its operator form says that multipliers of $H^2$ of norm at most $1$ are characterised by positivity of a kernel.
This viewpoint later led to the theory of complete Pick spaces.
The same method treats interpolation in the upper half-plane and boundary interpolation problems, and it has applications in control theory.
For infinitely many points the condition becomes positivity of an infinite Pick matrix, and the interpolating sequences are characterised by Carleson.
