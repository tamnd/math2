---
tag: NX1JQMFC4F
kind: concept
name: Morrey–Campanato space
msc: ["46E30", 42B35, "46E35"]
sources:
  - url: https://en.wikipedia.org/wiki/Morrey%E2%80%93Campanato_space
same_as:
  wikidata: Q6913505
  wikipedia: Morrey–Campanato space
---

## Summary

Morrey spaces and Campanato spaces measure the size of a function on small balls, uniformly over all centres.
A Morrey space asks that the $L^p$ mass of $f$ on a ball of radius $r$ is at most a constant times $r^\lambda$.
A Campanato space asks the same of the oscillation of $f$ around its mean on the ball.
Special cases are [[Lebesgue spaces|SASP14MA1Z]], [[bounded mean oscillation|QJYTXFT8Y4]] and [[Hölder continuous|012PBA0FMD]] functions.
They are a basic tool for the regularity of solutions of elliptic equations.

## Explanations

### L1 human

Take a function and look at it through a small round window of radius $r$.
Measure how much of the function you see, or how much it varies, inside the window.
If this amount shrinks like a power $r^\lambda$ as the window gets smaller, wherever you put it, the function lies in the Morrey or Campanato space with exponent $\lambda$.
A larger $\lambda$ means a tamer function.
For instance, a function with a mild spike such as $\abs{x}^{-a}$ is still allowed for small enough $\lambda$.
