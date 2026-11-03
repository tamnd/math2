---
tag: ZA4YXJ9T1P
kind: statement
role: theorem
name: CSP dichotomy theorem
msc: ["08A70", "68Q25", "08A40"]
uses: [MJF9M19E3E, KBXSZC6BV1, A0K9EZRM7E, QEAMRNRJJD]
about: [3EH4F5H7FT]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
---

## Statement

Let $\mathbb{B}$ be a finite [[relational structure|MJF9M19E3E]] with finitely many relations.
The problem $\mathrm{CSP}(\mathbb{B})$ takes as input a finite structure $\mathbb{A}$ of the same signature and asks whether there is a [[homomorphism|KBXSZC6BV1]] from $\mathbb{A}$ to $\mathbb{B}$.
A finite structure is a *core* if each of its endomorphisms is an automorphism.
Let $\mathbb{C}$ be the core of $\mathbb{B}$, that is, a core that admits homomorphisms $\mathbb{B} \to \mathbb{C}$ and $\mathbb{C} \to \mathbb{B}$; it is unique up to isomorphism.
A *Taylor polymorphism* of $\mathbb{C}$ is a [[polymorphism|A0K9EZRM7E]] $t$ of $\mathbb{C}$ of some arity $n \ge 2$ that is a [[Taylor operation|QEAMRNRJJD]].
That is, $t(x, \ldots, x) = x$ for all $x$.
Also, for each position $i \le n$, $t$ satisfies an identity $t(u_1, \ldots, u_n) \approx t(v_1, \ldots, v_n)$ with each $u_j, v_j \in \set{x, y}$, $u_i = x$ and $v_i = y$.
Then exactly one of the following holds.

1. $\mathbb{C}$ has a Taylor polymorphism, and $\mathrm{CSP}(\mathbb{B})$ is solvable in [[polynomial time|GVT2NKN37K]].
2. $\mathbb{C}$ has no Taylor polymorphism, and $\mathrm{CSP}(\mathbb{B})$ is [[NP|QQRA9GBW51]]-complete.

In particular, each such [[constraint satisfaction problem|5EHA6R2M6K]] is either in P or NP-complete.

## Remarks

The two algebraic cases exclude each other.
The two complexity outcomes are different only if $\mathrm{P} \ne \mathrm{NP}$.
The hardness half was proved earlier in the [[algebraic approach to constraint satisfaction|3EH4F5H7FT]].
Without a Taylor polymorphism, the polymorphism clone of the core allows a reduction from an NP-complete problem such as 3-colouring.
The tractability half was proved independently by Andrei Bulatov and by Dmitriy Zhuk, with two different polynomial-time algorithms.
This settled the [[Feder–Vardi dichotomy conjecture|WNHZC07XVP]].
By a theorem of Siggers, a finite core has a Taylor polymorphism exactly when it has an idempotent 6-ary polymorphism $s$ of a special form.
This $s$ satisfies $s(x, y, x, z, y, z) = s(y, x, z, x, z, y)$ for all $x, y, z$; see [[Siggers term|JYW1H3J8SX]].

Example: let $\mathbb{B} = K_n$ be the complete graph on $n$ vertices.
Then $\mathrm{CSP}(K_n)$ is the $n$-colouring problem.
For $n = 2$, the majority operation on the two vertices is a polymorphism and a Taylor operation.
So $2$-colouring is in P.
For $n \ge 3$ the graph $K_n$ is a core with no Taylor polymorphism, and $n$-colouring is NP-complete.
More generally, let $H$ be a finite undirected graph.
Then $\mathrm{CSP}(H)$ is in P if $H$ is bipartite or has a loop, and NP-complete otherwise (Hell and Nešetřil).

Passing to the core matters, because a Taylor polymorphism must be idempotent.
For example, the disjoint union of $K_3$ and a single vertex with a loop has no Taylor polymorphism.
Its core is the looped vertex, which has one, and indeed its CSP is trivial: every input maps to the loop.

## Explanations

### L1 human

Many puzzles ask to label the points of a finite input so that given local rules hold, as in map colouring or Sudoku-like constraints.
When the allowed labels and rules are fixed, each such puzzle type is a constraint satisfaction problem.
The theorem says that every such problem type is either solvable by a fast algorithm or as hard as any problem in NP.
There is nothing in between.
Which side a problem falls on is decided by an algebraic test: whether the rules are preserved by a certain kind of "averaging" operation.

### L2 human

The polymorphisms of $\mathbb{B}$ form a clone, and the complexity of $\mathrm{CSP}(\mathbb{B})$ depends only on the identities that this clone satisfies.
The Taylor condition is the weakest nontrivial such identity, and by the cyclic term and Siggers term theorems it can be tested by a single identity.
Earlier special cases include Schaefer's theorem for Boolean structures and the Hell–Nešetřil theorem for undirected graphs.
For infinite templates, and for counting or optimisation versions, separate classification programs exist.
