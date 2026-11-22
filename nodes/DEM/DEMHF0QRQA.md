---
tag: DEMHF0QRQA
kind: example
name: The square root of minus one is not unique
msc: ["00A35", "12E99"]
topics: [BP0WAF23HB]
audience: ug1
not_instance_of:
  - target: 5P955TVSS2
    note: two complex numbers satisfy the condition, and no algebraic property of the field selects one of them
uses: [5P955TVSS2, 09FTAET5Z4, 0ESCX36MMC, 0FTH2E9TAS, DSQ17TNW1C]
sources:
  - url: https://en.wikipedia.org/wiki/Imaginary_unit
    locator: i vs. −i
---

## Example

Consider the phrase "the complex number $z$ with $z^2 = -1$".
We show that it is not a legal [[definite description|5P955TVSS2]] in the field $\mathbb{C}$ of [[complex numbers|09FTAET5Z4]].

1. Existence holds.
   Write $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$ with $i^2 = -1$, so $i$ satisfies $z^2 = -1$.
2. Uniqueness fails.
   The number $-i$ also satisfies the equation:
   $$(-i)^2 = (-1)^2 \, i^2 = 1 \cdot (-1) = -1.$$
3. The two solutions differ, because $i - (-i) = 2i \ne 0$.
   So "the" does not pick one of them.
4. No extra algebraic condition can pick one.
   [[Complex conjugation|0FTH2E9TAS]], $a + bi \mapsto a - bi$, is a field [[automorphism|DSQ17TNW1C]] of $\mathbb{C}$ that fixes every real number and sends $i$ to $-i$.
5. So every condition built from addition, multiplication and real constants that $i$ satisfies, $-i$ satisfies too.

## Remarks

The [[imaginary unit|0ESCX36MMC]] $i$ comes from a choice, not from a definite description.
A construction such as $\mathbb{C} = \mathbb{R}^2$ with $i = (0, 1)$ names one solution, but the other solution $(0, -1)$ would serve equally well, and every theorem would stay true with $i$ and $-i$ exchanged.

In $\mathbb{R}$, the extra condition "non-negative" makes "the square root of $4$" legal and picks $2$.
No such condition exists in $\mathbb{C}$, because $\mathbb{C}$ has no order that is compatible with its field operations.
This has a cost.
The real rule $\sqrt{a} \sqrt{b} = \sqrt{ab}$ for $a, b \ge 0$ fails if we force $\sqrt{-1} = i$ and apply it to negative numbers:
$$-1 = i \cdot i = \sqrt{-1} \, \sqrt{-1} \ne \sqrt{(-1)(-1)} = \sqrt{1} = 1.$$

## Explanations

### L1 human

The number $4$ has two square roots, $2$ and $-2$.
For positive numbers we agree that "the" square root is the positive one.
The number $-1$ also has two square roots, called $i$ and $-i$.
But neither of them is positive or negative, so the same agreement does not work.
In fact the two numbers behave in exactly the same way, so no rule of arithmetic tells them apart.

### L2 human

We check step 5 for polynomial equations with real coefficients.
Let $p(z) = c_n z^n + \dots + c_1 z + c_0$ with real $c_k$, and suppose $p(i) = 0$.
Conjugation preserves sums and products and fixes each real $c_k$, so
$$0 = \overline{p(i)} = c_n \, \bar{i}^{\,n} + \dots + c_1 \, \bar{i} + c_0 = p(-i).$$
So every real polynomial equation that $i$ solves, $-i$ solves too.
For example, $i$ is a root of $z^4 - 1$, and $(-i)^4 = 1$ as well.
Watch out: "$i$ is the root above the real axis" picks one root, but it uses a picture of the plane, not the field operations, so it is a convention and not a definition.
