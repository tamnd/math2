---
tag: SR51EVK9H0
kind: definition
name: Abelian extension
msc: [12F10, 11R20]
defines: EQDEXBWGJH
uses: [0DS2F7GK05, 0XVR72M51M, 071DDFVG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_extension
---

## Definition

Let $L/K$ be a [[Galois extension|0DS2F7GK05]] with [[Galois group|0XVR72M51M]] $\Gal(L/K)$.
The extension $L/K$ is *abelian* if $\Gal(L/K)$ is an [[abelian group|071DDFVG4J]].

## Remarks

Example: $\Q(\sqrt{2}, \sqrt{3})/\Q$ is Galois of degree $4$.
Its Galois group consists of the four maps $\sqrt{2} \mapsto \pm\sqrt{2}$, $\sqrt{3} \mapsto \pm\sqrt{3}$, which commute, so the extension is abelian.
Non-example: the splitting field $L = \Q(\sqrt[3]{2}, \omega)$ of $x^3 - 2$, with $\omega = e^{2\pi i/3}$, is Galois over $\Q$.
Its Galois group permutes the three roots of $x^3 - 2$ in all six ways, so it is isomorphic to $S_3$, which is not abelian.
Every subextension of a finite abelian extension is abelian, because every subgroup of an abelian group is normal and every quotient is abelian.
