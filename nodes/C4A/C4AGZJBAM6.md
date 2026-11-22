---
tag: C4AGZJBAM6
kind: example
name: A scalar multiplication on R^2 that breaks only the unit law
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
not_instance_of:
  - target: 000AYPA9AJ
    fails: [6]
    note: with a(x, y) = (ax, 0), axioms 1 to 5, 7 and 8 hold, and 1(0, 1) = (0, 0) is not (0, 1)
uses: [05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Two, Section I
---

## Example

Let $V = \mathbb{R}^2$ with the usual addition $(x, y) + (x', y') = (x + x', y + y')$.
Define a new scalar multiplication that scales the first entry and throws away the second:
$$a \cdot (x, y) = (ax, 0) \qquad (a \in \mathbb{R}).$$
We check each axiom of the [[definition|05EGHEQZAW]] of a [[vector space|000AYPA9AJ]].

1. Closure: $(ax, 0)$ is again in $\mathbb{R}^2$.
2. Axioms 1 to 4 concern only the addition, which is the usual one, so they hold, with zero $(0, 0)$ and $-(x, y) = (-x, -y)$.
3. Axiom 5 holds: $a \cdot (b \cdot (x, y)) = a \cdot (bx, 0) = (abx, 0)$, and $(ab) \cdot (x, y) = (abx, 0)$.
4. Axiom 6 fails: $1 \cdot (0, 1) = (0, 0)$, which is not $(0, 1)$.
5. Axiom 7 holds: $a \cdot ((x, y) + (x', y')) = (a(x + x'), 0)$, and $a \cdot (x, y) + a \cdot (x', y') = (ax + ax', 0)$.
6. Axiom 8 holds: $(a + b) \cdot (x, y) = ((a + b)x, 0)$, and $a \cdot (x, y) + b \cdot (x, y) = (ax + bx, 0)$.

So $V$ with these operations is not a vector space, and axiom 6 is the only axiom that fails.

## Remarks

The example shows that the unit law $1v = v$ does not follow from the other seven axioms.
Without it the definition would even allow the rule $a \cdot v = 0$ for all $a$ and $v$, which carries no information about the scalars.

Small changes to the rule show how the axioms interact.
With $a \cdot (x, y) = (ax, ay)$ we get back the usual space $\mathbb{R}^2$.
With $a \cdot (x, y) = (ax, y)$ the unit law holds, but axiom 8 fails:
$$(1 + 1) \cdot (0, 1) = (0, 1), \qquad 1 \cdot (0, 1) + 1 \cdot (0, 1) = (0, 2).$$
So keeping the second entry repairs axiom 6 and breaks axiom 8 instead.

## Explanations

### L1 human

This rule for scaling throws away the second entry of every vector.
Scaling by $1$ should change nothing, but here it turns $(0, 1)$ into $(0, 0)$.
All the other rules still work, so the rule "scaling by $1$ changes nothing" must be listed on its own.

### L2 human

We test the failing axiom and one axiom that holds, with $v = (2, 3)$.
The unit law fails, since the second entry is lost:
$$1 \cdot (2, 3) = (2, 0) \ne (2, 3).$$
Axiom 8 with $a = 1$ and $b = 2$ holds, since both sides keep only the first entry:
$$3 \cdot (2, 3) = (6, 0), \qquad 1 \cdot (2, 3) + 2 \cdot (2, 3) = (2, 0) + (4, 0) = (6, 0).$$
Watch out: checking only the axioms that look interesting can miss a failure, so every axiom must be checked.
