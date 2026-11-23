---
tag: WRN90EH74V
kind: example
name: Mutual divisibility of integers does not give equality
msc: ["00A35", "11A05"]
topics: [MEKKHHQTKB]
audience: ug1
not_instance_of:
  - target: S3QADD13E9
    note: divisibility on the integers is not antisymmetric, so the two relations a | b and b | a do not give a = b
uses: [S3QADD13E9, 0PG2H7WKGG, 0M0H1ZH8TT, 053E86NWVK]
sources:
  - url: https://en.wikipedia.org/wiki/Antisymmetric_relation
    locator: lead section
---

## Example

On the set $\mathbb{Z}$ of all integers, [[divisibility|0PG2H7WKGG]] $a \mid b$ means that $b = ak$ for some integer $k$.
A student argues: "$a \mid b$ and $b \mid a$, so $a = b$, by [[equality by two inequalities|S3QADD13E9]]."
We show that this step fails on $\mathbb{Z}$, and we find what is true instead.

1. Take $a = 2$ and $b = -2$.
   Then $-2 = 2 \cdot (-1)$, so $2 \mid -2$, and $2 = (-2) \cdot (-1)$, so $-2 \mid 2$.
2. But $2 \ne -2$, so the two divisibilities do not give equality.
3. The relation $\mid$ on $\mathbb{Z}$ is reflexive and transitive but not [[antisymmetric|0M0H1ZH8TT]].
   It is a preorder, not a partial order, so the method does not apply.
4. Now let $a \mid b$ and $b \mid a$ with $a \ne 0$, and write $b = ak$ and $a = b\ell$ with integers $k$ and $\ell$.
5. Substitute the first equation into the second to get $a = ak\ell$; since $a \ne 0$, this gives $k\ell = 1$.
6. The only integer solutions of $k\ell = 1$ are $k = \ell = 1$ and $k = \ell = -1$, so $b = a$ or $b = -a$.
7. If $a = 0$, then $a \mid b$ forces $b = 0 = a$.
   So on $\mathbb{Z}$ the correct conclusion is $b = \pm a$.

## Remarks

The method needs antisymmetry.
In a preorder, two "inequalities" give only equivalence, and here the equivalence is "$b = \pm a$".
In ring theory, elements that divide each other are called [[associates|053E86NWVK]]; in an integral domain they differ by a unit factor, and the units of $\mathbb{Z}$ are $\pm 1$.

A choice of representatives restores the method.
On the positive integers, $\mid$ is antisymmetric, as in [[mutual divisibility of natural numbers|P2AJBVRA3S]].
In the polynomials over $\mathbb{R}$, $x + 1$ and $2x + 2$ divide each other and differ, and monic polynomials play the role of the positive integers.

## Explanations

### L1 human

The numbers $2$ and $-2$ divide each other, because each is the other times $-1$.
But they are different numbers.
So "each divides the other" does not mean "they are equal" once negative numbers are allowed.
It means only that they are equal up to a sign.

### L2 human

We find all integers $b$ with $6 \mid b$ and $b \mid 6$.

1. From $b \mid 6$, the number $b$ is one of $\pm 1, \pm 2, \pm 3, \pm 6$.
2. From $6 \mid b$, the number $b$ is a multiple of $6$, and only $6$ and $-6$ on that list qualify.
3. So $b = \pm 6$, in agreement with step 7 of the example.

This is why a greatest common divisor in $\mathbb{Z}$ or in a polynomial ring is unique only up to a unit, unless a normal form is chosen.
Watch out: quoting "$a \mid b$ and $b \mid a$ give $a = b$" without the word "positive" is the error.
