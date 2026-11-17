---
tag: 5BM35ES8WK
kind: example
name: Irreducible and prime differ in Z[√-5]
aliases: [two-is-irreducible-but-not-prime]
msc: ["13F15", "13A05"]
topics: [BP0WAF23HB]
audience: ug2
not_instance_of:
  - target: NZ42PS2P1A
    note: the two definitions of a prime, by divisors and by the divisor property, single out different elements of this ring
uses: [NZ42PS2P1A, 787PD6B171, 052SDEPZH7, 0MNHXBSX3M, 0XVEZDE9J8, 0F4WRWBZZC, KRNFEZWPY0]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_element
    locator: Example
  - url: https://en.wikipedia.org/wiki/Irreducible_element
    locator: Relationship with prime elements
---

## Example

Let $R = \mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$, a ring of [[quadratic integers|0F4WRWBZZC]].
In an integral domain, the two definitions of a prime from [[two definitions of a prime number|787PD6B171]] become two different notions.

- An [[irreducible element|052SDEPZH7]] is a nonzero non-unit whose only factorizations $x = yz$ have $y$ or $z$ a unit.
- A [[prime element|0MNHXBSX3M]] is a nonzero non-unit $p$ such that $p \mid yz$ implies $p \mid y$ or $p \mid z$.

We show that $2$ is irreducible but not prime in $R$.

1. Let $N(a + b\sqrt{-5}) = a^2 + 5b^2$. This [[norm|KRNFEZWPY0]] is multiplicative: $N(xy) = N(x)N(y)$, because $N(x) = x\bar{x}$ for the complex conjugate $\bar{x}$.
2. If $u$ is a [[unit|0XVEZDE9J8]], then $N(u)N(u^{-1}) = N(1) = 1$, so $N(u) = 1$. Then $a^2 + 5b^2 = 1$ gives $b = 0$ and $a = \pm 1$. So the units are $\pm 1$.
3. Suppose that $2 = yz$ with non-units $y$ and $z$. Then $N(y)N(z) = N(2) = 4$, and $N(y) \neq 1 \neq N(z)$, so $N(y) = 2$.
4. But $a^2 + 5b^2 = 2$ has no integer solution: $b \neq 0$ gives at least $5$, and $b = 0$ gives a square. So $2$ is irreducible.
5. Now $(1 + \sqrt{-5})(1 - \sqrt{-5}) = 1 + 5 = 6 = 2 \cdot 3$, so $2$ divides the product.
6. If $2 \mid 1 + \sqrt{-5}$, then $1 + \sqrt{-5} = 2(c + d\sqrt{-5})$, so $2c = 1$, which has no integer solution. In the same way, $2 \nmid 1 - \sqrt{-5}$.
7. So $2$ divides a product but neither factor, and $2$ is not prime.

So in $R$, the two definitions of a prime are not [[equivalent|NZ42PS2P1A]].

## Remarks

1. The direction "prime implies irreducible" still holds in each integral domain. Only the other direction fails.
2. The number $6$ has two factorizations into irreducibles, $2 \cdot 3$ and $(1 + \sqrt{-5})(1 - \sqrt{-5})$. The factors are not associates, because the only units are $\pm 1$. So $R$ is not a unique factorization domain.
3. In a unique factorization domain, irreducible and prime elements coincide. So the failure of equivalence here is a sign of the failure of unique factorization.

## Explanations

### L1 human

In ordinary whole numbers, a prime cannot be split, and a prime that divides a product divides one of the factors.
In some larger number systems these two facts come apart.
In the system of numbers $a + b\sqrt{-5}$, the number $2$ cannot be split into smaller pieces.
But $2$ divides $6$, and $6$ equals $(1 + \sqrt{-5})(1 - \sqrt{-5})$, while $2$ divides neither of these two factors.
So a definition that worked for whole numbers splits into two different ideas here.

### L2 human

We check step 6 for the second factor, with the definition of divisibility in $R$.

1. Suppose that $1 - \sqrt{-5} = 2(c + d\sqrt{-5})$ with integers $c$ and $d$.
2. Compare the parts without $\sqrt{-5}$: $1 = 2c$.
3. No integer $c$ satisfies $1 = 2c$. So $2 \nmid 1 - \sqrt{-5}$.

A faster test uses the norm: if $2 \mid x$, then $N(2) = 4$ divides $N(x)$.
Here $N(1 \pm \sqrt{-5}) = 6$, and $4 \nmid 6$.
A trap is to use the converse of this test: $4 \mid N(x)$ does not imply $2 \mid x$.
