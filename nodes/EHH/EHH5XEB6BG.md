---
tag: EHH5XEB6BG
kind: example
name: Three-colourability in existential monadic second-order logic
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

A [[graph|00C0BR7D7H]] is a structure $(V, E)$ with a symmetric and irreflexive edge relation $E$.
It is [[3-colourable|0XHZW0VCPR]] when there is a map $c : V \to \set{1, 2, 3}$ with $c(u) \neq c(v)$ for every edge $\set{u, v}$.
The existential [[monadic second-order|3WHQFSHR58]] sentence is
$$\chi_3 := \exists R \exists G \exists B \Bigl( \forall x\, (R(x) \lor G(x) \lor B(x)) \land \forall x \forall y \bigl( E(x, y) \to \neg (R(x) \land R(y)) \land \neg (G(x) \land G(y)) \land \neg (B(x) \land B(y)) \bigr) \Bigr).$$
We show that a graph satisfies $\chi_3$ if and only if it is 3-colourable.

1. Let $c$ be a proper colouring with colours $1, 2, 3$. Put $R = c^{-1}(1)$, $G = c^{-1}(2)$ and $B = c^{-1}(3)$.
2. Every vertex has a colour, so every vertex lies in $R$, $G$ or $B$, and the first conjunct holds.
3. If $E(u, v)$, then $c(u) \neq c(v)$, so $u$ and $v$ do not lie in the same one of the three sets, and the second conjunct holds.
4. Conversely, let $R, G, B$ witness $\chi_3$. The sets may overlap, so we define $c(v) = 1$ if $v \in R$, $c(v) = 2$ if $v \in G \setminus R$, and $c(v) = 3$ otherwise.
5. By the first conjunct, a vertex with $c(v) = 3$ lies in $B$. So each vertex lies in the set that matches its colour.
6. If $E(u, v)$ and $c(u) = c(v)$, then $u$ and $v$ lie in the same set by step 5, which contradicts the second conjunct. So $c$ is proper.

Two instances follow.

- The 5-cycle with vertices $1, \ldots, 5$ satisfies $\chi_3$, with $R = \set{1, 3}$, $G = \set{2, 4}$ and $B = \set{5}$. The edges are $12, 23, 34, 45, 51$, and each joins two different sets.
- The complete graph $K_4$ fails $\chi_3$. For any witnesses, two of its four vertices lie in a common set by the [[pigeonhole principle|0HGVCWQGY3]], and these two vertices are adjacent.

## Remarks

The sentence has the form $\exists X_1 \cdots \exists X_k\, \varphi$ with $\varphi$ first-order, so it lies in existential MSO (EMSO).
It quantifies only over sets of vertices, so it is an $\mathrm{MSO}_1$ sentence.

The parameter is the number of colours.
For $k$ colours we use $k$ set variables and the same two conjuncts, and for $k = 2$ we get the bipartite graphs.
Deciding 2-colourability takes polynomial time, while deciding 3-colourability is [[NP-complete|JGZWHWA8P8]].
So evaluating one fixed EMSO sentence on finite graphs can already be NP-complete.
This agrees with [[Fagin's theorem|BG8Q0BYSQ3]], by which existential second-order logic defines exactly the properties in NP.
On graphs of bounded [[treewidth|CD2XB4Y1SF]], Courcelle's theorem decides $\chi_3$ in linear time.

## Explanations

### L1 human

A map is 3-colourable when we can paint each country red, green or blue so that neighbours get different colours.
The logic says this directly: "there is a red set, a green set and a blue set".
Every country must be in one of the sets.
No two neighbours may be in the same set.
A ring of five countries can be painted this way, but four countries that all touch each other cannot, since two of them would share a colour.

### L2 human

We check $\chi_3$ on the wheel $W_5$: a 5-cycle $1, 2, 3, 4, 5$ and a centre $0$ joined to all five.

1. In a proper colouring the centre is adjacent to every other vertex, so its colour appears nowhere else; say $B = \set{0}$.
2. The 5-cycle must then use only $R$ and $G$, so it must be 2-coloured.
3. Along the cycle the colours must alternate, so vertices $1, 3, 5$ get one colour and vertices $2, 4$ get the other.
4. Then the edge $51$ joins two vertices of the same colour, so no witnesses exist, and $W_5$ fails $\chi_3$.

The typical use of the sentence is to show that a graph property belongs to NP, or to apply Courcelle's theorem to it.
A trap is to require that $R$, $G$ and $B$ are disjoint and then forget the condition in the proof.
Our sentence does not require it, and step 4 of the example removes the overlaps.
