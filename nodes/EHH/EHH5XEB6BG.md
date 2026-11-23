---
tag: EHH5XEB6BG
kind: example
name: Three-colorability in existential monadic second-order logic
msc: ["03B16", "03C13", "05C15", "68Q19"]
topics: [MDHDYV8QZW]
audience: grad
instance_of: [3WHQFSHR58]
uses: [3WHQFSHR58, 0XHZW0VCPR, 00C0BR7D7H, BG8Q0BYSQ3]
sources:
  - url: https://en.wikipedia.org/wiki/Courcelle's_theorem
    locator: Vertex sets
  - url: https://en.wikipedia.org/wiki/Monadic_second-order_logic
    locator: Variants
---

## Example

To color a graph with three colors is to choose three sets of vertices, one for each color.
So a quantifier over sets of vertices can say that a coloring exists.

A [[graph|00C0BR7D7H]] is a structure $(V, E)$ with a symmetric and irreflexive edge relation $E$.
It is [[3-colorable|0XHZW0VCPR]] when there is a map $c : V \to \set{1, 2, 3}$ with $c(u) \neq c(v)$ for every edge $\set{u, v}$.
The existential [[monadic second-order|3WHQFSHR58]] sentence $\chi_3$ is this:
$$\exists R \exists G \exists B \Bigl( \forall x\, (R(x) \lor G(x) \lor B(x)) \land \forall x \forall y \bigl( E(x, y) \to \neg (R(x) \land R(y)) \land \neg (G(x) \land G(y)) \land \neg (B(x) \land B(y)) \bigr) \Bigr).$$
We show that a graph satisfies $\chi_3$ if and only if it is 3-colorable.

1. Let $c$ be a proper coloring with the colors $1, 2, 3$.
   Put $R = c^{-1}(1)$, $G = c^{-1}(2)$ and $B = c^{-1}(3)$.
2. Every vertex has a color, so every vertex lies in $R$, $G$ or $B$, and the first conjunct holds.
3. If $E(u, v)$, then $c(u) \neq c(v)$.
   So $u$ and $v$ do not lie in the same one of the three sets, and the second conjunct holds.
4. Conversely, let $R, G, B$ satisfy the matrix of $\chi_3$.
   The sets can overlap, so we put $c(v) = 1$ if $v \in R$, $c(v) = 2$ if $v \in G \setminus R$, and $c(v) = 3$ otherwise.
5. By the first conjunct, a vertex with $c(v) = 3$ lies in $B$.
   So each vertex lies in the set that matches its color.
6. If $E(u, v)$ and $c(u) = c(v)$, then $u$ and $v$ lie in the same set by step 5, and this contradicts the second conjunct.
   So $c$ is proper.

## Remarks

### Two small graphs

The 5-cycle has the vertices $1, \ldots, 5$ and the edges $12, 23, 34, 45, 51$.
We try these sets:
$$R = \set{1, 3}, \qquad G = \set{2, 4}, \qquad B = \set{5}.$$
Check: the edges join $R$ to $G$, $G$ to $R$, $R$ to $G$, $G$ to $B$ and $B$ to $R$.
So no edge stays inside one set.
The complete graph $K_4$ fails $\chi_3$.
Each of its four vertices lies in one of three sets.
So two of them share a set by the [[pigeonhole principle|0HGVCWQGY3]], and these two vertices are adjacent.

### Where the sentence sits

The sentence has the form $\exists X_1 \cdots \exists X_k\, \varphi$ with $\varphi$ first-order, so it is in existential MSO (EMSO).
It quantifies only over sets of vertices, not over sets of edges, so it is an $\mathrm{MSO}_1$ sentence.

### More colors, and the cost of checking

For $k$ colors we use $k$ set variables and the same two conjuncts.
For $k = 2$ the sentence defines the bipartite graphs.
A program decides 2-colorability in polynomial time, but 3-colorability is [[NP-complete|JGZWHWA8P8]].
So the evaluation of one fixed EMSO sentence on finite graphs can already be NP-complete.
This agrees with [[Fagin's theorem|BG8Q0BYSQ3]]: existential second-order logic defines exactly the properties in NP.
On graphs of bounded [[treewidth|CD2XB4Y1SF]], Courcelle's theorem decides $\chi_3$ in linear time.

## Explanations

### L1 human

A map is 3-colorable when we can paint each country red, green or blue, and neighbors always get different colors.
The logic says this directly: "there is a red set, a green set and a blue set".
Every country must be in one of the sets, and no two neighbors may be in the same set.
A ring of five countries can be painted this way.
Four countries that all touch each other cannot, because two of them would share a color.

### L2 human

We check $\chi_3$ on the wheel $W_5$.
It has a 5-cycle $1, 2, 3, 4, 5$ and a center $0$ that is joined to all five.

1. In a proper coloring, the center is adjacent to every other vertex, so its color appears nowhere else.
   Say the center has color $3$.
2. Then the 5-cycle uses only the colors $1$ and $2$, so the colors must alternate along it.
3. Going around from vertex $1$, the vertices $1, 3, 5$ get one color and the vertices $2, 4$ get the other.
4. Then the edge $51$ joins two vertices of the same color.
   So $W_5$ has no proper 3-coloring, and $W_5$ fails $\chi_3$.

Check: a cycle with an odd number of vertices has no 2-coloring, and $5$ is odd.
The typical use of the sentence is to show that a graph property is in NP, or to apply Courcelle's theorem to it.
Watch out: do not require in a proof that $R$, $G$ and $B$ are disjoint when the sentence does not say so.
Our sentence allows overlaps, and step 4 of the example removes them.
