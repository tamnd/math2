---
tag: 071DDFVG4J
kind: definition
name: Abelian group
msc: [20Kxx]
topics: [BAZT8JJ70S]
audience: ug1
defines: 082GHNPJ53
uses: [G5S1M9, 04E4V9G5FR]
formal:
  - system: lean4
    library: mathlib
    decl: CommGroup
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_group
    locator: Definition
  - book: isbn:9780471433347
    locator: Section 1.1
inventory: [EEC7QXJMXQ]
---

## Definition

An abelian group is a [[group|G5S1M9]] $(G, \ast)$ whose operation is [[commutative|099E72KTF8]].
Thus $a \ast b = b \ast a$ for all $a, b \in G$.

## Notation

The operation of an abelian group is often written $a + b$.
Then the identity element is written $0$, the inverse of $a$ is written $-a$, and $a + (-b)$ is written $a - b$.
For an integer $n$, the [[power|00DRK90Z6K]] $a^n$ becomes the multiple $na$.
In Mathlib, `CommGroup` is the multiplicative form and `AddCommGroup` is the additive form.

## Remarks

The integers, the rational numbers and the real numbers under addition are abelian groups.
The group $\mathrm{GL}_2(\mathbb{R})$ of invertible $2 \times 2$ real matrices under multiplication is not abelian.
To show that a group is abelian, we must check $ab = ba$ for all pairs $a, b$.
To show that a group is not abelian, one pair with $ab \neq ba$ is enough.
The concept page [[abelian group|082GHNPJ53]] gives more examples, the non-examples and the first properties.

## Explanations

### L1 human

In an abelian group, the order of two elements in a product does not matter.
Addition of numbers is the model: $2 + 3$ and $3 + 2$ are both $5$.
The name honours the Norwegian mathematician Niels Henrik Abel.

### L2 human

We check the definition on the group $\{1, -1\}$ under multiplication of numbers.

1. It is a group: $1$ is the identity, and $(-1)(-1) = 1$, so each element is its own inverse.
2. The products of the two different elements are $1 \cdot (-1) = -1$ and $(-1) \cdot 1 = -1$. They are equal.
3. A pair $(a, a)$ always gives $aa = aa$, so only the pairs of different elements need a check.

So the group is abelian.
A trap is to check only the pairs $(a, a)$: they never fail, so they prove nothing.
