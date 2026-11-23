---
tag: QXFENZWRWM
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

The integers satisfy the recursion equations of addition and multiplication, but they fail the axiom that $0$ is not a successor.
Let $\mathfrak{Z}$ be the $L_A$-structure with domain $\mathbb{Z}$, with $0^{\mathfrak{Z}} = 0$, $S^{\mathfrak{Z}}(n) = n + 1$, the usual addition and multiplication, and the usual order.
We show that $\mathfrak{Z}$ is not a [[model|MVCH6N9SNW]] of [[Robinson arithmetic|TT8MXRTVBM]].

1. $\mathsf{Q}1$ is the sentence $\forall x\,(S x \ne 0)$.
2. In $\mathfrak{Z}$, take $x = -1$, so that $S^{\mathfrak{Z}}(-1) = 0$.
3. So $\mathfrak{Z} \not\models \mathsf{Q}1$, and $\mathfrak{Z}$ is not a model of $\mathsf{Q}$.

The structure fails a second axiom as well.

4. $\mathsf{Q}8$ says $x < y \leftrightarrow \exists v\,(v + S x = y)$.
5. Take $x = 5$ and $y = 0$, so that $v = -6$ gives $v + 6 = 0$ and the right side holds.
6. But $5 < 0$ is false in $\mathfrak{Z}$, so $\mathsf{Q}8$ fails.

The other axioms $\mathsf{Q}2$ to $\mathsf{Q}7$ hold in $\mathfrak{Z}$, since $S$ is a bijection and $+$ and $\cdot$ satisfy the recursion equations.

## Remarks

The example shows which axioms of $\mathsf{Q}$ separate $\mathbb{N}$ from $\mathbb{Z}$: $\mathsf{Q}1$ and $\mathsf{Q}8$.

Is $\mathsf{Q}1$ needed, then, or could the others do its work?
Change the order of $\mathfrak{Z}$ to the relation that $\mathsf{Q}8$ defines, and you get a model of $\mathsf{Q}2$ to $\mathsf{Q}8$.
In that model $v = y - x - 1$ always solves $v + S x = y$, so every element is below every element.
So the true sentence $\neg(\overline{1} < 0)$ is not provable from $\mathsf{Q}2$ to $\mathsf{Q}8$.
That sentence is $\Delta_0$, so [[Σ1-completeness|69234Z1V00]] fails for the smaller theory, and $\mathsf{Q}1$ cannot be dropped.

## Explanations

### L1 human

The integers go on forever in both directions: $\ldots, -2, -1, 0, 1, 2, \ldots$.
In them, zero is the "next" number after $-1$.
Robinson arithmetic says that zero is not the "next" number of anything.
So the integers break this rule, and they are not a world for Robinson arithmetic.

### L2 human

A related fact: no finite structure is a model of $\mathsf{Q}$.
Let $\mathfrak{A}$ be a finite model of $\mathsf{Q}2$, with domain $A$.
By $\mathsf{Q}2$, $S^{\mathfrak{A}}$ is injective, and an injective map of a finite set to itself is a bijection.
So $0^{\mathfrak{A}} = S^{\mathfrak{A}}(c)$ for some $c \in A$, and $\mathfrak{A}$ fails $\mathsf{Q}1$.
For example, the integers modulo $5$ with $S(n) = n + 1$ have $S(4) = 0$.

The typical use of a non-example is to show that an axiom cannot be dropped.
Watch out: $\mathbb{Z}$ does not fail because of negative products.
The multiplication axioms $\mathsf{Q}6$ and $\mathsf{Q}7$ hold in $\mathbb{Z}$, and only the successor and the order cause trouble.
