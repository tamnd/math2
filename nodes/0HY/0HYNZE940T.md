---
tag: 0HYNZE940T
kind: statement
role: proposition
name: Modulus is multiplicative
msc: [30A99]
uses: [0KW2X0TFBX, 0ZB7J071WQ]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_value
    locator: Complex numbers
---

## Statement

For all complex numbers $z$ and $w$,
$$|z w| = |z| \, |w|,$$
where $|\cdot|$ is the [[modulus|0KW2X0TFBX]].

## Remarks

Proof: $|z w|^2 = z w \overline{z w} = (z \bar{z})(w \bar{w}) = |z|^2 |w|^2$, and both sides are nonnegative.
For $z = a + b i$ and $w = c + d i$, this is the identity $(a^2 + b^2)(c^2 + d^2) = (a c - b d)^2 + (a d + b c)^2$.
On the real numbers, it gives that the [[absolute value is multiplicative|0GMV7GP8W0]].

## Explanations

### L1 human

The length of a product is the product of the lengths.
For example, $|(1 + i)(1 - i)| = |2| = 2$, and $|1 + i| \cdot |1 - i| = \sqrt{2} \cdot \sqrt{2} = 2$.
