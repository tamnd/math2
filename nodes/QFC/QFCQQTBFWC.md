---
tag: QFCQQTBFWC
kind: example
name: Antiderivatives on an interval are unique up to a constant
msc: ["00A35", "26A36"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [CBC72TX3NQ]
uses: [CBC72TX3NQ, 0BYWRWFT4F, 0V1EJCT8G6, 0BARQY52N5, 0Q1D85B8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Antiderivative
    locator: Uses and properties
---

## Example

Let $I$ be an open [[interval|0Q1D85B8G6]], and let $f : I \to \mathbb{R}$.
An [[antiderivative|0BYWRWFT4F]] of $f$ is a differentiable function $F$ with $F' = f$ on $I$.
We show that two antiderivatives differ by a constant, so the antiderivative is unique [[up to|CBC72TX3NQ]] a constant.

1. Let $F$ and $G$ be antiderivatives of $f$, and let $H = F - G$.
2. Then $H$ is differentiable, and $H' = F' - G' = f - f = 0$ on $I$.
3. Let $x < y$ be points of $I$. The interval $[x, y]$ lies in $I$, because $I$ is an interval.
4. By the [[mean value theorem|0BARQY52N5]], there is a $c$ between $x$ and $y$ with $H(y) - H(x) = H'(c)(y - x) = 0$.
5. So $H(x) = H(y)$ for all $x$ and $y$ in $I$, and $H$ is a constant $C$.
6. So $F = G + C$. Conversely, $G + C$ is an antiderivative for each constant $C$.

The relation is $F \sim G$ when $F - G$ is constant, and the antiderivatives of $f$ form exactly one class.

## Remarks

1. The hypothesis "interval" is needed. On $\mathbb{R} \setminus \{0\}$, the function equal to $0$ for $x < 0$ and to $1$ for $x > 0$ has derivative $0$, but it is not constant.
2. So on $\mathbb{R} \setminus \{0\}$, the antiderivatives of $1/x$ have the form $\ln\abs{x} + C_1$ for $x < 0$ and $\ln\abs{x} + C_2$ for $x > 0$, with two independent constants.
3. The notation $\int f(x)\, dx = F(x) + C$ names the whole class. The "$+ C$" is the "up to a constant".
4. The condition $F(a) = 0$ for a fixed $a \in I$ picks one representative. With it, "the" antiderivative is legal.

## Explanations

### L1 human

The functions $x^2$ and $x^2 + 5$ have the same rate of change at every point.
Adding a constant moves the graph up, but it does not change its steepness anywhere.
So when we look for a function with a given rate of change, we can find it only up to a constant.
That is why the answers in integration tables end with "$+ C$".

### L2 human

We find the antiderivative $F$ of $f(x) = 2x$ on $\mathbb{R}$ with $F(1) = 5$.

1. The function $x^2$ is an antiderivative, because $(x^2)' = 2x$.
2. By the theorem, each antiderivative has the form $F(x) = x^2 + C$.
3. The condition $F(1) = 5$ gives $1 + C = 5$, so $C = 4$.
4. So $F(x) = x^2 + 4$, and this is the only solution.

The typical use: find one antiderivative, add $C$, and fix $C$ with an extra condition.
A trap is a domain that is not an interval, as remark 1 shows.
