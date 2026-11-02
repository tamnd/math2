---
tag: C00HSE6W2A
kind: definition
name: Scaling function and refinement equation
msc: [42C40, 65T60, 39B22]
defines: YH4BERB952
uses: [1GHQMBR7DE, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Multiresolution_analysis
---

## Definition

Let $(V_j)_{j \in \Z}$ be a [[multiresolution analysis|1GHQMBR7DE]] of $L^2(\R)$.
A *scaling function* of it is a function $\varphi \in V_0$ whose integer translates $(\varphi(\cdot - k))_{k \in \Z}$ form an orthonormal basis of $V_0$.
The functions $\sqrt2 \, \varphi(2 \cdot - k)$, $k \in \Z$, form an orthonormal basis of $V_1$, and $\varphi \in V_1$.
Hence there is a unique sequence $(h_k)_{k \in \Z} \in \ell^2(\Z)$ with
$$\varphi(x) = \sqrt2 \sum_{k \in \Z} h_k \, \varphi(2x - k),$$
with convergence in $L^2(\R)$ (see [[Lp space|SASP14MA1Z]]).
This identity is the *refinement equation* (or two-scale equation) of $\varphi$, and $(h_k)$ is its *low-pass filter*; explicitly $h_k = \ip{\varphi}{\sqrt2 \, \varphi(2 \cdot - k)}$.

## Remarks

Orthonormality of the translates of $\varphi$ gives $\sum_k h_k \overline{h_{k + 2m}} = \delta_{m,0}$ for all $m \in \Z$.
If $\varphi$ is integrable with $\int \varphi \ne 0$, integrating the refinement equation gives $\sum_k h_k = \sqrt2$.
The function $\psi(x) = \sqrt2 \sum_k (-1)^k \overline{h_{1-k}} \, \varphi(2x - k)$ is then an orthonormal wavelet.

Example: in the Haar multiresolution analysis, $\varphi = 1_{[0, 1)}$ and $\varphi(x) = \varphi(2x) + \varphi(2x - 1)$.
So $h_0 = h_1 = 1/\sqrt2$ and $h_k = 0$ otherwise.
The formula for $\psi$ gives $\psi(x) = \varphi(2x) - \varphi(2x - 1) = 1_{[0, 1/2)}(x) - 1_{[1/2, 1)}(x)$, the Haar wavelet.

Non-example: $\varphi = 1_{[0, 2)}/\sqrt2$ satisfies the refinement equation $\varphi(x) = \varphi(2x) + \varphi(2x - 2)$, but its integer translates overlap, so $\ip{\varphi}{\varphi(\cdot - 1)} = \tfrac12 \ne 0$ and it is not the scaling function of a multiresolution analysis in the sense above.
