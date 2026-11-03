---
tag: FBFFS10WGS
kind: definition
name: Chern–Weil homomorphism
msc: [53C05, 57R20]
defines: 82ZPRD39J7
uses: [NJ21PN5ZGJ, ZAJFW1S078, GX74C07T0G, 7HACJC0JE2]
sources:
  - url: https://en.wikipedia.org/wiki/Chern%E2%80%93Weil_homomorphism
---

## Definition

Let $G$ be a Lie group with [[Lie algebra|WKVBS76432]] $\mathfrak{g}$, and let $\mathbb{K}$ be $\R$ or $\C$.
For $k \ge 0$, let $I^k(G)$ be the space of symmetric $k$-linear maps $f : \mathfrak{g}^k \to \mathbb{K}$ that are invariant under the [[adjoint action|P6ZP0TE07M]]: $f(\mathrm{Ad}_g X_1, \dots, \mathrm{Ad}_g X_k) = f(X_1, \dots, X_k)$ for all $g \in G$.
Let $\pi : P \to M$ be a principal $G$-bundle with a [[connection form|NJ21PN5ZGJ]] $\omega$ and [[curvature form|ZAJFW1S078]] $\Omega$.
For $f \in I^k(G)$, the $2k$-form $f(\Omega, \dots, \Omega)$ on $P$ (formed with the wedge product) equals $\pi^* \alpha_f$ for a unique closed $2k$-form $\alpha_f$ on $M$.
The *Chern–Weil homomorphism* is the map
$$I^*(G) = \bigoplus_{k \ge 0} I^k(G) \to H^{\mathrm{even}}_{\mathrm{dR}}(M; \mathbb{K}), \quad f \mapsto [\alpha_f],$$
into [[de Rham cohomology|GX74C07T0G]], which does not depend on the choice of $\omega$.

## Remarks

The form $f(\Omega, \dots, \Omega)$ descends to $M$ because $\Omega$ vanishes on vertical vectors and $f$ is $\mathrm{Ad}$-invariant; it is closed by the Bianchi identity $d\Omega = [\Omega \wedge \omega]$ and invariance.
For two connections $\omega_0, \omega_1$, the forms $\alpha_f$ differ by the exterior derivative of a transgression form built from the path $\omega_t = (1-t)\omega_0 + t\omega_1$; so the class is independent of $\omega$.
With the product of symmetric multilinear forms, $I^*(G)$ is a commutative algebra and the map is an algebra homomorphism.
Example: for $G = \mathrm{U}(1)$, $\mathfrak{g} = i\R$ and $f(X) = \frac{i}{2\pi} X$, the class $[\alpha_f]$ is the first Chern class of the associated line bundle.
For $G = \mathrm{U}(n)$, $\det\big(I + \frac{i}{2\pi} \Omega\big)$ gives the total Chern class, and its images are the [[characteristic classes|7HACJC0JE2]] with real coefficients.
