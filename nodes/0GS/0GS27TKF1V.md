---
tag: 0GS27TKF1V
kind: definition
name: Completely multiplicative function
aliases: [totally-multiplicative-function]
msc: [11A25]
defines: 0RXKW044R4
uses: [0H2EPRZC0D, 0AP80TT660]
sources:
  - url: https://en.wikipedia.org/wiki/Completely_multiplicative_function
    locator: Definition
---

## Definition

An [[arithmetic function|0H2EPRZC0D]] $f$ is completely multiplicative if $f(1) = 1$ and $f(mn) = f(m) f(n)$ for all positive integers $m$ and $n$.

## Remarks

Each completely multiplicative function is [[multiplicative|0AP80TT660]]. The converse fails: [[Euler's totient function|0VV04M41AN]] has $\varphi(4) = 2$ but $\varphi(2)^2 = 1$.
A completely multiplicative function is determined by its values at the primes.
Examples are $n \mapsto n^k$, the [[Liouville function|08RQAPXF1T]] and, for a fixed odd prime $p$, the [[Legendre symbol|01J8AMV9RS]] $n \mapsto \left(\frac{n}{p}\right)$.

## Explanations

### L1 human

A completely multiplicative function respects every product, not only products of coprime numbers.
So it is enough to know its values at the primes, as for the function $n \mapsto n^2$.
