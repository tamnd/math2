---
tag: 9BKCZPMQT6
kind: definition
name: Height of a prime ideal
msc: ["13C15"]
defines: 87WH65FJB8
uses: [0GYGHKX834, 06HC6HK0Z8, 1B4G153ZGE]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_dimension
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $P$ be a [[prime ideal|06HC6HK0Z8]] of $R$.
The *height* $\operatorname{ht} P$ of $P$ is the supremum of the integers $n$ for which there is a chain of prime ideals $P_0 \subsetneq P_1 \subsetneq \cdots \subsetneq P_n = P$ of $R$.

## Remarks

The height is an element of $\set{0, 1, 2, \dots} \cup \set{\infty}$, and $\operatorname{ht} P = \dim R_P$, the [[Krull dimension|1B4G153ZGE]] of the localization at $P$.
Example: in $k[x, y]$ over a field $k$, $\operatorname{ht}(x, y) = 2$, because of the chain $(0) \subsetneq (x) \subsetneq (x, y)$, and the dimension of $k[x, y]$ is $2$.
Non-example of a chain ending at $(x, y)$: $(x^2) \subsetneq (x) \subsetneq (x, y)$ does not give height $3$, because $(x^2)$ is not prime.
The prime ideals of height $0$ are the [[minimal prime ideals|S2D8823P8B]] of $R$.
For any ideal $I \ne R$, the height of $I$ is the least height of a prime ideal that contains $I$.
One has $\operatorname{ht} P + \dim R/P \le \dim R$.

## Explanations

### L1 human

The height of a prime ideal is the length of the longest strictly increasing chain of prime ideals that ends at it.
