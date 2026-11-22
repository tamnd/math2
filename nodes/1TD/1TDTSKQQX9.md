---
tag: 1TDTSKQQX9
kind: example
name: The list 1, 2, 4, ... does not determine its next term
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
not_instance_of:
  - target: QKEX4PD029
    note: the ellipsis does not fix a unique rule, so the display has no single meaning
uses: [QKEX4PD029, 0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Ellipsis
    locator: lead section
---

## Example

A worksheet asks "continue the [[sequence|0G9EKM0E15]] $1, 2, 4, \ldots$".
We read the display
$$1, 2, 4, \ldots$$
as a proposed definition of a sequence $a_0, a_1, a_2, \ldots$, and we show that two simple rules fit the three given terms and disagree at the next one.

1. Rule A is $a_n = 2^n$.
   It gives $a_0 = 1$, $a_1 = 2$ and $a_2 = 4$, and then $a_3 = 8$.
2. Rule B is $b_n = \frac{n^2 + n + 2}{2}$.
   It gives
   $$b_0 = \frac{2}{2} = 1, \quad b_1 = \frac{4}{2} = 2, \quad b_2 = \frac{8}{2} = 4, \quad b_3 = \frac{14}{2} = 7.$$
3. Both rules agree with the display, and $a_3 = 8 \neq 7 = b_3$.
4. So the display does not determine the next term.
   It fails the basic requirement of [[mathematical notation|QKEX4PD029]]: one expression, one meaning.

## Remarks

Both rules occur in real problems.
Rule A counts the subsets of a set with $n$ elements, and rule B counts the largest number of pieces that $n$ straight cuts make of a flat pancake.

No finite list fixes its continuation.
For any finite list of numbers and any chosen next value, some polynomial fits all of them, by Lagrange interpolation.
The display becomes correct notation when the author adds the rule, for example "$1, 2, 4, \ldots, 2^n, \ldots$" or "$a_n = 2^n$".
An ellipsis is safe in $1, 2, 3, \ldots, n$ only because every reader shares the habit that the step is $1$.

## Explanations

### L1 human

Dots after a few numbers ask the reader to guess the rule.
For $1, 2, 4$ one reader doubles each time and gets $8$ next.
Another reader adds $1$, then $2$, then $3$, and gets $7$ next.
Both readers follow a fair rule, so the dots alone do not say which number comes next.

### L2 human

We can do more: find a rule that fits $1, 2, 4$ and gives any chosen value $c$ next.
Try $c_n = 2^n + t \, n(n-1)(n-2)$ with a constant $t$.
For $n = 0, 1, 2$ the added term is $0$, so $c_0 = 1$, $c_1 = 2$ and $c_2 = 4$.
For $n = 3$ the added term is $t \cdot 3 \cdot 2 \cdot 1 = 6t$, so
$$c_3 = 8 + 6t, \qquad t = \frac{c - 8}{6}.$$
For $c = 7$ this gives $t = -\tfrac{1}{6}$.
Check: $c_3 = 8 + 6 \cdot \left(-\tfrac{1}{6}\right) = 7$, the value of rule B.
So a pattern in a few numbers is a conjecture, not a definition and not a proof.
Watch out: a long list of matching terms makes a rule plausible, but it never proves the rule.
