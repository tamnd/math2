---
tag: E0NXWECXTB
kind: definition
name: Chern–Simons theory
msc: [57K16, 81T45, 58J28]
defines: F28G886PWD
uses: [R20TB2KEQQ, 8E37E74XVP, NJ21PN5ZGJ, 0E3G0GRPZ6]
sources:
  - url: https://en.wikipedia.org/wiki/Chern%E2%80%93Simons_theory
---

## Definition

Let $G = SU(n)$, a compact Lie group with Lie algebra $\mathfrak{su}(n)$, and let $M$ be a closed oriented [[3-manifold|R20TB2KEQQ]].
Every [[principal $G$-bundle|8E37E74XVP]] over $M$ is trivial, so a [[connection|NJ21PN5ZGJ]] on it is given by a $\mathfrak{su}(n)$-valued [[differential $1$-form|0E3G0GRPZ6]] $A$ on $M$.
The *Chern–Simons functional* is
$$CS(A) = \frac{1}{8\pi^2} \int_M \tr\left(A \wedge dA + \tfrac{2}{3} A \wedge A \wedge A\right).$$
For an integer $k$, called the level, *Chern–Simons theory* is the gauge theory on $M$ with gauge group $G$ and action $S_k(A) = 2\pi k \, CS(A)$.
Its quantum partition function is the formal path integral
$$Z_k(M) = \int e^{i S_k(A)} \, \mathcal{D}A$$
over connections modulo gauge transformations.

## Remarks

Example: the trivial connection $A = 0$ has $CS(0) = 0$.
The first variation of $CS$ is $\delta CS = \frac{1}{4\pi^2} \int_M \tr(\delta A \wedge F_A)$, where $F_A = dA + A \wedge A$ is the curvature, so the critical points of $CS$ are exactly the flat connections.

$CS$ is not invariant under gauge transformations: a gauge transformation $g \colon M \to G$ changes $CS(A)$ by an integer, the winding number of $g$ up to sign.
So $CS$ is not a function on connections modulo gauge, but $e^{i S_k}$ is, because $k$ is an integer; this is why the level must be an integer.

The path integral is not a rigorous mathematical definition.
Its predicted values are realised rigorously by the Witten–Reshetikhin–Turaev invariants.
