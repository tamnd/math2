---
tag: QHDDWVK1NJ
kind: example
name: Square roots of positive numbers as a first-order sentence
msc: ["03B10", "12J15"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [086QKPF0A6]
uses: [086QKPF0A6, WDVVEYD6AT, DKFGQTRYZE, 0P3VCBDEE2, DDY3Q3PJ6W]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Syntax
  - url: https://en.wikipedia.org/wiki/Real_closed_field
    locator: lead section
---

## Example

One short [[first-order|086QKPF0A6]] sentence tells the real numbers apart from the rational numbers.
Take the [[signature|WDVVEYD6AT]] $\sigma = \{ +, \cdot, -, 0, 1, < \}$ of [[ordered fields|0P3VCBDEE2]], and let $\mathrm{Sq}$ be
$$\forall x \, \big(0 < x \to \exists y \, (y \cdot y = x)\big).$$
We check that $\mathrm{Sq}$ is a first-order [[sentence|DKFGQTRYZE]], that it is true in $\mathbb{R}$, and that it is false in $\mathbb{Q}$.

1. The strings $0 < x$ and $y \cdot y = x$ are atomic formulas.
   Here $<$ is a binary relation symbol, $=$ is the equality symbol, and $0$, $x$ and $y \cdot y$ are terms.
2. The quantifier $\exists y$ applied to $y \cdot y = x$ gives a formula, and $\to$ joins it to $0 < x$.
3. The quantifier $\forall x$ applied to the whole gives a formula, and both quantifiers range over elements, so the formula is first-order.
4. The variable $y$ is bound by $\exists y$, and $x$ is bound by $\forall x$, so no variable is free and $\mathrm{Sq}$ is a sentence.
5. In $\mathbb{R}$, let $a > 0$; the number $b = \sqrt{a}$ is real and $b \cdot b = a$, so $\mathbb{R}$ satisfies $\mathrm{Sq}$.
6. In $\mathbb{Q}$, take $x = 2$, so $0 < 2$ holds.
   Suppose $(p/q)^2 = 2$ with integers $p, q$, $q \neq 0$ and $\gcd(p, q) = 1$.
   Then $p^2 = 2q^2$, so $p$ is even, say $p = 2k$.
   Then $4k^2 = 2q^2$, so $q^2 = 2k^2$ and $q$ is even too, against $\gcd(p, q) = 1$.
7. So no rational $y$ has $y \cdot y = 2$, and $\mathbb{Q}$ does not satisfy $\mathrm{Sq}$.

## Remarks

The guard $0 < x$ matters.
Without it, $\forall x \, \exists y \, (y \cdot y = x)$ is false in $\mathbb{R}$, since $y \cdot y = -1$ has no real solution.
That shorter sentence is true in $\mathbb{C}$, but $\mathbb{C}$ has no field order, so there it lives in the signature of fields without $<$.

The proof of step 5 uses the completeness of $\mathbb{R}$, for example through the intermediate value theorem for $y \mapsto y^2$.
The sentence itself does not mention completeness, and it holds in smaller fields too.
It is one of the axioms of [[real closed fields|DDY3Q3PJ6W]], together with one sentence for each odd $n$ that says every monic polynomial of degree $n$ has a root.
Those axioms hold in $\mathbb{R}$ and also in the countable field of real algebraic numbers.

## Explanations

### L1 human

The sentence says: "every positive number has a square root".
It talks only about numbers, so it is a first-order sentence.
It is true for the real numbers: the square root of $2$ is about $1.414$.
It is false for the fractions: no fraction times itself gives exactly $2$.
So the same sentence can be true in one number system and false in another.

### L2 human

We read the sentence in the ordered field $\mathbb{Q}(\sqrt{2})$ of the numbers $a + b\sqrt{2}$ with $a, b \in \mathbb{Q}$, ordered as real numbers.
Here $2$ has a square root, namely $\sqrt{2}$, so the witness from $\mathbb{Q}$ no longer works.
Try $x = 3$ instead, and suppose $(a + b\sqrt{2})^2 = 3$.
Expanding and comparing the rational part and the $\sqrt{2}$ part gives
$$a^2 + 2b^2 = 3, \qquad 2ab = 0.$$
If $b = 0$, then $a^2 = 3$, which has no rational solution by the argument of step 6 with the prime $3$.
If $a = 0$, then $2b^2 = 3$, so $(2b)^2 = 6$, which has no rational solution by the same argument with the prime $2$.
So $\mathrm{Sq}$ is false in $\mathbb{Q}(\sqrt{2})$, with the witness $x = 3$.
The typical use of such a sentence is to show that two structures are not elementarily equivalent.
Watch out: a sentence is true or false only in a fixed structure, so "$\mathrm{Sq}$ is true" means nothing until the structure is named.
