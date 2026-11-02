---
tag: CGEXQ8BAH5
kind: definition
name: Geometric quantization
msc: [53D50]
defines: FG33N4ZHDG
uses: [CAN490EPRT, C5EH3B4BEP, 2S0MXDT4YH, HM2HHE3J51, GX74C07T0G]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_quantization
---

## Definition

Let $(M, \omega)$ be a [[symplectic manifold|CAN490EPRT]] of dimension $2n$ and let $\hbar > 0$.
Assume the integrality condition: the [[de Rham class|GX74C07T0G]] of $\omega / (2\pi\hbar)$ lies in the image of $H^2(M; \Z) \to H^2(M; \R)$.
Geometric quantization consists of the following data and steps.

1. (Prequantization) A *prequantum line bundle* is a Hermitian complex line bundle $L \to M$, a [[vector bundle|P4DZM975BV]] of rank one, with a connection $\nabla$. The connection must preserve the Hermitian metric and have curvature $-\frac{i}{\hbar}\omega$.
The *prequantum Hilbert space* is the space of sections $s$ of $L$ with $\int_M \abs{s}^2 \, \omega^n / n! < \infty$.
To a smooth function $f$ it assigns the operator $\hat{f} = -i\hbar \nabla_{X_f} + f$ on sections, where $X_f$ is the [[Hamiltonian vector field|C5EH3B4BEP]] of $f$.
2. (Polarization) A *polarization* is a subbundle $P \subset TM \otimes \C$ of complex rank $n$ that is closed under the Lie bracket of vector fields. The complex-bilinear extension of $\omega$ must vanish on $P$.
3. (Quantization) The *quantum Hilbert space* is the [[Hilbert space|HM2HHE3J51]] of square-integrable sections $s$ that are polarized: $\nabla_X s = 0$ for every section $X$ of $P$.

## Remarks

The integrality condition holds exactly when a prequantum line bundle exists.
With consistent conventions, $f \mapsto \hat{f}$ sends the [[Poisson bracket|2S0MXDT4YH]] to the commutator up to the factor $\pm i\hbar$, which is Dirac's quantization condition.
Only functions whose flows preserve $P$ act directly on the polarized sections; in practice one also adds half-forms, the metaplectic correction, to obtain the correct spectra.
Sign and factor conventions differ from author to author.

Example: take $M = \C^n$ with the standard form and the Kähler polarization spanned by the vectors $\partial / \partial \bar{z}_j$.
Then the quantum Hilbert space is the Segal–Bargmann space of holomorphic functions that are square-integrable for a Gaussian weight.
For the sphere $S^2 = \mathbb{CP}^1$ with total area $2\pi\hbar k$, $k \ge 1$ an integer, the prequantum bundle is the line bundle of degree $k$.
The polarized sections are its holomorphic sections, a space of dimension $k + 1$.

Non-example: for the sphere with total area $\pi\hbar$, the integrality condition fails, since $\int_{S^2} \omega / (2\pi\hbar) = \frac{1}{2}$ is not an integer, so no prequantum line bundle exists.
