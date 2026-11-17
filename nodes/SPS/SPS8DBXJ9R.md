---
tag: SPS8DBXJ9R
kind: example
name: Prime factorization is unique up to order and sign
msc: ["00A35", "11A51"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [CBC72TX3NQ]
uses: [CBC72TX3NQ, 084HH1NDCB, 01826KMG2H, 051VYKA1EX]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
    locator: Canonical representation of a positive integer
---

## Example

Let $n$ be an integer with $\abs{n} > 1$.
A factorization of $n$ into irreducibles is a product $n = q_1 q_2 \cdots q_k$, where each $\abs{q_j}$ is a [[prime number|01826KMG2H]].
We explain in what sense such a factorization is unique [[up to|CBC72TX3NQ]] order and sign.

1. Factorizations of $6$ include $2 \cdot 3$, $3 \cdot 2$, $(-2)(-3)$ and $(-3)(-2)$. So the factorization is not unique as a list.
2. Call two factorizations $q_1 \cdots q_k$ and $r_1 \cdots r_l$ equivalent if $k = l$ and the $r_j$ can be reordered so that $r_j = \pm q_j$ for each $j$.
3. This relation is reflexive, symmetric and transitive, so it is an equivalence relation.
4. All four factorizations of $6$ above are equivalent, because each has two factors, and after reordering the factors are $\pm 2$ and $\pm 3$.
5. The [[fundamental theorem of arithmetic|084HH1NDCB]] says that any two factorizations of $n$ are equivalent. Its uniqueness part uses [[Euclid's lemma|051VYKA1EX]].
6. So the factorization is unique up to order and sign, and it is not unique without these words.

## Remarks

1. For positive $n$ and positive primes, the sign disappears, and the factorization is unique up to order.
2. Writing the primes in increasing order, $n = p_1^{a_1} \cdots p_r^{a_r}$ with $p_1 < \dots < p_r$, picks one representative of the class. This is the canonical representation, and it is unique without "up to".
3. The convention that $1$ is not prime is needed here. If $1$ were prime, then $6 = 2 \cdot 3 = 1 \cdot 2 \cdot 3$ would give inequivalent factorizations, see [[choosing good definitions|S1R1VD31BS]].
4. In a unique factorization domain, "up to sign" becomes "up to units": factors may change by a unit factor.

## Explanations

### L1 human

The number $6$ can be written as $2 \cdot 3$ or as $3 \cdot 2$.
With negative numbers, it can also be written as $(-2) \cdot (-3)$.
These look different, but they all use the primes $2$ and $3$, once each.
Only the order and the signs change.
So we say that $6$ splits into primes in only one way, up to order and sign.

### L2 human

We use the theorem to show that $2^a = 3^b$ with integers $a, b \geq 1$ is impossible.

1. The left side is a product of $a$ factors equal to $2$.
2. The right side is a product of $b$ factors equal to $3$.
3. Both are factorizations of the same positive integer, so by uniqueness up to order they have the same factors.
4. But $2$ is not $\pm 3$. So the factorizations are not equivalent, which is a contradiction.

The typical use: compare the primes on both sides of an equation.
A trap is to compare lists in a fixed order, which the theorem does not provide.
