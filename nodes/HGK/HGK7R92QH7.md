---
tag: HGK7R92QH7
kind: definition
name: Hilbert class field
msc: [11R37, 11R29]
defines: WWCJ7CR2R3
uses: [MWBDFS2KJ5, 0QMZAQ6QQ4, 082GHNPJ53, H5RC67SD24, BT5V3TSNY6, WQ46BD3ARY, 7938EKMMVR, E0VZTNPJXA]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_class_field
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] and fix an algebraic closure $\overline{K}$ of $K$.
A finite extension $L/K$ is *unramified at every place* if two conditions hold.
Every nonzero prime ideal of $\mathcal{O}_K$ is [[unramified|H5RC67SD24]] in $L$.
Every real embedding of $K$ extends only to real embeddings of $L$.
Consider the finite [[Galois extensions|0QMZAQ6QQ4]] $L/K$ in $\overline{K}$ with [[abelian|082GHNPJ53]] Galois group that are unramified at every place.
The *Hilbert class field* of $K$ is the compositum $H \subseteq \overline{K}$ of all these fields $L$.

## Remarks

By class field theory, $H/K$ is a finite abelian extension, unramified at every place, and the [[Artin map|7938EKMMVR]] gives an isomorphism from the [[ideal class group|WQ46BD3ARY]] $\mathrm{Cl}(K)$ onto $\Gal(H/K)$.
So $[H : K] = h_K$, and a prime ideal of $\mathcal{O}_K$ splits completely in $H$ if and only if it is principal.
Every ideal of $\mathcal{O}_K$ becomes principal in $\mathcal{O}_H$ (the principal ideal theorem).

Example: $K = \Q(\sqrt{-5})$ and $L = K(i) = \Q(\sqrt{-5}, i)$.
The three quadratic subfields of $L$ are $\Q(i)$, $\Q(\sqrt{5})$ and $\Q(\sqrt{-5})$, with [[discriminants|E0VZTNPJXA]] $-4$, $5$ and $-20$, so $d_L = (-4) \cdot 5 \cdot (-20) = 400 = d_K^2$.
Hence the relative discriminant of $L/K$ has norm $1$ and no finite prime ramifies; $K$ has no real embedding, so $L/K$ is unramified at every place.
Since $h_K = 2 = [L : K]$, the field $L$ is the Hilbert class field of $K$.

Non-example: $L' = \Q(\sqrt{-5}, \sqrt{2})$ is abelian of degree $2$ over $K$ but not unramified.
Its quadratic subfields have discriminants $8$, $-20$ and $-40$, so $d_{L'} = 6400 = 16 \, d_K^2$, and some prime of $K$ above $2$ ramifies in $L'$.
