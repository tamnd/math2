---
tag: JA2EBWVW8A
kind: concept
name: Products of modal logics
aliases: [product-of-modal-logics, product-frame, two-dimensional-modal-logic]
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
uses: [NGHWZ9Y7ZV, C3RZY20ETK, VC3A2VWXND, 1MDT9BF81H, 9A4CYWXPEA]
sources:
  - url: https://en.wikipedia.org/wiki/Multimodal_logic
    locator: Overview
  - url: https://en.wikipedia.org/wiki/Cylindric_algebra
    locator: Cylindric set algebras
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Summary

Take the frame $(\{0, 1\}, <)$ twice and form the $2 \times 2$ grid of pairs $(u, v)$.
Let one box move right along a row, from $(0, v)$ to $(1, v)$, and the other move up along a column, from $(u, 0)$ to $(u, 1)$.
From $(0, 0)$, right then up reaches $(1, 1)$, and up then right reaches $(1, 1)$ too.
So $\lozenge_1 \lozenge_2 p \leftrightarrow \lozenge_2 \lozenge_1 p$ holds at $(0, 0)$ under every valuation.

This grid is a *product frame*, and the formulas valid on all such grids form a *product logic*.
The idea is to combine two modal dimensions, each box acting on one coordinate and leaving the other fixed.
The coordinates are independent, and that independence makes the two boxes commute, as on the grid.
Students slip on two points: products are not fusions, since the boxes interact, and products of decidable logics can be undecidable.

## Motivation

Many applications combine two modal dimensions, such as time and space, or time and the knowledge of an agent.
A point of a product is a pair, for example a moment and a place, and each box moves in one coordinate only.
Products also connect [[modal logic|C3RZY20ETK]] with first-order logic.
In $\mathsf{S5} \times \mathsf{S5}$, the boxes behave as the quantifiers $\forall x$ and $\forall y$ of a language with two variables.
This makes products the modal counterpart of [[cylindric algebras|1MDT9BF81H]] of finite dimension.

## Notation

Let $\mathfrak{F}_1 = (W_1, R_1)$ and $\mathfrak{F}_2 = (W_2, R_2)$ be [[Kripke frames|NGHWZ9Y7ZV]].
Their product is the bimodal frame $\mathfrak{F}_1 \times \mathfrak{F}_2 = (W_1 \times W_2, R_h, R_v)$.
Here $(u, v) R_h (u', v')$ holds when $u R_1 u'$ and $v = v'$, and $(u, v) R_v (u', v')$ holds when $u = u'$ and $v R_2 v'$.
The box $\square_1$ moves along $R_h$, the box $\square_2$ along $R_v$, and $\lozenge_1, \lozenge_2$ are their diamonds.
For Kripke complete unimodal logics $L_1$ and $L_2$, the product logic $L_1 \times L_2$ is the set of bimodal formulas valid in every $\mathfrak{F}_1 \times \mathfrak{F}_2$ with $\mathfrak{F}_1 \models L_1$ and $\mathfrak{F}_2 \models L_2$.
The *fusion* $L_1 \otimes L_2$ is the least bimodal logic that contains $L_1$ for $\square_1$ and $L_2$ for $\square_2$.
The *commutator* is $[L_1, L_2] = L_1 \otimes L_2 \oplus \mathrm{com} \oplus \mathrm{chr}$, with the following axioms.
$$\mathrm{com}: \ \square_1 \square_2 p \leftrightarrow \square_2 \square_1 p, \qquad \mathrm{chr}: \ \lozenge_1 \square_2 p \to \square_2 \lozenge_1 p$$
$L^n$ is the $n$-fold product $L \times \cdots \times L$, for example $\mathsf{S5}^2 = \mathsf{S5} \times \mathsf{S5}$.

## Remarks

### Worked examples

In every product frame, $\mathrm{com}$ and $\mathrm{chr}$ are valid, so they are theorems of every product logic; see [[commutativity and the Church-Rosser property in product frames|1GA9KST2HQ]].
In a product of two universal relations, $\square_1$ and $\square_2$ read as $\forall x$ and $\forall y$.
There the formula $\square_2 \lozenge_1 p \to \lozenge_1 \square_2 p$ fails, as $\forall y \, \exists x$ fails to imply $\exists x \, \forall y$; see [[S5 times S5 and quantifier exchange|8X3T3SY6N6]].
On the grid of the Summary, $\square_1 p$ at $(0, 0)$ says that $p$ holds at $(1, 0)$, and $\square_1 p$ at $(1, 0)$ holds vacuously.

### Non-examples

A bimodal frame in which two arrows from one point cannot be completed to a square refutes $\mathrm{chr}$.
So it is not a product, and it does not validate $\mathsf{K} \times \mathsf{K}$; see [[a bimodal frame that is not a product|34Y1KZBF0D]].
The fusion $\mathsf{K} \otimes \mathsf{K}$ is not a product logic: its frames are all bimodal frames, and it does not prove $\mathrm{com}$.

