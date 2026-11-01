---
tag: KTBBV459TV
kind: definition
name: Embedded prime
msc: ["13A15", "13C05"]
defines: RVKPM94MDF
uses: [0MVH4Y1CRZ, 0MYSA6MYNA, 1RJJ33KKSS]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_prime
---

## Definition

Let $R$ be a commutative [[Noetherian ring|0MVH4Y1CRZ]] and let $I \ne R$ be an [[ideal|0MYSA6MYNA]] of $R$.
An [[associated prime|1RJJ33KKSS]] $P$ of $R/I$ is an *embedded prime* of $I$ if there is another associated prime $P'$ of $R/I$ with $P' \subsetneq P$.
An associated prime that is not embedded is called a minimal or isolated prime of $I$.

## Remarks

Example: for $I = (x^2, xy)$ in $k[x, y]$ over a field $k$, the associated primes are $(x)$ and $(x, y)$, and $(x) \subsetneq (x, y)$, so $(x, y)$ is embedded.
Non-example: $(x)$ is not embedded for the same $I$, because no associated prime is strictly smaller.
The minimal primes of $I$ in this sense are exactly the [[minimal prime ideals|S2D8823P8B]] over $I$.
In a [[primary decomposition|M2VPVJH33K]], the components at embedded primes are not unique, while those at minimal primes are.
The same terms apply to the associated primes of a module.

## Explanations

### L1 human

An embedded prime is an associated prime that sits strictly above another associated prime.
