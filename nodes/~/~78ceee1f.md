---
tag: ~78ceee1f
kind: example
name: The integers are not a model of Robinson arithmetic
msc: ["03F30", "03C62"]
topics: [QHCRN4JVG0]
audience: grad
not_instance_of:
  - target: 3K1AKGXF8A
    note: in the integers with successor n + 1, the element -1 has successor 0, so the axiom that 0 is not a successor fails
uses: [TT8MXRTVBM, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
---

## Example

Let $\mathfrak{Z}$ be the $L_A$-structure with domain $\Z$, with $0^{\mathfrak{Z}} = 0$, $S^{\mathfrak{Z}}(n) = n + 1$, the usual addition and multiplication, and the usual order.
We show that $\mathfrak{Z}$ is not a model of [[Robinson arithmetic|TT8MXRTVBM]].

1. $\mathsf{Q}1$ is the sentence $\forall x\,(S x \ne 0)$.
2. In $\mathfrak{Z}$, take $x = -1$. Then $S^{\mathfrak{Z}}(-1) = 0$.
3. So $\mathfrak{Z} \not\models \mathsf{Q}1$, and $\mathfrak{Z}$ is not a model of $\mathsf{Q}$.

The structure fails a second axiom as well.

4. $\mathsf{Q}8$ says $x < y \leftrightarrow \exists v\,(v + S x = y)$.
5. Take $x = 5$ and $y = 0$. Then $v = -6$ gives $v + 6 = 0$, so the right side holds.
6. But $5 < 0$ is false in $\mathfrak{Z}$, so $\mathsf{Q}8$ fails.

The other axioms $\mathsf{Q}2$ to $\mathsf{Q}7$ hold in $\mathfrak{Z}$, since $S$ is a bijection and $+$ and $\cdot$ satisfy the recursion equations.

## Remarks

The example shows which axioms of $\mathsf{Q}$ separate $\N$ from $\Z$: $\mathsf{Q}1$ and $\mathsf{Q}8$.
Removing $\mathsf{Q}1$ is not harmless.
Change the order of $\mathfrak{Z}$ to the relation that $\mathsf{Q}8$ defines; the result is a model of $\mathsf{Q}2$ to $\mathsf{Q}8$.
In that model, $\exists v\,(v + S x = y)$ holds for all $x$ and $y$, so every element is below every element.
So the true sentence $\neg(\overline{1} < 0)$ is not provable from $\mathsf{Q}2$ to $\mathsf{Q}8$, and the [[Σ1-completeness theorem|~1e1241ee]] fails for that theory.
A finite structure also fails $\mathsf{Q}$: if $S$ is injective on a finite set, then $S$ is a bijection, so $0$ is a successor.

## Explanations

### L1 human

The integers go on forever in both directions: $\ldots, -2, -1, 0, 1, 2, \ldots$.
In them, zero is the "next" number after $-1$.
Robinson arithmetic says that zero is not the "next" number of anything.
So the integers break this rule and are not a world for Robinson arithmetic.

### L2 human

We show that no finite structure is a model of $\mathsf{Q}$, a fact related to this example.

1. Let $\mathfrak{A}$ be a finite model of $\mathsf{Q}2$, with domain $A$.
2. $S^{\mathfrak{A}}$ is injective by $\mathsf{Q}2$, so it is a bijection of the finite set $A$.
3. So $0^{\mathfrak{A}} = S^{\mathfrak{A}}(c)$ for some $c \in A$.
4. Then $\mathfrak{A} \not\models \mathsf{Q}1$, so $\mathfrak{A}$ is not a model of $\mathsf{Q}$.

The typical use of a non-example is to show that an axiom cannot be dropped.
A trap is to think that $\Z$ fails because of negative products; the multiplication axioms $\mathsf{Q}6$ and $\mathsf{Q}7$ hold in $\Z$.
