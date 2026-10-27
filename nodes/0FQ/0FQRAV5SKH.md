---
tag: 0FQRAV5SKH
kind: statement
role: proposition
name: Inverse of a complex number
msc: [12D99]
uses: [0ZB7J071WQ, 0FRSR10DWF]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_number
    locator: Complex conjugate, absolute value, argument and division
inventory: [S5RZYX8ENN]
---

## Statement

Let $z$ be a complex number with $z \neq 0$.
Then
$$z^{-1} = \frac{\bar{z}}{|z|^2}.$$
With $z = a + b i$ and $a, b$ real, this is $z^{-1} = \dfrac{a}{a^2 + b^2} - \dfrac{b}{a^2 + b^2} \, i$.

## Remarks

Proof: $z \bar{z} = |z|^2$ by the formula for [[a complex number times its conjugate|0ZB7J071WQ]], and $|z|^2 > 0$ because $z \neq 0$. Divide by $|z|^2$.
To compute a quotient $w / z$, multiply the numerator and the denominator by $\bar{z}$.

## Explanations

### L1 human

To divide by a complex number, multiply above and below by its conjugate. Then the denominator becomes a positive real number.
For example, $\dfrac{1}{1 + i} = \dfrac{1 - i}{(1 + i)(1 - i)} = \dfrac{1 - i}{2}$.
