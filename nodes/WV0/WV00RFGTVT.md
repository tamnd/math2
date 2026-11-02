---
tag: WV00RFGTVT
kind: definition
name: Rogers–Ramanujan continued fraction
msc: [11A55, 11P84, "11F03"]
defines: 7A68BZR6QS
uses: [04P2RJ4WPS, X6XGGH5FPW]
sources:
  - url: https://en.wikipedia.org/wiki/Rogers–Ramanujan_continued_fraction
---

## Definition

Let $\tau$ be in the [[upper half-plane|X6XGGH5FPW]], let $q = e^{2\pi i \tau}$, and let $q^{1/5} = e^{2\pi i \tau / 5}$.
The *Rogers–Ramanujan continued fraction* is
$$R(\tau) = \cfrac{q^{1/5}}{1 + \cfrac{q}{1 + \cfrac{q^2}{1 + \cfrac{q^3}{1 + \cdots}}}},$$
the limit of the finite [[continued fractions|04P2RJ4WPS]] obtained by stopping after the term $q^n$, as $n \to \infty$.

## Remarks

Since $\abs{q} < 1$ the limit exists, and Rogers and Ramanujan showed
$$R(\tau) = q^{1/5} \prod_{n=1}^{\infty} \frac{(1 - q^{5n-1})(1 - q^{5n-4})}{(1 - q^{5n-2})(1 - q^{5n-3})} = q^{1/5}\, \frac{H(q)}{G(q)},$$
with $G(q) = \sum_{n \ge 0} \frac{q^{n^2}}{(q; q)_n}$ and $H(q) = \sum_{n \ge 0} \frac{q^{n^2 + n}}{(q; q)_n}$, the two sides of the [[Rogers–Ramanujan identities|M24H4GJPPW]].

Example: $\tau = i$, so $q = e^{-2\pi} \approx 0.001867$.
Then $R(i) = \sqrt{\frac{5 + \sqrt5}{2}} - \frac{1 + \sqrt5}{2} \approx 0.284079$.
A numerical check: $q^{1/5} = e^{-2\pi/5} \approx 0.284609$, and the continued fraction $1 + q/(1 + q^2/(1 + \cdots))$ is about $1.001867$, whose quotient is about $0.284079$.

Non-example: with numerators $1, 1, 1, \dots$ instead of $q, q^2, q^3, \dots$, the fraction $\cfrac{1}{1 + \cfrac{1}{1 + \cdots}}$ is $\frac{\sqrt5 - 1}{2}$, the inverse of the golden ratio, and it does not depend on $q$; it is not $R$.

Another common notation is $R(q)$ in place of $R(\tau)$.
