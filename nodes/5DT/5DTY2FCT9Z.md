---
tag: 5DTY2FCT9Z
kind: definition
name: Seiberg–Witten invariants
msc: [57R57, 57K41, 53C27]
defines: PRDDMSTR4X
uses: [8H58Q6YJCH, F45VQ47GPV, Q61VFHCH2J, RSPZ9TCFQ8, 3DXGJTEQZH, WK8GKRKAVD]
sources:
  - url: https://en.wikipedia.org/wiki/Seiberg%E2%80%93Witten_invariants
---

## Definition

Let $M$ be a closed, oriented, [[smooth|F45VQ47GPV]] [[4-manifold|8H58Q6YJCH]] with $b_2^+(M) \ge 2$, where $b_2^+(M)$ is the number of positive eigenvalues of its [[intersection form|WK8GKRKAVD]].
Fix a [[Riemannian metric|Q61VFHCH2J]] $g$ on $M$ and an orientation of $H^1(M; \R) \oplus H^2_+(M; \R)$.
Let $\mathfrak{s}$ be a spin$^c$ structure on $M$, a generalization of a [[spin structure|RSPZ9TCFQ8]], with spinor bundles $W^\pm$ and determinant line bundle $L$.
For a $U(1)$-connection $A$ on $L$, let $D_A \colon \Gamma(W^+) \to \Gamma(W^-)$ be the associated [[Dirac operator|3DXGJTEQZH]].

1. Let $F_A^+$ be the self-dual part of the curvature of $A$.
Let $\sigma(\psi)$ be the trace-free part of the endomorphism $\psi \otimes \psi^*$ of $W^+$, viewed as a self-dual $2$-form by Clifford multiplication.
Let $\eta$ be a generic self-dual $2$-form.
The *Seiberg–Witten equations* for a pair $(A, \psi)$ with $\psi \in \Gamma(W^+)$ are
$$D_A \psi = 0, \qquad F_A^+ = \sigma(\psi) + i\eta.$$
2. The gauge group $\mathrm{Map}(M, S^1)$ acts by $u \cdot (A, \psi) = (A - 2u^{-1} du, u \psi)$, and the *moduli space* $\mathcal{M}(\mathfrak{s})$ is the set of solutions modulo this action.
3. Let $c_1(L)$ be the first Chern class of $L$, $\chi(M)$ the Euler characteristic and $\sigma(M)$ the signature.
The moduli space is a compact smooth oriented manifold of dimension
$$d(\mathfrak{s}) = \frac{c_1(L)^2 - 2\chi(M) - 3\sigma(M)}{4}.$$

The *Seiberg–Witten invariant* $SW_M(\mathfrak{s}) \in \Z$ is defined as follows.
If $d(\mathfrak{s}) = 0$, it is the signed number of points of $\mathcal{M}(\mathfrak{s})$.
If $d(\mathfrak{s}) > 0$ is even, it is the integral over $\mathcal{M}(\mathfrak{s})$ of a power of a natural degree-$2$ class.
In the other cases it is $0$.

## Remarks

When $b_2^+(M) \ge 2$, the number $SW_M(\mathfrak{s})$ does not depend on $g$ or $\eta$, so it is an invariant of $M$ with its orientation data.
For example, a closed symplectic $4$-manifold with $b_2^+ \ge 2$ has $SW = \pm 1$ on its canonical spin$^c$ structure, by a theorem of Clifford Taubes.
In contrast, a connected sum $M_1 \# M_2$ with $b_2^+(M_i) \ge 1$ for both summands has all Seiberg–Witten invariants zero.
When $b_2^+(M) = 1$ the count can jump as $g$ and $\eta$ vary, so the definition then depends on a chamber.
Normalizations of $\sigma(\psi)$ and of the gauge action differ by constants between authors.
