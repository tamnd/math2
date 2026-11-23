---
tag: SSJGW960SY
kind: example
name: Resolution as a Cook-Reckhow proof system
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
instance_of: [3V24CYWDT6]
uses: [3V24CYWDT6, 6JSH907W5R, S367PDDP61]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
  - url: https://en.wikipedia.org/wiki/Tseitin_transformation
    locator: lead section
---

## Example

We prove the tautology of modus ponens,
$$\tau = (p \land (\neg p \lor q)) \to q,$$
by refuting its negation with [[resolution|6JSH907W5R]], and then we check that the whole scheme is a [[propositional proof system|3V24CYWDT6]].

1. *The CNF of $\neg \tau$.*
   By De Morgan's laws, $\neg \tau$ is $p \land (\neg p \lor q) \land \neg q$.
   This is already a CNF, with the clauses $C_1 = \{p\}$, $C_2 = \{\neg p, q\}$ and $C_3 = \{\neg q\}$.
2. *The refutation.*
   Resolve $C_1$ and $C_2$ on $p$ to get $C_4 = \{q\}$.
   Resolve $C_4$ and $C_3$ on $q$ to get the empty clause $C_5 = \square$.
3. *The proof string.*
   The proof of $\tau$ is $w = \tau \, \# \, C_1, C_2, C_3, C_4, C_5$.
4. *The check.*
   The checker $f$ computes the CNF of $\neg \tau$ and tests that $C_1, C_2, C_3$ are its clauses.
   It tests that $C_4$ and $C_5$ are resolvents of earlier clauses and that $C_5$ is empty.
   All tests pass, so $f(w) = \tau$.

For a general $\tau$ the CNF of $\neg \tau$ by distribution can be exponentially long, so $f$ must fix one translation that runs in polynomial time.
A standard choice is the [[Tseitin transformation|S367PDDP61]], which adds a new variable for each subformula of $\neg \tau$ and writes $O(\lvert \tau \rvert)$ clauses of width at most $3$.
The result $F_\tau$ is satisfiable if and only if $\neg \tau$ is satisfiable.
With this translation $f$ is a proof system.

1. *Polynomial time.*
   Computing $F_\tau$ and checking each resolution step take time polynomial in $\lvert w \rvert$.
2. *Soundness.*
   If $\pi$ refutes $F_\tau$, then $F_\tau$ is unsatisfiable, so $\neg \tau$ is unsatisfiable and $\tau$ is a tautology.
3. *Completeness.*
   If $\tau$ is a tautology, then $F_\tau$ is unsatisfiable, and resolution refutes every unsatisfiable CNF.

## Remarks

The measure of $w$ is its size in symbols, which counts $\tau$ and the clauses of the refutation.
Here the refutation has $5$ clauses with $1 + 2 + 1 + 1 + 0 = 5$ literals in all, so the proof is tiny.

The translation is part of the system.
Two translations of $\neg \tau$ into a CNF can give two proof systems with different proof sizes, although each is sound and complete.
For CNFs given directly, such as the [[pigeonhole formulas|RJ571F7FF0]], we use resolution as a refutation system and skip the translation.
Watch out: if you drop the requirement that the translation run in polynomial time, the checker is no longer fast, and the scheme fails condition 1 of the definition.

## Explanations

### L1 human

Resolution works with lists of "or" clauses and derives new clauses until it reaches the empty clause, which is a contradiction.
To show that $\tau$ is always true, we refute the clauses that say "$\tau$ is false".
Here "if $p$, and $p$ implies $q$, then $q$" is proved by refuting "$p$", "not $p$ or $q$" and "not $q$".
Two steps do it: the first two give "$q$", and "$q$" with "not $q$" gives the contradiction.

### L2 human

We count the work of the checker on $w$.

1. Translate $\neg \tau$ into its $3$ clauses.
2. Check $C_4 = \{q\}$: the pivot $p$ is in $C_1$, $\neg p$ is in $C_2$, and the rest of $C_1 \cup C_2$ is $\{q\}$.
3. Check $C_5 = \square$: the pivot $q$ is in $C_4$, $\neg q$ is in $C_3$, and nothing else remains.
4. Output $\tau$.

Each step takes time polynomial in $\lvert w \rvert$, so the check is fast.
This is the typical way to turn a refutation system into a proof system for tautologies.
