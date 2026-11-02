---
tag: 3XNJ04AMCW
kind: definition
name: Lerch zeta function
msc: ["11M35", "33B30"]
defines: EAQDSQD4DW
uses: [8MWTEF6462, G4SW7HJG88, 96CHDZKGQ0]
sources:
  - url: https://en.wikipedia.org/wiki/Lerch_transcendent
---

## Definition

Let $\lambda \in \R$, let $\alpha$ be a real number with $0 < \alpha \le 1$, and let $s \in \C$.
The *Lerch zeta function* is the generalized [[Dirichlet series|8MWTEF6462]]
$$L(\lambda, \alpha, s) = \sum_{n=0}^{\infty} \frac{e^{2\pi i \lambda n}}{(n + \alpha)^s}.$$
It converges for $\operatorname{Re} s > 1$, and also for $\operatorname{Re} s > 0$ when $\lambda \notin \Z$.

## Remarks

The *Lerch transcendent* is $\Phi(z, s, a) = \sum_{n \ge 0} z^n (n + a)^{-s}$, defined for $\abs{z} < 1$ and $a \notin \set{0, -1, -2, \ldots}$, and for $\abs{z} = 1$ when $\operatorname{Re} s > 1$.
The two are related by $L(\lambda, \alpha, s) = \Phi(e^{2\pi i \lambda}, s, \alpha)$.

Example: for $\lambda \in \Z$ every phase factor is $1$, so $L(\lambda, \alpha, s) = \zeta(s, \alpha)$ is the [[Hurwitz zeta function|G4SW7HJG88]], and $L(0, 1, s) = \zeta(s)$.
With $a = 1$ the transcendent gives the [[polylogarithm|96CHDZKGQ0]]: $z \, \Phi(z, s, 1) = \sum_{n \ge 0} z^{n+1} / (n+1)^s = \operatorname{Li}_s(z)$.

Non-example: $\lambda = 0$, $\alpha = 1$, $s = 1$ gives the harmonic series $\sum 1/(n+1)$, which diverges; the condition $\operatorname{Re} s > 1$ is needed when $\lambda \in \Z$.
For $\lambda = \frac12$ and the same $\alpha, s$, the series is $1 - \frac12 + \frac13 - \cdots = \log 2$, which converges.

As a function of $s$, $L(\lambda, \alpha, s)$ extends to a meromorphic function on $\C$; for $\lambda \notin \Z$ it is entire.
