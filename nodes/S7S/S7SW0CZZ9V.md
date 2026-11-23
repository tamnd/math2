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

Three theorems about infinite graphs, orders and families of sets all follow from their finite cases by one argument.
First, choose variables that describe the unknown object.
Second, write each condition on the object as a formula, so that the models of the set of formulas are exactly the objects.
Third, show that every finite subset of the formulas is satisfiable, by a theorem about finite objects.
Then the [[compactness theorem|4X9126SEMM]] gives a model, and so an object.

Application A, the de Bruijn-Erdős theorem: let $G = (V, E)$ be a [[graph|00C0BR7D7H]] and $k \ge 1$ an integer.
If every finite subgraph of $G$ has a proper $k$-coloring, then $G$ has a proper $k$-[[coloring|0NCPXH194Y]].

1. Variables: $p_{x,i}$ for $x \in V$ and $i \in \{ 1, \dots, k \}$, read as "the vertex $x$ has color $i$".
2. Formulas of $\Sigma_G$: (a) $p_{x,1} \lor \cdots \lor p_{x,k}$ for each $x \in V$; (b) $\neg (p_{x,i} \land p_{x,j})$ for each $x$ and $i < j$; (c) $\neg (p_{x,i} \land p_{y,i})$ for each edge $xy \in E$ and each $i$.
3. A model gives a coloring.
   If $v$ satisfies $\Sigma_G$, put $c(x) = i$ for the unique $i$ with $v(p_{x,i}) = 1$.
   This $i$ exists by (a) and is unique by (b), and (c) says that adjacent vertices get different colors.
4. Finite satisfiability.
   A finite $\Sigma_0 \subseteq \Sigma_G$ mentions finitely many vertices; call this set $V_0$.
   The subgraph of $G$ on $V_0$ is finite, so it has a proper coloring $c_0$ by hypothesis.
5. Put $v(p_{x,i}) = 1$ if $x \in V_0$ and $c_0(x) = i$, and $v(p_{x,i}) = 0$ otherwise.
   Each formula of $\Sigma_0$ mentions only vertices of $V_0$.
6. Check of step 5: (a) holds because $c_0(x)$ is a color, (b) holds because $c_0(x)$ is only one color, and (c) holds because an edge $xy$ with $x, y \in V_0$ gets $c_0(x) \ne c_0(y)$.
   So $v$ satisfies $\Sigma_0$.
7. Compactness gives a model of $\Sigma_G$, and step 3 turns it into a proper $k$-coloring of $G$.

Application B, the order extension principle: every [[partial order|0QV2JS9RJ3]] $\le$ on a set $A$ extends to a [[total order|0FRXBVVR03]] on $A$, a [[linear extension|Q3EAVBDA8J]].

8. The finite case is proved by induction on $|A|$, and the empty order is its own linear extension.
   A finite nonempty partial order has a [[minimal element|V9NXB85SYT]] $m$, because a strictly decreasing chain in a finite set cannot go on forever.
9. By the induction hypothesis, the order on $A \setminus \{ m \}$ has a linear extension; put $m$ below every other element.
   If $a < b$ in $A$, then $b \ne m$ by minimality.
   So either $a = m$, which comes first, or both lie in $A \setminus \{ m \}$.
10. Variables: $p_{ab}$ for $a, b \in A$ with $a \ne b$, read as "$a$ comes before $b$".
11. Formulas of $\Sigma_A$: (a) $p_{ab} \lor p_{ba}$ for $a \ne b$; (b) $\neg (p_{ab} \land p_{ba})$ for $a \ne b$; (c) $(p_{ab} \land p_{bc}) \to p_{ac}$ for distinct $a, b, c$; (d) $p_{ab}$ whenever $a < b$ in the given order.
12. A model gives a linear extension.
    Put $a \sqsubseteq b$ when $a = b$ or $v(p_{ab}) = 1$.
    Then (a) gives totality, (b) antisymmetry, (c) transitivity, and (d) says that $\sqsubseteq$ extends $\le$.
