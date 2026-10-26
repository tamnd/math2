---
tag: 0KBEMAJAYA
kind: statement
role: theorem
name: Distributive law
aliases: [distributivity-of-multiplication-over-addition]
msc: [03F30]
uses: [0W5DSDFQ4G, 0JRC32D6K2, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Distributive_property
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Natural_number
    locator: Relationship between addition and multiplication
---

## Statement

For all natural numbers $a$, $b$ and $c$, $a \cdot (b + c) = a \cdot b + a \cdot c$.
Here $+$ is the [[addition|0W5DSDFQ4G]] and $\cdot$ is the [[multiplication|0JRC32D6K2]] of natural numbers.

## Remarks

This is the left distributive law. With commutativity of multiplication, it gives the right law $(b + c) \cdot a = b \cdot a + c \cdot a$.
The proof from the recursive definitions uses [[induction|0ASJVEFA9J]] on $c$.
The same law holds in the integers, the rationals, the reals and the complex numbers.

## Explanations

### L1 human

To multiply a number by a sum, you can multiply it by each part and then add.
For example, $3 \cdot (10 + 2) = 30 + 6 = 36$, and this is how many people compute $3 \cdot 12$.
