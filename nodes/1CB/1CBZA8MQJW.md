---
tag: 1CBZA8MQJW
kind: concept
name: Ramanujan theta function
msc: [11F27, 33D15]
specializes: [2F5CYQJVAF]
sources:
  - url: https://en.wikipedia.org/wiki/Ramanujan_theta_function
same_as:
  wikidata: Q2630765
  wikipedia: Ramanujan theta function
---

## Summary

Ramanujan's general theta function is $f(a, b) = \sum_{n \in \Z} a^{n(n+1)/2} b^{n(n-1)/2}$ for complex $a, b$ with $\abs{ab} < 1$.
It is a two-variable form of the Jacobi [[theta function|2F5CYQJVAF]], symmetric in $a$ and $b$.
By the [[Jacobi triple product|JFP2DGMNXT]] it is an infinite product.
Its special cases $\varphi(q)$, $\psi(q)$ and $f(-q)$ are the theta functions that Ramanujan used for partitions and modular equations.

## Explanations

### L1 human

The function $f(a, b)$ is a sum over all integers $n$, where positive $n$ mostly use powers of $a$ and negative $n$ mostly use powers of $b$.
Choosing $a$ and $b$ as powers of one variable $q$ gives famous series.
For example, $f(q, q) = \sum_{n \in \Z} q^{n^2} = 1 + 2q + 2q^4 + 2q^9 + \cdots$, where each square $n^2 > 0$ appears twice, once for $n$ and once for $-n$.
Its square counts the ways to write a number as a sum of two squares.
