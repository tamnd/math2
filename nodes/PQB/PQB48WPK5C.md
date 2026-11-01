---
tag: PQB48WPK5C
kind: definition
name: Classical group
msc: [20G15, 20H20]
defines: 75H4HY10Z4
uses: [04C5ZBG1WT, 018W3V3TCT, 0FCHE902D7, 0V9PMN0RBH, 0SQZMXB6GP, 054YEQ0Y8M, 0TKYAEJ8N7, 0R9R0Y1HDK]
sources:
  - url: https://en.wikipedia.org/wiki/Classical_group
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] and let $V$ be a [[finite-dimensional vector space|018W3V3TCT]] over $F$.
A *classical group* over $F$ is one of the following groups:

1. the [[general linear group|0FCHE902D7]] $\mathrm{GL}(V)$ of invertible linear maps $V \to V$, or the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}(V)$ of those of determinant $1$;
2. the [[orthogonal group|0TKYAEJ8N7]] $\mathrm{O}(V, B) = \set{g \in \mathrm{GL}(V) : B(gu, gv) = B(u, v) \text{ for all } u, v}$ of a nondegenerate symmetric [[bilinear form|0SQZMXB6GP]] $B$ on $V$, where $F$ has characteristic not $2$;
3. the symplectic group $\mathrm{Sp}(V, \omega)$ of all $g \in \mathrm{GL}(V)$ preserving a nondegenerate alternating bilinear form $\omega$ on $V$;
4. the [[unitary group|0R9R0Y1HDK]] $\mathrm{U}(V, h)$ of all $g \in \mathrm{GL}(V)$ preserving $h$. Here $h$ is a nondegenerate Hermitian [[sesquilinear form|054YEQ0Y8M]] for an automorphism $\sigma$ of $F$ of order $2$;

together with their subgroups of elements of determinant $1$, such as $\mathrm{SO}(V, B)$ and $\mathrm{SU}(V, h)$.

## Remarks

The term is a name for this list rather than a single axiom, and authors vary.
Many include the analogous groups over the quaternions or over other division rings, and the projective quotients such as $\mathrm{PSL}(V)$, which give finite simple groups when $F$ is finite.

Example: $\mathrm{SO}(3)$, the special orthogonal group of the standard form $B(u, v) = u_1 v_1 + u_2 v_2 + u_3 v_3$ on $\R^3$, is classical; $B$ is symmetric and nondegenerate, since its matrix is the identity.

Non-example: the group of $g \in \mathrm{GL}_2(\R)$ preserving $B(u, v) = u_1 v_1$ is not given by clause 2, since $B$ is degenerate: $B(u, (0, 1)) = 0$ for all $u$.
This group consists of the matrices $\begin{pmatrix} \pm 1 & 0 \\ c & d \end{pmatrix}$ with $d \neq 0$.

When $F = \C$ and $\sigma$ is complex conjugation, clause 4 gives $\mathrm{U}(n)$ for the standard positive definite form; a nondegenerate alternating form exists only when $\dim V$ is even.
