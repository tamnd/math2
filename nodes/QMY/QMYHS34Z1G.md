---
tag: QMYHS34Z1G
kind: example
name: The equation x^2 = x + 2 has exactly one natural solution
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0QAJHFGZZJ]
uses: [0QAJHFGZZJ, 0N3ADS4CHH]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.6
---

## Example

Let $P(x)$ be the predicate "$x^2 = x + 2$".
We show that $\exists! x \in \mathbb{N} \; P(x)$ is true, with the definition of the [[uniqueness quantifier|0N3ADS4CHH]].
Here $\mathbb{N}$ is the set of natural numbers, with or without $0$, and the result is the same either way.

| $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $x^2$ | 0 | 1 | 4 | 9 | 16 |
| $x + 2$ | 2 | 3 | 4 | 5 | 6 |

1. Factor: $x^2 - x - 2 = (x - 2)(x + 1)$, so $P(x)$ holds exactly when $x = 2$ or $x = -1$.
   A product is $0$ exactly when one factor is $0$.
2. Existence: $2 \in \mathbb{N}$ and $2^2 = 4 = 2 + 2$, so $P(2)$ is true.
3. Uniqueness: let $y \in \mathbb{N}$ with $P(y)$.
   By step 1, $y = 2$ or $y = -1$, and since $-1 \notin \mathbb{N}$, we get $y = 2$.
4. Steps 2 and 3 give $P(2) \land \forall y \in \mathbb{N} \, (P(y) \to y = 2)$.
   So $\exists! x \in \mathbb{N} \; P(x)$ is true, and the unique element is $2$.

## Remarks

The truth value of $\exists! x \, P(x)$ depends on the domain of discourse.
Over $\mathbb{Z}$, the same predicate has the truth set $\{-1, 2\}$.
Existence still holds there, but uniqueness fails with $x = -1$ and $y = 2$, so $\exists! x \in \mathbb{Z} \; P(x)$ is false.
Over the even integers the truth set is $\{2\}$, and the $\exists!$ statement is true again.
For the equation $x^2 = x + 6$, the factorization $(x - 3)(x + 2) = 0$ gives the unique natural solution $3$.

## Explanations

### L1 human

We look for whole numbers $0, 1, 2, 3, \ldots$ whose square is $2$ more than the number.
For $0$ the two sides are $0$ and $2$, and for $1$ they are $1$ and $3$, so these fail.
For $2$ the two sides are $4$ and $4$, so $2$ works.
From $3$ on the square grows faster: $9$ against $5$, $16$ against $6$, and so on.
So $2$ is the only whole number that works.
If negative numbers are allowed, $-1$ also works, since $(-1)^2 = 1 = -1 + 2$.

### L2 human

A proof of an $\exists!$ statement has two labeled parts.
Existence shows one element of the domain with the property, here $2$.
Uniqueness takes an arbitrary element $y$ of the domain with the property and shows that $y$ equals that element.
The domain enters only in the uniqueness part, where it removes the solution $-1$.
For practice, show that $\exists! x \in \mathbb{N} \; (x^2 = 3x + 4)$ is true: $(x - 4)(x + 1) = 0$, and the unique natural solution is $4$.
Watch out: the statement $\exists! x \, P(x)$ has no truth value until the domain is fixed, so "the equation has one solution" without naming the set is incomplete.
