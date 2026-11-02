---
tag: AEZNCY3N3K
kind: definition
name: Abelian and Tauberian theorems
msc: ["40E05", "40D05", "11M45"]
defines: D6XWK1NRY1
uses: [8X25Q4XYMN, 6ZDP261K7R, 0CVVKY7GY2, 0JH4MN4K1C]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
---

## Definition

Let $M$ be a [[summability method|8X25Q4XYMN]] that assigns values to some [[series|0JH4MN4K1C]] of complex numbers.

1. An *Abelian theorem* for $M$ is a theorem stating that every [[convergent series|0CVVKY7GY2]] is $M$-summable to its sum.
More generally, an Abelian theorem for two methods $M$ and $M'$ states that every $M$-summable series is $M'$-summable to the same value.
2. A *Tauberian theorem* for $M$ is a theorem stating that an $M$-summable series converges if its terms satisfy a stated additional condition.
Its sum is then its $M$-value.
The additional condition is called a [[Tauberian condition|6ZDP261K7R]].

The same terms are used for methods that act on sequences, functions or measures, with "convergent" replaced by the corresponding ordinary limit.

## Remarks

Example of an Abelian theorem: Abel's theorem on power series says that if $\sum a_n$ converges to $s$, then $\sum a_n x^n \to s$ as $x \to 1^-$.
Example of a Tauberian theorem: Tauber's theorem says that if $\sum a_n x^n \to s$ as $x \to 1^-$ and $n a_n \to 0$, then $\sum a_n$ converges to $s$.

Non-example: the statement "if $\sum a_n x^n \to s$ as $x \to 1^-$, then $\sum a_n$ converges" has no Tauberian condition, and it is false.
For $a_n = (-1)^n$ one has $\sum a_n x^n = \frac{1}{1+x} \to \frac12$, but $\sum (-1)^n$ diverges.

The names honour Abel and Tauber.
