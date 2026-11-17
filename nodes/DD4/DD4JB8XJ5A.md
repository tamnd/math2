---
tag: DD4JB8XJ5A
kind: statement
role: theorem
name: Courcelle's theorem
aliases: [courcelles-theorem, mso-model-checking-bounded-treewidth]
msc: ["03B25", "05C85", "05C83"]
topics: [E4AVTNWE9E]
audience: research
about: [CD2XB4Y1SF, G6X7SZSNC5, 3VSFM7K70Z]
uses: [BG8Q0BYSQ3, QQRA9GBW51, JGZWHWA8P8, 0JD5C82QMB, FJ5E6FZVRJ, CD2XB4Y1SF, G6X7SZSNC5, 3VSFM7K70Z, AK66XQ59Z3, X499BMR9MS, YY4JBMXMXQ, HWC687ES0Q]
sources:
  - url: https://en.wikipedia.org/wiki/Courcelle%27s_theorem
    locator: Formulations
  - url: https://en.wikipedia.org/wiki/Courcelle%27s_theorem
    locator: Proof strategy and complexity
  - url: https://en.wikipedia.org/wiki/Treewidth
    locator: Courcelle's theorem
history:
  first_stated: "1990"
  notes: "Courcelle, The monadic second-order logic of graphs I: recognizable sets of finite graphs, Information and Computation, 1990."
---

## Statement

A finite [[graph|0JD5C82QMB]] $G = (V, E)$ is viewed as a two-sorted structure with domain $V \cup E$, unary predicates for the two sorts, and the incidence relation $\operatorname{inc}(v, e)$, "the vertex $v$ is an end of the edge $e$".
MSO₂ is monadic second-order logic over this structure: its variables range over vertices, edges, sets of vertices and sets of edges.
MSO₁ is the weaker logic over the structure $(V, \operatorname{adj})$, with variables for vertices and sets of vertices only.
The [[treewidth|FJ5E6FZVRJ]] $\operatorname{tw}(G)$ is the least width of a tree decomposition of $G$.

**Theorem (Courcelle).** For every MSO₂ sentence $\varphi$ and every $k \in \N$ there is an algorithm that decides, for a graph $G$ with $\operatorname{tw}(G) \le k$, whether $G \models \varphi$.
It runs in time $f(\varphi, k) \cdot n$, where $n$ is the number of vertices of $G$ and $f$ is a computable function.
The algorithm is computed from $\varphi$ and $k$.

So MSO₂ model checking is fixed-parameter tractable when parametrized by the length of $\varphi$ plus the treewidth, in the sense of [[parameterized complexity|X499BMR9MS]].

The [[proof|HWWE6X0X92]] proves in full the core lemma, due to Thatcher and Wright and to Doner.
It says that an MSO sentence about finite labelled trees is equivalent to a deterministic bottom-up [[tree automaton|3VSFM7K70Z]].
The proof gives the encoding of graphs of treewidth at most $k$ as labelled trees in outline, and it cites the linear-time computation of tree decompositions.

## Remarks

### Why each hypothesis is needed

- Bounded treewidth. Three-colourability is MSO₁-definable: there are sets $X_1, X_2, X_3$ that cover $V$ and contain no edge. The problem is NP-complete on all graphs, so a polynomial algorithm for all graphs would give P = NP.
- A fixed sentence. The running time is linear in $n$ but grows very fast with $\varphi$. Frick and Grohe showed that, unless P = NP, no algorithm decides MSO on finite trees in time $f(\varphi) \cdot p(n)$ with $p$ a polynomial and $f$ elementary.
- Monadic quantifiers. By [[Fagin's theorem|BG8Q0BYSQ3]], existential second-order logic with quantifiers over relations defines every [[NP|QQRA9GBW51]] property of finite structures. Trees can encode arbitrary binary strings, so one fixed such sentence defines an [[NP-complete|JGZWHWA8P8]] property of trees, which have treewidth $1$.

### Consequences

1. Hamiltonicity is decidable in linear time on graphs of treewidth at most $k$. It is MSO₂-definable: there is an edge set $F$ such that every vertex lies on exactly two edges of $F$, and every partition of $V$ into two nonempty sets is crossed by an edge of $F$.
2. Three-colourability, the existence of a perfect matching, and planarity are likewise decided in linear time on graphs of bounded treewidth.
3. The MSO₂ theory of the class of graphs of treewidth at most $k$ is [[decidable|HWC687ES0Q]]. Each such graph is coded by a labelled tree, and satisfiability reduces to the emptiness of a tree automaton.
4. Seese's theorem gives a converse to consequence 3: a class of graphs with a decidable MSO₂ theory has bounded treewidth ([[Seese's theorem|RT898AFHWT]]).

