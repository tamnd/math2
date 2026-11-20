---
tag: ZMEQVXEZH8
kind: example
name: A Boolean algebra with disjunction as multiplication is not residuated
msc: ["03G15", "06E25"]
topics: [QYA4H5Y7VR]
audience: research
not_instance_of:
  - target: KCG48CWY69
    note: the residual of 0 by 1 does not exist, since 1 joined with anything is 1
uses: [NX61CKEYY9, 0XADJKM699]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_Boolean_algebra
    locator: Definition
---

## Example

Let $B$ be a [[Boolean algebra|0XADJKM699]] with $0 \ne 1$.
Put $x \cdot y = x \lor y$ and $e = 0$.

1. Boolean algebra. This is given.
2. Monoid. $\lor$ is associative, and $x \lor 0 = x = 0 \lor x$.
3. Residuation fails. The residual $1 \backslash 0$ would be the largest $y$ with $1 \lor y \le 0$.
4. But $1 \lor y = 1 \not\le 0$ for every $y$. So the set of such $y$ is empty, and $1 \backslash 0$ does not exist.

So $B$ with $\lor$ is not a [[residuated Boolean algebra|KCG48CWY69]]; see [[the definition|NX61CKEYY9]].

## Remarks

1. A residuated multiplication satisfies $x \cdot 0 = 0$. Here $1 \cdot 0 = 1 \lor 0 = 1 \ne 0$, which gives a second proof.
2. The multiplication $\lor$ preserves joins in each argument, but it does not preserve the empty join $0$. This is the exact point of failure.
3. Dually, $\lor$ with unit $0$ is a dual residuated multiplication: $x \lor y \ge z$ iff $y \ge z - x$, where $z - x = z \land \neg x$.

## Explanations

### L1 human

"Or" behaves badly as a multiplication here.
Once one side is "true", the result is "true" whatever the other side is.
So no element can bring "true or $y$" down to "false".

### L2 human

1. Take $B = \set{0, 1}$.
2. The candidates for $1 \backslash 0$ are the $y$ with $1 \lor y \le 0$.
3. For $y = 0$ and $y = 1$, $1 \lor y = 1$. So no candidate exists.

The typical use: the example shows that monotonicity and a unit are not enough for residuation.
The trap: $\lor$ is a monoid operation and preserves nonempty joins, but residuation needs the empty join too.
