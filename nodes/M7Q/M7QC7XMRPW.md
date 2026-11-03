---
tag: M7QC7XMRPW
kind: definition
name: Bloch sphere
msc: [81P16, 81P45]
defines: A4Q88T5695
uses: [E9QTT3XBXS, V1JTB52E8C, XAQCW3D4QQ, P9CM4GQ2T0]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch_sphere
---

## Definition

Let $\sigma_x, \sigma_y, \sigma_z$ be the [[Pauli matrices|XAQCW3D4QQ]], and for $r = (r_x, r_y, r_z) \in \R^3$ put $r \cdot \sigma = r_x \sigma_x + r_y \sigma_y + r_z \sigma_z$.
Every [[density matrix|V1JTB52E8C]] $\rho$ of a [[qubit|E9QTT3XBXS]] can be written in exactly one way as
$$\rho = \tfrac12 (I + r \cdot \sigma), \qquad r \in \R^3, \quad \norm{r} \le 1.$$
The vector $r$ is the *Bloch vector* of $\rho$, and the set $\set{r \in \R^3 : \norm{r} \le 1}$ is the *Bloch ball*.
The *Bloch sphere* is its boundary, the unit [[sphere|P9CM4GQ2T0]] $\set{r \in \R^3 : \norm{r} = 1}$, whose points are the Bloch vectors of the pure states.

## Remarks

In coordinates, the pure state $\cos(\theta/2)|0\rangle + e^{i\varphi}\sin(\theta/2)|1\rangle$, with $0 \le \theta \le \pi$ and $0 \le \varphi < 2\pi$, has Bloch vector $(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$.

Example: $|{+}\rangle = (|0\rangle + |1\rangle)/\sqrt2$ has $\rho = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = \tfrac12(I + \sigma_x)$, so its Bloch vector is $(1, 0, 0)$, of norm $1$.

Non-example: for $r = (0, 0, 2)$, the matrix $\tfrac12(I + 2\sigma_z) = \mathrm{diag}(\tfrac32, -\tfrac12)$ has a negative eigenvalue, so it is not a state.
In general the eigenvalues of $\tfrac12(I + r\cdot\sigma)$ are $\tfrac12(1 \pm \norm{r})$, which explains the condition $\norm{r} \le 1$.

Orthogonal pure states have opposite Bloch vectors.
Conjugation $\rho \mapsto U\rho U^*$ by a unitary $U$ acts on Bloch vectors by a rotation, and this gives the covering homomorphism from $SU(2)$ onto $SO(3)$.
