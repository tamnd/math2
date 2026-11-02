---
tag: FQYSKP388T
kind: concept
name: Elliptic hypergeometric series
msc: [33D15, "33E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_hypergeometric_series
same_as:
  wikidata: Q5365800
  wikipedia: Elliptic hypergeometric series
---

## Summary

An elliptic hypergeometric series is a series $\sum c_n$ in which the ratio $c_{n+1}/c_n$ is an [[elliptic function|FF9ZPCZ59K]] of $n$.
In ordinary [[hypergeometric series|428M453CR2]] the ratio is a rational function of $n$.
In [[basic hypergeometric series|EB4N9RQR51]] it is a rational function of $q^n$, and the elliptic case is the next step.
The terms are built from theta functions in place of the factors $1 - aq^k$.
Setting the elliptic nome $p$ to $0$ gives back basic hypergeometric series.

## Explanations

### L1 human

Many classical series are built so that each term is the previous one times a simple factor.
For hypergeometric series the factor is a fraction of polynomials in the index $n$.
For elliptic hypergeometric series the factor is a doubly periodic function of $n$, made from theta functions.
In the theta-function notation, putting the extra parameter $p$ equal to $0$ turns every theta factor $\theta(x; p)$ into $1 - x$, and the series becomes a familiar $q$-series.
So elliptic hypergeometric series are a common generalization of the classical and the $q$-series.
