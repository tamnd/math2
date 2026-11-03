---
tag: H77Y8DTXQC
kind: definition
name: Spin network
msc: [83C45, "22E70"]
defines: B173ESJ4YX
uses: [00C0BR7D7H, 9V6PRD1Z90, WHDZ3MK56B]
sources:
  - url: https://en.wikipedia.org/wiki/Spin_network
---

## Definition

For $j \in \set{0, \frac12, 1, \frac32, \dots}$, let $V_j$ be the irreducible representation of $SU(2)$ of dimension $2j + 1$ (see [[representation theory of SU(2)|9V6PRD1Z90]]).
An *($SU(2)$) spin network* is a triple $(\Gamma, j, \iota)$ where:

1. $\Gamma$ is a finite oriented [[graph|00C0BR7D7H]], possibly with loops and multiple edges;
2. $j$ assigns to each edge $e$ a spin $j_e \ne 0$;
3. $\iota$ assigns to each vertex $v$ an intertwiner $\iota_v$, that is, an $SU(2)$-invariant vector of $\bigotimes_{e \text{ incoming at } v} V_{j_e} \otimes \bigotimes_{e \text{ outgoing at } v} V_{j_e}^*$.

In loop quantum gravity, $\Gamma$ is embedded in a three-manifold $\Sigma$.
The spin network then defines the function $\Psi(A) = \left( \bigotimes_v \iota_v \right) \cdot \left( \bigotimes_e \rho_{j_e}(h_e(A)) \right)$ of a connection $A$.
Here $h_e(A)$ is the [[holonomy|WHDZ3MK56B]] of $A$ along $e$, $\rho_j$ is the representation on $V_j$, and $\cdot$ means contracting all indices.

## Remarks

Example: let $\Gamma$ be one edge $e$ that is a closed loop, with a two-valent vertex $v$ and $\iota_v$ the identity of $V_j$, an invariant element of $V_j \otimes V_j^*$.
Then $\Psi(A) = \tr \rho_j(h_e(A))$, the Wilson loop of $A$ in spin $j$.
Non-example: a trivalent vertex with three edges of spin $\frac12$ admits no nonzero intertwiner.
Indeed $V_{1/2} \otimes V_{1/2} \otimes V_{1/2} \cong V_{1/2} \oplus V_{1/2} \oplus V_{3/2}$ contains no copy of $V_0$.
In general, three spins at a trivalent vertex must satisfy the triangle inequalities and have an integer sum.
Spin network states on embedded graphs, with orthonormal intertwiners at the vertices, form an orthonormal basis of the gauge-invariant Hilbert space of loop quantum gravity.
