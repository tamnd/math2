---
tag: ~fc72b1ed
kind: example
name: Łukasiewicz implication defines maximum
msc: ["03B50", "03B52"]
topics: [WZP584JQ06]
audience: research
instance_of: [~ca73eab3]
uses: [~3e406741]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Definitions
---

## Example

In [[infinite-valued Łukasiewicz logic|~3e406741]], we compute the value of $(p \to q) \to q$ at $p = x$, $q = y$.

1. Case $x \le y$: $x \to y = \min(1, 1 - x + y) = 1$.
2. Then $1 \to y = \min(1, y) = y = \max(x, y)$.
3. Case $x > y$: $x \to y = 1 - x + y$, which is less than $1$.
4. Then $(1 - x + y) \to y = \min(1, 1 - (1 - x + y) + y) = \min(1, x) = x = \max(x, y)$.
5. So $(p \to q) \to q$ has value $\max(x, y)$ in both cases.

At $x = 0.3$, $y = 0.8$: $0.3 \to 0.8 = 1$ and $1 \to 0.8 = 0.8$.
At $x = 0.8$, $y = 0.3$: $0.8 \to 0.3 = 0.5$ and $0.5 \to 0.3 = 0.8$.

## Remarks

1. The value is symmetric in $p$ and $q$ although the formula is not; the third Łukasiewicz axiom expresses one half of this symmetry.
2. Wikipedia's MV-algebra article states the same fact as the identity $x \lor y = (x \to y) \to y$.
3. In Gödel logic the same formula fails: at $x = 0.8$, $y = 0.3$ it gives $0.3 \to 0.3 = 1$.

## Explanations

### L1 human

"If $p$ then $q$, then $q$" sounds odd, but in Łukasiewicz logic it means "$p$ or $q$".
Its value is the larger of the two values.
We check it in two cases: $p$ below $q$, and $p$ above $q$.

### L2 human

1. Split by the order of $x$ and $y$.
2. In each case, remove $\min$ by deciding which argument is smaller.
3. Simplify.

The typical use is to reduce the primitive connectives to $\neg$ and $\to$.
A trap: in the case $x > y$, the outer value is $\min(1, x)$, not $1$; the $\min$ only removes a value above $1$.
