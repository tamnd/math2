---
tag: 4XYXDYXQZR
kind: definition
name: Darboux integral
msc: [26A42]
defines: F961Q88FHK
uses: [0QRQVH0CRW, 09FQT057T7, 069P20KYQT]
sources:
  - url: https://en.wikipedia.org/wiki/Darboux_integral
---

## Definition

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a bounded function.
For a [[partition|069P20KYQT]] $P$ given by $a = x_0 < x_1 < \cdots < x_n = b$, let $M_i = \sup_{[x_{i-1}, x_i]} f$ and $m_i = \inf_{[x_{i-1}, x_i]} f$, and form the [[upper and lower Darboux sums|0QRQVH0CRW]]
$$U(f, P) = \sum_{i=1}^{n} M_i (x_i - x_{i-1}), \qquad L(f, P) = \sum_{i=1}^{n} m_i (x_i - x_{i-1}).$$
The [[upper and lower Darboux integrals|09FQT057T7]] are $\overline{I}(f) = \inf_P U(f, P)$ and $\underline{I}(f) = \sup_P L(f, P)$.
The function $f$ is *Darboux integrable* on $[a, b]$ if $\overline{I}(f) = \underline{I}(f)$.
Its *Darboux integral* $\int_a^b f(x)\, dx$ is then this common value.

## Remarks

Example: $f(x) = x$ on $[0, 1]$.
For the partition $P_n$ into $n$ equal parts, $U(f, P_n) - L(f, P_n) = \sum_{i=1}^{n} \frac1n \cdot \frac1n = \frac1n$, so the two Darboux integrals agree, and the integral is $\lim_n U(f, P_n) = \lim_n \frac{n+1}{2n} = \frac12$.

Non-example: the [[Dirichlet function|03Z4JC4YRJ]], equal to $1$ on rationals and $0$ on irrationals in $[0, 1]$.
Every subinterval contains both kinds of numbers, so $U(f, P) = 1$ and $L(f, P) = 0$ for every $P$, and the Darboux integrals $1$ and $0$ differ.

Riemann's criterion: $f$ is Darboux integrable if and only if for every $\varepsilon > 0$ there is a partition $P$ with $U(f, P) - L(f, P) < \varepsilon$.
A bounded function is Darboux integrable exactly when it is [[Riemann integrable|0N1JQXZXHC]], with the same integral.
