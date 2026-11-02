---
tag: 95QBBPRJ9E
kind: concept
name: Besov space
msc: ["46E35", 42B35]
sources:
  - url: https://en.wikipedia.org/wiki/Besov_space
same_as:
  wikidata: Q526261
  wikipedia: Besov space
---

## Summary

A Besov space $B^s_{p,q}(\R^n)$ is a space of functions or [[tempered distributions|AES2T5JPFP]] that measures smoothness of order $s$ in the $L^p$ sense.
A third index $q$ gives a fine tuning.
It is defined by cutting the [[Fourier transform|DPVM34ADZV]] of a function into dyadic frequency shells and measuring each piece in $L^p$.
Besov spaces contain many classical spaces, such as Hölder spaces and fractional Sobolev spaces, and they are stable under real [[interpolation|VX1R6FN6PS]].
They appear naturally as spaces of boundary values of Sobolev functions and in the study of nonlinear evolution equations.

## Explanations

### L1 human

A function can be split into pieces that oscillate at frequencies of size about $1, 2, 4, 8, \ldots$.
Smoothness means that the high-frequency pieces are small.
The Besov norm asks that the piece at frequency $2^j$ be smaller than $2^{-js}$ in the $L^p$ sense, in a summable way controlled by $q$.
For $p = q = 2$ this is the familiar condition $\int (1 + \abs{\xi}^2)^s \abs{\hat f(\xi)}^2 \, d\xi < \infty$ on the Fourier transform.