### Converse

For the running time the converse fails for MSO₁: by generalization 2, MSO₁ model checking is linear on the complete graphs, whose treewidth is unbounded.
For the decidability of the MSO₂ theory the converse is exact, by Seese's theorem.

### Generalizations

1. Optimization. Arnborg, Lagergren and Seese (1991) and Borie, Parker and Tovey (1992) extended the theorem to optimization and counting problems, such as the largest independent set.
2. [[Clique-width|YY4JBMXMXQ]]. Courcelle, Makowsky and Rotics proved the analogue for MSO₁ on graphs of bounded clique-width, given a clique-width expression.
3. Counting MSO. The theorem holds for counting MSO, which adds predicates "$|X| \equiv r \pmod m$".
4. Words and trees. For paths and trees the theorem reduces to the [[Büchi-Elgot-Trakhtenbrot theorem|AK66XQ59Z3]] and its version for trees.

## History

Bruno Courcelle proved the theorem in 1990, in the first paper of a series on the monadic second-order logic of graphs.
Its core is older: Thatcher and Wright in 1968 and Doner in 1970 proved that MSO on finite trees is equivalent to tree automata.
Linear running time needs a tree decomposition, which Bodlaender showed in 1996 how to compute in linear time for each fixed $k$.

## Explanations

### L1 human

Some graphs look like thick trees: they can be cut into small pieces arranged in a tree, each piece with at most $k + 1$ vertices.
Courcelle showed that every property written in a certain logic of vertices, edges, and sets of them can be checked fast on such graphs.
The program walks the tree of pieces from the leaves to the root and keeps a fixed amount of information about each piece.
For example, "the graph can be coloured with three colours" is checked this way, although it is hard on general graphs.

### L2 human

We check three-colourability on a path $P_n$ with vertices $1, 2, \ldots, n$, which has treewidth $1$.

1. The bags are $\set{1, 2}, \set{2, 3}, \ldots, \set{n-1, n}$, arranged along a path.
2. For each bag the algorithm stores the set of colourings of the bag that extend to a proper colouring of the part already processed.
3. For $\set{1, 2}$ these are the $6$ pairs of distinct colours.
4. Passing from $\set{i-1, i}$ to $\set{i, i+1}$ forgets $i - 1$ and adds a colour for $i + 1$ different from that of $i$. Again all $6$ pairs survive.
5. At the root the set is nonempty, so $P_n$ is three-colourable. Each step costs a constant, so the total time is linear in $n$.

The typical use is to prove that a graph problem is linear-time solvable on bounded treewidth by writing it in MSO₂.
A trap is to read the theorem as a practical algorithm: the hidden constant can be a tower of exponentials in the length of $\varphi$.

### L3 human

Courcelle's theorem transfers the correspondence between monadic second-order logic and finite tree automata from trees to graphs that are tree-like.
Graphs of treewidth at most $k$ are the values of terms over a finite set of gluing operations, and an MSO₂ sentence about the graph becomes an MSO sentence about the term.
In Courcelle's algebraic language, MSO-definable sets of graphs are recognizable, which means that they have finitely many classes for each of the gluing operations.
Seese's theorem and the grid minor theorem show that bounded treewidth is the right boundary for MSO₂.
