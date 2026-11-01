---
tag: 1RJJ33KKSS
kind: definition
name: Associated prime
msc: ["13C05", "13A15"]
defines: ERFZ6S8X0X
uses: [0GYGHKX834, 09VDS2W1E8, 06HC6HK0Z8, HB4XDKJTW8]
sources:
  - url: https://en.wikipedia.org/wiki/Associated_prime
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $M$ be an $R$-[[module|09VDS2W1E8]].
For $m \in M$, let $\operatorname{Ann}_R(m) = \set{r \in R : rm = 0}$ be the [[annihilator|HB4XDKJTW8]] of $m$.
A [[prime ideal|06HC6HK0Z8]] $P$ of $R$ is an *associated prime* of $M$ if $P = \operatorname{Ann}_R(m)$ for some $m \in M$.
The set of associated primes of $M$ is written $\operatorname{Ass}_R(M)$.

## Remarks

For an ideal $I$ of $R$, the associated primes of $I$ usually means $\operatorname{Ass}_R(R/I)$.
Example: for $M = \Z/12\Z$ over $\Z$, $\operatorname{Ann}(6) = (2)$ and $\operatorname{Ann}(4) = (3)$, so $(2)$ and $(3)$ are associated primes; in fact $\operatorname{Ass}(M) = \set{(2), (3)}$.
Non-example: $(0)$ is not an associated prime of $\Z/12\Z$, because $12$ kills every element, so no annihilator is $(0)$.
For $M = \Z$, the annihilator of every nonzero element is $(0)$, so $\operatorname{Ass}(\Z) = \set{(0)}$.
Equivalently, $P \in \operatorname{Ass}_R(M)$ when $M$ has a submodule isomorphic to $R/P$.
For rings that are not Noetherian, some authors use other variants, such as weakly associated primes.

## Explanations

### L1 human

An associated prime of a module is a prime ideal that is exactly the set of ring elements killing some one element of the module.
