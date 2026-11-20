---
tag: QGFVNSRD06
kind: example
name: Colorings of infinite graphs by ultraproducts
msc: ["03C20", "05C15"]
topics: [HZG1YP26AB]
audience: grad
instance_of: [EY09JT7270]
uses: [EY09JT7270, AX9Q86GB8M, 00C0BR7D7H, 0NCPXH194Y, 3MKZST79MK]
sources:
  - url: https://en.wikipedia.org/wiki/De_Bruijn%E2%80%93Erd%C5%91s_theorem_(graph_theory)
    locator: Proofs
---

## Example

Let $G = (V, E)$ be a [[graph|00C0BR7D7H]], let $k \ge 1$, and suppose every finite subgraph of $G$ has a proper $k$-[[coloring|0NCPXH194Y]].
We build a proper $k$-coloring of $G$ by the [[ultraproduct method|EY09JT7270]].

1. Let $I$ be the set of finite subsets of $V$. For $S \in I$ choose a proper $k$-coloring $c_S$ of the subgraph on $S$, and extend it to $V$ by the color $1$.
2. For $v \in V$ let $A_v = \set{S \in I : v \in S}$. The finite intersection $A_{v_1} \cap \dots \cap A_{v_n}$ contains $\set{v_1, \dots, v_n}$.
3. By the [[ultrafilter lemma|3MKZST79MK]] there is an ultrafilter $\mathcal{U}$ on $I$ that contains every $A_v$.
4. Fix $v$. The $k$ sets $\set{S : c_S(v) = j}$ for $j = 1, \dots, k$ partition $I$, so exactly one of them lies in $\mathcal{U}$. Call its index $c(v)$.
5. Let $uv \in E$. The intersection of $A_u \cap A_v$ with $\set{S : c_S(u) = c(u)}$ and $\set{S : c_S(v) = c(v)}$ lies in $\mathcal{U}$, so it has a member $S$.
6. For this $S$, $u, v \in S$ and $c_S$ is proper on $S$, so $c(u) = c_S(u) \neq c_S(v) = c(v)$.

So $c$ is a proper $k$-coloring of $G$.

## Remarks

Step 4 reads off colors in the ultraproduct.
Consider the structures $(V, E, P_1, \dots, P_k)$ with $P_j = c_S^{-1}(j)$, indexed by $S \in I$; the class of the constant function at $v$ has the color $c(v)$ in their ultraproduct.
The result is the theorem of de Bruijn and Erdős of 1951: the chromatic number of a graph is the largest chromatic number of its finite subgraphs, when this is finite.
For $k = 4$ and planar finite graphs, it extends the four color theorem to infinite planar graphs.
The finiteness of $k$ is needed in step 4: with infinitely many colors, the sets may all miss $\mathcal{U}$.
The same proof shows that every partial order extends to a linear order, from the finite case.

## Explanations

### L1 human

Imagine a map with infinitely many countries, where any finite part of the map can be colored with $4$ colors so that neighbors differ.
For each finite part we pick such a coloring.
The ultrafilter acts as a vote: each country takes the color that it gets in "most" of the chosen colorings.
Two neighbors are in most of the finite parts together, and there they always get different colors.
So the vote gives a good coloring of the whole map.

### L2 human

Let $V = \Z$ with an edge between $n$ and $n + 1$, and let $k = 2$.

1. For a finite $S$, color $n \in S$ by $1$ if $n - \min S$ is even and by $2$ otherwise. This is proper on $S$.
2. For a fixed $v$ and $S \in A_v$, the color $c_S(v)$ depends only on the parity of $\min S$.
3. The ultrafilter $\mathcal{U}$ picks one parity class of $\min S$ in step 4, and the same choice works for all $v$ at once.
4. So $c$ is one of the two colorings of $\Z$ by parity.

The typical use is to turn a statement about all finite parts into a statement about the whole infinite object.
The trap is to take the colors of a single finite $S$; no one $S$ sees all edges.
