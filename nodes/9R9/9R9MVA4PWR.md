---
tag: 9R9MVA4PWR
kind: definition
name: Injective object
msc: [18G05]
defines: 5QRFTBF4PG
uses: [A2DE66937D, 859F0TFVA3, Y2NP1JFR86, VJXS8AK67E, Y9CZ3MTNF1, 85H7PRHDPZ, ZXVBEPMTCN]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_object
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
An object $I$ of $\mathcal{C}$ is *injective* if, for every [[monomorphism|Y2NP1JFR86]] $m \colon A \to B$ and every [[morphism|859F0TFVA3]] $f \colon A \to I$, there is a morphism $g \colon B \to I$ with $g \circ m = f$.

## Remarks

Equivalently, the contravariant [[hom functor|VJXS8AK67E]] $\Hom(-, I)$ sends monomorphisms to surjections of sets.
In an [[abelian category|Y9CZ3MTNF1]], $I$ is injective if and only if $\Hom(-, I)$ is exact, and if and only if every short exact sequence $0 \to I \to B \to C \to 0$ splits.
In the category of modules over a ring, the injective objects are the [[injective modules|85H7PRHDPZ]].
An injective object of $\mathcal{C}$ is the same as a projective object of the opposite category.

Example: $\Q$ is injective in the category of abelian groups.
It is a [[divisible group|ZXVBEPMTCN]], and by Baer's criterion a divisible abelian group is injective: a map $f \colon n\Z \to \Q$ extends to $\Z$ by sending $1$ to $f(n)/n$.

Non-example: $\Z$ is not injective in the category of abelian groups.
For $m \colon \Z \to \Z$, $m(x) = 2x$, and $f = 1_{\Z}$, an extension $g$ would need $2 g(1) = g(m(1)) = f(1) = 1$, which has no solution in $\Z$.
