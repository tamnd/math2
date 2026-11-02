---
tag: 5M3THA1S6E
kind: concept
name: Fractional iteration
msc: [39B12, 26A18]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_function
---

## Summary

Fractional iteration extends the [[iterates|AYVTR2ES5B]] $f^n$ of a map $f$ from whole numbers $n$ to real numbers $t \ge 0$.
One asks for maps $f^t$ with $f^0 = \id$, $f^1 = f$ and $f^s \circ f^t = f^{s+t}$, so that $f$ becomes the time-one map of a flow.
Then $f^{1/n}$ is an [[iterative root|27C6J3YNZY]] of order $n$ of $f$.
The main tools are [[Schröder's equation|VTJV7JVJEA]] and the [[Abel equation|68SHB7Z721]], which turn iteration into multiplication or into addition.

## Explanations

### L1 human

Applying $f$ twice is easy to picture, but what does applying $f$ one and a half times mean?
Fractional iteration gives an answer: a family of maps $f^t$, one for each time $t$, that fit together like the positions of a moving object.
For $f(x) = 2x$, the natural choice is $f^t(x) = 2^t x$.
For $f(x) = x + c$, it is $f^t(x) = x + tc$.
For most maps there is no single natural choice, and one adds conditions such as continuity or analyticity in $t$.
