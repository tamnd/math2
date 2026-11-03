---
tag: 7RGCG5QWRB
kind: statement
role: theorem
name: Mason's gain formula
msc: [94C15, 05C20, 15A06]
uses: [4YHZJGMGFC, 0KFYGSHHF5, 0977KZ6PQB, 00KDZRW4C0, RYTSV821V8]
about: [4YHZJGMGFC]
sources:
  - url: https://en.wikipedia.org/wiki/Mason%27s_gain_formula
same_as:
  wikidata: Q2273232
  wikipedia: Mason's gain formula
---

## Statement

Let a [[signal-flow graph|4YHZJGMGFC]] over a field $F$ have exactly one source node $x_{\mathrm{in}}$, and let $x_{\mathrm{out}}$ be another node.
A *forward path* is a directed path from $x_{\mathrm{in}}$ to $x_{\mathrm{out}}$ that visits no node twice.
A *loop* is a directed cycle that visits no node twice.
Two paths or loops *touch* if they have a common node.
Let $P_1, \ldots, P_K$ be the gains of the forward paths.
The gain of a loop is the product of the gains of its edges.
Define
$$\Delta = 1 - \sum_{i} L_i + \sum_{i, j} L_i L_j - \sum_{i, j, k} L_i L_j L_k + \cdots,$$
where each $L$ is the gain of a loop.
The first sum runs over all loops, and the second over all unordered pairs of loops that do not touch.
The third sum runs over all unordered triples of pairwise non-touching loops, and so on.
Let $\Delta_k$ be the same expression formed only with the loops that do not touch the $k$-th forward path.
If $\Delta \ne 0$, the equations of the graph have a unique solution, and
$$x_{\mathrm{out}} = \frac{\sum_{k=1}^{K} P_k \Delta_k}{\Delta} \, x_{\mathrm{in}}.$$

## Remarks

Let $A$ be the matrix of gains among the nodes other than $x_{\mathrm{in}}$; the equations read $(I - A) x = b \, x_{\mathrm{in}}$, and $\Delta = \det(I - A)$.
The proof expands this [[determinant|00KDZRW4C0]] as a sum over permutations.
The nontrivial cycles of a permutation give a collection of pairwise disjoint loops, and the sign of the permutation gives the signs in $\Delta$.
[[Cramer's rule|0977KZ6PQB]] then gives $x_{\mathrm{out}}$ as a ratio of determinants, and the numerator expands in the same way into the terms $P_k \Delta_k$.
Example: take the edges $r \to e$ of gain $1$, $e \to y$ of gain $G$ and $y \to e$ of gain $-H$.
There is one loop, of gain $-GH$, and one forward path, of gain $G$, which touches it.
So $\Delta = 1 + GH$, $\Delta_1 = 1$, and $y = \frac{G}{1 + GH} r$, the [[closed-loop transfer function|RYTSV821V8]].
The hypothesis $\Delta \ne 0$ is needed: with $G = 1$ and $H = -1$ one has $\Delta = 0$, and the equations $e = r + y$, $y = e$ have no solution for $r \ne 0$.

## Explanations

### L1 human

The formula computes the overall gain from the input to the output of a linear network drawn as a graph.
One lists the routes from input to output and the feedback loops, and multiplies gains along each.
The answer combines these products, correcting each route for the loops it does not pass through.
It replaces solving a linear system by bookkeeping on a picture.

### L2 human

In control engineering, block diagrams of interconnected linear time-invariant systems are turned into signal-flow graphs with gains in the field of rational functions of $s$.
Mason's formula then gives the transfer function between any two signals.
It is a graphical form of Cramer's rule, and the loop expansion of $\det(I - A)$ is the same combinatorics as the expansion of a determinant over permutations by their cycles.
For a single loop of gain $L$ that touches every forward path, it reduces to $\sum_k P_k / (1 - L)$.
