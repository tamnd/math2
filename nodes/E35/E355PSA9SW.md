---
tag: E355PSA9SW
kind: example
name: The complex field is definable in the real field
aliases: [complex-field-definable-in-real-field, c-in-r-interpretation]
msc: ["03C07", "03C64"]
topics: [SZRM3N6BXW]
audience: grad
instance_of: [7R0SJPH37J]
uses: [C5BWHPHAGA, 09FTAET5Z4, FSJ9NGRRPA, T7JW5QY6KR]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Definition
  - book: isbn:9780387987606
    locator: Section 1.3
---

## Example

Let $M = (\R, +, \cdot, 0, 1)$ and $N = (\C, +, \cdot, 0, 1)$, the field of [[complex numbers|09FTAET5Z4]].
We give a $2$-dimensional [[interpretation|C5BWHPHAGA]] of $N$ in $M$ without parameters, with $\varepsilon$ equal to equality.

- Domain: $\partial(x_1, x_2)$ is $x_1 = x_1$, so the domain is all of $\R^2$.
- Equality: $\varepsilon(\bar x, \bar y)$ is $x_1 = y_1 \wedge x_2 = y_2$.
- Addition: $\varphi_+(\bar x, \bar y, \bar z)$ is $z_1 = x_1 + y_1 \wedge z_2 = x_2 + y_2$.
- Multiplication: $\varphi_\times(\bar x, \bar y, \bar z)$ is $z_1 = x_1 y_1 - x_2 y_2 \wedge z_2 = x_1 y_2 + x_2 y_1$.
- Constants: $\varphi_0(\bar x)$ is $x_1 = 0 \wedge x_2 = 0$, and $\varphi_1(\bar x)$ is $x_1 = 1 \wedge x_2 = 0$.
- Coordinate map: $f(a, b) = a + b i$.

We check each condition.

1. Surjectivity and equality. Each complex number is $a + b i$ for exactly one pair $(a, b) \in \R^2$. So $f$ is a bijection, and $f(\bar a) = f(\bar b)$ exactly when $\bar a = \bar b$.
2. Addition. $(a + b i) + (c + d i) = (a + c) + (b + d) i$, which is $\varphi_+$.
3. Multiplication. $(a + b i)(c + d i) = a c + a d i + b c i + b d i^2 = (a c - b d) + (a d + b c) i$, since $i^2 = -1$. This is $\varphi_\times$.
4. Constants. $f(0, 0) = 0$ and $f(1, 0) = 1$.

So $\C$ is definable in $\R$ without parameters.
The formula $x_1 = 1$ uses the constant $1$ of the signature, and the subtraction in $\varphi_\times$ can be removed by writing $z_1 + x_2 y_2 = x_1 y_1$.

## Remarks

The interpretation defines more than the field structure of $\C$.
Complex conjugation is the $\emptyset$-definable map $(a, b) \mapsto (a, -b)$, and the real part is $(a, b) \mapsto (a, 0)$.
So the structure $(\C, +, \cdot, \bar{\cdot})$ with conjugation is also definable in $\R$, and in it the subfield $\R$ is definable as the set of fixed points of conjugation.

The reduction property sends each sentence about $\C$ to a sentence about $\R$.
By [[Tarski's quantifier elimination|FSJ9NGRRPA]], the theory of $\R$ is decidable, so the theory of $\C$ is decidable as well.
The converse fails: $\R$ is not interpretable in $\C$, even with parameters, since the theory of $\C$ is [[stable|T7JW5QY6KR]] and the order of $\R$, defined by $\exists z \, (y - x = z^2)$, has the order property.

The same formulas work for any field $K$ in which $-1$ is not a square, and they interpret the quadratic extension $K(\sqrt{-1})$ in $K$.
With $-1$ replaced by a non-square $c \in K$, they interpret $K(\sqrt c)$ in $K$ with the parameter $c$.

## Explanations

### L1 human

A complex number $a + b i$ is a pair of real numbers $(a, b)$.
Adding complex numbers adds the pairs entry by entry.
Multiplying them follows a fixed rule with real numbers only.
For example, $(1 + i)(1 + i) = 2 i$, and the rule turns the pairs $(1, 1)$ and $(1, 1)$ into $(1 \cdot 1 - 1 \cdot 1, 1 \cdot 1 + 1 \cdot 1) = (0, 2)$.
So statements about complex numbers become statements about real numbers.

### L2 human

We translate one sentence about $\C$ into a sentence about $\R$.

1. The sentence $\psi$ is $\exists y \, (y \cdot y + 1 = 0)$: the number $-1$ has a square root.
2. Replace $y$ by a pair $(y_1, y_2)$ and the quantifier by $\exists y_1 \, \exists y_2$.
3. The product $y \cdot y$ is the pair $(y_1^2 - y_2^2, 2 y_1 y_2)$, and adding $1$ adds $1$ to the first entry.
4. The translation $\psi_\Gamma$ is $\exists y_1 \, \exists y_2 \, (y_1^2 - y_2^2 + 1 = 0 \wedge 2 y_1 y_2 = 0)$.
5. In $\R$, the pair $(0, 1)$ is a witness, so $\psi_\Gamma$ is true, and $\psi$ is true in $\C$, with witness $i$.

The typical use is to decide sentences about $\C$ by the decision method for $\R$.
A trap is to translate $\exists y$ into one real quantifier: each element of $\C$ needs two real coordinates.
