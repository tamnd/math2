---
tag: XT8PA31VAX
kind: concept
name: Weyl–Titchmarsh theory
msc: [34B20, 34L05, 34B24]
specializes: [7WV6B2502K]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm–Liouville_theory
---

## Summary

Weyl–Titchmarsh theory is the spectral theory of singular [[Sturm–Liouville|7WV6B2502K]] operators built on the Weyl–Titchmarsh function $m(z)$.
The function $m$ records the boundary values of the square integrable solution of $-y'' + q y = z y$ at the regular end.
It is a Herglotz function, and the measure in its integral representation is the spectral measure of the operator.
So the spectrum, the eigenfunction expansion and, by the Borg–Marchenko theorem, even the potential $q$ can be read off from $m$.
The theory goes back to Hermann Weyl and was developed by Edward Charles Titchmarsh.

## Explanations

### L1 human

For an equation on a half-line, most solutions blow up at infinity and only one direction of solutions stays square integrable.
The Weyl–Titchmarsh function is the ratio of slope to value of that good solution at the starting point.
It is one complex function of the spectral parameter, yet it carries all the spectral information of the operator.
For $-y'' = z y$ on $[0, \infty)$ the good solution is $e^{i\sqrt{z}\, x}$ and the function is $m(z) = i \sqrt{z}$.
