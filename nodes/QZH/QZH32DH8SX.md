---
tag: QZH32DH8SX
kind: definition
name: Jordan operator algebra
msc: [46L70, 17C65]
defines: QYES5210FJ
uses: [HM2HHE3J51, 0NEGN5CRSC, 6C2MCVB8C7, T4AWF1BRZB]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_operator_algebra
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]].
Let $B(H)_{\mathrm{sa}}$ be the real vector space of bounded [[self-adjoint operators|0NEGN5CRSC]] on $H$, with the operator norm $\norm{\cdot}$.
For $a, b \in B(H)_{\mathrm{sa}}$ put $a \circ b = \frac{1}{2}(ab + ba)$.
A *Jordan operator algebra*, or *JC-algebra*, on $H$ is a real linear subspace $A \subseteq B(H)_{\mathrm{sa}}$ such that:

1. $a \circ b \in A$ for all $a, b \in A$;
2. $A$ is closed in the norm topology.

## Remarks

Each JC-algebra is a [[special Jordan algebra|T4AWF1BRZB]], as a Jordan subalgebra of $B(H)^+$.
Clause 1 is equivalent to $a^2 \in A$ for all $a \in A$, since $a \circ b = \frac{1}{2}((a + b)^2 - a^2 - b^2)$.

Example: $H = \C^n$ and $A$ the real symmetric $n \times n$ matrices.
For symmetric $a$ and $b$, $(ab + ba)^T = ba + ab$, so clause 1 holds, and $A$ is closed because it is finite-dimensional.

Non-example: for $H = \C^2$, the real span of the Pauli matrices $\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ and $\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ fails clause 1.
Indeed $\sigma_x \circ \sigma_x = I$, and $I$ is not a combination of $\sigma_x$ and $\sigma_z$.

A JC-algebra that is closed in the weak operator topology is called a JW-algebra.
