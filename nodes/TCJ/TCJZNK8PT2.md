---
tag: TCJZNK8PT2
kind: example
name: The order is definable in the field of reals
msc: ["03C07", "12D15"]
topics: [NJDME6F845]
audience: ug2
instance_of: [CY1TXHF6KQ]
uses: [1DQ1M6ZWS4, 08J2M1JYAG, 1WTCZB4DVB]
sources:
  - url: https://en.wikipedia.org/wiki/Definable_set
    locator: lead section
---

## Example

Let $\mathcal{R} = (\R, +, \cdot, 0, 1)$ be the field of [[real numbers|08J2M1JYAG]], in the signature with no symbol for the order.
Let
$$\varphi(x, y) = \exists z \, (\neg (z = 0) \wedge x + z \cdot z = y).$$
We show that $\varphi$ defines the strict order: for all $a, b \in \R$, $\mathcal{R} \models \varphi[a, b]$ if and only if $a < b$.

1. Suppose $a < b$. Then $b - a > 0$, so $c = \sqrt{b - a}$ is a real number with $c \neq 0$.
2. Then $a + c \cdot c = a + (b - a) = b$, so $z \mapsto c$ witnesses $\varphi[a, b]$.
3. Conversely, suppose $c \neq 0$ and $a + c \cdot c = b$.
4. Then $b - a = c^2 > 0$, because the square of a nonzero real is positive. So $a < b$.

So the order $<$ is a [[definable relation|1DQ1M6ZWS4]] in $\mathcal{R}$ without parameters.

## Remarks

The proof uses that every positive real has a square root; in the field $\Q$, the same formula defines a smaller relation.
For example, $\mathcal{Q} \not\models \varphi[0, 2]$ in $(\Q, +, \cdot, 0, 1)$, because $2$ is not the square of a rational, although $0 < 2$.
So adding $<$ to the signature of $\mathcal{R}$ gives no new definable relations: each use of $x < y$ can be replaced by $\varphi(x, y)$.
Every automorphism of the field $\R$ preserves the order for this reason, and from this one shows that the identity is the only automorphism of the field $\R$.

## Explanations

### L1 human

In the real numbers, $a$ is less than $b$ exactly when you get from $a$ to $b$ by adding a positive number.
Positive numbers are the nonzero squares.
So "less than" can be written using only plus and times.

### L2 human

We check the formula on two pairs.

1. For $(a, b) = (1, 5)$, take $z \mapsto 2$: $2 \neq 0$ and $1 + 2 \cdot 2 = 5$. So $\varphi[1, 5]$ holds, and $1 < 5$.
2. For $(a, b) = (3, 3)$, a witness would need $z \cdot z = 0$, so $z = 0$, which the formula excludes. So $\varphi[3, 3]$ fails.

The typical use is to remove the order symbol from a formula about real numbers.
A trap is to omit $\neg (z = 0)$; then the formula defines $\leq$ instead of $<$.
