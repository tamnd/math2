---
tag: 6RE2JMYMA0
kind: definition
name: Fukaya category
msc: [53D37, 53D40]
defines: 4HS60JABC5
uses: [CAN490EPRT, H8ACPTMX08, N469E47V75, NCKFPAGHXF, 9SYWRGVTRS]
sources:
  - url: https://en.wikipedia.org/wiki/Fukaya_category
---

## Definition

This gives the simplest version, over the field $\F_2$, in the exact setting.
Let $(M, \omega)$ be an exact [[symplectic manifold|CAN490EPRT]], $\omega = d\lambda$, that is convex at infinity.
Fix a generic [[almost complex structure|9SYWRGVTRS]] $J$ compatible with $\omega$ and of contact type at infinity.

1. The objects are the closed exact [[Lagrangian submanifolds|H8ACPTMX08]] $L \subset M$, those for which $\lambda|_L$ is exact.
2. Let $L_0, L_1$ be objects meeting transversally. The morphism space $\hom(L_0, L_1)$ is the $\F_2$-vector space $CF(L_0, L_1)$ with basis the finite set $L_0 \cap L_1$. For non-transverse pairs one first moves $L_1$ by a chosen Hamiltonian perturbation.
3. For $k \ge 1$ and objects $L_0, \ldots, L_k$, there is a map
$$\mu^k \colon \hom(L_{k-1}, L_k) \otimes \cdots \otimes \hom(L_0, L_1) \to \hom(L_0, L_k)$$
It sends $x_k \otimes \cdots \otimes x_1$ to $\sum_y m(y; x_1, \ldots, x_k)\, y$. The number $m(y; x_1, \ldots, x_k) \in \F_2$ counts modulo $2$ certain [[pseudoholomorphic|N469E47V75]] maps $u$ from a disc with $k + 1$ boundary punctures to $M$. These maps send the boundary arcs in cyclic order to $L_0, L_1, \ldots, L_k$ and converge to $x_1, \ldots, x_k$ and $y$ at the punctures. Only maps in moduli spaces of dimension $0$ are counted.

The *Fukaya category* of $M$ is this collection of objects, morphism spaces and maps $\mu^k$.

## Remarks

The maps satisfy the $A_\infty$ relations: for every $k \ge 1$,
$$\sum_{m + n \le k} \mu^{k - m + 1}\left(x_k, \ldots, x_{n + m + 1}, \mu^m(x_{n + m}, \ldots, x_{n + 1}), x_n, \ldots, x_1\right) = 0,$$
with $m \ge 1$ and $n \ge 0$ (over $\F_2$ there are no signs).
For $k = 1$ this says $\mu^1 \circ \mu^1 = 0$, and $\mu^1$ is the Lagrangian [[Floer|NCKFPAGHXF]] differential.
For $k = 2$ it says that $\mu^2$ is a chain map, and for $k = 3$ that $\mu^2$ is associative up to the homotopy $\mu^3$.
So the cohomology groups $HF(L_0, L_1)$ with the product induced by $\mu^2$ form an ordinary category, the Donaldson–Fukaya category.

Example: in $T^*S^1 = \R \times S^1$ with $\lambda = p\,d\theta$, the zero section and the graph of $d f$ for a function $f$ on $S^1$ are exact Lagrangians.
A non-example of an object is a circle $\set{p = c}$ with $c \ne 0$: there $\lambda|_L = c\, d\theta$ is closed but not exact.

The construction for closed or non-exact manifolds needs much more work, because of disc bubbling; Fukaya, Oh, Ohta and Ono developed it with obstruction theory.
Working over $\Z$ or with a $\Z$-grading needs extra data on the Lagrangians, such as spin structures and gradings.
