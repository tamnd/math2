---
tag: EAQDSQD4DW
kind: concept
name: Lerch zeta function
msc: ["11M35", "33B30"]
sources:
  - url: https://en.wikipedia.org/wiki/Lerch_transcendent
---

## Summary

The Lerch zeta function is the series $\sum_{n \ge 0} e^{2\pi i \lambda n} (n + \alpha)^{-s}$, a generalized [[Dirichlet series|8MWTEF6462]] with a phase factor and a shift.
In the closely related form $\Phi(z, s, a) = \sum_{n \ge 0} z^n (n + a)^{-s}$ it is called the Lerch transcendent.
It contains the [[Hurwitz zeta function|G4SW7HJG88]], the [[Riemann zeta function|1XWBY4N0VT]], and the [[polylogarithm|96CHDZKGQ0]] as special cases.
Dirichlet $L$-functions are finite linear combinations of its values.
So identities proved for it hold for all of them at once.

## Explanations

### L1 human

The Riemann zeta function adds up $1/n^s$.
The Hurwitz zeta function shifts the integers to $n + \alpha$, and the polylogarithm weights the terms by powers $z^n$.
The Lerch zeta function does both: it adds up $z^n / (n + \alpha)^s$.
For instance, with $z = -1$, $\alpha = 1$ and $s = 1$, the sum is $1 - \frac12 + \frac13 - \cdots = \log 2$.
