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

Put $3$ pigeons into $2$ holes, and count the pairs (pigeon, hole) with the pigeon in the hole.
Each pigeon sits somewhere, so the count is at least $3$, and each hole holds at most one pigeon, so the count is at most $2$.
Buss's theorem says that a Frege system can carry out this double count for every $n$, in polynomial size.

Let $\mathcal F$ be a [[Frege system|J2BAR09TPF]].
There is a polynomial $q$ such that, for every $n \ge 1$, the tautology $\neg \mathrm{PHP}^{n+1}_n$ has an $\mathcal F$-proof of size at most $q(n)$.
Here $\mathrm{PHP}^{n+1}_n$ is the conjunction of the clauses of the [[pigeonhole formula|RJ571F7FF0]], which has size polynomial in $n$.
The system is Frege, and the measure is size in symbols.

## Remarks

### Why each hypothesis is needed

The system must be at least as strong as Frege.
In [[resolution|6JSH907W5R]] the same formulas need exponential size, by [[Haken's theorem|4PCEYEW3JG]].
In [[bounded-depth Frege|41QJ1WEMJ3]] of any fixed depth they need superpolynomial size, by [[Ajtai's theorem|Q0ERK64J78]].
The proof needs lines of depth growing like $\log n$, because it writes sums of up to $n(n+1)$ bits as formulas, and that is exactly what a fixed depth forbids.

### What it gives you

The theorem separates systems.
Frege is exponentially stronger than resolution, and superpolynomially stronger than every fixed depth of bounded-depth Frege, because one family has polynomial-size Frege proofs and no short proofs in the weaker systems.
It also removes the pigeonhole formulas from the list of candidates for [[lower bounds for Frege systems|ANSV13M4FS]].

### Other systems with short proofs

Frege is not the weakest system with polynomial-size proofs of these formulas.
[[Cutting planes|40KJ0VKNG7]] has them too, because its lines are linear inequalities and it can add up the pigeon clauses directly.

### Generalizations

The same counting method gives polynomial-size Frege proofs of $\neg \mathrm{PHP}^m_n$ for every $m > n$.
It also gives polynomial-size Frege proofs of the [[Tseitin formulas|JXTCC6KXNG]], where the count is modulo $2$, and of other principles of counting.

### Watch out

The polynomial size is a statement about Frege only.
It does not give short proofs in resolution, where lines are clauses, and a clause can only say that at least one of its literals is true.
A count such as "at least $3$ of these $6$ variables are true" needs many clauses, one for each way the count could fail.
The size is also not small in practice: the theorem gives some polynomial, and the formulas for binary sums make it a high one.

## History

Cook and Reckhow gave polynomial-size proofs in extended Frege in 1979 and asked whether Frege has them too.
Samuel Buss answered the question in 1987, in "Polynomial size proofs of the propositional pigeonhole principle" in the Journal of Symbolic Logic.

## Explanations

### L1 human

A Frege proof can count.
It writes, as formulas, the number of pigeons and the number of holes in binary, and it checks that the first number is larger.
For $1000$ pigeons, a search through all placements is hopeless, but a Frege proof whose size is a fixed power of $1000$ exists.

### L2 human

Here is the counting plan for $n = 2$, the formula $\mathrm{PHP}^3_2$ with variables $x_{ij}$ for "pigeon $i$ is in hole $j$".
Each of the $3$ pigeons sits in some hole, so the number of true $x_{ij}$ is at least $3$.
Each of the $2$ holes holds at most one pigeon, so the same number is at most $2$.
Since $3 \le 2$ is false, the clauses cannot all hold.
A Frege proof writes the two totals as formulas for binary numbers and proves each step in polynomial size, as the [[proof|PE43N5E9PR]] outlines.
This is the typical use of the theorem: to show that a counting argument, once it can be written with formulas, gives short Frege proofs.

### L3 human

The theorem is the propositional shadow of the fact that weak theories of arithmetic can count.
Counting needs formulas of logarithmic depth, which is the circuit class $\mathrm{NC}^1$, and Frege systems match exactly that class.
Bounded-depth Frege matches $\mathrm{AC}^0$, which cannot compute parity or majority, and that is why it fails on the same formulas.
