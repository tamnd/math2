---
tag: PY1C87VH5Y
kind: definition
name: Bra–ket notation
msc: ["81Q10", "46C05"]
defines: ZPPGSXJ45B
uses: [HM2HHE3J51, 4A82S5FVRT, TTC40N49M6, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] whose inner product $\ip{\cdot}{\cdot}$ is conjugate-linear in the first argument and linear in the second.
Bra–ket notation consists of the following conventions.

1. A *ket* $\lvert \psi \rangle$ is a vector $\psi \in \mathcal{H}$.
2. A *bra* $\langle \varphi \rvert$, for $\varphi \in \mathcal{H}$, is the continuous linear functional $\psi \mapsto \ip{\varphi}{\psi}$, an element of the [[continuous dual|4A82S5FVRT]] of $\mathcal{H}$.
3. The *bracket* $\langle \varphi \vert \psi \rangle$ is the value of $\langle \varphi \rvert$ at $\lvert \psi \rangle$, that is, $\ip{\varphi}{\psi}$.
4. For an operator $A$ on $\mathcal{H}$ and $\psi$ in its domain, $\langle \varphi \vert A \vert \psi \rangle = \ip{\varphi}{A\psi}$.
5. The *ket-bra* $\lvert \psi \rangle\langle \varphi \rvert$ is the operator $\chi \mapsto \ip{\varphi}{\chi}\, \psi$ on $\mathcal{H}$.

## Remarks

By the [[Riesz representation theorem|TTC40N49M6]], every continuous linear functional on $\mathcal{H}$ is a bra $\langle \varphi \rvert$ for exactly one $\varphi$.
The map $\lvert \varphi \rangle \mapsto \langle \varphi \rvert$ is conjugate-linear.

For an [[orthonormal basis|0S9GGTR0EX]] $(e_k)$, the expansion $\psi = \sum_k \ip{e_k}{\psi} e_k$ reads $\sum_k \lvert e_k \rangle\langle e_k \rvert = I$, with convergence of the sum applied to each vector.

Example: in $\C^2$, let $\lvert 0 \rangle = (1, 0)$ and $\lvert + \rangle = (1, 1)/\sqrt{2}$.
Then $\langle 0 \vert + \rangle = 1/\sqrt{2}$, and $\lvert 0 \rangle\langle 0 \rvert = \mathrm{diag}(1, 0)$ is the orthogonal projection onto the first axis.

Non-example: physicists write $\lvert x \rangle$ for a "position eigenstate" with $\langle x \vert \psi \rangle = \psi(x)$.
It is not a ket in the sense of clause 1: no vector of $L^2(\R)$ gives the functional $\psi \mapsto \psi(x)$, which is not even defined on all of $L^2(\R)$.
Such symbols are made precise as distributions, for example in a rigged Hilbert space.
