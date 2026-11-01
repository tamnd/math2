---
tag: H5YX5B7GVM
kind: concept
name: Separable degree
msc: [12F10, 12F15]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_extension
---

## Summary

The separable degree $[L:K]_s$ of an algebraic extension $L/K$ counts the embeddings of $L$ into an [[algebraically closed field|0PF6TM8TWT]].
Only the embeddings that extend a fixed embedding of $K$ are counted.
For a finite extension it divides the [[degree|0EAJ2XXADC]] $[L:K]$, and the quotient is a power of the characteristic exponent, called the inseparable degree.
It equals $[L:K]$ exactly when $L/K$ is [[separable|0WCX7NB4N7]], and it equals the degree of the [[separable closure|JJ91A1V8NQ]] of $K$ in $L$.
It measures how much of an extension is visible to Galois theory.

## Explanations

### L1 human

The degree of an extension counts dimensions.
The separable degree counts the distinct ways to place the extension inside a big field such as $\C$.
For $\Q(\sqrt{2})$ there are two ways, sending $\sqrt{2}$ to $\sqrt{2}$ or to $-\sqrt{2}$, and the degree is also $2$.
In characteristic $p$, the extension of $\F_p(t)$ by a $p$-th root of $t$ has degree $p$ but only one placement, because $x^p - t$ has only one root.
So its separable degree is $1$.
