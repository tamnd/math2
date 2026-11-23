---
tag: HF1GHVRDSD
kind: statement
role: theorem
name: Urquhart's theorem on Tseitin formulas
msc: ["03F20", "05C50"]
topics: [CBAF7J051K]
audience: research
uses: [JXTCC6KXNG, 6JSH907W5R, GWDGRPAQSM, BBR7QAD87Y]
about: [JXTCC6KXNG, 6JSH907W5R]
proofs: [HZ9VYPSH98]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
history:
  first_stated: "1987"
  notes: "Alasdair Urquhart, Hard examples for resolution, Journal of the ACM, 1987. The proof given here is the width proof of Ben-Sasson and Wigderson."
---

## Statement

Urquhart's theorem says that resolution needs exponentially many clauses to refute the Tseitin formulas of a well-connected graph.
For example, on the complete graph $K_4$, which is $3$-regular, the [[Tseitin formula|JXTCC6KXNG]] with odd charge has $6$ variables and $16$ clauses of width $3$.
Every set of $2$ vertices of $K_4$ has $4$ edges leaving it, and part 1 below says that every refutation then contains a clause of width at least $4$.

Let $G = (V, E)$ be a connected $d$-regular graph with $N = \lvert V \rvert \ge 4$ vertices, and let $\chi$ be a charge with odd total sum.
Write $E(U, V \setminus U)$ for the set of edges with one end in $U$ and one end outside $U$.
The *edge expansion* is
$$e(G) = \min \bigl\{ \lvert E(U, V \setminus U) \rvert : U \subseteq V, \ N/3 \le \lvert U \rvert \le 2N/3 \bigr\}.$$

**Theorem.**

1. Every [[resolution refutation|6JSH907W5R]] of $T(G, \chi)$ has width at least $e(G)$.
2. If $e(G) \ge d + 1$, every resolution refutation of $T(G, \chi)$ has at least $\exp\bigl((e(G) - d - 1)^2/(4 d N)\bigr)$ clauses.

**Corollary (Urquhart).** Let $d$ and $\varepsilon > 0$ be constants, and let $G_N$ be $d$-regular [[expander graphs|BBR7QAD87Y]] with $e(G_N) \ge \varepsilon N$ for infinitely many $N$.
Then resolution refutations of $T(G_N, \chi)$ with odd charge need $2^{\Omega(N)}$ clauses.

The proof system is general resolution, and the measures are width and size in clauses.

## Remarks

### Why each hypothesis is needed

The total charge must be odd, since otherwise the formula is satisfiable and has no refutation.
The graph must expand.
On a cycle of length $N$ we have $e(G) = 2$, and $T(G, \chi)$ has refutations of polynomial size that follow the cycle.
The degree must be bounded.
The formula has $2^{d-1}$ clauses per vertex, so for large $d$ its own size is exponential in $d$, and a bound exponential in $N$ may say little.

### What it gives you

Resolution is not polynomially bounded, by a second family besides the [[pigeonhole formulas|RJ571F7FF0]].
[[Frege systems|J2BAR09TPF]] and the [[polynomial calculus|ZERBQSTZB5]] over $\mathbb F_2$ refute these formulas in polynomial size.
So resolution is exponentially weaker than both of them.

### The converse

Alekhnovich and Razborov showed in 2002 that $T(G, \chi)$ has resolution refutations of size polynomial in $N$ times $2^{O(b)}$, where $b$ is the branch-width of $G$.
So graphs of small branch-width give easy Tseitin formulas, and the hardness comes from the expansion of the graph.

### Generalizations

The same width argument gives exponential bounds for random $3$-CNFs and for the pigeonhole formulas on bipartite expanders.
For the polynomial calculus over a field of characteristic other than $2$, the Tseitin formulas on expanders need linear degree.

### Watch out

Part 2 needs the general [[size-width relation|GWDGRPAQSM]], whose bound is weak for small width.
For $K_4$ the width bound $4$ is exactly $d + 1$, so part 2 gives only $1$ clause.
The theorem is an asymptotic statement, and it bites only when $e(G)$ is much larger than $\sqrt{dN}$.

## History

Grigori Tseitin introduced these formulas in 1968 and proved exponential lower bounds for regular resolution.
Alasdair Urquhart proved the exponential lower bound for general resolution on expanders in 1987, in "Hard examples for resolution".
Eli Ben-Sasson and Avi Wigderson gave the width proof in 1999.

## Explanations

### L1 human

Tseitin formulas say that a network with an odd total charge can be wired so that each node has the right parity.
The theorem says that resolution proofs that this is impossible are exponentially long on well-connected networks.
For example, on a network of $N$ nodes with $3$ links each and good connectivity, the number of steps grows like $c^N$ for a constant $c > 1$.

### L2 human

We read off the size bound for a $3$-regular graph with $e(G) \ge N/20$ and $N \ge 160$.
First, $e(G) - d - 1 \ge N/20 - 4 \ge N/40$, where the last step uses $N \ge 160$.
So the bound is
$$\exp\left(\frac{(N/40)^2}{12 N}\right) = \exp\left(\frac{N}{19200}\right).$$
The constant is small, but the bound is exponential in $N$.
The typical use is as a hard example for resolution and for SAT solvers based on it.
A trap: the theorem says nothing about stronger systems.
The polynomial calculus over $\mathbb F_2$ refutes these formulas in polynomial size, and cutting planes refutes them in quasi-polynomial size.

### L3 human

The proof measures how many vertex constraints a clause needs, and it shows that a clause in the middle of a refutation needs a medium-sized set of them.
Expansion then forces that clause to mention every edge that leaves the set.
This "medium complexity clause" argument is the common core of Haken's theorem, Urquhart's theorem and the bounds for random formulas.