13. Transitivity in step 12 also holds when two of $a, b, c$ are equal.
    If $a = b$ or $b = c$, the conclusion is one of the hypotheses, and if $a = c$, it holds because $a \sqsubseteq a$.
14. Finite satisfiability.
    A finite $\Sigma_0 \subseteq \Sigma_A$ mentions a finite set $A_0 \subseteq A$, and steps 8 and 9 give a linear extension $\sqsubseteq_0$ of $\le$ on $A_0$.
15. Put $v(p_{ab}) = 1$ when $a, b \in A_0$ and $a \sqsubseteq_0 b$, and $0$ otherwise.
    Then (a), (b), (c) hold on $A_0$ because $\sqsubseteq_0$ is a total order, and (d) holds because it extends $\le$.
16. Compactness gives a model of $\Sigma_A$, and step 12 gives the linear extension.
    This is the [[Szpilrajn extension theorem|T9CJHV6JW3]].

Application C, Hall's theorem for infinite families: let $(A_i)_{i \in I}$ be a family of finite sets.
Suppose that $\left| \bigcup_{i \in J} A_i \right| \ge |J|$ for every finite $J \subseteq I$.
Then there is an injective map $f$ on $I$ with $f(i) \in A_i$ for each $i$, a system of distinct representatives.

17. Variables: $p_{i,x}$ for $i \in I$ and $x \in A_i$, read as "$f(i) = x$".
18. Formulas of $\Sigma_H$: (a) $\bigvee_{x \in A_i} p_{i,x}$ for each $i$, a finite disjunction because $A_i$ is finite; (b) $\neg (p_{i,x} \land p_{i,y})$ for $x \ne y$ in $A_i$; (c) $\neg (p_{i,x} \land p_{j,x})$ for $i \ne j$ and $x \in A_i \cap A_j$.
19. The case $J = \{ i \}$ of the hypothesis gives $|A_i| \ge 1$, so each disjunction in (a) has at least one term.
20. A model gives the map.
    Put $f(i) = x$ for the unique $x$ with $v(p_{i,x}) = 1$, which exists by (a) and is unique by (b).
    Then (c) says that $f$ is injective.
