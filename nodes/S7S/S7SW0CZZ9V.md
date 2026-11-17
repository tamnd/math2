---
tag: S7SW0CZZ9V
kind: example
name: Applications of propositional compactness
msc: ["03B05", "05C15", "06A05", "05D15"]
topics: [JDK63589SA]
audience: ug2
illustrates: [4X9126SEMM]
uses: [4X9126SEMM, QN7M1JCGT9, 00C0BR7D7H, 0NCPXH194Y, 0QV2JS9RJ3, 0FRXBVVR03, Q3EAVBDA8J, V9NXB85SYT, 08WCB90WND]
sources:
  - url: https://en.wikipedia.org/wiki/De_Bruijn–Erdős_theorem_(graph_theory)
    locator: Proofs
  - url: https://en.wikipedia.org/wiki/Szpilrajn_extension_theorem
    locator: Proof via compactness
  - url: https://en.wikipedia.org/wiki/Hall%27s_marriage_theorem
    locator: Infinite families
  - book: isbn:9780122384523
    locator: Chapter 1
---

## Example

Each application follows the same plan.
First, choose variables that describe the unknown object.
Second, write each condition on the object as a formula, so that the models of the set of formulas are exactly the objects.
Third, show that every finite subset of the formulas is satisfiable, by a theorem about finite objects.
Then the [[compactness theorem|4X9126SEMM]] gives a model, and so an object.

Application A, the de Bruijn-Erdős theorem: let $G = (V, E)$ be a [[graph|00C0BR7D7H]] and $k \ge 1$ an integer.
If every finite subgraph of $G$ has a proper $k$-colouring, then $G$ has a proper $k$-[[colouring|0NCPXH194Y]].

1. Variables: $p_{x,i}$ for $x \in V$ and $i \in \set{1, \dots, k}$, read as "the vertex $x$ has colour $i$".
2. Formulas of $\Sigma_G$: (a) $p_{x,1} \lor \cdots \lor p_{x,k}$ for each $x \in V$; (b) $\neg (p_{x,i} \land p_{x,j})$ for each $x$ and $i < j$; (c) $\neg (p_{x,i} \land p_{y,i})$ for each edge $xy \in E$ and each $i$.
3. A model gives a colouring. If $v$ satisfies $\Sigma_G$, put $c(x) = i$ for the unique $i$ with $v(p_{x,i}) = 1$. It exists by (a) and is unique by (b), and (c) says that adjacent vertices get different colours.
4. Finite satisfiability. A finite $\Sigma_0 \subseteq \Sigma_G$ mentions finitely many vertices; call this set $V_0$. The subgraph of $G$ on $V_0$ is finite, so it has a proper colouring $c_0$ by hypothesis.
5. Put $v(p_{x,i}) = 1$ if $x \in V_0$ and $c_0(x) = i$, and $v(p_{x,i}) = 0$ otherwise. Each formula of $\Sigma_0$ mentions only vertices of $V_0$.
6. Check of step 5: (a) holds because $c_0(x)$ is one colour; (b) holds because $c_0(x)$ is only one colour; (c) holds because an edge $xy$ with $x, y \in V_0$ gets $c_0(x) \ne c_0(y)$. So $v$ satisfies $\Sigma_0$.
7. Compactness gives a model of $\Sigma_G$, and step 3 turns it into a proper $k$-colouring of $G$.

Application B, the order extension principle: every [[partial order|0QV2JS9RJ3]] $\le$ on a set $A$ extends to a [[total order|0FRXBVVR03]] on $A$, a [[linear extension|Q3EAVBDA8J]].

8. The finite case, by induction on $|A|$. The empty set is trivial. A finite nonempty partial order has a [[minimal element|V9NXB85SYT]] $m$, because a strictly decreasing chain in a finite set cannot go on forever.
9. By the induction hypothesis, the order on $A \setminus \set{m}$ has a linear extension; put $m$ below every other element. If $a < b$ in $A$, then $b \ne m$ by minimality. So either $a = m$, which comes first, or both lie in $A \setminus \set{m}$.
10. Variables: $p_{ab}$ for $a, b \in A$ with $a \ne b$, read as "$a$ comes before $b$".
11. Formulas of $\Sigma_A$: (a) $p_{ab} \lor p_{ba}$ for $a \ne b$; (b) $\neg (p_{ab} \land p_{ba})$ for $a \ne b$; (c) $(p_{ab} \land p_{bc}) \to p_{ac}$ for distinct $a, b, c$; (d) $p_{ab}$ whenever $a < b$ in the given order.
12. A model gives a linear extension. Put $a \sqsubseteq b$ when $a = b$ or $v(p_{ab}) = 1$. Then (a) gives totality, (b) antisymmetry, (c) transitivity, and (d) says that $\sqsubseteq$ extends $\le$.
13. Transitivity in step 12 when two of $a, b, c$ are equal: if $a = b$ or $b = c$, the conclusion is a hypothesis. If $a = c$, it holds because $a \sqsubseteq a$.
14. Finite satisfiability. A finite $\Sigma_0 \subseteq \Sigma_A$ mentions a finite set $A_0 \subseteq A$. Steps 8 and 9 give a linear extension $\sqsubseteq_0$ of $\le$ on $A_0$.
15. Put $v(p_{ab}) = 1$ when $a, b \in A_0$ and $a \sqsubseteq_0 b$, and $0$ otherwise. Then (a), (b), (c) hold on $A_0$ because $\sqsubseteq_0$ is a total order, and (d) holds because it extends $\le$.
16. Compactness gives a model of $\Sigma_A$, and step 12 gives the linear extension. This is the [[Szpilrajn extension theorem|T9CJHV6JW3]].

