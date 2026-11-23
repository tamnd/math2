---
tag: DG496EV8FE
kind: example
name: Łukasiewicz implication defines maximum
msc: ["03B50", "03B52"]
topics: [WZP584JQ06]
audience: research
instance_of: [NFCEM44XYH]
uses: [JQ713VVD0G]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Definitions
---

## Example

In [[infinite-valued Łukasiewicz logic|JQ713VVD0G]], we compute the value of $(p \to q) \to q$ at $v(p) = x$ and $v(q) = y$.
Recall that $x \to y = \min(1, 1 - x + y)$.

1. Suppose $x \le y$.
   Then $1 - x + y \ge 1$, so $x \to y = 1$.
2. In this case the outer implication is $1 \to y = \min(1, y) = y$, and $y = \max(x, y)$.
3. Suppose $x > y$.
   Then $1 - x + y < 1$, so $x \to y = 1 - x + y$.
4. In this case the outer implication is $\min(1, 1 - (1 - x + y) + y) = \min(1, x) = x$, and $x = \max(x, y)$.
5. So $(p \to q) \to q$ has the value $\max(x, y)$ in both cases.

Check at $x = 0.3$ and $y = 0.8$: $0.3 \to 0.8 = 1$ and $1 \to 0.8 = 0.8$.
Check at $x = 0.8$ and $y = 0.3$: $0.8 \to 0.3 = 0.5$ and $0.5 \to 0.3 = 0.8$.

## Remarks

The value is symmetric in $p$ and $q$, although the formula is not.
The third Łukasiewicz axiom, $((p \to q) \to q) \to ((q \to p) \to p)$, states one direction of this symmetry.
In MV-algebras the same fact appears as the identity $x \lor y = (x \to y) \to y$, so $\lor$ need not be a primitive connective.

The identity depends on the Łukasiewicz implication.
In Gödel logic, $x \to y$ is $1$ when $x \le y$ and $y$ otherwise.
At $x = 0.8$ and $y = 0.3$ this gives $0.8 \to 0.3 = 0.3$, and then $0.3 \to 0.3 = 1$, not $0.8$.

## Explanations

### L1 human

"If $p$ then $q$, then $q$" sounds odd, but in Łukasiewicz logic it means "$p$ or $q$".
Its value is the larger of the two values.
We check it in two cases: $p$ below $q$, and $p$ above $q$.

### L2 human

The method is a split by cases.
First decide the order of $x$ and $y$.
In each case remove each $\min$ by deciding which argument is smaller, and then simplify.
This is the typical way to reduce the primitive connectives of Łukasiewicz logic to $\neg$ and $\to$.
Watch out: in the case $x > y$, the outer value is $\min(1, x) = x$, not $1$.
The $\min$ only cuts values above $1$, and $x$ is not above $1$.
