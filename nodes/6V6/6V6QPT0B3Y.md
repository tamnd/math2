---
tag: 6V6QPT0B3Y
kind: definition
name: Ideal of an algebraic set
msc: [14A05, 13A15]
defines: HH6VEVM6Z0
uses: [VHFMQQYSTN, 0SDC934R52, 096Z9MP2ME, 437YRCNYRJ, 0PF6TM8TWT, D85VZWS9QK]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_variety
---

## Definition

Let $k$ be a field, let $n \ge 0$, and let $X \subseteq k^n$ be any subset.
The *ideal of $X$* (or vanishing ideal of $X$) is
$$I(X) = \set{f \in k[x_1, \dots, x_n] : f(a) = 0 \text{ for all } a \in X},$$
where $k[x_1, \dots, x_n]$ is the [[polynomial ring|0SDC934R52]].
It is used mostly when $X$ is an [[algebraic set|VHFMQQYSTN]].

## Remarks

$I(X)$ is an [[ideal|096Z9MP2ME]], and it equals its own [[radical|437YRCNYRJ]]: if $f^m$ vanishes at a point $a$, then $f(a)^m = 0$, so $f(a) = 0$.

Example: for the parabola $X = V(y - x^2) \subseteq k^2$ with $k$ infinite, $I(X) = (y - x^2)$.
Check: dividing $f(x, y)$ by $y - x^2$ as a polynomial in $y$ gives $f = (y - x^2) q + r(x)$; if $f$ vanishes on $X$, then $r(t) = 0$ for all $t \in k$, so $r = 0$.

Non-example: the ideal $(x^2)$ in $k[x]$ is not the ideal of any set.
It is not radical, since $x \notin (x^2)$ while $x^2 \in (x^2)$; in fact $I(V(x^2)) = I(\set{0}) = (x)$.

For an algebraic set $X$ one has $V(I(X)) = X$, and $X \subseteq Y$ if and only if $I(Y) \subseteq I(X)$.
If $k$ is [[algebraically closed|0PF6TM8TWT]], [[Hilbert's Nullstellensatz|D85VZWS9QK]] gives $I(V(J)) = \sqrt{J}$ for every ideal $J$.
So $X \mapsto I(X)$ is then an inclusion-reversing bijection from algebraic sets in $k^n$ to radical ideals of $k[x_1, \dots, x_n]$.
