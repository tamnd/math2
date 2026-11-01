---
tag: D8ZD10YF3Y
kind: conjecture
name: Rota's basis conjecture
msc: [05B35, 15A03]
uses: [000AYPA9AJ, 0KCQ9Y3QKA, PX31ZNYS3Z, QTSQR7130G]
about: [0KCQ9Y3QKA, PX31ZNYS3Z]
sources:
  - url: https://en.wikipedia.org/wiki/Rota%27s_basis_conjecture
same_as:
  wikidata: Q7370200
  wikipedia: Rota's basis conjecture
history:
  posed_by: "Gian-Carlo Rota"
  first_stated: "1989"
---

## Statement

Let $V$ be a [[vector space|000AYPA9AJ]] of dimension $n \ge 1$ over a field.
Let $B_1, \dots, B_n$ be [[bases|0KCQ9Y3QKA]] of $V$, regarded as $n$ disjoint labelled families of $n$ vectors.
Then the $n^2$ vectors can be arranged in an $n \times n$ grid with the following properties.
For each $i$, the $i$-th row consists of the vectors of $B_i$.
Each column is a basis of $V$.

## Remarks

The conjecture is due to Gian-Carlo Rota, and it is open.
It has a natural form for [[matroids|PX31ZNYS3Z]]: given $n$ [[bases|QTSQR7130G]] of a matroid of rank $n$, the elements can be arranged in such a grid with each column a basis.
For $n = 2$ the statement is easy to check by hand: with $B_1 = \set{a, b}$ and $B_2 = \set{c, d}$, at least one of the pairings $\set{a, c}, \set{b, d}$ or $\set{a, d}, \set{b, c}$ gives two bases.
Huang and Rota related the vector space form to the Alon–Tarsi conjecture on Latin squares, which gives the conjecture for some even $n$ over fields of characteristic zero.
Asymptotic versions are known that produce many disjoint column bases, but not $n$ of them in general.

## Explanations

### L1 human

Start with $n$ bases of an $n$-dimensional space, each written as a row of $n$ vectors.
The question is whether one can reorder each row so that every column also becomes a basis.
It looks like a puzzle in the style of Latin squares, and it is still unsolved in general.
