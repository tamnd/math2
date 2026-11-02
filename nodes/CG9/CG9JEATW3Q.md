---
tag: CG9JEATW3Q
kind: concept
name: Schwartz space
msc: [46F05, "46E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Schwartz_space
same_as:
  wikidata: Q1369621
  wikipedia: Schwartz space
---

## Summary

The Schwartz space $\mathcal{S}(\R^n)$ is the space of smooth functions on $\R^n$ that, together with all their derivatives, decay faster than any power of $1/\abs{x}$.
The [[Fourier transform|DPVM34ADZV]] maps it bijectively onto itself, which makes it the natural home of Fourier analysis on $\R^n$.
Its dual space is the space of [[tempered distributions|AES2T5JPFP]].
See the [[definition|GE020MY43M]].

## Explanations

### L1 human

A Schwartz function is smooth and dies off very fast at infinity, and so do all its derivatives.
The bell curve $e^{-x^2}$ is the basic example: it decays faster than $1/x^{100}$ or any other power.
The function $1/(1 + x^2)$ is smooth but decays only like $1/x^2$, so it is not a Schwartz function.
The point of the space is that differentiation, multiplication by polynomials and the Fourier transform never lead out of it.
