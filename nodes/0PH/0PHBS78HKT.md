---
tag: 0PHBS78HKT
kind: statement
role: theorem
name: First supplement to quadratic reciprocity
msc: [11A15]
uses: [01J8AMV9RS, 0M7DEDKSYB]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_reciprocity
    locator: q = ±1 and the first supplement
---

## Statement

Let $p$ be an odd prime.
Then
$$\left(\frac{-1}{p}\right) = (-1)^{(p-1)/2},$$
where the left side is a [[Legendre symbol|01J8AMV9RS]].

## Remarks

So $\left(\frac{-1}{p}\right) = 1$ if $p \equiv 1 \pmod 4$, and $\left(\frac{-1}{p}\right) = -1$ if $p \equiv 3 \pmod 4$.
The proof is [[Euler's criterion|0M7DEDKSYB]] with $a = -1$.
For example, $2^2 = 4 \equiv -1 \pmod 5$, but $-1$ is not a square modulo $7$.

## Explanations

### L1 human

The number $-1$ is a square modulo an odd prime $p$ exactly when $p$ leaves remainder $1$ on division by $4$.
So $-1$ is a square modulo $5$, $13$ and $17$, but not modulo $3$, $7$ and $11$.
