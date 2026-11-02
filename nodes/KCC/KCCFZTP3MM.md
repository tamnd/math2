---
tag: KCCFZTP3MM
kind: statement
role: theorem
name: Van Vleck's theorem
msc: [40A15, 30B70]
uses: [0BK6JBK58W, 0SRWNR42BQ, 070PFSYJJR]
about: [04P2RJ4WPS]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_problem
---

## Statement

Let $0 < \varepsilon < \pi/2$ and let $a_1, a_2, \dots$ be complex numbers with $\abs{\arg a_n} < \pi/2 - \varepsilon$ for every $n$.
Let $f_n$ be the $n$-th [[convergent|0SRWNR42BQ]] of the [[continued fraction|0BK6JBK58W]]
$$f = \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \cdots}}}.$$
Then:

1. every $f_n$ is finite and satisfies $\abs{\arg f_n} < \pi/2 - \varepsilon$;
2. the sequences $(f_{2n})$ and $(f_{2n+1})$ of even and odd convergents both converge;
3. the continued fraction converges, that is, $(f_n)$ has a finite limit, if and only if $\sum_{n \ge 1} \abs{a_n}$ diverges.

## Remarks

Item 1 follows by induction from the tail: the open sector $S = \set{z \ne 0 : \abs{\arg z} < \pi/2 - \varepsilon}$ is closed under addition, and $z \mapsto 1/z$ maps $S$ onto itself.
Here $\arg$ is the [[argument|070PFSYJJR]] with values in $(-\pi, \pi]$.
Example: $a_n = 1$ for all $n$ lies in the sector and $\sum \abs{a_n} = \infty$, so the continued fraction converges; its value is $\frac{\sqrt5 - 1}{2}$.
If $a_n = 2^{-n}$, the sum $\sum \abs{a_n}$ is finite, and by item 3 the even and odd convergents tend to different limits.
For positive real $a_n$ the theorem contains the classical criterion that $\cfrac{1}{a_1 + \cfrac{1}{a_2 + \cdots}}$ converges exactly when $\sum a_n$ diverges.

## Explanations

### L1 human

The theorem treats continued fractions whose partial denominators all point into a fixed wedge around the positive real axis.
Then the fraction converges exactly when these denominators are not too small in total, that is, when the sum of their sizes is infinite.

### L2 human

The sector condition keeps all convergents away from $0$ and $\infty$, so only the oscillation between even and odd convergents can prevent convergence.
The divergence of $\sum \abs{a_n}$ is what forces the even and odd limits to meet.
Compare the [[Śleszyński–Pringsheim theorem|NEC48RHNN0]], where large partial denominators give convergence.
