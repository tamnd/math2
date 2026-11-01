---
tag: 3DRNRZEW9D
kind: counterexample
name: Knaster–Kuratowski fan
msc: [54G20, 54D05]
uses: [0BXNDZFQME, 0V032VWTHD, 0RJSBR9GW1]
sources:
  - url: https://en.wikipedia.org/wiki/Knaster%E2%80%93Kuratowski_fan
same_as:
  wikidata: Q4105873
  wikipedia: Knaster–Kuratowski fan
---

## Counterexample

Let $C$ be the [[Cantor set|0BXNDZFQME]] on the segment $[0, 1] \times \set{0}$ of the plane, and let $p = (1/2, 1/2)$.
Let $E \subseteq C$ be the countable set of end points of the open intervals removed in the construction of $C$.
For $c \in C$, let $L(c)$ be the closed segment from $(c, 0)$ to $p$.
Let $X_c$ be the set of points of $L(c)$ whose second coordinate is rational if $c \in E$, and irrational if $c \in C \setminus E$.
The *Knaster–Kuratowski fan* is $F = \bigcup_{c \in C} X_c \cup \set{p}$, with the topology of a subspace of the plane.
Then $F$ is [[connected|0V032VWTHD]], but $F \setminus \set{p}$ is [[totally disconnected|0RJSBR9GW1]].
So removing one point from a connected space can leave no connected subset with more than one point.

## Remarks

For two points $c < c'$ of $C$, pick $t$ in a removed interval between them.
The line through $p$ and $(t, 0)$ misses $F \setminus \set{p}$, and the two open half-planes it bounds split $F \setminus \set{p}$ into two open pieces.
So a connected subset of $F \setminus \set{p}$ lies in a single set $X_c$.
Each $X_c$ is homeomorphic to the rational or to the irrational points of an interval, which is totally disconnected.
The proof that $F$ is connected is harder; it uses the [[Baire category theorem|0A7KGAYHGV]] on the Cantor set.
The point $p$ is called a dispersion point of $F$.
The space is also called Cantor's leaky tent or Cantor's teepee.

## Explanations

### L1 human

Picture a tent whose poles are the segments from the points of the Cantor set up to a common top.
Each pole is full of holes, keeping only points at rational heights or only at irrational heights.
The whole tent hangs together in one piece, but if one removes the top point, it falls apart into dust: no two points stay in one connected piece.
