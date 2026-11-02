---
tag: W5HF4GMVN9
kind: definition
name: Isospectral manifolds
msc: [58J53, 58J50]
defines: 18MQEGN13R
uses: [7CBT4SM83Y, B8TYKV7AA1, R9YWQS15AA]
sources:
  - url: https://en.wikipedia.org/wiki/Isospectral
---

## Definition

Let $(M_1, g_1)$ and $(M_2, g_2)$ be closed [[Riemannian manifolds|7CBT4SM83Y]].
They are *isospectral* if they have the same [[spectrum of the Laplace–Beltrami operator|B8TYKV7AA1]].
This means that each real number $\lambda$ has the same multiplicity as an eigenvalue of the Laplacian of $M_1$ and of $M_2$.

## Remarks

An [[isometry|R9YWQS15AA]] $M_1 \to M_2$ carries eigenfunctions to eigenfunctions, so isometric manifolds are isospectral.
By Weyl's law, isospectral manifolds have the same dimension and the same volume.
Variants compare the spectra of the Laplacian on $p$-forms, or the Dirichlet or Neumann spectra of domains with boundary.

Example: [[Milnor's two flat tori|JNR9YJTT54]] $\R^{16}/\Gamma_1$ and $\R^{16}/\Gamma_2$, built from two non-isometric even unimodular lattices, are isospectral and not isometric.

Non-example: the round spheres $S^2$ of radius $1$ and of radius $2$ are not isospectral.
Their eigenvalues are $k(k+1)$ and $k(k+1)/4$, so the first nonzero eigenvalues $2$ and $\tfrac12$ differ.
