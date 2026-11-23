---
tag: B5NGFKX1D3
kind: example
name: The statement that some real x satisfies x^2 + 1 = 0 is false
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0MSRQHCNN9]
uses: [0MSRQHCNN9, 0JW2FHW7G3, 05SZQKH75K, CX38X989TB, 0ESCX36MMC, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Example

Consider the [[existential statement|0JW2FHW7G3]] $\exists x \in \mathbb{R} \; (x^2 + 1 = 0)$.
We show that it is false, and that the same formula over the [[complex numbers|09FTAET5Z4]] is true.

1. By the [[negation of an existential statement|05SZQKH75K]], `not_exists` in Mathlib, the negation of the statement is equivalent to $\forall x \in \mathbb{R} \; \neg(x^2 + 1 = 0)$.
2. We [[prove this universal statement|CX38X989TB]].
   Let $x$ be an arbitrary real number.
3. The square of a real number is at least $0$, so $x^2 \ge 0$.
4. So $x^2 + 1 \ge 1 > 0$, and $x^2 + 1 \neq 0$.
5. Since $x$ was arbitrary, no real number is a witness, and $\exists x \in \mathbb{R} \; (x^2 + 1 = 0)$ is false.
6. Now change the domain to $\mathbb{C}$, and take the [[imaginary unit|0ESCX36MMC]] $i$, with $i^2 = -1$.
7. Then $i^2 + 1 = -1 + 1 = 0$, so $i$ is a witness, and $\exists x \in \mathbb{C} \; (x^2 + 1 = 0)$ is true.
   The number $-i$ is a second witness.

## Remarks

The example shows the two halves of the existential quantifier: one witness proves the statement, and a refutation must cover every element of the domain.
Steps 2 to 5 are a proof about all real numbers, while trying $x = 0, 1, -1$ and finding no witness would refute nothing.

The predicate $x^2 + 1 = 0$ is the same in both parts, so the truth value depends on the domain alone.
The pair of statements is a short form of one reason for the construction of $\mathbb{C}$: the polynomial $x^2 + 1$ has no root in $\mathbb{R}$ and has the roots $i$ and $-i$ in $\mathbb{C}$.

## Explanations

### L1 human

The question is whether some real number, squared and then increased by $1$, gives $0$.
A square is never negative, so the square plus $1$ is at least $1$.
So no real number works, and the claim "some real number does it" is false.
With complex numbers the claim becomes true, because the number $i$ has square $-1$.

### L2 human

Decide whether $\exists x \in \mathbb{Q} \; (x^2 = 2)$ is true.
In $\mathbb{R}$, the number $\sqrt{2}$ satisfies $x^2 = 2$, so $\exists x \in \mathbb{R} \; (x^2 = 2)$ is true.
Any real $x$ with $x^2 = 2$ is $\sqrt{2}$ or $-\sqrt{2}$.
Neither is rational, by the [[irrationality of the square root of a prime|0YHFMXJJAZ]].
So no rational number is a witness, and $\exists x \in \mathbb{Q} \; (x^2 = 2)$ is false.
This pattern is the usual way to show that an equation has no solution in a given set.
Watch out: giving $\sqrt{2}$ as a witness without checking the condition $x \in \mathbb{Q}$ of the restricted form is the typical error.
