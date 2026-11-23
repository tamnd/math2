---
tag: TCJZNK8PT2
kind: example
name: The order is definable in the field of reals
msc: ["03C07", "12D15"]
topics: [NJDME6F845, AY09KYSW81]
audience: ug2
instance_of: [CY1TXHF6KQ]
uses: [1DQ1M6ZWS4, 08J2M1JYAG, 1WTCZB4DVB]
sources:
  - url: https://en.wikipedia.org/wiki/Definable_set
    locator: lead section
---

## Example

Let $\mathcal{R} = (\mathbb{R}, +, \cdot, 0, 1)$ be the field of [[real numbers|08J2M1JYAG]], in a signature with no symbol for the order, and let
$$\varphi(x, y) = \exists z \, (\neg (z = 0) \wedge x + z \cdot z = y).$$
We show that $\varphi$ defines the strict order: for all $a, b \in \mathbb{R}$, $\mathcal{R} \models \varphi[a, b]$ holds if and only if $a < b$.

1. Suppose $a < b$.
   Then $b - a > 0$, so $c = \sqrt{b - a}$ is a real number with $c \ne 0$.
2. Then $a + c \cdot c = a + (b - a) = b$, so the value $c$ for $z$ witnesses $\varphi[a, b]$.
3. Conversely, suppose that $c \ne 0$ and $a + c \cdot c = b$.
4. Then $b - a = c^2 > 0$, because the square of a nonzero real is positive.
   So $a < b$.

So the order $<$ is a [[definable relation|1DQ1M6ZWS4]] of $\mathcal{R}$ without parameters.

## Remarks

Step 1 uses that every positive real has a square root, and over the rationals this fails.
In $(\mathbb{Q}, +, \cdot, 0, 1)$ the same formula defines a smaller relation: $\varphi[0, 2]$ fails, because $2$ is not the square of a rational, although $0 < 2$.
Over $\mathbb{R}$, adding $<$ to the signature gives no new definable relations, since each use of $x < y$ can be replaced by $\varphi(x, y)$.
For the same reason every automorphism of the field $\mathbb{R}$ preserves the order, and from this one shows that the identity is the only automorphism of the field $\mathbb{R}$.

## Explanations

### L1 human

In the real numbers, $a$ is less than $b$ exactly when you get from $a$ to $b$ by adding a positive number.
The positive numbers are exactly the squares of nonzero numbers.
So "less than" can be written with plus and times alone.

### L2 human

We check the formula on two pairs.
For $(1, 5)$, take $z \mapsto 2$: then $2 \ne 0$ and
$$1 + 2 \cdot 2 = 5,$$
so $\varphi[1, 5]$ holds, and indeed $1 < 5$.
For $(3, 3)$, a witness would need $3 + z \cdot z = 3$, so $z \cdot z = 0$ and $z = 0$, which the formula excludes, so $\varphi[3, 3]$ fails.
So any formula about real numbers that uses $<$ can be rewritten with $+$ and $\cdot$ alone.
Watch out: if you omit $\neg (z = 0)$, the formula defines $\le$ instead of $<$.
