---
tag: 75FDK6Q2MV
kind: definition
name: Faddeev–Popov ghost
msc: [81T13, 81T70]
defines: 5WKBCMW1BC
uses: [CYWSMK47CN, TXD7MTYQYS, 707DEWCCFX, 5JJYBJ6A8K, 1NYTFT5NPE]
sources:
  - url: https://en.wikipedia.org/wiki/Faddeev%E2%80%93Popov_ghost
---

## Definition

Let $G$ be a compact Lie group with [[Lie algebra|5JJYBJ6A8K]] $\mathfrak{g}$.
Consider a gauge theory of $\mathfrak{g}$-valued connections $A$ on $\R^4$.
The [[gauge group|707DEWCCFX]] of maps $\omega \colon \R^4 \to G$ acts on them by $A \mapsto A^\omega$.
Let $F(A) = 0$ be a [[gauge-fixing|TXD7MTYQYS]] condition, where $F(A)$ is a $\mathfrak{g}$-valued function.
The *Faddeev–Popov operator* at $A$ is the linear operator
$$M_A = \left. \frac{\delta F(A^{\omega})}{\delta \omega} \right|_{\omega = 1}$$
obtained by differentiating $F$ along infinitesimal gauge transformations at $A$.
The *Faddeev–Popov ghost* $c$ and *antighost* $\bar c$ are two independent $\mathfrak{g}$-valued fields with anticommuting components.
They are introduced in the [[path integral|1NYTFT5NPE]] so that
$$\det M_A = \int \mathcal{D}\bar c\, \mathcal{D}c\, \exp\!\left( -\int \bar c\, M_A\, c\; d^4x \right),$$
as a formal [[Berezin integral|CYWSMK47CN]].
The term $\int \bar c\, M_A\, c\, d^4x$ is the ghost action that is added to the gauge-fixed action.

## Remarks

In finite dimensions the identity is exact: for an $n \times n$ matrix $M$ and odd generators $\theta_1, \dots, \theta_n, \bar\theta_1, \dots, \bar\theta_n$, one has $\int d\bar\theta_1\, d\theta_1 \cdots d\bar\theta_n\, d\theta_n\, e^{-\bar\theta^T M \theta} = \det M$ with the convention $\int d\theta\, \theta = 1$.
For $n = 1$ this reads $\int d\bar\theta\, d\theta\, (1 - m\bar\theta\theta) = m$.
Sign and normalization conventions for the ghost action vary between texts.

Example: for the Lorenz gauge $F(A) = \partial^\mu A_\mu$, the operator $M_A$ is, up to sign and normalization, $\partial^\mu D_\mu$, where $D_\mu = \partial_\mu + [A_\mu, \cdot\,]$ is the covariant derivative in the adjoint representation.

Non-example of a need for ghosts: in electromagnetism, with $G = U(1)$, the bracket term vanishes and $M_A = \partial^\mu \partial_\mu$ does not depend on $A$.
Then $\det M_A$ is a constant that cancels in normalized expectation values, and the ghosts decouple.
