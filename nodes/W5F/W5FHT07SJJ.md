---
tag: W5FHT07SJJ
kind: definition
name: Symplectic vector space
msc: ["15A63", "53D05"]
topics: [DYAK7YMK7B]
audience: grad
defines: PQ7JJY0VPH
uses: [0ZHWKQMVX5, 0SQZMXB6GP, 08ZQAKBKHF, 0KAN330PAH]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Standard symplectic space
---

## Definition

A symplectic vector space is a finite-dimensional space with a nondegenerate alternating form.

Let $F$ be a field and let $V$ be a [[finite-dimensional vector space|0ZHWKQMVX5]] over $F$.
A *symplectic form* on $V$ is a [[bilinear form|0SQZMXB6GP]] $\omega \colon V \times V \to F$ such that:

1. $\omega$ is [[alternating|08ZQAKBKHF]]: $\omega(v, v) = 0$ for all $v \in V$;
2. $\omega$ is [[nondegenerate|0KAN330PAH]]: if $\omega(v, w) = 0$ for all $w \in V$, then $v = 0$.

A *symplectic vector space* is a pair $(V, \omega)$ of such a space $V$ and a symplectic form $\omega$ on $V$.
For a subspace $W$ of $V$, we write $W^\perp = \{ v \in V : \omega(w, v) = 0 \text{ for all } w \in W \}$.
A subspace $L$ of $V$ is *Lagrangian* when $L^\perp = L$.

## Notation

The standard symplectic space is $F^{2m}$ with $\omega(x, y) = x^{\mathsf{T}} J y$, where $J = \begin{pmatrix} 0 & I_m \\ -I_m & 0 \end{pmatrix}$.
Some books write $W^\omega$ for $W^\perp$, to stress that the complement is taken for $\omega$ and not for an inner product.

## Remarks

Each condition does its own job.
The alternating condition makes $\omega$ an area form: a vector spans no area with itself.
It implies skew-symmetry $\omega(v, w) = -\omega(w, v)$ in every characteristic, and when $1 + 1 \neq 0$ the two conditions are equivalent.
In characteristic $2$ they are not, and the definition asks for $\omega(v, v) = 0$, the stronger one.
The nondegenerate condition says that no nonzero vector is invisible to $\omega$.
Since $\omega$ is skew-symmetric, the radical in the first slot and the radical in the second slot are the same, so it does not matter which slot the condition names.
Finite dimension makes the dimension count $\dim L = \tfrac{1}{2} \dim V$ for Lagrangian subspaces available.

A standard example is $F^{2m}$ with coordinates $(x_1, \dots, x_m, y_1, \dots, y_m)$ and
$$\omega(u, u') = \sum_{i=1}^{m} (x_i y'_i - x'_i y_i).$$
It is alternating, since each term vanishes when $u = u'$.
It is also nondegenerate.
Let $e_i$ and $f_i$ be the standard basis vectors for the coordinates $x_i$ and $y_i$.
If $u$ has $x_i \neq 0$, then $\omega(u, f_i) = x_i \neq 0$, and if $u$ has $y_i \neq 0$, then $\omega(u, e_i) = -y_i \neq 0$.

A case that fails is $\omega(u, u') = x_1 y'_1 - x'_1 y_1$ on $F^3$ with coordinates $(x_1, y_1, z)$.
It is alternating, but the vector $(0, 0, 1)$ pairs to zero with every vector, so it is degenerate.
No alternating form on a space of odd dimension is nondegenerate, by the [[classification of alternating forms|V8KKHKXXB3]].
The concept page [[symplectic vector space|PQ7JJY0VPH]] gives more examples and the main properties.

## Explanations

### L1 human

A symplectic form is an area form on a vector space.
It gives zero for a vector paired with itself, and it gives a nonzero area for each nonzero vector paired with a suitable partner.
In the plane, the pair $(1, 0)$ and $(0, 1)$ has area $1$, and the pair $(1, 0)$ and $(3, 0)$ has area $0$.

### L2 human

On $F^2$, the form $\omega(x, y) = x_1 y_2 - x_2 y_1$ is symplectic.
Its matrix is $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, which is alternating and has determinant $1$.
Each line $L$ in $F^2$ is Lagrangian: $\omega(v, v) = 0$ gives $L \subseteq L^\perp$, and $\dim L^\perp = 2 - 1 = 1$, so $L^\perp = L$.
Watch out: over $\mathbb{F}_2$ the identity matrix $I_2$ gives a nondegenerate skew-symmetric form, but $\omega(e_1, e_1) = 1$, so it is not symplectic.
