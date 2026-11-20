---
tag: A815XEJAF7
kind: example
name: A scalar multiplication on R^2 that breaks only distributivity over scalars
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
not_instance_of:
  - target: 000AYPA9AJ
    fails: [8]
    note: with a(x, y) = (a^2 x, a^2 y), all axioms except (a + b)v = av + bv hold
uses: [05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: Definition and basic properties
---

## Example

Let $V = \R^2$ with the usual addition.
Define a scalar multiplication by $a \cdot (x, y) = (a^2 x, a^2 y)$ for $a \in \R$.
We check each axiom of the [[definition|05EGHEQZAW]] of a [[vector space|000AYPA9AJ]].

1. Closure: $(a^2 x, a^2 y) \in \R^2$.
2. Axioms 1 to 4 hold, because the addition is the usual one.
3. Axiom 5: $a \cdot (b \cdot v) = a^2 b^2 v$, and $(ab) \cdot v = (ab)^2 v = a^2 b^2 v$. It holds.
4. Axiom 6: $1 \cdot v = 1^2 v = v$. It holds.
5. Axiom 7: $a \cdot (u + v) = a^2(u + v) = a^2 u + a^2 v = a \cdot u + a \cdot v$. It holds.
6. Axiom 8 fails: take $a = b = 1$ and $v = (1, 0)$. Then $(1 + 1) \cdot v = (4, 0)$, while $1 \cdot v + 1 \cdot v = (2, 0)$.

So $V$ with these operations is not a vector space, and the only axiom that fails is axiom 8.

## Remarks

Here $a^2 v$ means the usual scalar multiple of $v$ by the number $a^2$.
The example shows that axiom 8 does not follow from the other seven.
Axiom 8 holds exactly when $(a + b)^2 = a^2 + b^2$, that is, when $2ab = 0$; this fails for $a = b = 1$.
Over the field $\mathbb{F}_2$ the same rule gives $a^2 = a$ for $a \in \set{0, 1}$, so it is the usual scalar multiplication and all axioms hold.

## Explanations

### L1 human

This rule scales a vector by the square of the number.
Scaling by $1$ and then by $1$ again, and adding, gives twice the vector.
Scaling once by $1 + 1 = 2$ gives four times the vector.
The two answers differ, so the rule is not allowed.

### L2 human

We test the failing axiom with $a = 2$, $b = 3$ and $v = (1, 1)$.

1. $(2 + 3) \cdot v = 25 v = (25, 25)$.
2. $2 \cdot v + 3 \cdot v = 4v + 9v = (13, 13)$.
3. The results differ, so axiom 8 fails.

A trap: the rule passes the tests $1 \cdot v = v$ and $a \cdot (b \cdot v) = (ab) \cdot v$, which are the ones that students often check first.
