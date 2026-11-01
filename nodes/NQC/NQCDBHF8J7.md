---
tag: NQCDBHF8J7
kind: definition
name: GCD domain
msc: [13F15, 13G05]
defines: ACDEK1GD9G
uses: [09S3PFBEPM, 0F7KNJ1ZYN, 04GNK7K4VP]
sources:
  - url: https://en.wikipedia.org/wiki/GCD_domain
---

## Definition

Let $R$ be an [[integral domain|09S3PFBEPM]].
$R$ is a *GCD domain* if for all $a, b \in R$ there is an element $d \in R$ such that:

1. $d \mid a$ and $d \mid b$;
2. for every $c \in R$ with $c \mid a$ and $c \mid b$, one has $c \mid d$.

Such a $d$ is a [[greatest common divisor|0F7KNJ1ZYN]] of $a$ and $b$.

## Remarks

Here $x \mid y$ means [[divisibility|04GNK7K4VP]] in $R$; a greatest common divisor is unique up to multiplication by a unit.
Example: $\Z$ is a GCD domain, and so is every [[unique factorisation domain|06YMXJMXYS]], where a gcd is read off from the factorizations.
Non-example: in $\Z[\sqrt{-5}]$, with the norm $N(x + y\sqrt{-5}) = x^2 + 5y^2$, the elements $6$ and $2(1 + \sqrt{-5})$ have no gcd.
Indeed $2$ and $1 + \sqrt{-5}$ are common divisors, so the norm of a gcd $d$ would be divisible by $N(2) = 4$ and by $N(1 + \sqrt{-5}) = 6$.
Also $N(d)$ would divide $N(6) = 36$ and $N(2 + 2\sqrt{-5}) = 24$, so $N(d) = 12$.
But $x^2 + 5y^2 = 12$ has no integer solution, so clause 2 fails for every common divisor $d$.
Equivalent form: any two elements have a least common multiple.
