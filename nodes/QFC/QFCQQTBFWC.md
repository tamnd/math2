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

Let $I$ be an open [[interval|0Q1D85B8G6]], and let $f \colon I \to \mathbb{R}$.
An [[antiderivative|0BYWRWFT4F]] of $f$ is a differentiable function $F \colon I \to \mathbb{R}$ with $F' = f$ on $I$.
Write $F \sim G$ when $F - G$ is a constant function on $I$; this is an equivalence relation.
We show that any two antiderivatives of $f$ satisfy $F \sim G$, so the antiderivative is unique [[up to|CBC72TX3NQ]] an added constant.

1. Let $F$ and $G$ be antiderivatives of $f$, and put $H = F - G$.
   Then $H$ is differentiable, and
   $$H' = F' - G' = f - f = 0 \quad \text{on } I.$$
2. Take points $x < y$ of $I$.
   The whole interval $[x, y]$ lies in $I$, because $I$ is an interval.
3. The function $H$ is continuous on $[x, y]$ and differentiable on $(x, y)$, so the [[mean value theorem|0BARQY52N5]] gives a point $c$ between $x$ and $y$ with
   $$H(y) - H(x) = H'(c)\,(y - x) = 0.$$
4. So $H(x) = H(y)$ for all $x, y \in I$, and $H$ equals a constant $C$.
5. So $F = G + C$, which means $F \sim G$.
   Conversely, $G + C$ is an antiderivative for every constant $C$, because the derivative of a constant is $0$.

So the antiderivatives of $f$ form exactly one equivalence class of $\sim$, whenever $f$ has one antiderivative.

## Remarks

The hypothesis "interval" is needed, and step 2 is where the proof uses it.
On $\mathbb{R} \setminus \{0\}$, the function equal to $0$ for $x < 0$ and to $1$ for $x > 0$ has derivative $0$ everywhere, but it is not constant.
So on $\mathbb{R} \setminus \{0\}$ the antiderivatives of $1/x$ are
$$F(x) = \begin{cases} \ln|x| + C_1, & x < 0, \\ \ln|x| + C_2, & x > 0, \end{cases}$$
with two independent constants, and they are unique only up to a locally constant function.

The notation $\int f(x) \, dx = F(x) + C$ names the whole class, and the "$+ C$" is the "up to a constant".
A condition $F(a) = 0$ for a fixed $a \in I$ picks one member of the class.
With it, "the antiderivative of $f$ that vanishes at $a$" is a legal definite description.

## Explanations

### L1 human

The functions $x^2$ and $x^2 + 5$ have the same rate of change at every point.
Adding a constant moves the graph up, but it does not change its steepness anywhere.
So when we look for a function with a given rate of change, we can find it only up to a constant.
That is why the answers in integration tables end with "$+ C$".

### L2 human

We find the antiderivative $F$ of $f(x) = 2x$ on $\mathbb{R}$ with $F(1) = 5$.
The function $x^2$ is one antiderivative, because $(x^2)' = 2x$.
By the result above, every antiderivative has the form $F(x) = x^2 + C$.
The condition gives
$$F(1) = 1 + C = 5, \qquad C = 4.$$
So $F(x) = x^2 + 4$, and no other function solves the problem.
Check: $F'(x) = 2x$ and $F(1) = 1 + 4 = 5$.
The typical use is to find one antiderivative, add $C$, and fix $C$ with one extra condition.
Watch out: on a domain that is not an interval, one condition does not fix all the constants, as the example of $1/x$ shows.
