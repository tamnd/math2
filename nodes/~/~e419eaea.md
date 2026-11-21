---
tag: ~e419eaea
kind: example
name: The rational field is not existentially closed
aliases: [rational-field-not-existentially-closed]
msc: ["03C25", "12F05"]
topics: [1A9JSC5YG8]
audience: grad
not_instance_of:
  - target: ~524465b6
    note: the equation y times y equals 2 has a solution in the field extension obtained by adjoining a square root of 2, but no solution in the rationals
uses: [~fc6b5431, 04C5ZBG1WT, 0EQWVHF3W5]
sources:
  - url: https://en.wikipedia.org/wiki/Existentially_closed_model
    locator: Examples
---

## Example

Let $T$ be the theory of [[fields|04C5ZBG1WT]] in the signature $\set{+, -, \cdot, 0, 1}$.
We show that $\Q$ is not an [[existentially closed model|~fc6b5431]] of $T$.

1. Let $F = \Q(\sqrt 2) = \set{a + b\sqrt 2 : a, b \in \Q}$, a subfield of $\R$. It is a [[field extension|0EQWVHF3W5]] of $\Q$, so $F \models T$ and $\Q \subseteq F$.
2. Let $\sigma$ be the existential sentence $\exists y \, (y \cdot y = 1 + 1)$. In $F$, $\sigma$ holds with $y = \sqrt 2$.
3. Suppose that $y = m/n$ in $\Q$, with $\gcd(m, n) = 1$, satisfies $y^2 = 2$. Then $m^2 = 2n^2$, so $m$ is even.
4. Write $m = 2k$. Then $4k^2 = 2n^2$, so $n^2 = 2k^2$ and $n$ is even. This contradicts $\gcd(m, n) = 1$.
5. So $\sigma$ fails in $\Q$, and $\Q \not\preceq_1 F$.

So $\Q$ is not existentially closed among fields.

## Remarks

The example shows the failure of existential closedness through a single existential sentence without parameters.
The same argument works for every field that is not algebraically closed, with a root of a polynomial in place of $\sqrt 2$.

When the class changes, the result changes in this way.

- Among ordered fields, $\Q$ is still not e.c., since $\Q(\sqrt 2)$ with the order from $\R$ is an ordered field that contains $\Q$.
- Among subfields of $\Q$, the field $\Q$ is the only member, so it is e.c. in that class. The notion depends on the class.

## Explanations

### L1 human

Among fractions, no number multiplied by itself gives $2$.
In a bigger number system, made of the numbers $a + b\sqrt 2$, such a number exists, namely $\sqrt 2$.
So the fractions lack a solution that a bigger field provides.
That is what "not existentially closed" means.

### L2 human

We check that $\Q(\sqrt 2)$ is closed under multiplication, as step 1 needs.

1. Take $a + b\sqrt 2$ and $c + d\sqrt 2$ with rational $a, b, c, d$.
2. Their product is $(ac + 2bd) + (ad + bc)\sqrt 2$, since $\sqrt 2 \cdot \sqrt 2 = 2$.
3. The coefficients $ac + 2bd$ and $ad + bc$ are rational.
4. For the inverse of a nonzero element, multiply by $a - b\sqrt 2$: $(a + b\sqrt 2)^{-1} = (a - b\sqrt 2)/(a^2 - 2b^2)$, and $a^2 - 2b^2 \ne 0$ by steps 3 and 4 of the example.

The typical use of the example is as the first test case for a definition of existential closedness.
A trap is to use an extension that is not a model: $\Q[x]$ is a ring extension, not a field extension.
