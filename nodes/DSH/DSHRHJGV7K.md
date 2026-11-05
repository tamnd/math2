---
tag: DSHRHJGV7K
kind: statement
role: theorem
name: Orlov's reconstruction theorem
sources:
  - wikipedia: en:63070573@r1369241780
    locator: Derived noncommutative algebraic geometry, section Orlov's reconstruction theorem
    note: adopted
    mention: wikipedia://en/63070573#HE7D
    sections: [Statement]
inventory: [A8TEZ8TTPY]
---

## Statement

If $X$ is a smooth projective variety with ample (anti-)canonical sheaf and there is an equivalence of derived categories $F: D^b(X) \to D^b(Y)$, then there is an isomorphism of the underlying varieties.

This theorem fails in the case $X$ is Calabi–Yau, since $\omega_X \cong \mathcal{O}_X$, or is the product of a variety which is Calabi–Yau. Abelian varieties are a class of examples where a reconstruction theorem could *never* hold. If $X$ is an abelian variety and $\hat{X}$ is its dual, the Fourier–Mukai transform with kernel $\mathcal{P}$, the Poincaré bundle, gives an equivalence

$$FM_{\mathcal{P}}:D^b(X) \to D^b(\hat{X})$$

of derived categories. Since an abelian variety is generally not isomorphic to its dual, there are derived equivalent derived categories without isomorphic underlying varieties. There is an alternative theory of **tensor triangulated geometry** where we consider not only a triangulated category, but also a monoidal structure, i.e. a tensor product. This geometry has a full reconstruction theorem using the spectrum of categories.

K3 surfaces are another class of examples where reconstruction fails due to their Calabi–Yau property. There is a criterion for determining whether or not two K3 surfaces are derived equivalent: the derived category of the K3 surface $D^b(X)$ is derived equivalent to another K3 $D^b(Y)$ if and only if there is a Hodge isometry $H^2(X, \mathbb{Z}) \to H^2(Y, \mathbb{Z})$, that is, an isomorphism of Hodge structure. Moreover, this theorem is reflected in the motivic world as well, where the Chow motives are isomorphic if and only if there is an isometry of Hodge structures.

One nice application of the proof of this theorem is the identification of autoequivalences of the derived category of a smooth projective variety with ample (anti-)canonical sheaf. This is given by

$$\operatorname{Auteq}(D^b(X)) \cong (\operatorname{Pic}(X)\rtimes \operatorname{Aut}(X))\times\mathbb{Z}$$

Where an autoequivalence $F$ is given by an automorphism $f:X\to X$, then tensored by a line bundle $\mathcal{L} \in \operatorname{Pic}(X)$ and finally composed with a shift. Note that $\operatorname{Aut}(X)$ acts on $\operatorname{Pic}(X)$ via the polarization map, $g \mapsto g^*(L)\otimes L^{-1}$.
