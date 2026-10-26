---
tag: 0VY3WPP9Y3
kind: statement
role: theorem
name: Bézout's identity in a Euclidean domain
msc: [13F07]
uses: [0GJ2HRG95T, 0F7KNJ1ZYN, 023VY493K0]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
    locator: For principal ideal domains
---

## Statement

Let $R$ be a [[Euclidean domain|0GJ2HRG95T]] and let $a, b \in R$.
Then $a$ and $b$ have a [[greatest common divisor|0F7KNJ1ZYN]] $d$, and there are $s, t \in R$ with
$$d = s a + t b.$$

## Remarks

The [[Euclidean algorithm|023VY493K0]] computes $d$. The extended Euclidean algorithm also computes $s$ and $t$, by back substitution.
In $\mathbb{Z}$: $\gcd(252, 198) = 18 = 4 \cdot 252 - 5 \cdot 198$.
The same identity holds in every [[principal ideal domain|0RZYDVZ475]], because the ideal $(a, b)$ is principal.
If $d \neq 0$, the coefficients are not unique: $s + k b/d$ and $t - k a/d$ also work for each $k \in R$.

## Explanations

### L1 human

The gcd of two elements is a combination of them with coefficients in the ring.
For example, $\gcd(4, 6) = 2 = 2 \cdot 4 - 1 \cdot 6$.
This is the main tool to solve linear equations $s a + t b = c$ in a Euclidean domain.
