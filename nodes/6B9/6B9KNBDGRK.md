---
tag: 6B9KNBDGRK
kind: definition
name: Vertex operator algebra
msc: [17B69, 81T40]
defines: GHRPQAJY43
uses: [R9WFXME6GC, 033WGN00BF, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Vertex_operator_algebra
---

## Definition

A *vertex operator algebra* over $\C$ consists of:

- a $\Z$-graded complex [[vector space|000AYPA9AJ]] $V = \bigoplus_{n \in \Z} V_n$ with $\dim V_n < \infty$ for all $n$ and $V_n = 0$ for all sufficiently negative $n$;
- a linear map $Y \colon V \to (\End V)[[z, z^{-1}]\,]$, written $Y(v, z) = \sum_{n \in \Z} v_n z^{-n-1}$ with $v_n \in \End V$, into [[formal series|033WGN00BF]] in a variable $z$;
- a vector $\mathbf{1} \in V_0$, the vacuum vector, and a vector $\omega \in V_2$, the conformal vector.

Write $\delta(x) = \sum_{n \in \Z} x^n$, and expand each binomial $(x_1 - x_2)^m$ in nonnegative powers of $x_2$.
These data must satisfy:

1. for all $u, v \in V$, $u_n v = 0$ for all sufficiently large $n$;
2. $Y(\mathbf{1}, z) = \id_V$, and for all $v \in V$, $Y(v, z)\mathbf{1}$ has only nonnegative powers of $z$ and its constant term is $v$;
3. (Jacobi identity) for all $u, v \in V$, in formal variables $z_0, z_1, z_2$,
$$z_0^{-1} \delta\!\left(\frac{z_1 - z_2}{z_0}\right) Y(u, z_1) Y(v, z_2) - z_0^{-1} \delta\!\left(\frac{z_2 - z_1}{-z_0}\right) Y(v, z_2) Y(u, z_1) = z_2^{-1} \delta\!\left(\frac{z_1 - z_0}{z_2}\right) Y(Y(u, z_0) v, z_2);$$
4. writing $Y(\omega, z) = \sum_{n \in \Z} L(n) z^{-n-2}$, there is a number $c \in \C$, the central charge, with $[L(m), L(n)] = (m - n) L(m + n) + \frac{c}{12}(m^3 - m)\, \delta_{m+n, 0}\, \id_V$ for all $m, n \in \Z$;
5. $L(0) v = n v$ for all $n \in \Z$ and $v \in V_n$;
6. $Y(L(-1) v, z) = \frac{d}{dz} Y(v, z)$ for all $v \in V$.

## Remarks

Clause 4 says that the operators $L(n)$ and the scalar $c$ give a representation of the [[Virasoro algebra|R9WFXME6GC]] on $V$.

Example: $V = V_0 = \C$ with $\mathbf{1} = 1$, $\omega = 0$ and $Y(a, z) = a \cdot \id_V$ is a vertex operator algebra of central charge $0$.
Indeed all $L(n)$ vanish, so clauses 4 to 6 hold with $c = 0$ on $V = V_0$, and the Jacobi identity reduces to the formal delta function identity $z_0^{-1}\delta\big(\frac{z_1 - z_2}{z_0}\big) - z_0^{-1}\delta\big(\frac{z_2 - z_1}{-z_0}\big) = z_2^{-1}\delta\big(\frac{z_1 - z_0}{z_2}\big)$.
Basic nontrivial examples are the Heisenberg vertex operator algebra of central charge $1$ and the lattice vertex operator algebras $V_L$ of even positive definite lattices $L$.
The moonshine module $V^\natural$ is an example of central charge $24$.

Non-example: let $V = \C[x]$, graded by degree, with $Y(a, z) b = ab$ for all $a, b$, $\mathbf{1} = 1$, and any $\omega \in V_2$.
This satisfies clauses 1 to 3, but $Y(\omega, z)$ is multiplication by $\omega$ with no dependence on $z$, so $L(0) = 0$.
Then $L(0) x = 0 \neq 1 \cdot x$, so clause 5 fails.

Without the grading and the conformal vector, the data $(V, Y, \mathbf{1})$ satisfying clauses 1 to 3 form a vertex algebra, and the Jacobi identity can be replaced by the locality axiom.
