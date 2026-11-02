---
tag: QREAJQH24A
kind: example
name: Tamari lattice
msc: [06B05, 05A15]
instance_of: [WH4SFAACAS]
uses: [0YWZJEABB2, 0D7EZ10V2R, DHC8TZXGYS, QX7WZ92QAK]
sources:
  - url: https://en.wikipedia.org/wiki/Tamari_lattice
---

## Example

Let $n \ge 1$, and consider the ways to fully parenthesize a product $x_0 x_1 \cdots x_n$ of $n + 1$ factors.
There are $C_n$ of them, where $C_n$ is the $n$-th [[Catalan number|0YWZJEABB2]].
A rotation replaces a subexpression $(A B) C$ by $A (B C)$, where $A$, $B$, $C$ are subexpressions.
The Tamari order $T_n$ sets $p \le q$ when $q$ can be reached from $p$ by a finite sequence of rotations.

For $n = 3$ there are $C_3 = 5$ bracketings of $abcd$.
From the least element $((ab)c)d$ to the greatest element $a(b(cd))$ there are two routes:
$$((ab)c)d \to (ab)(cd) \to a(b(cd)),$$
$$((ab)c)d \to (a(bc))d \to a((bc)d) \to a(b(cd)).$$
These are all the relations, so $T_3$ is the pentagon $N_5$, with a route of two steps beside a route of three steps.

## Remarks

Each $T_n$ is a [[lattice|WH4SFAACAS]].
Since $T_3$ is the [[pentagon lattice|DHC8TZXGYS]], the Tamari lattices are not [[modular|QX7WZ92QAK]] in general.
Bracketings of $n + 1$ factors correspond to [[binary trees|0D7EZ10V2R]] with $n$ internal nodes, and a rotation is the tree rotation used in balanced search trees.
The Hasse diagram of $T_n$ is the graph of the associahedron.

## Explanations

### L1 human

There are several ways to put brackets into a long product, and moving brackets to the right is a single step.
The Tamari lattice records which bracketings can be reached from which by such steps.
With four factors there are five bracketings, arranged like a pentagon.
