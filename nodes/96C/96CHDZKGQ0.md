---
tag: 96CHDZKGQ0
kind: concept
name: Polylogarithm
msc: ["33B30", "11G55"]
sources:
  - url: https://en.wikipedia.org/wiki/Polylogarithm
same_as:
  wikidata: Q1238449
  wikipedia: Polylogarithm
---

## Summary

The polylogarithm $\operatorname{Li}_s(z)$ is the power series $\sum_{k \ge 1} \frac{z^k}{k^s}$ and its [[analytic continuation|0M3YQJ81NB]].
For $s = 1$ it is $-\ln(1 - z)$, which explains the name, and for $\operatorname{Re} s > 1$ its value at $z = 1$ is the [[Riemann zeta function|1XWBY4N0VT]] $\zeta(s)$.
The case $s = 2$ is the [[dilogarithm|G0X0NWSDB7]].
Polylogarithms appear in number theory, in algebraic K-theory, in quantum field theory and in the statistics of Fermi and Bose gases.

## Explanations

### L1 human

The series $z + \frac{z^2}{2} + \frac{z^3}{3} + \cdots$ adds up to $-\ln(1 - z)$.
Dividing the $k$-th term by $k$ once more, or $s$ times in all, gives the polylogarithm of order $s$.
Each step is the same as integrating the previous function after dividing by $z$.
For $z = 1$ and $s = 2$ one gets $1 + \frac14 + \frac19 + \cdots = \frac{\pi^2}{6}$.
