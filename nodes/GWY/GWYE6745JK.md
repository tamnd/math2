---
tag: GWYE6745JK
kind: statement
role: theorem
name: Second main theorem of Nevanlinna theory
msc: ["30D35"]
uses: [0NSD1TPHR0, YT6Z0GWS0W, 1EHH63VNAD, 0CDMXGPSES]
about: [1EHH63VNAD, YT6Z0GWS0W]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna_theory
---

## Statement

Let $f$ be a [[meromorphic function|0NSD1TPHR0]] on $\C$ that is not constant, with [[Nevanlinna characteristic|YT6Z0GWS0W]] $T(r, f)$.
Let $q \ge 3$, and let $a_1, \dots, a_q$ be distinct points of the [[Riemann sphere|0CDMXGPSES]] $\C \cup \set{\infty}$.
For $a$ in the Riemann sphere, let $\overline{N}(r, a)$ be the counting function of the solutions of $f(z) = a$ counted without multiplicity, as in [[Nevanlinna theory|1EHH63VNAD]].
Then there is a set $E \subseteq (0, \infty)$ of finite Lebesgue measure such that
$$(q - 2)\, T(r, f) \le \sum_{j=1}^{q} \overline{N}(r, a_j) + S(r, f) \qquad (r \notin E),$$
where $S(r, f) = O\big(\log T(r, f) + \log r\big)$ as $r \to \infty$ outside $E$.

## Remarks

The proof rests on the lemma on the logarithmic derivative, which says that the mean of $\log^+ \abs{f'/f}$ on the circle $\abs{z} = r$ is small compared with $T(r, f)$ outside an exceptional set.
If $f$ is not rational, then $\log r = o(T(r, f))$, so $S(r, f) = o(T(r, f))$ outside $E$.
If $f$ has finite order, the exceptional set $E$ can be omitted.
For transcendental $f$, dividing by $T(r, f)$ and using the [[first main theorem|QJWCFAK4AK]] gives the defect relation $\sum_a \delta(a) \le 2$, where the sum runs over all points of the Riemann sphere.
For example, $e^z$ has $\delta(0) = \delta(\infty) = 1$, so the relation is sharp.

## Explanations

### L1 human

The first main theorem says that no value is taken too often.
The second main theorem says the opposite for almost all values: a meromorphic function takes nearly every value about as often as its growth allows.
At most two values can be strongly avoided.
This is a quantitative form of Picard's theorem.

### L2 human

[[Picard's little theorem|R2PHM118NG]] follows at once: if a transcendental meromorphic $f$ omitted three values, the right side would be $S(r, f) = o(T(r, f))$ while the left side is at least $T(r, f)$.
The theorem also implies that the set of values $a$ with $\delta(a) > 0$ is countable.
Counting without multiplicity yields results on ramification, such as bounds on the number of totally ramified values.
[[Ahlfors theory|M8611CV76A]] gives a geometric proof of a similar inequality, based on covering surfaces.
