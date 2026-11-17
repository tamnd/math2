---
tag: RT898AFHWT
kind: statement
role: theorem
name: Seese's theorem
aliases: [seeses-theorem, decidable-mso-theory-implies-bounded-treewidth]
msc: ["03B25", "05C83", "05C85"]
topics: [E4AVTNWE9E]
audience: research
about: [CD2XB4Y1SF, VYQ32ZBPEE, G6X7SZSNC5]
uses: [~2cb7df7c, 0JD5C82QMB, FJ5E6FZVRJ, CD2XB4Y1SF, QFE1AXQK2E, WP3GDNWJJW, YY4JBMXMXQ, G6X7SZSNC5, HWC687ES0Q, Z7TN2B35B0]
sources:
  - wikipedia: en:47857242@r1374729429
    locator: Logic of graphs, section Second order > Seese's theorem
    note: adopted
    mention: wikipedia://en/47857242#3UW8
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Courcelle%27s_theorem
    locator: Satisfiability and Seese's theorem
  - url: https://en.wikipedia.org/wiki/Treewidth
    locator: Grid minor size
history:
  first_stated: "1991"
  notes: "Seese, The structure of the models of decidable monadic theories of graphs, Annals of Pure and Applied Logic, 1991."
inventory: [DEE4BGX392]
---

## Statement

MSO₂ is monadic second-order logic over a [[graph|0JD5C82QMB]] viewed as a structure with vertices, edges and incidence, as in [[Courcelle's theorem|~2cb7df7c]].
MSO₁ is the weaker logic with variables for vertices and sets of vertices only, over the adjacency relation.
For a class $\mathcal{C}$ of finite graphs, the MSO₂ theory of $\mathcal{C}$ is the set of MSO₂ sentences true in every graph of $\mathcal{C}$.
It is [[decidable|HWC687ES0Q]] exactly when MSO₂ satisfiability in $\mathcal{C}$ is decidable, since $\varphi$ holds in some graph of $\mathcal{C}$ exactly when $\neg \varphi$ is not in the theory.

**Theorem (Seese).** Let $\mathcal{C}$ be a class of finite graphs whose MSO₂ theory is decidable.
Then $\mathcal{C}$ has bounded [[treewidth|FJ5E6FZVRJ]]: there is a $k$ with $\operatorname{tw}(G) \le k$ for every $G \in \mathcal{C}$.

Courcelle's theorem gives a decidable MSO₂ theory for the class of all graphs of treewidth at most $k$.
So, for classes closed under minors, bounded treewidth is the exact boundary for decidable MSO₂ theories (consequence 1).

The [[proof|~af9f53a2]] proves in full that the MSO theory of finite grids is undecidable, by encoding runs of Turing machines.
The transfer from grids to graphs of unbounded treewidth, which uses the excluded grid theorem and the MSO₂-definability of grid minors, is given in outline with citations.

## Remarks

### Why each hypothesis is needed

- Finite graphs. The proof uses the excluded grid theorem, which is a statement about finite graphs, and finite grids as the hard structures.
- MSO₂ rather than MSO₁. The complete graphs have unbounded treewidth, but their MSO₁ theory is decidable, since they have clique-width at most $2$. In MSO₁ one cannot quantify over the edge sets that pick out a grid minor inside a clique.
- Decidability of the whole theory. Model checking a single sentence on a single finite graph is always decidable, so the theorem concerns the theory of the class.

### Consequences

1. A class of finite graphs closed under taking minors has a decidable MSO₂ theory if and only if it has bounded treewidth, by this theorem and Courcelle's theorem. By the excluded grid theorem this holds exactly when the class omits some planar graph.
2. The class of finite planar graphs has an undecidable MSO₂ theory, because it contains all finite grids.
3. The MSO theory of the class of finite grids is undecidable, which is the first step of the proof.

### Converse

The converse is false for arbitrary classes.
Let $S$ be a non-computable set of positive integers, and let $\mathcal{C}$ be the class of the paths $P_n$ with $n \in S$.
Every graph in $\mathcal{C}$ has treewidth at most $1$.
For each $n$ a first-order sentence $\psi_n$ describes $P_n$ up to isomorphism, so $n \in S$ exactly when $\neg \psi_n$ is not in the theory of $\mathcal{C}$.
Hence the MSO₂ theory of $\mathcal{C}$ is undecidable.
The partial converse that holds is Courcelle's theorem for the class of all graphs of treewidth at most $k$.

### Generalizations

1. Seese's conjecture. Seese conjectured that every class of graphs with a decidable MSO₁ theory has bounded [[clique-width|YY4JBMXMXQ]]. The conjecture is open.
2. Courcelle and Oum (2007) proved a weakened form: the conclusion holds when MSO₁ is extended by a predicate stating that a set has even size.

## History

Detlef Seese proved the theorem in 1991, in a paper on the structure of the models of decidable monadic theories of graphs.
The proof combines the undecidability of grids, known from the theory of tiling and domino problems, with the grid minor theorem of Robertson and Seymour (Graph Minors V, 1986).
Seese's conjecture for clique-width remains open; Courcelle and Oum settled the version with parity predicates in 2007.

## Explanations

### L1 human

Monadic second-order logic can talk about vertices, edges, and sets of them.
Some families of graphs allow a computer to decide every sentence of this logic: for example the trees, or more generally the graphs that look like thick trees.
Seese showed that tree-likeness is also necessary.
If a family contains graphs that hide larger and larger grids, then the logic can describe a computer working step by step inside a grid, and no program can decide all such sentences.

### L2 human

We encode a tiny Turing machine run in a $3 \times 4$ grid, rows as times and columns as tape cells.

1. The machine starts in state $q_0$ on a blank tape, writes $1$, moves right and enters the halting state $q_h$.
2. Row $0$: cells $\sqcup \sqcup \sqcup \sqcup$, head at column $0$ in state $q_0$.
3. Row $1$: cells $1 \sqcup \sqcup \sqcup$, head at column $1$ in state $q_h$.
4. Row $2$: the same as row $1$, since the halting state repeats the configuration.
5. A sentence of the form "there are sets $C_\sqcup, C_1, H_{q_0}, H_{q_h}$ such that ..." checks every $2 \times 3$ window against the transition rule and finds $H_{q_h}$ nonempty.

The typical use of the theorem is a dichotomy: to show that an MSO₂ theory is undecidable, show that the class has unbounded treewidth.
A trap is to apply it to MSO₁: the complete graphs have unbounded treewidth and a decidable MSO₁ theory.

### L3 human

Seese's theorem is the logical counterpart of the grid minor theorem: large treewidth forces large grids, and grids carry computation.
It shows that Courcelle's theorem is optimal for MSO₂ and for minor-closed classes.
For MSO₁ the expected boundary is clique-width; Courcelle and Oum proved this for MSO₁ with parity predicates, and the general conjecture is open.
