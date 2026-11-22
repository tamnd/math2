---
tag: 0JB3DP1BMF
kind: definition
name: Linear combination
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
defines: 0V8F3E48E6
uses: [05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_combination
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 2A
inventory: [AW41B4D2VT]
---

## Definition

A linear combination of some vectors is a sum of scalar multiples of them.
Let $F$ be a field and let $V$ be a [[vector space|05EGHEQZAW]] over $F$.
Let $v_1, \dots, v_k \in V$ with $k \ge 0$.
A *linear combination* of $v_1, \dots, v_k$ is a vector of the form
$$a_1 v_1 + a_2 v_2 + \dots + a_k v_k,$$
where $a_1, \dots, a_k \in F$ are the *coefficients*.
For $k = 0$ the sum is empty, and its value is $0$.
For a family $(v_i)_{i \in I}$ with any index set $I$, a linear combination of the family is a sum $\sum_{i \in I} a_i v_i$ in which $a_i \in F$ for each $i$ and only finitely many $a_i$ are nonzero.

## Remarks

The coefficients lie in $F$ because scalar multiplication is defined only for scalars of $F$.
If you change the field, you change which combinations exist: $(1, \sqrt{2})$ is a combination of $(1, 0)$ and $(1, 1)$ with real coefficients, but not with rational ones.

The finiteness condition is there because a vector space has no notion of limit, so only finite sums have a value.
For example, $3e_1 + 5e_2 = (3, 5)$ is a linear combination of the standard vectors of $F^2$.
In $F[x]$, the series $1 + x + x^2 + \dots$ fails the condition, since it would need infinitely many nonzero coefficients.

The empty sum is allowed on purpose.
It makes the zero vector a combination of every family, even of the empty family, so the [[linear span|0DTY8B9HMS]] of the empty set is $\{0\}$.
The [[concept page|0V8F3E48E6]] gives worked examples, and the [[matrix-vector product|0PDVQEP0ZC]] $Ax$ is the combination of the columns of $A$ with the entries of $x$ as coefficients.

## Explanations

### L1 human

A linear combination mixes some vectors: scale each one by a number, then add the results.
With $(1, 0)$ and $(0, 1)$, the numbers $3$ and $5$ give $(3, 5)$.
Infinite sums are not allowed, so only finitely many numbers can be nonzero.

### L2 human

To test whether $(5, 6)$ is a combination of $(1, 3)$ and $(2, 4)$, solve $x_1 + 2x_2 = 5$ and $3x_1 + 4x_2 = 6$.
Elimination gives $x_1 = -4$ and $x_2 = \tfrac{9}{2}$.
Check: $-4(1, 3) + \tfrac{9}{2}(2, 4) = (-4 + 9, -12 + 18) = (5, 6)$.
