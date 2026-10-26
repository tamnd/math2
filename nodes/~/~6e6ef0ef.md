---
tag: ~6e6ef0ef
kind: statement
role: theorem
name: Bézout's identity in a Euclidean domain
msc: [13F07]
uses: [~58d9a8a1, ~2157072f, ~0dc7035d]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
    locator: For principal ideal domains
same_as:
  wikidata: Q513028
  wikipedia: Bézout's identity
---

## Statement

Let $R$ be a [[Euclidean domain|~58d9a8a1]] and let $a, b \in R$.
Then $a$ and $b$ have a [[greatest common divisor|~2157072f]] $d$, and there are $s, t \in R$ with
$$d = s a + t b.$$

## Remarks

The [[Euclidean algorithm|~0dc7035d]] computes $d$. The extended Euclidean algorithm also computes $s$ and $t$, by back substitution.
In $\mathbb{Z}$: $\gcd(252, 198) = 18 = 4 \cdot 252 - 5 \cdot 198$.
The same identity holds in every [[principal ideal domain|~91f9e139]], because the ideal $(a, b)$ is principal.
If $d \neq 0$, the coefficients are not unique: $s + k b/d$ and $t - k a/d$ also work for each $k \in R$.

## Explanations

### L1 human

The gcd of two elements is a combination of them with coefficients in the ring.
For example, $\gcd(4, 6) = 2 = 2 \cdot 4 - 1 \cdot 6$.
This is the main tool to solve linear equations $s a + t b = c$ in a Euclidean domain.
