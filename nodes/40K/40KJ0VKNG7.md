---
tag: 40KJ0VKNG7
kind: statement
role: theorem
name: Polynomial cutting-planes refutations of the pigeonhole formulas
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [KKCX2HQP2K, RJ571F7FF0]
about: [KKCX2HQP2K, RJ571F7FF0]
proofs: [13Y3JADJ8G]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
history:
  first_stated: "1987"
  notes: "William Cook, Collette Coullard and György Turán, On the complexity of cutting-plane proofs, Discrete Applied Mathematics 18 (1987)."
---

## Statement

Let $n \geq 1$, and take the variables $x_{ij}$ for $i \in \set{1, \dots, n+1}$ and $j \in \set{1, \dots, n}$, read as "pigeon $i$ sits in hole $j$".
The [[pigeonhole formula|RJ571F7FF0]] $\mathrm{PHP}^{n+1}_n$ is the CNF with these clauses.

1. **Pigeon clauses.** $x_{i1} \vee \cdots \vee x_{in}$ for each pigeon $i$.
2. **Hole clauses.** $\neg x_{ij} \vee \neg x_{kj}$ for each hole $j$ and all pigeons $i < k$.

Then $\mathrm{PHP}^{n+1}_n$ has a [[cutting-planes refutation|KKCX2HQP2K]] with $O(n^3)$ lines in which every coefficient and every constant has absolute value at most $2n$.
So the refutation has length $O(n^3)$ and size $O(n^5 \log n)$, which is polynomial in the size of the formula.

## Remarks

### Why each hypothesis is needed

The number of pigeons must be larger than the number of holes: with $n$ pigeons and $n$ holes, the formula is satisfied by $x_{ii} = 1$ and all other $x_{ij} = 0$, so it has no refutation.
The division rule of CP is needed for $n \geq 2$.
The point with all $x_{ij} = 1/n$ satisfies every axiom line: each pigeon line has sum $n \cdot (1/n) = 1$, and each hole line has sum $2/n \leq 1$.
A line derived by linear combination alone holds at this point too, since the weights are non-negative, so it cannot be $0 \geq 1$.

### Consequences

- By [[Haken's theorem|4PCEYEW3JG]], every [[resolution|6JSH907W5R]] refutation of $\mathrm{PHP}^{n+1}_n$ has size $2^{\Omega(n)}$. Since CP p-simulates resolution, CP is exponentially stronger than resolution.
- The same holds for bounded-depth Frege, in which the pigeonhole formulas also need exponential size; so [[bounded-depth Frege|41QJ1WEMJ3]] does not p-simulate CP.
- Lower bounds for CP need other formulas, such as the clique-colouring formulas of [[Pudlák's theorem|5RYPXFF0G2]].

### Converse

The statement is not an implication, so it has no converse in the strict sense.
The opposite question is whether every formula that is hard for resolution is easy for CP.
The answer is no: the clique-colouring formulas need exponential size in resolution, by [[monotone interpolation|F8GJ402PH2]], and exponential length in CP, by [[Pudlák's theorem|5RYPXFF0G2]].

### Generalizations

The same argument refutes $\mathrm{PHP}^m_n$ for every $m > n$: add only $n + 1$ of the pigeon lines.
It also refutes the variants with the functional and onto clauses, since the proof uses only the pigeon and hole clauses.

## History

William Cook, Collette Coullard and György Turán introduced cutting planes as a proof system and gave these refutations in 1987.

## Explanations

### L1 human

Put $n + 1$ pigeons into $n$ holes, with at most one pigeon in each hole.
Cutting planes proves that this is impossible by counting.
First it shows, for each hole, that the number of pigeons in it is at most $1$.
Adding over the holes, at most $n$ pigeons are placed.
But each pigeon is in some hole, so at least $n + 1$ are placed, and $n + 1 \leq n$ is false.
For $3$ pigeons and $2$ holes the count gives $3 \leq 2$.

### L2 human

For one hole $j$ and three pigeons, we derive $x_{1j} + x_{2j} + x_{3j} \leq 1$.

1. The hole axioms give $x_{1j} + x_{2j} \leq 1$, $x_{1j} + x_{3j} \leq 1$ and $x_{2j} + x_{3j} \leq 1$.
2. Their sum is $2 x_{1j} + 2 x_{2j} + 2 x_{3j} \leq 3$.
3. Division by $2$ gives $x_{1j} + x_{2j} + x_{3j} \leq \floor{3/2} = 1$.

The proof of the theorem repeats this step with $k$ pigeons in place of $2$.
A trap: the theorem gives polynomial size, and size counts the bits of the coefficients, so we must check that the coefficients stay small.
Here they are at most $2n$, so each has $O(\log n)$ bits.

### L3 human

The theorem shows that the hardness of a formula depends on the proof system: counting is hard for resolution and easy for CP.
The pigeonhole formulas are also easy for [[Frege systems|J2BAR09TPF]] (Buss), and they are hard for bounded-depth Frege.
In the [[algebraic proof systems|ZERBQSTZB5]] they are hard in degree: polynomial calculus needs degree at least $n/2 + 1$ (Razborov).
So each system has its own hard formulas, and a lower bound for one system says nothing about a stronger one.
