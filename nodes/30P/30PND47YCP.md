---
tag: 30PND47YCP
kind: statement
role: proposition
name: Lagrangian subspaces of a symplectic vector space
aliases: [lagrangian-subspace, maximal-isotropic-subspaces-of-a-symplectic-space]
msc: ["15A63", "53D05"]
topics: [DYAK7YMK7B]
audience: grad
about: [PQ7JJY0VPH]
uses: [W5FHT07SJJ, PQ7JJY0VPH, 05Q4JD6XEH, M2JH84VEY9, M0G958M917, MZHFGPV1YT]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectic_vector_space
    locator: Subspaces
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Statement

In a symplectic space of dimension $2m$, the subspaces on which the form vanishes have dimension at most $m$, and the largest ones, the Lagrangian subspaces, have dimension exactly $m$.

Let $(V, \omega)$ be a [[symplectic vector space|W5FHT07SJJ]] of dimension $2m$ over a field $F$.
For a subspace $W$, let $W^\perp = \{ v \in V : \omega(w, v) = 0 \text{ for all } w \in W \}$ be its [[orthogonal complement|05Q4JD6XEH]].
Call $W$ *isotropic* when $W \subseteq W^\perp$, and *Lagrangian* when $W = W^\perp$.

1. For each subspace $W$, $\dim W + \dim W^\perp = 2m$ and $(W^\perp)^\perp = W$.
2. Each isotropic subspace $W$ has $\dim W \leq m$.
3. A subspace $W$ is Lagrangian if and only if it is isotropic and $\dim W = m$.
4. Each isotropic subspace lies in a Lagrangian subspace. So Lagrangian subspaces exist, and they are exactly the maximal isotropic subspaces.

The [[proof|YKK5M72GW7]] uses the dimension formula for orthogonal complements and adds one vector of $W^\perp$ at a time.

## Remarks

### Why each hypothesis is needed

Nondegeneracy is needed for parts 1 to 3.
The zero form on $F^2$ is alternating, and the whole space $V$ is isotropic for it, of dimension $2 > 1$.

The form must be alternating for the dimension $m$ in part 4.
The dot product on $\mathbb{R}^2$ is symmetric and nondegenerate, but only $\{0\}$ is isotropic for it, so its maximal isotropic subspaces have dimension $0$, not $1$.

Finite dimension is needed for part 1, whose proof counts dimensions with the rank-nullity theorem.

### What it gives you

Part 3 is the usual test for a Lagrangian subspace: check that $\omega$ vanishes on pairs of basis vectors, then count the dimension.
In a symplectic plane every line is Lagrangian, because every vector is [[isotropic|MZHFGPV1YT]] and $m = 1$.

A larger use is the graph of a matrix.
In $F^{2m}$ with $\omega((x, y), (x', y')) = x^{\mathsf{T}} y' - x'^{\mathsf{T}} y$, take an $m \times m$ matrix $A$ and its graph $\Gamma_A = \{ (x, Ax) : x \in F^m \}$, which has dimension $m$.
Compute the form on two points of the graph:
$$\omega((x, Ax), (x', Ax')) = x^{\mathsf{T}} A x' - x'^{\mathsf{T}} A x = x^{\mathsf{T}} (A - A^{\mathsf{T}}) x'.$$
So $\Gamma_A$ is Lagrangian exactly when $A$ is symmetric.
For example, $A = \begin{pmatrix} 1 & 2 \\ 2 & 0 \end{pmatrix}$ gives a Lagrangian plane in $F^4$, and $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ does not, since $x^{\mathsf{T}} (A - A^{\mathsf{T}}) x'$ is $x_1 x'_2 - x_2 x'_1$.

An isotropic subspace $W$ of dimension $k$ has $\dim W^\perp = 2m - k \geq k$, so $W^\perp$ contains $W$ and is coisotropic.

### The converse

Part 2 is sharp: for each $k \leq m$, the span of $e_1, \dots, e_k$ in the standard space is isotropic of dimension $k$.
Part 3 is already an equivalence.
Part 4 has the converse built in: a maximal isotropic subspace is Lagrangian, and a Lagrangian subspace is maximal isotropic.

### Generalizations

For a nondegenerate symmetric form in characteristic not $2$, all maximal totally isotropic subspaces also have one common dimension, the Witt index, by the [[Witt decomposition|BPMRSPB6GD]].
That index can be less than half the dimension, and it is $0$ for the dot product.
If $W$ is coisotropic, then $\omega$ induces a symplectic form on the quotient $W / W^\perp$, a construction called linear symplectic reduction.
The tangent spaces of a [[Lagrangian submanifold|H8ACPTMX08]] of a symplectic manifold are Lagrangian subspaces.

### Watch out

A Lagrangian subspace is its own complement, so it never has a complement of the form $L^\perp$.
In $F^2$ with the determinant form, $L = \operatorname{span}(e_1)$ has $L^\perp = L$, and $L + L^\perp = L$ is not the whole plane.
A Lagrangian complement of $L$, such as $\operatorname{span}(e_2)$, must be found by other means.

## Explanations

### L1 human

In a symplectic space of dimension $2m$, an isotropic subspace is one on which the area form is zero.
In the plane ($m = 1$), every line is isotropic, but the whole plane is not, since $(1, 0)$ and $(0, 1)$ span area $1$.
In general an isotropic subspace has at most half the dimension of the space.
The isotropic subspaces of exactly half the dimension are Lagrangian, and every isotropic subspace grows into one.

### L2 human

Here is a typical task: grow $W = \operatorname{span}(e_1)$ to a Lagrangian subspace of $F^4$ with the basis $e_1, e_2, f_1, f_2$ and $\omega(e_i, f_j) = \delta_{ij}$, $\omega(e_i, e_j) = \omega(f_i, f_j) = 0$.
Write $v = a_1 e_1 + a_2 e_2 + b_1 f_1 + b_2 f_2$.
Then $\omega(e_1, v) = b_1$, so $W^\perp = \operatorname{span}(e_1, e_2, f_2)$, of dimension $3 = 4 - 1$.
Take $x = e_2 + f_2$, which lies in $W^\perp$ but not in $W$, and put $L = \operatorname{span}(e_1, e_2 + f_2)$.
Since $\omega(e_1, e_2 + f_2) = 0$, the plane $L$ is isotropic, and $\dim L = 2 = m$, so $L$ is Lagrangian by part 3.
Check directly:
$$\omega(e_2 + f_2, v) = b_2 - a_2,$$
so $L^\perp = \{ b_1 = 0, \ b_2 = a_2 \}$, which is exactly $L$.
This one-vector-at-a-time growth is the proof of part 4 in miniature.

### L3 human

The Lagrangian subspaces of $\mathbb{R}^{2m}$ form the Lagrangian Grassmannian, a manifold of dimension $m(m + 1) / 2$.
Near $L_0 = \operatorname{span}(e_1, \dots, e_m)$, the Lagrangian subspaces that meet $\operatorname{span}(f_1, \dots, f_m)$ only in $0$ are the graphs of symmetric $m \times m$ matrices, and these matrices have $m(m + 1) / 2$ free entries.
The same graph picture works for the Lagrangian complements of any fixed Lagrangian subspace, so the Lagrangian Grassmannian is covered by charts that are spaces of symmetric matrices.
The [[classification of alternating forms|V8KKHKXXB3]] supplies the symplectic bases that these charts need.
