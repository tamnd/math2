---
tag: 0NW1JP7TBR
kind: statement
role: theorem
name: Multiplicativity of the Legendre symbol
msc: [11A15]
uses: [01J8AMV9RS, 0M7DEDKSYB]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_symbol
    locator: Properties of the Legendre symbol
---

## Statement

Let $p$ be an odd prime, and let $a$ and $b$ be integers.
Then
$$\left(\frac{ab}{p}\right) = \left(\frac{a}{p}\right) \left(\frac{b}{p}\right),$$
where the symbols are [[Legendre symbols|01J8AMV9RS]].

## Remarks

The proof follows from [[Euler's criterion|0M7DEDKSYB]], because $(ab)^{(p-1)/2} = a^{(p-1)/2} b^{(p-1)/2}$.
In words: modulo $p$, the product of two nonresidues is a residue, and the product of a residue and a nonresidue is a nonresidue.
For example, $3$ and $5$ are nonresidues modulo $7$, and $15 \equiv 1 \pmod 7$ is a residue.
So the map $a \mapsto \left(\frac{a}{p}\right)$ is a completely multiplicative function of $a$.

## Explanations

### L1 human

To decide whether a product is a square modulo $p$, you can test each factor.
Two "no" answers give "yes", just as two negative signs give a positive sign.
