---
tag: 35KXRGMAHT
kind: definition
name: Extended finite element method
msc: [65N30, 74S05, 74R10]
defines: MWB6Y5Q4VK
uses: [98GZ9DVHTA, NH739XXVXK, 09C4JP7Y0M, Y5B0PEBKE8]
sources:
  - url: https://en.wikipedia.org/wiki/Extended_finite_element_method
---

## Definition

Let $\mathcal{T}_h$ be a mesh of a domain $\Omega \subset \R^d$ with nodes $x_i$, $i \in I$.
Let $N_i$ be standard [[finite element|98GZ9DVHTA]] shape functions with $\sum_{i \in I} N_i = 1$ on $\Omega$, a [[partition of unity|NH739XXVXK]].
Let $\psi \colon \Omega \to \R$ be an enrichment function that carries a known local feature of the solution.
Let $J \subseteq I$ be the set of nodes whose shape function support meets the region of that feature.
The *extended finite element method* is the [[Galerkin method|Y5B0PEBKE8]] in the space of functions
$$u_h(x) = \sum_{i \in I} N_i(x) \, u_i + \sum_{j \in J} N_j(x) \, \psi(x) \, a_j,$$
with unknown coefficients $u_i$ and $a_j$.

## Remarks

The extra functions $N_j \psi$ have small support, so the system matrix stays sparse.
If all $a_j$ equal one value $a$, then on a region where $\sum_{j \in J} N_j = 1$ the enrichment equals $a \psi$ exactly.
Common choices of $\psi$ are a [[Heaviside function|09C4JP7Y0M]] across a crack, and the singular functions of the crack tip, which behave like $\sqrt{r}$.
Often one uses the shifted form $\psi(x) - \psi(x_j)$, so that $u_h(x_i) = u_i$ at the nodes.

Example: on $\Omega = (0, 1)$ with nodes $x_i = ih$, let a crack sit at a point $c$ inside $(x_k, x_{k+1})$.
Take $\psi(x) = H(x - c)$, with $H$ the Heaviside step, and $J = \set{k, k+1}$.
Then $u_h$ can jump at $c$ by $N_k(c) a_k + N_{k+1}(c) a_{k+1}$, while the mesh does not have a node at $c$.

Non-example: the standard space with only the first sum is continuous on $\Omega$.
It has no enrichment, $J = \emptyset$, so it cannot jump at $c$ unless $c$ is a mesh node and the mesh is split there.
