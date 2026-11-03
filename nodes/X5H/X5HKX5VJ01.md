---
tag: X5HKX5VJ01
kind: statement
role: theorem
name: Greedy algorithm for matroids
msc: [05B35, 90C27]
uses: [PX31ZNYS3Z, PSM6NKYJB8, QTSQR7130G, 5FPWTYFJRA]
about: [PX31ZNYS3Z, PSM6NKYJB8]
sources:
  - url: https://en.wikipedia.org/wiki/Matroid
---

## Statement

Let $E$ be a finite set, and let $\mathcal{I}$ be a family of subsets of $E$ with $\emptyset \in \mathcal{I}$.
Assume that every subset of a member of $\mathcal{I}$ is in $\mathcal{I}$.
For a weight $w \colon E \to \R$, the *greedy algorithm* lists the elements of $E$ as $e_1, \dots, e_n$ with $w(e_1) \ge \cdots \ge w(e_n)$.
It starts with $I = \emptyset$, and for $i = 1, \dots, n$ it adds $e_i$ to $I$ when $w(e_i) > 0$ and $I \cup \set{e_i} \in \mathcal{I}$.
It returns the final set $I$.

1. If $(E, \mathcal{I})$ is a [[matroid|PX31ZNYS3Z]], then for every $w \colon E \to \R$ the greedy algorithm returns a set $I \in \mathcal{I}$ of largest weight $\sum_{e \in I} w(e)$.
2. Conversely, if for every $w \colon E \to \R$ the greedy algorithm returns a set in $\mathcal{I}$ of largest weight, then $(E, \mathcal{I})$ is a matroid.

## Remarks

For part 1, let $I = \set{a_1, \dots, a_k}$ be the greedy output in the order of choice.
Let $J = \set{b_1, \dots, b_m}$ be any independent set of positive elements with $w(b_1) \ge \cdots \ge w(b_m)$.
The exchange axiom shows that $w(a_j) \ge w(b_j)$ for each $j \le \min(k, m)$, and that $m \le k$; summing gives $w(I) \ge w(J)$.
For part 2, if the exchange axiom fails for sets $A, B$ with $\abs{A} > \abs{B}$, one chooses weights slightly larger on $B$ than on $A \setminus B$, and zero elsewhere.
Then greedy picks $B$ first and gets stuck, while $A$ has larger weight.

Example: take the graphic matroid of a connected graph with edge costs $c$, and set $w = C - c$ for a constant $C$ larger than every cost.
Then the greedy algorithm is [[Kruskal's algorithm|5FPWTYFJRA]], and it returns a minimum spanning tree.

Without the matroid hypothesis, part 1 fails.
Take $E = \set{x, y, z}$ and $\mathcal{I}$ the subsets of $\set{x}$ and of $\set{y, z}$, with $w(x) = 3$ and $w(y) = w(z) = 2$.
Greedy returns $\set{x}$ of weight $3$, but $\set{y, z}$ has weight $4$.

## Explanations

### L1 human

The greedy rule is: always take the best item that still fits.
For most problems this short-sighted rule can go wrong, as when taking one big item blocks two medium items worth more together.
The theorem says the rule never goes wrong exactly when the notion of "fits" has the structure of a matroid.
This explains why picking cheapest edges works for spanning trees.

### L2 human

The theorem is often called the Rado–Edmonds theorem, and it characterizes matroids among independence systems.
Its form for bases says that, without the condition $w(e_i) > 0$, the greedy algorithm finds a [[basis|QTSQR7130G]] of largest weight.
It is the basis of [[greedy algorithm|PSM6NKYJB8]] analysis in combinatorial optimization.
For the intersection of two matroids greedy fails, and one needs the matroid intersection algorithm instead.
In polyhedral terms, the greedy algorithm also proves that the matroid polytope is described by $x \ge 0$ and the rank inequalities $x(A) \le r(A)$ for $A \subseteq E$.
