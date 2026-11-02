---
tag: B7EFVHCEQV
kind: concept
name: Asymptotic expansion from poles of a Mellin transform
msc: [44A15, "30E15", 41A60]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Summary

The poles of the [[Mellin transform|N5PVGRJE1T]] of a function $f$ control the behaviour of $f(x)$ as $x \to 0^+$ and as $x \to \infty$.
A pole at $s = \rho$ left of the [[fundamental strip|1JAA21FHHQ]] gives a term $x^{-\rho}$ in the [[asymptotic expansion|BJQTEPEZ9G]] of $f$ near $0$.
A multiple pole adds powers of $\log x$ to this term.
Poles to the right of the strip give the expansion of $f$ near $\infty$ in the same way.
The method turns asymptotic questions about sums and integrals into the study of a [[meromorphic function|0ZZ7ZYDR8W]].
It is a basic tool in analytic number theory and in the analysis of algorithms.

## Explanations

### L1 human

The Mellin transform sends a function of $x > 0$ to a function of a complex variable $s$.
Each singular point of the transform is a fingerprint of one term of $f$: a simple pole at $s = \rho$ with residue $c$ corresponds to a term $c\, x^{-\rho}$.
To find these terms one moves the line of the inverse Mellin integral across the poles and collects the [[residues|0PHN07KVQT]].
For example, the Mellin transform of $e^{-x}$ is the [[gamma function|0H5SYBSED9]] $\Gamma(s)$.
Its poles at $s = -n$ have residues $(-1)^n / n!$, and they give back the Taylor series $e^{-x} = \sum_{n \ge 0} (-1)^n x^n / n!$.
