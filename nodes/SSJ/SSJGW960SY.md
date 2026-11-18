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

Let $\tau = (p \land (\neg p \lor q)) \to q$, written with $\neg$, $\land$, $\lor$ as $\neg(p \land (\neg p \lor q)) \lor q$.

1. *The CNF of $\neg \tau$.* By De Morgan's laws, $\neg \tau$ is $p \land (\neg p \lor q) \land \neg q$, a CNF with the clauses $C_1 = \set{p}$, $C_2 = \set{\neg p, q}$ and $C_3 = \set{\neg q}$.
2. *The refutation.* Resolve $C_1$ and $C_2$ on $p$ to get $C_4 = \set{q}$. Resolve $C_4$ and $C_3$ on $q$ to get the empty clause $C_5 = \emptyset$.
3. *The proof.* The [[resolution|6JSH907W5R]] proof of $\tau$ is the string $w = \tau \# C_1, C_2, C_3, C_4, C_5$.
4. *The check.* The checker $f$ computes the CNF of $\neg \tau$, tests that $C_1, C_2, C_3$ are its clauses, that $C_4$ and $C_5$ are resolvents of earlier clauses, and that $C_5$ is empty. All tests pass, so $f(w) = \tau$.

For a general $\tau$, a CNF of $\neg \tau$ by distribution can be exponentially long.
So $f$ fixes one translation: if pushing the negations inward gives a CNF, as here, $f$ uses it; otherwise $f$ uses the [[Tseitin transformation|S367PDDP61]].
The Tseitin transformation adds a new variable for each subformula of $\neg \tau$, and it writes $O(\abs{\tau})$ clauses of width at most $3$.
The result $F_\tau$ is satisfiable if and only if $\neg \tau$ is satisfiable, and $f$ computes it in polynomial time.
With this choice $f$ is a [[propositional proof system|3V24CYWDT6]]: soundness and completeness of resolution for CNFs give soundness and completeness of $f$.

## Remarks

The measure of $w$ is its length in symbols.
Here $\tau$ has $13$ symbols and the refutation has $5$ clauses with $5$ literals in all, so $s_f(\tau)$ is small.
Different translations of $\neg \tau$ into a CNF can give different proof systems, so the translation is part of the system.
For CNFs given directly, such as the pigeonhole formulas, one uses resolution as a refutation system and skips the translation.

## Explanations

### L1 human

Resolution refutes a list of clauses: it derives new clauses until it reaches the empty clause, which is a contradiction.
To prove that $\tau$ is always true, one refutes the clauses that say "$\tau$ is false".
For example, "if $p$, and $p$ implies $q$, then $q$" is proved by refuting the three clauses "$p$", "not $p$ or $q$" and "not $q$".

### L2 human

We count the steps of the check.

1. Translate $\neg \tau$ into $3$ clauses.
2. Check $C_4$: it contains $q$, which is in $C_2$, and nothing else, and the pivot $p$ occurs in $C_1$ and negated in $C_2$.
3. Check $C_5$: it is empty, and the pivot $q$ occurs in $C_4$ and negated in $C_3$.
4. Output $\tau$.

Each step takes time polynomial in the length of $w$.
A trap: the proof system includes the choice of translation, and the size of a proof counts the clauses of the refutation together with $\tau$.
