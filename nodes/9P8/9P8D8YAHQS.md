---
tag: 9P8D8YAHQS
kind: concept
name: Exponential type
msc: ["30D15"]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_type
same_as:
  wikidata: Q5421531
  wikipedia: Exponential type
---

## Summary

An [[entire function|0419794R0T]] is of exponential type if its modulus grows at most like $e^{\tau \abs{z}}$ for some constant $\tau$.
The least such $\tau$ is the type of the function.
Fourier and Laplace transforms of functions or measures with bounded support are of exponential type, and the Paley–Wiener theorem gives a converse.
They are the natural setting of the [[Paley–Wiener theorem|THY12GPZ8C]] and of [[Carlson's theorem|6F5B8KPEGH]].

## Explanations

### L1 human

The exponential $e^{\tau z}$ grows like $e^{\tau \abs{z}}$ in the direction where $z$ is positive real.
A function of exponential type never grows faster than this in any direction, for some fixed $\tau$.
Polynomials, $\sin z$, $\cos z$ and $e^{3z}$ are of exponential type, with types $0$, $1$, $1$ and $3$.
The function $e^{z^2}$ grows like $e^{\abs{z}^2}$ along the real axis and is not of exponential type.
