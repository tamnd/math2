---
tag: 850Y7GFENR
kind: example
name: Divisibility poset
msc: [06D05, 11A05]
instance_of: [0QV2JS9RJ3, WH4SFAACAS, 0HM0HQCK6N]
uses: [0PG2H7WKGG, 0C8WYW4KYQ, 007NPQX34K, 084HH1NDCB]
sources:
  - url: https://en.wikipedia.org/wiki/Divisor
---

## Example

Let $\Z_{>0}$ be the set of positive integers, and write $a \mid b$ when $a$ [[divides|0PG2H7WKGG]] $b$.
The relation $\mid$ is a [[partial order|0QV2JS9RJ3]] on $\Z_{>0}$.
It is reflexive since $a = 1 \cdot a$.
It is antisymmetric since $a \mid b$ and $b \mid a$ give $a \le b \le a$ for positive integers.
It is transitive since $b = ka$ and $c = lb$ give $c = (kl) a$.

It is a [[lattice|WH4SFAACAS]]: the meet of $a$ and $b$ is their [[greatest common divisor|0C8WYW4KYQ]], and the join is their [[least common multiple|007NPQX34K]].
It is a [[distributive lattice|0HM0HQCK6N]].
By the [[fundamental theorem of arithmetic|084HH1NDCB]], write $a$, $b$, $c$ as products of primes.
For each prime $p$, gcd takes the minimum and lcm takes the maximum of the exponents of $p$.
The identity $\min(x, \max(y, z)) = \max(\min(x, y), \min(x, z))$ for integers then gives $\gcd(a, \operatorname{lcm}(b, c)) = \operatorname{lcm}(\gcd(a, b), \gcd(a, c))$.

## Remarks

The element $1$ is the least element, and there is no greatest element in $\Z_{>0}$.
If $0$ is added, it becomes the greatest element, since every integer divides $0$.
The positive divisors of a fixed $n$ form a finite sublattice; for $n = p_1^{e_1} \cdots p_k^{e_k}$ it is isomorphic to a product of chains with $e_1 + 1, \ldots, e_k + 1$ elements.
The order is not total: $2$ and $3$ are incomparable.

## Explanations

### L1 human

Order the positive integers by "divides" instead of "is smaller than".
Then $2$ is below $6$, but $2$ and $3$ are side by side, and the primes sit just above $1$.
The greatest common divisor and the least common multiple play the roles of "meet" and "join".
