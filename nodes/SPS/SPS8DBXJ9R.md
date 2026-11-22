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

Let $n$ be an integer with $|n| > 1$.
A factorization of $n$ into irreducibles is a product $n = q_1 q_2 \cdots q_k$ in which each $|q_j|$ is a [[prime number|01826KMG2H]].
We make precise the sense in which such a factorization is unique [[up to|CBC72TX3NQ]] order and sign.

1. Factorizations of $6$ include
   $$2 \cdot 3, \qquad 3 \cdot 2, \qquad (-2)(-3), \qquad (-3)(-2).$$
   So the factorization is not unique as a list.
2. Call two factorizations $q_1 \cdots q_k$ and $r_1 \cdots r_l$ equivalent if $k = l$ and the $r_j$ can be reordered so that $r_j = \pm q_j$ for each $j$.
3. This relation is reflexive (use no reordering and the sign $+$), symmetric (undo the reordering, and $\pm$ is its own inverse) and transitive (compose the reorderings and multiply the signs).
   So it is an equivalence relation.
4. The four factorizations of $6$ above are equivalent.
   Each has two factors, and after a reordering the factors are $\pm 2$ and $\pm 3$.
5. The [[fundamental theorem of arithmetic|084HH1NDCB]] says that any two factorizations of $n$ are equivalent.
   Its uniqueness part rests on [[Euclid's lemma|051VYKA1EX]]: a prime that divides a product divides one of the factors.
6. So the factorization is unique up to order and sign, and it is not unique without these words.

## Remarks

For positive $n$ and positive primes the signs disappear, and the factorization is unique up to order alone.
Writing the primes in increasing order, $n = p_1^{a_1} \cdots p_r^{a_r}$ with $p_1 < \dots < p_r$, picks one representative from each class.
This canonical form is unique with no "up to": for $12$ it is $2^2 \cdot 3$.

The convention that $1$ is not prime is needed here.
If $1$ were prime, then $6 = 2 \cdot 3 = 1 \cdot 2 \cdot 3$ would give two factorizations of different lengths, and no reordering relates them, as [[choosing good definitions|S1R1VD31BS]] explains.
In a unique factorization domain, "up to sign" becomes "up to units": two factorizations are equivalent when, after a reordering, matching factors differ by a unit factor.

## Explanations

### L1 human

The number $6$ can be written as $2 \cdot 3$ or as $3 \cdot 2$.
With negative numbers, it can also be written as $(-2) \cdot (-3)$.
These look different, but they all use the primes $2$ and $3$, once each.
Only the order and the signs change.
So we say that $6$ splits into primes in only one way, up to order and sign.

### L2 human

We use the theorem to show that $2^a = 3^b$ has no solution in integers $a, b \ge 1$.
The left side is a factorization with $a$ factors, each equal to $2$.
The right side is a factorization with $b$ factors, each equal to $3$.
Both are factorizations of the same integer greater than $1$, so by the theorem they are equivalent, and some factor $3$ must equal $\pm 2$.
That is false, so no such $a$ and $b$ exist.
The typical use is to compare the primes on the two sides of an equation.
Watch out: the theorem matches the factors only after a reordering, so you may not compare the first factor on one side with the first factor on the other.
