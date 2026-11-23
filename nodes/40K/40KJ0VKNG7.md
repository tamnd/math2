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

The pigeonhole formulas, which are exponentially hard for resolution, have short refutations in cutting planes, because cutting planes can count.

Let $n \geq 1$, and take the variables $x_{ij}$ for $i \in \{1, \dots, n+1\}$ and $j \in \{1, \dots, n\}$, read as "pigeon $i$ sits in hole $j$".
The [[pigeonhole formula|RJ571F7FF0]] $\mathrm{PHP}^{n+1}_n$ is the CNF with these clauses.

1. The pigeon clause $x_{i1} \vee \cdots \vee x_{in}$, for each pigeon $i$.
2. The hole clause $\neg x_{ij} \vee \neg x_{kj}$, for each hole $j$ and all pigeons $i < k$.

Then $\mathrm{PHP}^{n+1}_n$ has a [[cutting-planes refutation|KKCX2HQP2K]] with $O(n^3)$ lines in which every coefficient and every constant has absolute value at most $2n$.
So the refutation has length $O(n^3)$ and size $O(n^5 \log n)$ in bits, which is polynomial in the size of the formula.

## Remarks

### Three pigeons and two holes

For $n = 2$ the formula $\mathrm{PHP}^3_2$ has $3$ pigeon clauses and $2 \cdot \binom{3}{2} = 6$ hole clauses, so $9$ clauses in all.
For hole $1$ the three hole lines are $x_{11} + x_{21} \leq 1$, $x_{11} + x_{31} \leq 1$ and $x_{21} + x_{31} \leq 1$.
Their sum, divided by $2$ and rounded, is the line for hole $1$:
$$2(x_{11} + x_{21} + x_{31}) \leq 3, \qquad x_{11} + x_{21} + x_{31} \leq \lfloor 3/2 \rfloor = 1.$$
Hole $2$ gives $x_{12} + x_{22} + x_{32} \leq 1$ in the same way, and the sum of the two hole lines says that all six variables add up to at most $2$.
The three pigeon lines $x_{i1} + x_{i2} \geq 1$ add up to at least $3$.
So the sum of all six variables is both at most $2$ and at least $3$, and adding the two lines gives $0 \geq 1$.

### Why each hypothesis is needed

The number of pigeons must be larger than the number of holes.
With $n$ pigeons and $n$ holes, the assignment $x_{ii} = 1$ and all other $x_{ij} = 0$ satisfies every clause, so no refutation exists.

The division rule is needed for $n \geq 2$.
The point with every $x_{ij} = 1/n$ satisfies each pigeon line, since the sum is $n \cdot (1/n) = 1$, and each hole line, since $2/n \leq 1$.
Every line derived by linear combination alone holds at this point too, because the weights are non-negative.
So such lines never reach $0 \geq 1$.

### What it gives you

By [[Haken's theorem|4PCEYEW3JG]], every [[resolution|6JSH907W5R]] refutation of $\mathrm{PHP}^{n+1}_n$ has size $2^{\Omega(n)}$ in clauses.
Since CP p-simulates resolution, CP is exponentially stronger than resolution.
In [[bounded-depth Frege|41QJ1WEMJ3]] of fixed depth $d$, refutations of the same formulas need size $2^{n^{\varepsilon_d}}$ for some $\varepsilon_d > 0$.
So bounded-depth Frege does not p-simulate CP.

### Not every hard formula is easy here

Is every formula that is hard for resolution easy for CP?
No.
The clique-coloring formulas need resolution refutations of size $2^{n^{\Omega(1)}}$, by [[monotone interpolation|F8GJ402PH2]].
They also need CP refutations with $2^{n^{\Omega(1)}}$ lines, by [[Pudlák's theorem|5RYPXFF0G2]].

### Generalizations

The same argument refutes $\mathrm{PHP}^m_n$ for every $m > n$, because the final count uses the pigeon lines of only $n + 1$ pigeons.
It also refutes the variants with functional and onto clauses, since the refutation never uses the extra clauses.

### Watch out

The theorem bounds size, and size counts the bits of the coefficients.
A refutation with few lines but coefficients of exponential size would not be short in this sense.
Here every number is at most $2n$, so each number has $O(\log n)$ bits.
A second slip is to carry the upper bound down to a weaker system.
CP p-simulates resolution, but resolution does not p-simulate CP, and the same formulas need exponential size in resolution.

## History

William Cook, Collette Coullard and György Turán studied cutting planes as a propositional proof system and gave these refutations in 1987.

## Explanations

### L1 human

Put $n + 1$ pigeons into $n$ holes, with at most one pigeon in each hole.
Cutting planes proves that this is impossible by counting.
First it shows, for each hole, that the number of pigeons in it is at most $1$.
Adding over the holes, at most $n$ pigeons are placed.
But each pigeon is in some hole, so at least $n + 1$ are placed, and $n + 1 \leq n$ is false.
For $3$ pigeons and $2$ holes the count gives $3 \leq 2$.

### L2 human

The only hard part is the line $\sum_i x_{ij} \leq 1$ for one hole, because the clauses speak about pairs of pigeons only.
The [[proof|13Y3JADJ8G]] adds one pigeon at a time.
Suppose that pigeons $1$ and $2$ already satisfy $x_{1j} + x_{2j} \leq 1$, and we bring in pigeon $3$.
Take one copy of the old line and the two new hole lines $x_{1j} + x_{3j} \leq 1$ and $x_{2j} + x_{3j} \leq 1$:
$$(x_{1j} + x_{2j}) + (x_{1j} + x_{3j}) + (x_{2j} + x_{3j}) \leq 3.$$
The left side is $2(x_{1j} + x_{2j} + x_{3j})$, and division by $2$ gives the line for three pigeons.
With $k$ pigeons in the old line, we take $k - 1$ copies of it, add the $k$ new hole lines and divide by $k$.
This is the typical use of CP: build a counting inequality by induction, one division per step.

### L3 human

The theorem shows that the hardness of a formula depends on the proof system: counting is hard for resolution and easy for CP.
The pigeonhole formulas are also easy for [[Frege systems|J2BAR09TPF]], by Buss's theorem of 1987, and hard for bounded-depth Frege.
In the [[algebraic proof systems|ZERBQSTZB5]] they are hard in degree: Razborov proved in 1998 that polynomial calculus refutations need degree growing linearly in $n$.
So each system has its own hard formulas, and a lower bound for one system says nothing about a stronger one.
