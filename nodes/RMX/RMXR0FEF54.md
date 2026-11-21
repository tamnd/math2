---
tag: RMXR0FEF54
kind: object
name: Rado graph
aliases: [rado-graph, countable-random-graph, erdos-renyi-graph]
msc: ["05C63", "03C15"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [HJVRBDQSGG]
uses: [00C0BR7D7H, 0F7QKGJS6B, TNT3DG0HRJ, 0MWKJ44V5A, HJVRBDQSGG, ~7468669e, 4S189K88T3, 0EREPBVG2G, 0MCYJ72VGA, 0R46A1XY60, A22K1X8GKD]
sources:
  - url: https://en.wikipedia.org/wiki/Rado_graph
    locator: Constructions
  - url: https://en.wikipedia.org/wiki/Rado_graph
    locator: Model theory and 0-1 laws
  - book: isbn:9780521587136
same_as:
  wikidata: Q7281501
  wikipedia: Rado graph
---

## Description

The Rado graph $R$ has vertex set $\N = \set{0, 1, 2, \dots}$, the [[natural numbers|0MWKJ44V5A]].
For $i < j$, the vertices $i$ and $j$ are adjacent when the binary digit of $j$ at position $i$ is $1$.
Equivalently, $\floor{j / 2^i}$ is odd.

It has the extension property, stated as follows.
For any two disjoint finite sets $U, V \subseteq \N$, some vertex $z \notin U \cup V$ is adjacent to every vertex of $U$ and to no vertex of $V$.
Check: let $N$ be larger than every element of $U \cup V$ and put $z = 2^N + \sum_{u \in U} 2^u$.
Then $z > N$, so $z \notin U \cup V$, and every $w \in U \cup V$ satisfies $w < z$.
The binary digit of $z$ at position $w$ is $1$ if $w \in U$ and $0$ if $w \in V$.
So $z$ is adjacent to every vertex of $U$ and to no vertex of $V$.

Any two countable [[graphs|00C0BR7D7H]] with the extension property are [[isomorphic|0F7QKGJS6B]]; see [[this back-and-forth example|3713A2H6N4]].
So these properties determine $R$ up to isomorphism.

## Remarks

### Other constructions

- Number theory: take as vertices the primes $p \equiv 1 \pmod 4$, with $p \sim q$ when $p$ is a quadratic residue modulo $q$. Quadratic reciprocity makes the relation symmetric, and Dirichlet's theorem with the Chinese remainder theorem gives the extension property.
- Probability: on $\N$, join each pair independently with probability $\frac12$. The resulting [[random graph|TNT3DG0HRJ]] has the extension property [[almost surely|0R46A1XY60]], so it is isomorphic to $R$ with probability $1$.
- Fraïssé theory: $R$ is the [[Fraïssé limit|HJVRBDQSGG]] of the class of finite graphs.

### Properties

- $R$ is [[ultrahomogeneous|~7468669e]]: every isomorphism between finite [[induced subgraphs|0EREPBVG2G]] extends to an automorphism.
- $R$ is a [[universal graph|4S189K88T3]]: every countable graph is an induced subgraph of it.
- $R$ is isomorphic to its [[complement|0MCYJ72VGA]], since the complement also has the extension property.
- Removing finitely many vertices, or changing finitely many edges, gives a graph isomorphic to $R$.
- If the vertex set is split into finitely many parts, at least one part induces a copy of $R$.

### Model theory

The theory of $R$ is axiomatized by the graph axioms and the extension axioms, one for each pair of sizes $\lvert U \rvert$, $\lvert V \rvert$.
It is [[$\aleph_0$-categorical|A22K1X8GKD]] and has quantifier elimination.
A first-order sentence holds in $R$ exactly when it holds in almost all finite graphs on $n$ vertices as $n \to \infty$, with all graphs equally likely.
This gives the zero-one law for finite graphs: each sentence has asymptotic probability $0$ or $1$.

### History

Ackermann described the graph in 1937 while coding hereditarily finite sets by natural numbers.
Erdős and Rényi showed in 1963 that the countable random graph is unique with probability $1$.
Rado gave the binary construction in 1964.
The zero-one law was proved by Glebskii, Kogan, Liogon'kii and Talanov in 1969, and independently by Fagin in 1976.

## Explanations

### L1 human

The Rado graph is an infinite graph that contains every finite and every countable graph as an induced subgraph.
Its central feature is that any finite wish list "be joined to these vertices and not to those" is met by some vertex.
If one draws a countable graph by flipping a fair coin for each pair of vertices, one gets this same graph with probability one.

### L2 human

We find a vertex joined to $0$ and $2$ but not to $1$.

1. Take $U = \set{0, 2}$ and $V = \set{1}$, and $N = 3$.
2. Put $z = 2^3 + 2^0 + 2^2 = 13$, which is $1101$ in binary.
3. The digits of $13$ at positions $0, 1, 2$ are $1, 0, 1$.
4. So $13$ is adjacent to $0$ and $2$, and not to $1$.

The typical use of $R$ is as the generic countable graph: a property shared by almost all finite graphs usually holds in $R$.
A trap is to read the binary digit of the smaller vertex; the rule always looks at the larger one.

### L3 human

The automorphism group of $R$ is a closed oligomorphic subgroup of $\operatorname{Sym}(\N)$, and Truss proved that it is a simple group.
It has the [[small index property|~22edb57f]], through [[Hrushovski's extension property|~6881f8c3]] for finite graphs.
With a generic linear order added, $R$ becomes the limit of a Ramsey class, and the [[Kechris-Pestov-Todorcevic correspondence|~d7362f14]] applies.
