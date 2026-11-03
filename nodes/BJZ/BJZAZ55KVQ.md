---
tag: BJZAZ55KVQ
kind: definition
name: Frame fields in general relativity
msc: [83C05, 53B30, 53C50]
defines: KH9BG71N36
uses: [63ZKC7AFX2, 0299VCW1TH, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Frame_fields_in_general_relativity
---

## Definition

Let $(M, g)$ be a [[spacetime|63ZKC7AFX2]] of signature $(-, +, +, +)$ and let $U \subseteq M$ be open.
A *frame field* (or *tetrad*) on $U$ is a quadruple of smooth [[vector fields|0299VCW1TH]] $e_0, \ldots, e_3$ on $U$ such that:

1. $g(e_a, e_b) = \eta_{ab}$ for all $a, b \in \set{0, 1, 2, 3}$, where $\eta = \operatorname{diag}(-1, 1, 1, 1)$.
2. $e_0$ is future-directed.

So at each point $p \in U$ the vectors $e_a(p)$ form an [[orthonormal basis|0S9GGTR0EX]] of $T_pM$ with timelike vector $e_0(p)$.

## Remarks

The dual coframe is the quadruple of one-forms $\theta^0, \ldots, \theta^3$ with $\theta^a(e_b) = \delta^a_b$, and then $g = \eta_{ab} \, \theta^a \otimes \theta^b$, summed over $a, b$.
Example: for the Schwarzschild metric $g = -f \, dt^2 + f^{-1} dr^2 + r^2(d\theta^2 + \sin^2\theta \, d\phi^2)$ with $f = 1 - 2m/r$, on the region $r > 2m$, $0 < \theta < \pi$, the static frame is $e_0 = f^{-1/2} \partial_t$, $e_1 = f^{1/2} \partial_r$, $e_2 = r^{-1} \partial_\theta$, $e_3 = (r \sin\theta)^{-1} \partial_\phi$; for example $g(e_0, e_0) = f^{-1} \cdot (-f) = -1$.
Non-example: the coordinate fields $\partial_t, \partial_r, \partial_\theta, \partial_\phi$ there are not a frame field, since $g(\partial_\theta, \partial_\theta) = r^2 \ne 1$ in general.
Two frame fields on $U$ differ at each point by a Lorentz transformation, $e'_b = \Lambda^a{}_b \, e_a$.
The integral curves of $e_0$ are the world lines of the observers that the frame field describes.
