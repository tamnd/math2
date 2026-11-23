---
tag: 20CVX2A6VV
kind: proof
name: Proof structure of Ajtai's theorem by the matching switching lemma
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
proves: Q0ERK64J78
uses: [41QJ1WEMJ3, RJ571F7FF0, J2BAR09TPF, 8ZVN9X9WEC, 3B55HNS754]
methods: [0J0XBKG64S, 3B55HNS754, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
---

## Proof

We give the structure of the proof of the exponential form, following Pitassi, Beame and Impagliazzo, and Krajíček, Pudlák and Woods.
The step that we cite is the *matching switching lemma* of these authors, which we state in step 6 without its constants.
Work with a depth-$d$ refutation $\pi$ of size $S$, with lines over $\land$, $\lor$ and literals.
Its axioms are the pigeon clauses $P_i = \bigvee_j x_{ij}$ and the hole clauses $H_{i,i',j} = \neg x_{ij} \lor \neg x_{i'j}$.
We show that $S \ge 2^{n^{\varepsilon_d}}$ for large $n$.

### Part 1: restrictions and trees

1. A *matching restriction* $\rho$ is a partial matching between pigeons and holes.
   It sets $x_{ij} = 1$ when $\rho$ matches $i$ with $j$.
   It sets $x_{ij'} = 0$ and $x_{i'j} = 0$ for the other pairs at a matched pigeon $i$ or hole $j$, and it leaves the other variables free.
2. If $\rho$ matches $n - m$ pairs, then $\mathrm{PHP}^{n+1}_n$ restricted by $\rho$ is $\mathrm{PHP}^{m+1}_m$ on the unmatched pigeons and holes, up to clauses that become true.
   So $\pi$ restricted by $\rho$ is a depth-$d$ refutation of $\mathrm{PHP}^{m+1}_m$ of size at most $S$.
3. A *matching decision tree* over $m + 1$ pigeons and $m$ holes is a [[decision tree|8ZVN9X9WEC]] whose nodes ask "where is pigeon $i$?" or "which pigeon is in hole $j$?".
   The branches are the holes or pigeons that are still free, so each path is a partial matching.
   Each leaf has a label $0$ or $1$, and the *height* of the tree is the length of its longest path.
4. Two partial matchings are *compatible* if their union is a matching.
   A *matching term* is a partial matching, read as the conjunction of its variables $x_{ij}$.
   A *matching DNF* is a disjunction of matching terms.
5. A tree $T$ *represents* a matching DNF $D$ if every path to a $1$-leaf contains a term of $D$, and every path to a $0$-leaf is incompatible with every term of $D$.

### Part 2: the switching step

6. *Matching switching lemma (cited).* Let $D$ be a matching DNF whose terms have at most $s$ pairs, and let $\rho$ be a random matching restriction that leaves $m$ holes free.
   Then the probability that $D$ restricted by $\rho$ has no representing matching decision tree of height at most $s$ is at most $\alpha^s$.
7. A matching decision tree restricted by a matching restriction is a matching decision tree of no larger height, so trees found in one round survive the later rounds.
   Conjunctions are read by De Morgan's laws as negated disjunctions of negations.
8. Apply $d$ rounds of random matching restrictions $\rho_1, \dots, \rho_d$.
   In round $k$, take each subformula $\bigvee \Phi$ of depth $k$ of every line of $\pi$, where each $\varphi \in \Phi$ already has a tree $T(\varphi)$ of height at most $s$.
   Apply step 6 to the matching DNF whose terms are the paths to $1$-leaves of the trees $T(\varphi)$ for $\varphi \in \Phi$.
9. The number $\alpha < 1$ of step 6 depends on $s$, $m$ and $n$, and it is small when $s$ and $m$ are small powers of $n$.
   The proof $\pi$ has at most $S$ subformulas in all its lines.
   By the union bound, round $k$ fails for some subformula with probability at most $S \alpha^s$.
10. Choose $s = n^{\delta_d}$ for a small $\delta_d > 0$.
    If $S < 2^{n^{\varepsilon_d}}$ with $\varepsilon_d < \delta_d$, then $S \alpha^s < 1$ for large $n$.
    So in each round some restriction succeeds for every subformula at once.
11. After the $d$ rounds there are $m_d$ free holes, where $m_d$ is a positive power of $n$ that depends on $d$, and $s$ is small compared with $m_d$.

### Part 3: the evaluation

12. Steps 8 to 11 give a map $T$ from subformulas to matching decision trees of height at most $s$, called an *$s$-evaluation*.
    The tree of $x_{ij}$ asks "where is pigeon $i$?" and has label $1$ only on the branch to hole $j$.
    The tree of $\neg \varphi$ exchanges the labels of the tree of $\varphi$.
    The tree of $\bigvee \Phi$ represents the matching DNF of step 8.
13. Let $\sigma$ be a path that extends a leaf path of $T(\bigvee \Phi)$ and of every $T(\varphi)$ for $\varphi \in \Phi$.
    Then the label of $T(\bigvee \Phi)$ at $\sigma$ is the disjunction of the labels of the $T(\varphi)$ at $\sigma$, by the two conditions of step 5.
    So along such a $\sigma$, the labels obey the truth tables of $\neg$ and $\lor$.
14. Say that a line $\varphi$ is *true under $T$* if every leaf of $T(\varphi)$ has label $1$.

### Part 3, the axioms and the rules

15. Every pigeon clause $P_i$ is true under $T$.
    A $0$-leaf path $\sigma$ would be incompatible with every pair $(i, j)$ with $j$ free.
    Then $\sigma$ would fill all $m_d$ free holes with other pigeons, which needs length $m_d > s$.
16. Every hole clause $H_{i,i',j}$ is true under $T$.
    A $0$-leaf path $\sigma$ would be incompatible with every pair $(i, j')$ and every pair $(i', j')$ with $j' \ne j$.
    Since $\sigma$ has length at most $s < m_d$, it leaves holes free, so it must match both $i$ and $i'$ to $j$, which a matching cannot do.
17. Each rule of $\mathcal F$ preserves truth under $T$.
    A rule involves a bounded number $r$ of subformulas, and compatible paths of total length below $m_d$ extend to one matching.
    So the trees of these subformulas have a common refinement of height at most $r s$.
    On its leaves, step 13 gives the subformulas Boolean values, and the sound rule gives the conclusion the value $1$.
18. So, by induction on the lines of $\pi$, every line is true under $T$.
19. The last line of $\pi$ is the empty disjunction, the constant $0$.
    Its tree is the single leaf $0$, so it is not true under $T$, and this contradicts step 18.
20. So the assumption of step 10 fails, and $S \ge 2^{n^{\varepsilon_d}}$ for large $n$. $\blacksquare$

## Idea

A small proof of bounded depth collapses under a random partial matching.
After the collapse every line is a shallow matching decision tree, and these trees behave like truth values that satisfy the axioms and the rules.
But no truth values can satisfy all axioms of the pigeonhole principle and also its contradictory last line.
Students often slip on why the axioms come out true.
The trees are shallow compared with the number of free holes, so a short path can never rule out every hole for a pigeon.

## Variants

Ajtai's original proof built a nonstandard model of arithmetic with a bijection between $n + 1$ and $n$ that is generic for the bounded formulas, by forcing.
A combinatorial lemma on restrictions plays the role of the switching lemma there, and it gives only a superpolynomial bound.
Urquhart and Fu gave a shorter version of the switching argument for the pigeonhole principle.
The same structure with other restrictions gives lower bounds in bounded depth for counting principles modulo $p$ and for Tseitin formulas, and only the switching lemma changes.
