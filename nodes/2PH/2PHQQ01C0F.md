---
tag: 2PHQQ01C0F
kind: definition
name: Rectifiable set
msc: [28A75, 49Q15]
defines: 7N0GFMW05R
uses: [Q1TGZK8RN6, 0TMZ21WKCN]
sources:
  - url: https://en.wikipedia.org/wiki/Rectifiable_set
    locator: Definition
---

## Definition

Let $n$ and $m$ be integers with $1 \le m \le n$, and let $\mathcal{H}^m$ be the $m$-dimensional [[Hausdorff measure|Q1TGZK8RN6]] on $\R^n$.
A set $E \subseteq \R^n$ is *$m$-rectifiable* if there are [[Lipschitz maps|0TMZ21WKCN]] $f_i \colon \R^m \to \R^n$, for $i = 1, 2, \dots$, such that
$$\mathcal{H}^m\Big(E \setminus \bigcup_{i=1}^{\infty} f_i(\R^m)\Big) = 0.$$
A set $E \subseteq \R^n$ is *purely $m$-unrectifiable* if $\mathcal{H}^m(E \cap F) = 0$ for every $m$-rectifiable set $F \subseteq \R^n$.

## Remarks

This is the countable rectifiability of Federer and Mattila.
Some authors also require $\mathcal{H}^m(E) < \infty$, or use $C^1$ maps instead of Lipschitz maps; the second change gives the same class of sets.
Example: the unit circle $S \subseteq \R^2$ is $1$-rectifiable, since the Lipschitz map $f(t) = (\cos t, \sin t)$ satisfies $f(\R) = S$.
Non-example: the unit square $Q = [0,1]^2$ is not $1$-rectifiable.
Each set $f_i(\R)$ has $\sigma$-finite $\mathcal{H}^1$ measure, so it has Lebesgue measure zero in $\R^2$.
Hence $Q \setminus \bigcup_i f_i(\R)$ has positive area, and so its $\mathcal{H}^1$ measure is infinite, not zero.
The image of a [[rectifiable curve|0HATW2VWAZ]] is $1$-rectifiable.
