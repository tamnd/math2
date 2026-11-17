---
tag: XSDTDMVKHX
kind: example
name: The fraction in lowest terms is a canonical form for fractions
msc: ["00A35", "11A05"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [F8WNADZFMM]
uses: [F8WNADZFMM, 0R64A2CVN4, 0C8WYW4KYQ, 0G8VEZ3WTK, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_fraction
    locator: Uniqueness
  - url: https://en.wikipedia.org/wiki/Canonical_form
    locator: Definition
---

## Example

Let $X$ be the set of pairs $(a, b)$ of integers with $b \neq 0$, where the pair $(a, b)$ stands for the fraction $a/b$.
Define $(a, b) \sim (c, d)$ when $ad = bc$; this is the [[equivalence relation|0G8VEZ3WTK]] "the two fractions are equal".
For $(a, b) \in X$ let $g = \gcd(a, b) > 0$, the [[greatest common divisor|0C8WYW4KYQ]], and let $s = 1$ if $b > 0$ and $s = -1$ if $b < 0$.
Define $c(a, b) = (sa/g, \, sb/g)$.
We check that $c$ is a [[canonical form|F8WNADZFMM]] for $\sim$.

1. The map $c$ is defined on all of $X$. Since $b \neq 0$, we have $g \geq 1$, and $g$ divides $a$ and $b$, so $sa/g$ and $sb/g$ are integers, and $sb/g \neq 0$.
2. We have $c(a, b) \sim (a, b)$. The cross products are $(sa/g) \cdot b$ and $(sb/g) \cdot a$, and both equal $sab/g$.
3. The pair $c(a, b) = (a', b')$ has $b' = |b|/g > 0$ and $\gcd(a', b') = 1$, because a common divisor $d > 1$ of $a'$ and $b'$ would make $dg$ a common divisor of $a$ and $b$ larger than $g$.
4. If $(a, b) \sim (c_1, d_1)$, then the two pairs give the same rational number $q$. By the [[uniqueness of the fraction in lowest terms|0R64A2CVN4]], there is exactly one pair $(a', b')$ with $b' > 0$, $\gcd(a', b') = 1$ and $a'/b' = q$. By steps 2 and 3, both $c(a, b)$ and $c(c_1, d_1)$ are this pair. So $c(a, b) = c(c_1, d_1)$.
5. Computations: $c(6, 8) = (3, 4)$ with $g = 2$; $c(-6, -4) = (3, 2)$ with $g = 2$ and $s = -1$; $c(0, 5) = (0, 1)$ with $g = \gcd(0, 5) = 5$.

## Remarks

The example shows both conditions of a canonical form: each fraction is equal to its form (step 2), and equal fractions have the same form (step 4).
The sign rule is needed.
Without it, $(3, 2)$ and $(-3, -2)$ are both in lowest terms and equal as fractions, so the form would not be unique.
Decimal expansions are a canonical form for rational numbers only with an extra rule, because $0.999\ldots$ and $1.000\ldots$ name the same number; the usual rule forbids an expansion that ends in repeated nines.
The [[set of rational numbers|0NCJ5WXN6Z]] can be built as the set of equivalence classes of $\sim$, and the canonical form picks one element of each class.

## Explanations

### L1 human

The fractions $2/4$, $3/6$ and $50/100$ all mean one half.
To compare fractions, we simplify each one as far as it goes, and we keep the bottom number positive.
Every fraction that means one half simplifies to the same result, $1/2$.
This simplest form is the canonical form: there is exactly one for each value, and no choice is involved.

### L2 human

We decide whether $35/-49$ and $-15/21$ are equal.

1. For $(35, -49)$: $g = \gcd(35, 49) = 7$ and $s = -1$. So $c(35, -49) = (-35/7, \, 49/7) = (-5, 7)$.
2. For $(-15, 21)$: $g = \gcd(15, 21) = 3$ and $s = 1$. So $c(-15, 21) = (-5, 7)$.
3. The forms agree, so the fractions are equal. As a check, $35 \cdot 21 = 735$ and $(-49) \cdot (-15) = 735$.

The typical use of a canonical form is this test: compute the forms and compare them.
A trap: the test needs a form that is unique in its class, so a "simplified" form without the sign rule can give a wrong "not equal".
