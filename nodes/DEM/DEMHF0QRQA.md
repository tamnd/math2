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
We show that this is not a legal [[definite description|5P955TVSS2]] in the field $\mathbb{C}$ of [[complex numbers|09FTAET5Z4]].

1. Existence holds: with $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$ and $i^2 = -1$, the number $i$ satisfies $z^2 = -1$.
2. Uniqueness fails: $(-i)^2 = (-1)^2 i^2 = -1$, so $-i$ also satisfies $z^2 = -1$.
3. The two numbers differ: $i - (-i) = 2i \neq 0$.
4. So the condition $z^2 = -1$ has two solutions, and "the" does not pick one of them.
5. No added algebraic condition can pick one. The [[complex conjugation|0FTH2E9TAS]] $a + bi \mapsto a - bi$ is a field [[automorphism|DSQ17TNW1C]] of $\mathbb{C}$ that fixes $\mathbb{R}$ and exchanges $i$ and $-i$.
6. So each condition built from addition, multiplication and real numbers that $i$ satisfies is also satisfied by $-i$.

## Remarks

1. The [[imaginary unit|0ESCX36MMC]] $i$ is introduced by a choice, not by a definite description. A construction such as $\mathbb{C} = \mathbb{R}^2$ with $i = (0, 1)$ names one solution, but the other solution would serve equally well.
2. In $\mathbb{R}$, "the square root of $4$" is made legal by the extra condition "non-negative". No such condition exists in $\mathbb{C}$, because $\mathbb{C}$ has no order compatible with its field operations.
3. The rule $\sqrt{a}\sqrt{b} = \sqrt{ab}$ for real $a, b \geq 0$ does not extend to a fixed choice $\sqrt{-1} = i$. The extension would give $-1 = i \cdot i = \sqrt{(-1)(-1)} = \sqrt{1} = 1$.

## Explanations

### L1 human

The number $4$ has two square roots, $2$ and $-2$.
For positive numbers, we agree that "the" square root is the positive one.
The number $-1$ also has two square roots, called $i$ and $-i$.
But neither of them is positive or negative, so the same agreement does not work.
In fact the two numbers behave in exactly the same way, so no rule of arithmetic can tell them apart.

### L2 human

We check that conjugation preserves each polynomial equation with real coefficients.

1. Let $p(z) = c_n z^n + \dots + c_1 z + c_0$ with real numbers $c_k$, and suppose $p(i) = 0$.
2. Conjugation preserves sums and products, and it fixes each real number.
3. So $\overline{p(i)} = c_n \bar{i}^n + \dots + c_1 \bar{i} + c_0 = p(-i)$.
4. Since $p(i) = 0$ and $\bar{0} = 0$, we get $p(-i) = 0$.

So no real polynomial equation separates $i$ from $-i$.
A trap is to use a picture: "$i$ is the root above the real axis" uses the plane, not the field operations, and it is a convention.
