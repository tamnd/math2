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

Let $V = \mathbb{R}^2$ with the usual addition.
Define a new scalar multiplication that scales by the square of the scalar:
$$a \cdot (x, y) = (a^2 x, a^2 y) \qquad (a \in \mathbb{R}).$$
Below, $a^2 v$ means the usual multiple of $v$ by the number $a^2$.
We check each axiom of the [[definition|05EGHEQZAW]] of a [[vector space|000AYPA9AJ]].

1. Closure: $(a^2 x, a^2 y)$ is again in $\mathbb{R}^2$.
2. Axioms 1 to 4 concern only the addition, which is the usual one, so they hold.
3. Axiom 5 holds: $a \cdot (b \cdot v) = a^2 (b^2 v) = a^2 b^2 v$, and $(ab) \cdot v = (ab)^2 v = a^2 b^2 v$.
4. Axiom 6 holds: $1 \cdot v = 1^2 v = v$.
5. Axiom 7 holds: $a \cdot (u + v) = a^2 (u + v) = a^2 u + a^2 v = a \cdot u + a \cdot v$.
6. Axiom 8 fails. Take $a = b = 1$ and $v = (1, 0)$. Then
$$(1 + 1) \cdot v = 4v = (4, 0), \qquad 1 \cdot v + 1 \cdot v = v + v = (2, 0).$$

So $V$ with these operations is not a vector space, and axiom 8 is the only axiom that fails.

## Remarks

The example shows that axiom 8 does not follow from the other seven, so a definition that left it out would allow this rule.
The failure has a simple form.
For $v \ne 0$, axiom 8 asks for $(a + b)^2 = a^2 + b^2$, which means $2ab = 0$, and that fails whenever $a$ and $b$ are both nonzero.

What changes with the field?
Over the field $\mathbb{F}_2 = \{0, 1\}$ we have $a^2 = a$ for both elements, so the rule is the usual scalar multiplication on $\mathbb{F}_2^2$, and every axiom holds.
Over $\mathbb{F}_3$ it fails again: $2^2 = 4 = 1$ in $\mathbb{F}_3$, so $2 \cdot v = v$, while $1 \cdot v + 1 \cdot v = 2v \ne v$ for $v \ne 0$.

## Explanations

### L1 human

This rule scales a vector by the square of the number.
Scaling by $1$ twice and adding gives twice the vector.
Scaling once by $1 + 1 = 2$ gives four times the vector.
The two answers differ, so the rule breaks one of the laws that a scaling must obey.

### L2 human

We test the failing axiom with $a = 2$, $b = 3$ and $v = (1, 1)$.
On the left, scale by $2 + 3 = 5$, which multiplies by $25$:
$$(2 + 3) \cdot v = 25v = (25, 25).$$
On the right, scale by $2$ and by $3$, which multiplies by $4$ and by $9$, and add:
$$2 \cdot v + 3 \cdot v = (4, 4) + (9, 9) = (13, 13).$$
The results differ by $2ab \, v = 12v$, as the remark predicts.
Watch out: the rule passes the tests $1 \cdot v = v$ and $a \cdot (b \cdot v) = (ab) \cdot v$, which students often check first, so every axiom must be checked.
