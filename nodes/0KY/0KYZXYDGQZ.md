---
tag: 0KYZXYDGQZ
kind: statement
role: theorem
name: Quadratic formula
msc: [12D10]
uses: [0FRSR10DWF, 0YM6P6C206]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_formula
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quadratic_formula
    locator: Derivation by completing the square
same_as:
  wikidata: Q15909572
  wikipedia: Quadratic formula
---

## Statement

Let $a$, $b$ and $c$ be complex numbers with $a \neq 0$, and let $s$ be a complex number with $s^2 = b^2 - 4 a c$.
Then, for each complex number $x$,
$$a x^2 + b x + c = 0 \iff x = \frac{-b + s}{2 a} \text{ or } x = \frac{-b - s}{2 a}.$$

## Remarks

Such an $s$ exists, by the [[existence of nth roots|0YM6P6C206]] for $n = 2$.
The number $\Delta = b^2 - 4 a c$ is the discriminant. For real $a, b, c$, there are two real roots if $\Delta > 0$, one double real root if $\Delta = 0$, and two conjugate non-real roots if $\Delta < 0$.
The same formula holds in each field in which $2 \neq 0$.

## Explanations

### L1 human

The formula solves every quadratic equation.
For $x^2 + 2 x + 5 = 0$, the discriminant is $4 - 20 = -16$, so $s = 4 i$, and the roots are $-1 + 2 i$ and $-1 - 2 i$.
Completing the square proves the formula: the equation becomes $(2 a x + b)^2 = b^2 - 4 a c$.
