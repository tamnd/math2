---
tag: 6WYYMPH21Q
kind: statement
role: theorem
name: Fundamental recurrence formulas
msc: [40A15, 11A55, 30B70]
uses: [0BK6JBK58W, 0SRWNR42BQ, 0CDMXGPSES]
about: [04P2RJ4WPS, 0D474C7ES1]
sources:
  - url: https://en.wikipedia.org/wiki/Continued_fraction
---

## Statement

Let $b_0, b_1, b_2, \dots$ be complex numbers and let $a_1, a_2, \dots$ be nonzero complex numbers.
Consider the [[continued fraction|0BK6JBK58W]] $b_0 + \cfrac{a_1}{b_1 + \cfrac{a_2}{b_2 + \cdots}}$, and let $x_n$ be its $n$-th [[convergent|0SRWNR42BQ]], evaluated in the [[Riemann sphere|0CDMXGPSES]] with $a/0 = \infty$ and $a/\infty = 0$ for $a \ne 0$.
Define $A_{-1} = 1$, $A_0 = b_0$, $B_{-1} = 0$, $B_0 = 1$ and, for $n \ge 1$,
$$A_n = b_n A_{n-1} + a_n A_{n-2}, \qquad B_n = b_n B_{n-1} + a_n B_{n-2}.$$
Then for every $n \ge 0$:

1. $x_n = \dfrac{A_n}{B_n}$, where $A_n$ and $B_n$ are not both $0$;
2. $A_n B_{n-1} - A_{n-1} B_n = (-1)^{n-1} a_1 a_2 \cdots a_n$.

## Remarks

Proof idea: write $x_n = t_0 \circ t_1 \circ \cdots \circ t_n(0)$ with $t_0(w) = b_0 + w$ and $t_k(w) = \frac{a_k}{b_k + w}$.
These are [[Möbius transformations|0B346DDAM5]], and the product of their matrices is $\begin{pmatrix} A_{n-1} & A_n \\ B_{n-1} & B_n \end{pmatrix}$ by induction.
Taking determinants gives item 2, and applying the product to $0$ gives item 1; item 2 shows that $A_n$ and $B_n$ do not both vanish.
Example: for $1 + \cfrac{1}{2 + \cfrac{1}{2 + \cdots}}$ the recurrences give $A_n = 1, 3, 7, 17, \dots$ and $B_n = 1, 2, 5, 12, \dots$, the convergents of $\sqrt{2}$.
Item 2 gives $x_n - x_{n-1} = \dfrac{(-1)^{n-1} a_1 \cdots a_n}{B_n B_{n-1}}$, so the convergents are the partial sums of a series, and convergence questions become questions about series.

## Explanations

### L1 human

Computing a continued fraction from the inside out has to be redone each time a new level is added.
These formulas compute each new convergent from the two previous ones, with one multiplication and addition for its numerator and one for its denominator.

### L2 human

The numerators $A_n$ and denominators $B_n$ satisfy a three-term linear recurrence, the same one for both.
For a [[simple continued fraction|06XF7BCFFJ]] they reduce to the recurrences for $p_n$ and $q_n$, and item 2 becomes $p_n q_{n-1} - p_{n-1} q_n = (-1)^{n-1}$.
The difference formula in the remarks is the starting point of the [[Śleszyński–Pringsheim theorem|NEC48RHNN0]] and other convergence tests for continued fractions.
