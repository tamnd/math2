---
tag: T2TBP1SA2T
kind: example
name: The rational field is interpretable in the ring of integers
aliases: [rationals-interpretable-in-integers, q-in-z-interpretation]
msc: ["03C07", "11U09"]
topics: [SZRM3N6BXW]
audience: grad
instance_of: [7R0SJPH37J]
uses: [C5BWHPHAGA, 0F2PTGX1A2, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Example
  - book: isbn:9780387987606
    locator: Section 1.3
---

## Example

Let $M = (\Z, +, \cdot, 0, 1)$ and $N = (\Q, +, \cdot, 0, 1)$.
We give a $2$-dimensional [[interpretation|C5BWHPHAGA]] of $N$ in $M$ without parameters.
This is the construction of $\Q$ as the [[field of fractions|0F2PTGX1A2]] of $\Z$, written in first-order [[formulas|HYJ10AF6RT]].

- Domain: $\partial(x_1, x_2)$ is $\neg\, x_2 = 0$.
- Equality: $\varepsilon(x_1, x_2, y_1, y_2)$ is $x_1 \cdot y_2 = y_1 \cdot x_2$.
- Addition: $\varphi_+(\bar x, \bar y, \bar z)$ is $z_1 \cdot (x_2 \cdot y_2) = (x_1 \cdot y_2 + y_1 \cdot x_2) \cdot z_2$.
- Multiplication: $\varphi_\times(\bar x, \bar y, \bar z)$ is $z_1 \cdot (x_2 \cdot y_2) = (x_1 \cdot y_1) \cdot z_2$.
- Constants: $\varphi_0(\bar x)$ is $x_1 = 0$, and $\varphi_1(\bar x)$ is $x_1 = x_2$.
- Coordinate map: $f(a, b) = a / b$ for $a, b \in \Z$ with $b \neq 0$.

We check each condition, for pairs $(a, b), (c, d), (g, h)$ in the domain, so $b, d, h \neq 0$.

1. Surjectivity. Each rational number is $a / b$ with $b \neq 0$, so $f$ is onto $\Q$.
2. Equality. $a / b = c / d$ holds in $\Q$ exactly when $a d = c b$ holds in $\Z$, by multiplying both sides by $b d \neq 0$.
3. Addition. In $\Q$, $a/b + c/d = (a d + c b)/(b d)$. So $a/b + c/d = g/h$ exactly when $(a d + c b) h = g (b d)$, which is $\varphi_+$.
4. Multiplication. In $\Q$, $(a/b)(c/d) = (a c)/(b d)$. So the product is $g/h$ exactly when $a c h = g b d$, which is $\varphi_\times$.
5. Constants. $a / b = 0$ exactly when $a = 0$, and $a / b = 1$ exactly when $a = b$.

So all the conditions of the definition hold, and $\Q$ is interpretable in $\Z$ without parameters.

## Remarks

The formula $\varepsilon$ is not equality, so this interpretation is not a definition of $\Q$ in $\Z$.
The equality condition makes $\varepsilon$ an equivalence relation on the domain.
A direct check of transitivity uses that $\Z$ has no zero divisors: from $a d = c b$ and $c h = g d$ we get $d (a h - g b) = 0$, and $d \neq 0$ gives $a h = g b$.

The same formulas interpret the field of fractions of any integral domain $R$ in $R$.
They work in every model of the theory of integral domains, because each check above uses only the axioms of integral domains.
If the domain formula is dropped, transitivity fails; see [[this non-example|ZRFSPE7TCQ]].

The reduction property gives a translation of each sentence about $\Q$ into a sentence about $\Z$.
The converse also holds: Julia Robinson showed that $\Z$ is definable in the field $\Q$, so the two structures are interpretable in each other.

## Explanations

### L1 human

Every fraction is a pair of whole numbers, the top and the bottom, with a bottom that is not zero.
Two pairs give the same fraction when "cross-multiplication" gives equal numbers.
For example, $(1, 2)$ and $(3, 6)$ give the same fraction, because $1 \cdot 6 = 3 \cdot 2$.
Adding and multiplying fractions are rules about the top and the bottom.
So everything about fractions can be said in terms of whole numbers.

### L2 human

We check one instance of the addition formula.

1. Take $\bar x = (1, 2)$, $\bar y = (1, 3)$ and $\bar z = (5, 6)$.
2. The left side of $\varphi_+$ is $5 \cdot (2 \cdot 3) = 30$.
3. The right side is $(1 \cdot 3 + 1 \cdot 2) \cdot 6 = 5 \cdot 6 = 30$.
4. So $\varphi_+$ holds, and indeed $1/2 + 1/3 = 5/6$.
5. With $\bar z = (10, 12)$ the formula also holds, since $10 \cdot 6 = 5 \cdot 12$. The formula is invariant under $\varepsilon$, as it must be.

The typical use is to transfer facts about $\Z$ to facts about $\Q$.
A trap is to write the addition formula as $z_1 = x_1 y_2 + y_1 x_2 \wedge z_2 = x_2 y_2$.
This formula picks one representative of the sum, so it is not invariant under $\varepsilon$, and the relations condition fails for $\bar z = (10, 12)$.
