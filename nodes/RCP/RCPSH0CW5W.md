---
tag: RCPSH0CW5W
kind: example
name: The additive group of rational numbers has countably infinite order
msc: [20A05, 20K99]
topics: [BAZT8JJ70S]
audience: ug1
instance_of: [0B85S2V2DR]
uses: [0NCJ5WXN6Z, 01TQB88H4C]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_number
    locator: lead section
---

## Example

Let $\mathbb{Q}$ be the set of [[rational numbers|0NCJ5WXN6Z]], with addition.
We show that the [[order|0B85S2V2DR]] of the group $(\mathbb{Q}, +)$ is infinite and [[countable|01TQB88H4C]].

1. The set $\mathbb{Q}$ with addition is a [[group|G5S1M9]]. The sum of two fractions is a fraction, addition is associative, $0$ is the identity element, and $-r$ is the inverse of $r$.
2. The order is infinite. The integers $1, 2, 3, \ldots$ are different rational numbers, so $\mathbb{Q}$ is not finite.
3. Each rational number $r$ has exactly one form $r = p/q$ with $p \in \mathbb{Z}$, $q$ a positive integer, and $\gcd(p, q) = 1$. Let $s = 0$ when $p \geq 0$, and let $s = 1$ when $p < 0$.
4. Define $f(r) = 2^{|p|} \, 3^{q} \, 5^{s}$. This is a positive integer.
5. The map $f$ is injective. By the uniqueness of the prime factorization, $f(r)$ determines the exponents $|p|$, $q$ and $s$, and these three numbers determine $p$, $q$ and so $r$.
6. An injective map from $\mathbb{Q}$ into the natural numbers shows that $\mathbb{Q}$ is countable.

By steps 2 and 6, $(\mathbb{Q}, +)$ has countably infinite order.

## Remarks

The group $(\mathbb{Z}, +)$ of [[integers|0C4JS9RF5M]] also has countably infinite order, so the two groups have the same order.
They are not [[isomorphic|08MG7H8JW5]].
The group $\mathbb{Z}$ is [[cyclic|0KVGH0J5B3]], with generator $1$.
The group $\mathbb{Q}$ is not cyclic: when $r \neq 0$, the number $r/2$ is not an integer multiple $kr$ of $r$, because $k = 1/2$ is not an integer.
The group $(\mathbb{R}, +)$ of [[real numbers|08J2M1JYAG]] has an uncountable order, by [[Cantor's diagonal argument|0XCH8QVDCQ]], so it is not isomorphic to $(\mathbb{Q}, +)$.

## Explanations

### L1 human

The fractions, positive, negative and zero, form a group under addition.
There are infinitely many fractions.
But we can still put all of them in one infinite list, with a first, second, third fraction and so on.
So the group has an infinite order of the smallest kind, called countable.

### L2 human

We compute $f$ for three numbers, to see that the code works.

1. For $r = 3/4$ we have $p = 3$, $q = 4$, $s = 0$, so $f(r) = 2^3 \cdot 3^4 = 8 \cdot 81 = 648$.
2. For $r = -1/2$ we have $p = -1$, $q = 2$, $s = 1$, so $f(r) = 2 \cdot 9 \cdot 5 = 90$.
3. For $r = 0$ we have $p = 0$, $q = 1$, $s = 0$, so $f(r) = 3$.

The three values are different, as step 5 says.
A trap is to use all forms $p/q$, not only the reduced form: then $1/2$ and $2/4$ get two different codes, and $f$ is not a function on $\mathbb{Q}$.
