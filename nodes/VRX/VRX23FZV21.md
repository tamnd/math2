---
tag: VRX23FZV21
kind: statement
role: theorem
name: Buss's theorem on Frege proofs of the pigeonhole principle
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
uses: [RJ571F7FF0, J2BAR09TPF]
about: [J2BAR09TPF, RJ571F7FF0, ANSV13M4FS]
proofs: [PE43N5E9PR]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
history:
  first_stated: "1987"
  notes: "Samuel R. Buss, Polynomial size proofs of the propositional pigeonhole principle, Journal of Symbolic Logic, 1987."
---

## Statement

Let $\mathcal F$ be a [[Frege system|J2BAR09TPF]].
There is a polynomial $q$ such that, for every $n \ge 1$, the tautology $\neg \mathrm{PHP}^{n+1}_n$ has an $\mathcal F$-proof of size at most $q(n)$.

Here $\mathrm{PHP}^{n+1}_n$ is the conjunction of the clauses of the [[pigeonhole formula|RJ571F7FF0]], so $\neg \mathrm{PHP}^{n+1}_n$ has size polynomial in $n$.
The system is Frege, and the measure is size in symbols.

## Remarks

### Why each hypothesis is needed

- The system must be at least as strong as Frege. Resolution and bounded-depth Frege need exponential size; see [[Haken's theorem|4PCEYEW3JG]] and [[Ajtai's theorem|Q0ERK64J78]].
- The proof uses formulas of depth growing like $\log n$, to count. So depth-$d$ Frege for a fixed $d$ does not suffice.

### Consequences

- Frege systems are exponentially stronger than resolution and than every fixed depth of bounded-depth Frege.
- The pigeonhole formulas are not candidates for [[lower bounds for Frege systems|ANSV13M4FS]].

### Converse

The theorem is an upper bound for Frege systems.
The matching question for weaker systems has a negative answer: resolution and bounded-depth Frege have no polynomial-size proofs of these formulas.

### Generalizations

- The same counting method gives polynomial-size Frege proofs of $\neg \mathrm{PHP}^m_n$ for every $m > n$.
- It also gives polynomial-size Frege proofs of the [[Tseitin formulas|JXTCC6KXNG]] and of other statements of counting.

## History

Cook and Reckhow gave polynomial-size proofs in extended Frege in 1979 and asked about Frege.
Samuel Buss answered the question in 1987, in "Polynomial size proofs of the propositional pigeonhole principle".

## Explanations

### L1 human

A Frege proof can count.
It writes, as formulas, the binary number of pigeons and the binary number of holes, and it checks that the first number is larger.
For $n = 1000$, a direct search through all placements of pigeons is hopeless, but a Frege proof of size about a fixed power of $1000$ exists.

### L2 human

We see the counting plan for $n = 2$.

1. Each of the $3$ pigeons sits in some hole, so the total number of pairs (pigeon, hole) that are true is at least $3$.
2. Each of the $2$ holes has at most one pigeon, so the same total is at most $2$.
3. $3 \le 2$ is false.

A Frege proof writes the totals as formulas for binary numbers, and it proves each step in polynomial size.
A trap: the proof needs formulas that compute sums of many bits, so it does not work in resolution, whose lines are clauses.
