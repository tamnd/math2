---
tag: WJXX7H6B6V
kind: statement
role: theorem
name: PCP theorem
msc: [68Q15, 68Q17, 68Q10]
uses: [QQRA9GBW51, K99S0Q0814, ESPYW94XGR]
about: [QQRA9GBW51]
sources:
  - url: https://en.wikipedia.org/wiki/PCP_theorem
same_as:
  wikidata: Q1140200
  wikipedia: PCP theorem
---

## Statement

Let $r, q \colon \N \to \N$ be functions.
A *probabilistically checkable proof verifier* with randomness $r$ and query complexity $q$ for a language $L \subseteq \set{0,1}^*$ is a [[probabilistic|K99S0Q0814]] polynomial-time algorithm $V$ with these properties.
It gets an input $x$ of length $n$ and oracle access to a string $\pi$, the proof.
It uses at most $r(n)$ random bits, reads at most $q(n)$ bits of $\pi$, and accepts or rejects.

1. Completeness: if $x \in L$, there is a proof $\pi$ such that $V$ accepts $x$ with probability $1$.
2. Soundness: if $x \notin L$, then for every string $\pi$, $V$ accepts $x$ with probability at most $1/2$.

The [[class|ESPYW94XGR]] $\mathrm{PCP}(r, q)$ is the set of languages that have such a verifier.

**Theorem.**
$$\mathrm{NP} = \mathrm{PCP}(O(\log n), O(1)).$$
That is, every language in [[NP|QQRA9GBW51]] has a verifier that uses $O(\log n)$ random bits and reads only a constant number of bits of the proof.

## Remarks

The inclusion $\mathrm{PCP}(O(\log n), O(1)) \subseteq \mathrm{NP}$ is easy.
With $O(\log n)$ random bits there are only polynomially many random strings.
So a nondeterministic machine can guess the polynomially many proof bits that can ever be read, and then check all random strings.
The hard inclusion was proved by Arora and Safra and by Arora, Lund, Motwani, Sudan and Szegedy, with algebraic tools such as low-degree tests.
Dinur later gave a combinatorial proof by repeated gap amplification of constraint graphs.

The theorem is equivalent to a statement on approximation.
There is a constant $\varepsilon > 0$ such that it is NP-hard to tell satisfiable 3-CNF formulas from those in which every assignment violates at least an $\varepsilon$ fraction of the clauses.
So MAX-3SAT has no polynomial-time approximation scheme unless $\mathrm{P} = \mathrm{NP}$.

The soundness constant $1/2$ is not essential: any constant in $(0, 1)$ gives the same class, by repeating the test a constant number of times.

## Explanations

### L1 human

A proof of a mathematical claim usually has to be read entirely to be checked.
The PCP theorem says that every NP proof can be rewritten in a robust format.
In this format a checker reads only a few randomly chosen bits and still catches a wrong proof with good probability.
The rewriting makes the proof only polynomially longer.

### L2 human

The PCP theorem is the starting point of hardness of approximation.
Its gap form says that approximating MAX-3SAT within some constant factor is as hard as solving it exactly.
Reductions that preserve gaps then transfer this hardness to clique, vertex cover, set cover and many other problems.
Refined versions, such as Håstad's three-query verifiers, give optimal constants for several problems.
The unique games conjecture asks for a strengthening with a special kind of two-query test.