Application C, Hall's theorem for infinite families: let $(A_i)_{i \in I}$ be a family of finite sets.
Suppose that $\left| \bigcup_{i \in J} A_i \right| \ge |J|$ for every finite $J \subseteq I$.
Then there is an injective map $f$ on $I$ with $f(i) \in A_i$ for each $i$, a system of distinct representatives.

17. Variables: $p_{i,x}$ for $i \in I$ and $x \in A_i$, read as "$f(i) = x$".
18. Formulas of $\Sigma_H$: (a) $\bigvee_{x \in A_i} p_{i,x}$ for each $i$, a finite disjunction because $A_i$ is finite; (b) $\neg (p_{i,x} \land p_{i,y})$ for $x \ne y$ in $A_i$; (c) $\neg (p_{i,x} \land p_{j,x})$ for $i \ne j$ and $x \in A_i \cap A_j$.
19. The case $J = \set{i}$ of the hypothesis gives $|A_i| \ge 1$, so each disjunction in (a) has at least one term.
20. A model gives the map. Put $f(i) = x$ for the unique $x$ with $v(p_{i,x}) = 1$, by (a) and (b). Then (c) says that $f$ is injective.
21. Finite satisfiability. A finite $\Sigma_0 \subseteq \Sigma_H$ mentions a finite set $J \subseteq I$ of indices. The finite family $(A_i)_{i \in J}$ satisfies the condition, so the finite [[Hall's marriage theorem|08WCB90WND]] gives an injective $f_0$ on $J$ with $f_0(i) \in A_i$.
22. Put $v(p_{i,x}) = 1$ when $i \in J$ and $f_0(i) = x$, and $0$ otherwise. Then (a) and (b) hold for $i \in J$, and (c) holds for $i, j \in J$ because $f_0$ is injective.
23. Compactness gives a model of $\Sigma_H$, and step 20 gives the system of distinct representatives.

Counterexample D: the sets must be finite.
Let $A_0 = \set{1, 2, 3, \dots}$ and $A_n = \set{n}$ for $n \ge 1$.

24. The condition holds. For a finite $J \subseteq \mathbb{N}$ without $0$, the union is $J$ itself. For a finite $J$ with $0 \in J$, the union contains the infinite set $A_0$.
25. There is no system of distinct representatives. For $n \ge 1$ we must take $f(n) = n$. Then $f(0) = m$ for some $m \ge 1$, and $f(0) = f(m)$.
26. The encoding of step 18 breaks: for $i = 0$ the formula (a) would be an infinite disjunction, which is not a formula.

## Remarks

The three proofs share one pattern: each condition on the object involves finitely many variables, and a finite theorem solves each finite piece.
The finiteness of $k$ in Application A is needed, as in Counterexample D.
Every finite subgraph of the complete graph on an uncountable set has a colouring with countably many colours, but the whole graph has none.
In the encoding, formula (a) of step 2 would be an infinite disjunction.

The theorem of Application A was proved by Nicolaas de Bruijn and Paul Erdős in 1951, and Walter Gottschalk gave a proof by Tychonoff's theorem in the same year.
Edward Szpilrajn proved the order extension principle in 1930.
For a countable graph, a countable set or a countable family, the variables are countable, and compactness needs no choice.
For arbitrary sizes, the de Bruijn-Erdős theorem is equivalent over ZF to the [[Boolean prime ideal theorem|STPBXBKSZP]].

The [[chromatic number|0C5M7AM6FH]] of an infinite graph is therefore the largest chromatic number of its finite subgraphs, when this is finite.
With the axiom of choice, for example, the unit-distance graph of the plane has the same chromatic number as one of its finite subgraphs.

## Explanations

### L1 human

Imagine an endless map, where each country must get one of three colours and neighbours must differ.
Suppose that every finite part of the map can be coloured this way.
Compactness says that the whole endless map can then be coloured.
Each rule, such as "these two neighbours differ", talks about only a few countries.
Compactness puts together the many finite solutions into one solution for everything.

### L2 human

We colour the graph on the integers, with an edge between $n$ and $n + 1$, with $k = 2$ colours.

1. Variables: $p_{n,1}$ and $p_{n,2}$ for each integer $n$.
2. Formulas: $p_{n,1} \lor p_{n,2}$, $\neg (p_{n,1} \land p_{n,2})$, and $\neg (p_{n,i} \land p_{n+1,i})$ for $i = 1, 2$.
3. A finite subset mentions only the integers in some interval $[-N, N]$.
4. Colour $n$ with colour 1 when $n$ is even and colour 2 when $n$ is odd. Adjacent integers have different parity, so the colouring is proper.
5. This assignment makes the finite subset true, so the set is finitely satisfiable.
6. Compactness gives a proper 2-colouring of the whole graph.

The typical use is the one of Applications A, B and C, where no single formula for the infinite object is known in advance.
The trap is Counterexample D: the method needs every condition to be a finite formula, and the theorem fails for families with an infinite set.

### L3 human

These applications are statements of the form "local solutions give a global solution", and compactness is the topological reason behind them.
The space of all candidate objects (all colourings, all relations, all choice functions) is a closed subspace of a product of finite discrete spaces, and so compact.
Over ZF, many of these statements are equivalent to the Boolean prime ideal theorem, so they sit strictly between ZF and the axiom of choice.
The same method with first-order logic gives nonstandard models, and the method of finite pieces appears again in Ramsey theory and in the theory of infinite graphs.
