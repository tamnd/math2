---
tag: CDCZ3DZ40E
kind: proof
name: Proof of induction from an arbitrary base case
msc: [03F30]
proves: 0GF6AJEBZ0
uses: [0ASJVEFA9J, 0Y9H52BT03, 0W5DSDFQ4G, 0C32J27WQC]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Base case other than 0 or 1
---

## Proof

We apply ordinary [[induction|0ASJVEFA9J]] to a shifted property.
Let $m$ and $P$ be as in the statement.
For each natural number $k$, let $Q(k)$ be the property "$P(m + k)$ holds".
Here $+$ is the [[addition|0W5DSDFQ4G]] of natural numbers.

1. For each natural number $k$, we have $m \le m + k$ by the definition of the [[order|0Y9H52BT03]]. So $P(m + k)$ makes sense.
2. Base case: $m + 0 = m$, and $P(m)$ holds by hypothesis. So $Q(0)$ holds.
3. Induction step: suppose that $Q(k)$ holds, that is, $P(m + k)$ holds.
4. By step 1, $m + k \ge m$. So the second hypothesis of the statement, applied to $n = m + k$, gives $P((m + k) + 1)$.
5. By the [[associativity of addition|0C32J27WQC]], $(m + k) + 1 = m + (k + 1)$. So $Q(k + 1)$ holds.
6. By induction, $Q(k)$ holds for every natural number $k$.
7. Now let $n$ be a natural number with $n \ge m$. By the definition of the order, there is a natural number $k$ with $m + k = n$.
8. By step 6, $Q(k)$ holds, that is, $P(n)$ holds. This holds for every $n \ge m$.

## Idea

Shift the numbering so that the first domino gets the number $0$.
The number $m + k$ becomes the number $k$, and ordinary induction applies to the shifted property.
