---
tag: JXTCC6KXNG
kind: example
name: Tseitin formulas
aliases: [tseitin-formulas, tseitin-tautologies]
msc: ["03F20", "05C50"]
topics: [CBAF7J051K]
audience: research
illustrates: [6JSH907W5R, HF1GHVRDSD]
uses: [6JSH907W5R, 0B3D4C8YF2, BBR7QAD87Y, 0KA4S8R39M]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
  - url: https://en.wikipedia.org/wiki/Expander_graph
    locator: lead section
---

## Example

Take the triangle on the vertices $1, 2, 3$, put a charge $1$ on vertex $1$ and $0$ on the others, and ask for $0/1$ values on the edges whose sum at each vertex is its charge modulo $2$.
Let $a = x_{12}$, $b = x_{13}$ and $c = x_{23}$.
The three parity constraints, each written as two clauses, give six clauses.

- Vertex $1$, $a \oplus b = 1$: $\{a, b\}$ and $\{\neg a, \neg b\}$.
- Vertex $2$, $a \oplus c = 0$: $\{\neg a, c\}$ and $\{a, \neg c\}$.
- Vertex $3$, $b \oplus c = 0$: $\{\neg b, c\}$ and $\{b, \neg c\}$.

The charges add up to $1$, an odd number, so no assignment satisfies all six clauses.
Indeed, adding the three equations modulo $2$ gives $2a + 2b + 2c = 0$ on the left and $1$ on the right.

In general, let $G = (V, E)$ be a finite connected graph, and let $\chi \colon V \to \{0, 1\}$ be a *charge* on its vertices.
Take one variable $x_e$ for each edge $e$.
For a vertex $v$, the *parity constraint* $\mathrm{PAR}_v$ says that the sum modulo $2$ of the $x_e$ over the edges $e$ at $v$ is $\chi(v)$.
Write $\mathrm{PAR}_v$ as a [[CNF|0B3D4C8YF2]]: for each assignment to the edges at $v$ with the wrong parity, add the clause that excludes it.
For a vertex of degree $d$, this gives $2^{d-1}$ clauses of width $d$.
The *Tseitin formula* $T(G, \chi)$ is the union of these CNFs over all $v \in V$.

**Fact.** $T(G, \chi)$ is unsatisfiable if and only if $\sum_{v \in V} \chi(v)$ is odd.

1. Add all the constraints modulo $2$.
   Each edge has two ends, so each $x_e$ occurs twice, and the left sides add up to $0$.
2. So a satisfying assignment gives $\sum_v \chi(v) \equiv 0 \pmod 2$.
   If the sum is odd, no assignment exists.
3. If the sum is even, choose a spanning tree of $G$, set the edges outside the tree to $0$, and fix the tree edges from the leaves inward.
   Each leaf edge is forced by its leaf, and the last vertex is right because the total sum is even.

## Remarks

### The proof systems

On a family of bounded-degree [[expander graphs|BBR7QAD87Y]], every [[resolution refutation|6JSH907W5R]] of $T(G, \chi)$ with odd total charge has size $2^{\Omega(\lvert V \rvert)}$ in clauses.
This is [[Urquhart's theorem|HF1GHVRDSD]] of 1987, and its modern proof bounds the width first.
The formulas have polynomial-size [[Frege|J2BAR09TPF]] proofs, which add the parity constraints by Gaussian elimination over $\mathbb F_2$, with formulas for the parity of many variables.
In the [[polynomial calculus|ZERBQSTZB5]] over $\mathbb F_2$, each $\mathrm{PAR}_v$ gives a linear equation, and the sum of all of them is $1 = 0$.
So that system refutes $T(G, \chi)$ in polynomial size, with degree at most the largest degree of $G$.
Over fields of characteristic other than $2$, the degree must be large on expanders.
Dadush and Tiwari gave quasi-polynomial-size [[cutting planes|KKCX2HQP2K]] refutations of the Tseitin formulas in 2020.

### Why the degree is bounded

For a $d$-regular graph, $T(G, \chi)$ has $2^{d-1} \lvert V \rvert$ clauses of width $d$.
So the input is of polynomial size only when $d$ is bounded, and then the [[size-width relation|GWDGRPAQSM]] applies with $w(F) = d$.

### Watch out

Up to replacing some variables $x_e$ by $\neg x_e$, the formula depends on the charge only through the parity of its total.
Changing the charge on two vertices $u$ and $v$ gives the formula that we get by this replacement for the edges of a path from $u$ to $v$.
So hardness is a property of the graph, and the graphs that make resolution fail are the well-connected ones.
On a cycle the refutation follows the cycle and stays small.

### History

Grigori Tseitin introduced these formulas in 1968, in his work on the complexity of derivations in propositional calculus.
He proved exponential lower bounds for regular resolution on them.
Alasdair Urquhart extended the bound to general resolution in 1987.

## Explanations

### L1 human

Put a number $0$ or $1$ on each vertex of a network, and ask for a choice of $0$ or $1$ on each link.
The rule is that the links at each vertex add up to its number, counted modulo $2$.
If the vertex numbers add up to an odd number, this is impossible, because every link is counted at both of its ends.
Resolution cannot see this short parity argument when the network is well connected, and it needs exponentially many steps.

### L2 human

We refute the triangle case by resolution.

1. From $\{a, b\}$ and $\{\neg b, c\}$, resolve on $b$: $\{a, c\}$.
2. From $\{a, c\}$ and $\{a, \neg c\}$, resolve on $c$: $\{a\}$.
3. From $\{\neg a, \neg b\}$ and $\{b, \neg c\}$, resolve on $b$: $\{\neg a, \neg c\}$.
4. From $\{\neg a, \neg c\}$ and $\{\neg a, c\}$, resolve on $c$: $\{\neg a\}$.
5. From $\{a\}$ and $\{\neg a\}$, resolve on $a$: $\square$.

The refutation uses all six axioms and has $11$ clauses and width $2$.
On expanders the width must grow with the number of vertices.
The typical use of the formulas is as a test: a proof system that can count modulo $2$ refutes them easily.
A trap: the number of clauses is exponential in the degree, so the graphs must have bounded degree.

### L3 human

Tseitin formulas are the standard hard examples for systems that cannot reason about linear equations over $\mathbb F_2$.
Their hardness for resolution comes from the expansion of the graph: a clause that "knows" about a large set of vertices must mention every edge leaving that set.
They separate resolution from the polynomial calculus over $\mathbb F_2$, and they play the same role for many other systems.
