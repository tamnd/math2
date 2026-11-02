---
tag: Q0XKJ01SY6
kind: definition
name: Spinor bundle
msc: [53C27, 15A66]
defines: PYYQQKAZ0C
uses: [RSPZ9TCFQ8, A38B1QFK20, 8E37E74XVP]
sources:
  - url: https://en.wikipedia.org/wiki/Spinor_bundle
---

## Definition

Let $(M, g)$ be an oriented Riemannian manifold of dimension $n \ge 2$ with a [[spin structure|RSPZ9TCFQ8]] $(P, \xi)$, where $P$ is a principal $\operatorname{Spin}(n)$-bundle.
Let $\Sigma_n$ be a complex vector space of dimension $2^{\floor{n/2}}$ that is an irreducible module over the complexified [[Clifford algebra|A38B1QFK20]] $\mathbb{C}\ell_n$.
Let $\kappa \colon \operatorname{Spin}(n) \to GL(\Sigma_n)$ be the restriction of this module structure to $\operatorname{Spin}(n) \subset \mathbb{C}\ell_n$.
It is the complex spin representation of the spin group.
The *spinor bundle* of $(M, g, P, \xi)$ is the associated complex vector bundle
$$S = P \times_\kappa \Sigma_n = (P \times \Sigma_n) / \sim, \qquad (p \cdot a, v) \sim (p, \kappa(a) v) \text{ for } a \in \operatorname{Spin}(n).$$

## Remarks

The bundle $S$ has rank $2^{\floor{n/2}}$.
Clifford multiplication of $\mathbb{C}\ell_n$ on $\Sigma_n$ gives a bundle map $TM \otimes S \to S$, $X \otimes \psi \mapsto X \cdot \psi$, with $X \cdot X \cdot \psi = -g(X, X) \psi$.
The Levi-Civita connection lifts to a connection on $S$, and the Dirac operator is $D\psi = \sum_i e_i \cdot \nabla_{e_i} \psi$ for a local orthonormal frame $e_1, \dots, e_n$.
If $n$ is even, $S = S^+ \oplus S^-$ splits into half-spinor bundles of rank $2^{n/2 - 1}$.

Example: on $\R^n$ with its unique spin structure $P = \R^n \times \operatorname{Spin}(n)$, the spinor bundle is the trivial bundle $\R^n \times \Sigma_n$, and spinor fields are maps $\R^n \to \C^{2^{\floor{n/2}}}$.

Non-example: the bundle $P \times_{\kappa'} \C^n$ for the representation $\kappa'$ of $\operatorname{Spin}(n)$ through $\rho \colon \operatorname{Spin}(n) \to SO(n) \subset GL(\C^n)$ is the complexified tangent bundle $TM \otimes \C$, not the spinor bundle.
The element $-1 \in \operatorname{Spin}(n)$ acts as the identity in $\kappa'$ but as $-\id$ in the spin representation $\kappa$.