### The rules you can use

1. In a product frame, $R_h \circ R_v = R_v \circ R_h$, and whenever $x R_h y$ and $x R_v z$, there is $t$ with $y R_v t$ and $z R_h t$.
   These two facts give $\mathrm{com}$ and $\mathrm{chr}$.
2. A formula with $\square_1$ only is true at $(u, v)$ exactly when it is true at $u$ in $\mathfrak{F}_1$, under the valuation of the row $W_1 \times \{v\}$.
   So for consistent Kripke complete $L_1, L_2$, the $\square_1$-part of $L_1 \times L_2$ is $L_1$, and the same holds for $\square_2$.
3. Hence $L_1 \otimes L_2 \subseteq [L_1, L_2] \subseteq L_1 \times L_2$.
4. Gabbay and Shehtman proved $L_1 \times L_2 = [L_1, L_2]$ when $L_1$ and $L_2$ are axiomatized by formulas whose frame conditions are [[universal Horn sentences|9A4CYWXPEA]].
   This covers $\mathsf{K}$, $\mathsf{T}$, $\mathsf{K4}$, $\mathsf{S4}$ and $\mathsf{S5}$, so for example $\mathsf{K} \times \mathsf{K} = [\mathsf{K}, \mathsf{K}]$.
5. The logics $\mathsf{K} \times \mathsf{K}$ and $\mathsf{S5} \times \mathsf{S5}$ are decidable.
6. Hirsch, Hodkinson and Kurucz proved that every trimodal logic $L$ with $\mathsf{K}^3 \subseteq L \subseteq \mathsf{S5}^3$ is undecidable.

### History

Krister Segerberg and Valentin Shehtman studied two-dimensional modal logics such as $\mathsf{S5} \times \mathsf{S5}$ in the 1970s.
Dov Gabbay and Valentin Shehtman introduced products of arbitrary modal logics in 1998 and proved the product matching theorem for Horn axiomatized logics.
Robin Hirsch, Ian Hodkinson and Agi Kurucz proved the undecidability of the logics between $\mathsf{K}^3$ and $\mathsf{S5}^3$.
The monograph "Many-dimensional modal logics: theory and applications" by Gabbay, Kurucz, Wolter and Zakharyaschev appeared in 2003.

### Watch out

Not every frame of $L_1 \times L_2$ is a product.
The frame $W = \{x, y\}$ with $R_1 = R_2 = \{(x, y), (y, y)\}$ validates $\mathsf{K}$ for each box, $\mathrm{com}$ and $\mathrm{chr}$, hence $\mathsf{K} \times \mathsf{K}$.
But in a product two points related by both relations must be equal, and here $x \neq y$ with $x R_1 y$ and $x R_2 y$.
Also, products of decidable logics need not be decidable: two dimensions are often fine, and three are not.

### Try it

On the $2 \times 2$ grid of the Summary, let $p$ be true at $(1, 0)$ only.
Is $\lozenge_1 \square_2 p$ true at $(0, 0)$?
Answer: no, since $(1, 0)$ sees $(1, 1)$ vertically and $p$ fails there.
Is $\square_2 \lozenge_1 p$ true at $(0, 0)$?
Answer: no, since $(0, 1)$ sees only $(1, 1)$ horizontally, where $p$ fails; and $\mathrm{chr}$ is not contradicted, because its antecedent is false.

## Explanations

### L1 human

Think of a chessboard.
One kind of step moves a piece along its row, and the other kind moves it along its column.
A product logic describes what is true about such boards.
For example, a move right and then up reaches the same squares as a move up and then right.

### L2 human

Here is how one checks $\mathrm{com}$ on any product.
The points reached from $(u, v)$ by $R_h$ then $R_v$ are the $(u', v')$ with $u R_1 u'$ and $v R_2 v'$.
The points reached by $R_v$ then $R_h$ are the same, since the two conditions do not interact.
Both $\square_1 \square_2 p$ and $\square_2 \square_1 p$ say that $p$ holds at all these points, so they are equivalent.
The typical use of products is to model two independent dimensions, such as time and space.
Watch out: the logic of all product frames can be much more complex than either component, as the three-dimensional case shows.

### L3 human

The product $\mathsf{S5}^n$ is the modal form of a fragment of first-order logic: $n$ variables, no equality, and atoms only of the form $P(x_1, \ldots, x_n)$.
Its algebras are the representable diagonal-free cylindric algebras of dimension $n$.
In two dimensions, decidability parallels that of [[two-variable logic|S7C3C7DJRF]].
In three dimensions, undecidability parallels that of first-order logic with three variables.
Products are one way to combine logics, with strong interaction, and the fusion is the combination without interaction.
