---
tag: WM62GKCBWN
kind: concept
name: Nonstandard analysis
msc: ["26E35", "03H05"]
sources:
  - url: https://en.wikipedia.org/wiki/Nonstandard_analysis
same_as:
  wikidata: Q1503766
  wikipedia: Nonstandard analysis
---

## Summary

Nonstandard analysis is a way of doing analysis with genuine infinitesimal and infinite numbers.
Abraham Robinson founded it in the 1960s, using model theory to build an ordered field of [[hyperreal numbers|421QMTFG9T]] that extends the [[real numbers|08J2M1JYAG]].
The [[transfer principle|3RT74FQYG1]] lets first-order statements pass between the reals and the hyperreals.
The [[standard part function|1ZBY4W4E81]] rounds a finite hyperreal to the nearest real.
With these tools, limits, derivatives and integrals get short definitions close to the intuition of Leibniz.
The theory proves the same theorems about real numbers as ordinary analysis.
An axiomatic version is Nelson's [[internal set theory|V0PGBXYJ9R]].

## Explanations

### L1 human

The founders of calculus spoke of infinitely small quantities, but for a long time no one could make this precise.
Nonstandard analysis makes it precise: there is a larger number system with positive numbers smaller than every positive real.
For example, to differentiate $f(x) = x^2$, take an infinitesimal $\varepsilon \ne 0$.
Then $(f(x + \varepsilon) - f(x)) / \varepsilon = 2x + \varepsilon$, and rounding away the infinitesimal gives $f'(x) = 2x$.
