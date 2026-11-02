---
tag: RDX55HQ3XT
kind: statement
role: theorem
name: Gromov's non-squeezing theorem
msc: [53D35, 57R17]
uses: [CAN490EPRT, N469E47V75]
about: [CAN490EPRT]
sources:
  - url: https://en.wikipedia.org/wiki/Non-squeezing_theorem
same_as:
  wikidata: Q3527214
  wikipedia: Non-squeezing theorem
---

## Statement

Let $n \ge 1$ and give $\R^{2n}$ the coordinates $(x_1, y_1, \ldots, x_n, y_n)$ and the standard symplectic form $\omega_0 = \sum_{i=1}^n dx_i \wedge dy_i$.
For $r > 0$, let $B^{2n}(r)$ be the open ball of radius $r$ centered at $0$.
For $R > 0$, let
$$Z^{2n}(R) = \set{(x, y) \in \R^{2n} : x_1^2 + y_1^2 < R^2}$$
be the open cylinder of radius $R$ over a disc in the $(x_1, y_1)$-plane.
If there is a symplectic embedding $\varphi \colon B^{2n}(r) \to Z^{2n}(R)$, that is, a smooth embedding with $\varphi^* \omega_0 = \omega_0$, then $r \le R$.

## Remarks

Gromov proved the theorem in 1985 with [[pseudoholomorphic curves|N469E47V75]].
Assume $r > R$ and an embedding exists; compactify the cylinder to $S^2 \times T^{2n-2}$ with $S^2$ of area slightly more than $\pi R^2$.
For a suitable almost complex structure, there is a pseudoholomorphic sphere in the class of $S^2$ through the image of the center of the ball.
Its area is less than $\pi R^2 + \varepsilon$.
Pulled back to the ball, it gives a proper minimal surface through the center with area less than $\pi r^2$.
This contradicts the monotonicity formula, which says that such a surface has area at least $\pi r^2$.

The hypothesis that the disc lies in a symplectic plane is needed.
The map $(x_1, y_1, x_2, y_2) \mapsto (\lambda x_1, \lambda^{-1} y_1, \lambda x_2, \lambda^{-1} y_2)$ with small $\lambda > 0$ is a linear symplectomorphism that squeezes any ball into the cylinder $\set{x_1^2 + x_2^2 < R^2}$ over the $(x_1, x_2)$-plane, which is Lagrangian.
For $n = 1$ the theorem is just the statement that area-preserving maps preserve area.

## Explanations

### L1 human

A symplectic map preserves volume, but in dimension four and higher it is much more rigid than that.
A ball cannot be squeezed by a symplectic map through a round hole whose radius is smaller than the ball's, even though the cylinder over the hole has infinite volume.
This is sometimes called the principle of the symplectic camel.

### L2 human

The theorem marks the birth of symplectic topology: it shows that symplectic maps are not just volume-preserving maps.
It leads to the notion of a [[symplectic capacity|8KCB5KJKNT]], a size of a symplectic set that is invariant under symplectic embeddings.
By Liouville's theorem, Hamiltonian flows preserve volume; non-squeezing gives a finer constraint on them, a classical analogue of the uncertainty principle.
