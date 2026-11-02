---
tag: 1PDGBGEHM2
kind: concept
name: Barnes integral
msc: [33C60, 33C05, "30E20"]
sources:
  - url: https://en.wikipedia.org/wiki/Barnes_integral
same_as:
  wikidata: Q4201931
  wikipedia: Barnes integral
---

## Summary

A Barnes integral, also called a Mellin–Barnes integral, is a kind of [[contour integral|06ZGPYTWK8]].
Its integrand is a quotient of products of values of the [[gamma function|0H5SYBSED9]], times a power $z^{-s}$.
The path runs from $-i\infty$ to $+i\infty$ and separates two families of poles of the integrand.
Many special functions, such as the [[hypergeometric function|463X5V31D9]], have such an integral as a representation.
Closing the path to the left or to the right and summing residues turns the integral into a series.
This gives convergent series and asymptotic expansions.

## Explanations

### L1 human

The gamma function has poles at $0, -1, -2, \dots$, and a Barnes integral is built so that these poles sit on known sides of a vertical path.
When one pushes the path far to one side, the [[residue theorem|032HKYS329]] collects one term of a series at each pole that the path crosses.
So a single integral can stand for a power series near $z = 0$ and for another expansion near $z = \infty$.
The smallest example is $\frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \Gamma(s)\, x^{-s}\, ds$ with $c > 0$ and $x > 0$.
The poles of $\Gamma(s)$ at $s = -n$ have residues $(-1)^n / n!$, and their sum gives $e^{-x}$.
