---
tag: YYE2JHRR32
kind: definition
name: Kirby–Siebenmann class
msc: [57Q25, 57N55]
defines: E4NJER1RFQ
uses: [QQQ9B1DK4P, 15MKGRNM9K, 6N7BC70CX0, P976WYEFMB]
sources:
  - url: https://en.wikipedia.org/wiki/Kirby%E2%80%93Siebenmann_class
---

## Definition

Let $M$ be a [[topological manifold|QQQ9B1DK4P]].
Let $\mathrm{TOP}$ and $\mathrm{PL}$ be the stable groups of homeomorphisms and of piecewise linear homeomorphisms of Euclidean spaces, with classifying spaces $B\mathrm{TOP}$ and $B\mathrm{PL}$.
The stable tangent microbundle of $M$ has a classifying map $\tau_M \colon M \to B\mathrm{TOP}$.
The forgetful map $B\mathrm{PL} \to B\mathrm{TOP}$ is a fibration up to homotopy, with fibre $\mathrm{TOP}/\mathrm{PL}$.
By a theorem of Kirby and Siebenmann, $\mathrm{TOP}/\mathrm{PL}$ is an Eilenberg–MacLane space $K(\Z/2, 3)$: its only nonzero [[homotopy group|P976WYEFMB]] is $\pi_3 \cong \Z/2$.
The *Kirby–Siebenmann class* $\operatorname{ks}(M) \in H^4(M; \Z/2)$ is the obstruction class, in [[singular cohomology|6N7BC70CX0]] with coefficients $\pi_3(\mathrm{TOP}/\mathrm{PL}) \cong \Z/2$, to lifting $\tau_M$ to a map $M \to B\mathrm{PL}$.

## Remarks

The $4$-dimensional $E_8$ manifold $M_{E_8}$ has $\operatorname{ks}(M_{E_8}) \ne 0$ in $H^4(M_{E_8}; \Z/2) \cong \Z/2$.
For a closed simply connected topological $4$-manifold with even intersection form, $\operatorname{ks}$ is the signature divided by $8$, taken modulo $2$, and the $E_8$ form has signature $8$.

A space that is not a manifold, such as a finite graph with a vertex of degree three, has no tangent microbundle, so the definition does not apply to it.

If $M$ has a [[piecewise linear structure|15MKGRNM9K]], or a smooth structure, then $\operatorname{ks}(M) = 0$.
Conversely, if $\dim M \ge 5$ and $\operatorname{ks}(M) = 0$, then $M$ has a piecewise linear structure; for any $M$, $\operatorname{ks}(M) = 0$ if and only if $M \times \R$ has one.
The class is natural: for an open subset $U \subseteq M$, $\operatorname{ks}(U)$ is the restriction of $\operatorname{ks}(M)$.
