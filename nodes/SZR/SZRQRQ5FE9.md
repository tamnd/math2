---
tag: SZRQRQ5FE9
kind: example
name: Defining the inverse function in group theory
msc: ["03B10", "20A05"]
topics: [H8QZY0RZXZ]
audience: grad
instance_of: [GCK0NN60E4]
uses: [GCK0NN60E4, G5S1M9, 0ZNZH0EXFX, BXBNDHV1HW]
sources:
  - url: https://en.wikipedia.org/wiki/Extension_by_definition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: lead section
---

## Example

Every group text writes $x^{-1}$, although the group axioms only say that some inverse exists.
The notation is safe because each element has exactly one inverse, so "the inverse of $x$" is a definition.

Let $T$ be the theory of [[groups|G5S1M9]] in the language $L = \{ \cdot, e \}$, with the three axioms
$$\forall x\, \forall y\, \forall z\, ((x \cdot y) \cdot z = x \cdot (y \cdot z)), \qquad \forall x\, (x \cdot e = x \land e \cdot x = x), \qquad \forall x\, \exists y\, (x \cdot y = e \land y \cdot x = e).$$
Let $\psi(x, y)$ be $x \cdot y = e \land y \cdot x = e$, which says that $y$ is an [[inverse|0ZNZH0EXFX]] of $x$.
We check that a new [[function symbol|BXBNDHV1HW]] $i$ with the axiom $\forall x\, \forall y\, (i(x) = y \leftrightarrow \psi(x, y))$ gives an [[extension by definitions|GCK0NN60E4]].

1. Existence: $T \vdash \forall x\, \exists y\, \psi(x, y)$, since this is the third axiom.
2. Uniqueness: assume $\psi(x, y)$ and $\psi(x, z)$.
   Then $y = y \cdot e$ by the second axiom.
3. Next, $y \cdot e = y \cdot (x \cdot z)$, since $x \cdot z = e$ by $\psi(x, z)$.
4. Next, $y \cdot (x \cdot z) = (y \cdot x) \cdot z$ by the first axiom.
   And $(y \cdot x) \cdot z = e \cdot z$, since $y \cdot x = e$ by $\psi(x, y)$.
5. Finally, $e \cdot z = z$ by the second axiom.
   So $y = z$, and $T \vdash \forall x\, \exists ! y\, \psi(x, y)$.
6. So the theory $T'$ with $i$ is an extension by definitions, and it is conservative over $T$.
7. We translate $\forall x\, (i(i(x)) = x)$.
   The innermost occurrence is $i(x)$, and unnesting it gives $\forall x\, \exists y\, (\psi(x, y) \land i(y) = x)$.
8. The atomic formula $i(y) = x$ is equivalent in $T'$ to $\psi(y, x)$ by the defining axiom.
   So the translation is $\forall x\, \exists y\, (\psi(x, y) \land \psi(y, x))$.
9. The formula $\psi(y, x)$ is $y \cdot x = e \land x \cdot y = e$, the same two equations as $\psi(x, y)$.
   So the translation is equivalent to $\forall x\, \exists y\, \psi(x, y)$, the third axiom, and $T'$ proves $\forall x\, (i(i(x)) = x)$.

## Remarks

### Substructures change

The extension changes no theorem in the language $\{ \cdot, e \}$, but it changes the substructures.
In the language $\{ \cdot, e \}$, the natural numbers with $+$ and $0$ form a substructure of the integers with $+$ and $0$.
In the language $\{ \cdot, e, i \}$ they do not, because $i(1) = -1$ is not a natural number.
So the substructures of a group in the extended language are exactly its subgroups, while in the old language they are the submonoids.

### Monoids

For monoids the same definition fails, because the third axiom is missing.
The element $0$ of the monoid of natural numbers under multiplication has no inverse.

## Explanations

### L1 human

In a group every element has an "undo" element, its inverse.
For whole numbers with addition, the inverse of $5$ is $-5$, because $5 + (-5) = 0$.
Since each element has exactly one inverse, we may introduce a symbol for "the inverse of".
This symbol is only shorthand, so it does not add new facts about groups.

### L2 human

We check the uniqueness argument in the group of nonzero rational numbers under multiplication, with $x = 4$.

1. The element $y = \tfrac14$ satisfies $4 \cdot \tfrac14 = 1$ and $\tfrac14 \cdot 4 = 1$, so $\psi(4, \tfrac14)$ holds.
2. If $z$ also satisfies $4 z = 1$, then $z = \tfrac14 \cdot 4 \cdot z = \tfrac14 \cdot 1 = \tfrac14$, which is the chain of steps 2 to 5.
3. So $i(4) = \tfrac14$ in the unique expansion.

The typical use is to write group theory with $x^{-1}$ and to know that this is harmless.
Watch out: in a monoid, do not define $i$ by $x \cdot y = e$ alone, because right inverses need not exist or be unique.