21. Finite satisfiability.
    A finite $\Sigma_0 \subseteq \Sigma_H$ mentions a finite set $J \subseteq I$ of indices.
    The finite family $(A_i)_{i \in J}$ satisfies the condition, so the finite [[Hall's marriage theorem|08WCB90WND]] gives an injective $f_0$ on $J$ with $f_0(i) \in A_i$.
22. Put $v(p_{i,x}) = 1$ when $i \in J$ and $f_0(i) = x$, and $0$ otherwise.
    Then (a) and (b) hold for $i \in J$, and (c) holds for $i, j \in J$ because $f_0$ is injective.
23. Compactness gives a model of $\Sigma_H$, and step 20 gives the system of distinct representatives.

Counterexample D: the sets must be finite.
Let $A_0 = \{ 1, 2, 3, \dots \}$ and $A_n = \{ n \}$ for $n \ge 1$.

24. The condition holds.
    For a finite $J \subseteq \mathbb{N}$ without $0$, the union is $J$ itself.
    For a finite $J$ with $0 \in J$, the union contains the infinite set $A_0$.
25. There is no system of distinct representatives.
    For $n \ge 1$ we must take $f(n) = n$.
    Then $f(0) = m$ for some $m \ge 1$, and $f(0) = f(m)$.
26. The encoding of step 18 breaks: for $i = 0$ the formula (a) would be an infinite disjunction, which is not a formula.

## Remarks

### The common pattern

The three proofs share one pattern: each condition on the object involves finitely many variables, and a finite theorem solves each finite piece.
The finite solutions need not agree with each other, and compactness replaces any gluing argument.

### What changes when something is infinite

The finiteness of $k$ in Application A is needed, as in Counterexample D.
Every finite subgraph of the complete graph on an uncountable set has a coloring with countably many colors, but the whole graph has none.
In the encoding, formula (a) of step 2 would be an infinite disjunction.

The [[chromatic number|0C5M7AM6FH]] of an infinite graph is therefore the largest chromatic number of its finite subgraphs, when this is finite.
With the axiom of choice, for example, the unit-distance graph of the plane has the same chromatic number as one of its finite subgraphs.

### How much choice is needed

For a countable graph, a countable set or a countable family, the variables are countable, and compactness needs no choice.
For arbitrary sizes, the variables form a set of arbitrary size, and the proof uses compactness for arbitrary $P$, which needs a choice principle.
No proof in ZF alone can exist.
For a family of disjoint pairs, a 2-coloring of the graph whose edges are the pairs, or a system of distinct representatives, picks one element from each pair.
In Application B, the order with $a \le b$ only for $a = b$ shows that every set can be linearly ordered, and that again picks one element from each pair.

### Watch out

Do not drop the transitivity formulas (c) of step 11.
Without them, the set $A = \{ a, b, c \}$ with the empty order has the model $v(p_{ab}) = v(p_{bc}) = v(p_{ca}) = 1$ and $v(p_{ba}) = v(p_{cb}) = v(p_{ac}) = 0$.
It satisfies (a) and (b), but it describes a cycle, not an order.
With (c), the instance $(p_{ab} \land p_{bc}) \to p_{ac}$ is false under this $v$, so the models are exactly the total orders.

### History

Nicolaas de Bruijn and Paul Erdős proved the theorem of Application A in 1951, and Walter Gottschalk gave a proof by Tychonoff's theorem in the same year.
Edward Szpilrajn proved the order extension principle in 1930.

## Explanations

### L1 human

Imagine an endless map, where each country must get one of three colors and neighbors must differ.
Suppose that every finite part of the map can be colored this way.
Compactness says that the whole endless map can then be colored.
Each rule, such as "these two neighbors differ", talks about only a few countries.
Compactness puts together the many finite solutions into one solution for everything.

### L2 human

We show that every set $X$, of any size, has a total order.
Nobody can write one down for a set such as the set of all subsets of the real line, so a direct construction is out of reach.
Apply Application B to the partial order on $X$ with $a \le b$ only when $a = b$.
Then (d) of step 11 is empty, and $\Sigma_X$ consists of the formulas
$$p_{ab} \lor p_{ba}, \qquad \neg (p_{ab} \land p_{ba}), \qquad (p_{ab} \land p_{bc}) \to p_{ac}$$
for distinct $a, b, c \in X$.

A finite $\Sigma_0 \subseteq \Sigma_X$ mentions a finite set $\{ a_1, \dots, a_n \}$ of distinct elements, and we order it by the index.
Put $v(p_{a_i a_j}) = 1$ when $i < j$, and $0$ otherwise.
Exactly one of $i < j$, $j < i$ holds, so the first two formulas are true, and $i < j < l$ gives $i < l$, so the third is true.
Compactness gives a model of $\Sigma_X$, and step 12 turns it into a total order on $X$.

The typical use is this one: the finite pieces are easy, and compactness produces an infinite object that nobody can describe.
Watch out: every condition must be a finite formula, and Counterexample D shows that the method fails for a family with an infinite set.

### L3 human

These applications are statements of the form "local solutions give a global solution", and compactness is the topological reason behind them.
The space of all candidate objects, such as all colorings, all relations or all choice functions, is a closed subspace of a product of finite discrete spaces, and so compact.
Over ZF, all three statements for arbitrary sizes follow from the Boolean prime ideal theorem, and none of them follows from ZF alone.
The same method with first-order logic gives nonstandard models, and the method of finite pieces appears again in Ramsey theory and in the theory of infinite graphs.
