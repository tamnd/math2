---
tag: 12N6JEYVHX
kind: proof
name: Proof of the upper bounds for MLL and MALL provability
msc: ["03F52", "03B25", "68Q17"]
topics: [98QF5J4W16]
audience: research
proves: BNRWJB2R8C
uses: [SYMW99C0EV, 14Z5D0JX98, H408H4WHBA, SBDQH0TJ5X, XNRQHTG7QM]
methods: [X5HG1RNWQX, 0ASJVEFA9J, 0NTF6DMVAP]
sources:
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 4. Complexity
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - doi: 10.1016/0168-0072(92)90075-B
    locator: pages 239-311
    note: Lincoln, Mitchell, Scedrov and Shankar, Decision problems for propositional linear logic, Annals of Pure and Applied Logic 56 (1992)
  - doi: 10.1109/LICS.1992.185533
    locator: pages 200-210
    note: Kanovich, Horn programming in linear logic is NP-complete, LICS 1992
---

## Proof

This node proves that MLL provability is in NP and that MALL provability is in PSPACE.
It does not prove the hardness results or the undecidability of full linear logic; these are cited in the [[statement|BNRWJB2R8C]] from Kanovich (1992) and from Lincoln, Mitchell, Scedrov and Shankar (1992).
Let $n$ be the size of the input sequent $S$, that is, its number of occurrences of atoms, negated atoms, units and connectives.

**Part 1: MLL is in NP.**

1. By [[cut elimination for MLL|SYMW99C0EV]], $S$ is derivable if and only if it has a cut-free derivation.
2. By the same theorem, a cut-free derivation of $S$ has at most $n$ rule applications other than axioms and at most $n + 1$ axioms.
3. In a cut-free MLL derivation, the premises of each rule have total size at most that of the conclusion.
   So each of its at most $2n + 1$ sequents has size at most $n$.
4. So a cut-free derivation, written as a list of sequents with pointers to premises, has size polynomial in $n$.
5. A checker verifies in polynomial time that each listed sequent is an axiom or follows from its premises by one rule, and that the last one is $S$.
6. A nondeterministic machine guesses such a list and runs the checker.
   So MLL provability is in NP.

**Part 2: MALL is in PSPACE.**

1. By the [[phase semantics theorem|14Z5D0JX98]], part 3, $S$ is derivable in MALL if and only if it has a cut-free derivation.
2. In each rule of MALL other than cut, each premise has a smaller size than the conclusion.
   For $\otimes$ and $\mathbin{\wp}$ the premises lose one connective; for $\mathbin{\&}$ and $\oplus$ each premise loses one connective and one subformula; for $\bot$ the premise loses the constant.
3. So each branch of a cut-free derivation of $S$ has at most $n$ rule applications.
4. Define a recursive procedure $\mathrm{Prove}(\Gamma)$.
   It returns "true" if $\Gamma$ is an axiom: $\vdash A^{\perp}, A$, $\vdash 1$, or a sequent with $\top$.
5. Otherwise it tries, one at a time, each formula of $\Gamma$ and each way to read $\Gamma$ as the conclusion of a rule with that formula as principal.
   For $\otimes$ this includes each split of the rest of $\Gamma$ into two parts.
6. For each try it calls $\mathrm{Prove}$ on the premises, and it returns "true" if all premises of some try return "true".
7. By induction on the size of $\Gamma$, $\mathrm{Prove}(\Gamma)$ returns "true" if and only if $\Gamma$ has a cut-free derivation.
   The base is the axioms, and the step is step 6.
8. The recursion depth is at most $n$, by step 3.
9. Each level stores one sequent of size at most $n$ and the index of the current try, which needs $O(n)$ bits, since there are at most $2n \cdot 2^n$ tries.
10. So the procedure uses $O(n^2)$ space, and MALL provability is in PSPACE.

## Idea

Cut elimination bounds the search to the subformulas of the input.
Without contraction, every backward step makes the sequent smaller.
For MLL, the whole derivation is small and can be guessed; for MALL, only one branch is small, so depth-first search uses little space.

## Variants

The proof of Part 2 also works for MLL, which gives a weaker bound.
The hardness results need codings of NP-complete and PSPACE-complete problems into MLL and MALL, which are in the cited papers.
