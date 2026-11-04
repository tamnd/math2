---
tag: JY16CBEV99
kind: statement
role: proposition
name: The general Selberg trace formula for cocompact quotients
sources:
  - wikipedia: en:981694@r1371813961
    locator: Selberg trace formula, section The general Selberg trace formula for cocompact quotients
    note: adopted
    mention: wikipedia://en/981694#03R7
    sections: [Statement]
inventory: [Y16RJVXN70]
---

## Statement

Let *G* be a unimodular locally compact group, and $\Gamma$ a discrete cocompact subgroup of *G* and $\phi$ a compactly supported continuous function on *G*. The trace formula in this setting is the following equality:

$$\sum_{\gamma\in\{\Gamma\}} a_\Gamma^G(\gamma)\int_{G^\gamma\setminus G}\phi(x^{-1}\gamma x)\,dx = \sum_{\pi\in\widehat G}a_\Gamma^G(\pi)\operatorname{tr}\pi(\phi)$$

where $\{\Gamma\}$ is the set of conjugacy classes in $\Gamma$, $\widehat G$ is the unitary dual of *G* and:

- for an element $\gamma \in \Gamma$, $a_\Gamma^G(\gamma) = \text{volume}(\Gamma^\gamma\setminus G^\gamma)$ with $G^\gamma, \Gamma^\gamma$ the centralisers of $\gamma$ in $G,\Gamma$ respectively;
- for an irreducible unitary representation $\pi$ of $G$, $a_\Gamma^G(\pi)$ is the multiplicity of $\pi$ in the right-representation on $\Gamma\backslash G$ in $L^2(\Gamma\backslash G$), and $\pi(\phi)$ is the operator $\int_G \phi(g)\pi(g) dg$;
- all integrals and volumes are taken with respect to the Haar measure on $G$ or its quotients.

The left-hand side of the formula is called the *geometric side* and the right-hand side the *spectral side*. The terms $\int_{G^\gamma\setminus G}\phi(x^{-1}\gamma x)\,dx$ are orbital integrals.

When $G$ is a semisimple Lie group with a maximal compact subgroup $K$ and $X=G/K$ is the associated symmetric space the conjugacy classes in $\Gamma$ can be described in geometric terms using the compact Riemannian manifold (more generally orbifold) $\Gamma \backslash X$. The orbital integrals and the traces in irreducible summands can then be computed further and in particular one can recover the case of the trace formula for hyperbolic surfaces in this way.
