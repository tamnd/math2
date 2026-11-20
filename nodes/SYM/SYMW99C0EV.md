---
tag: SYMW99C0EV
kind: statement
role: theorem
name: Cut elimination for multiplicative linear logic
msc: ["03F05", "03F52"]
topics: [98QF5J4W16]
audience: research
uses: [H408H4WHBA, DAMGTSY6VV, Z2NXKDK06G]
about: [2P2184B6HE, HGVMPZ2DXA]
proofs: [3N689PA5JB]
sources:
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.1 Sequent calculus
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Sequent calculus presentation
  - doi: 10.1016/0304-3975(87)90045-4
    locator: pages 1-101
    note: Girard, Linear logic, Theoretical Computer Science 50 (1987)
---

## Statement

Let MLL be the one-sided sequent calculus of [[linear logic|H408H4WHBA]] restricted to the axiom, cut, $\otimes$, $\mathbin{\wp}$, $1$ and $\bot$ rules.
The *size* of a sequent is the number of occurrences of atoms, negated atoms, units and connectives in it.

1. Every sequent derivable in MLL has a derivation without the [[cut rule|DAMGTSY6VV]].
2. A cut-free derivation of a sequent of size $n$ has at most $n$ rule applications other than axioms, and at most $n + 1$ axioms.
3. Every formula in a cut-free derivation is a subformula of a formula of the end sequent, which is the [[subformula property|Z2NXKDK06G]].

## Remarks

### Why each hypothesis is needed

MLL has no contraction rule, so no case of the proof copies a cut.
With the exponential rule $?C$, a cut against a contraction makes two cuts, and the proof needs a different measure.
The bound of part 2 fails for full linear logic, since $?C$ keeps a formula in the premise and the premise can be as large as the conclusion.

### Consequences

Part 2 gives a certificate of polynomial size for each derivable MLL sequent, which is the first step of the proof that MLL [[provability is in NP|BNRWJB2R8C]].
Part 3 gives that MLL is a conservative extension of each of its fragments: a cut-free derivation of a sequent uses only connectives of that sequent.

### Generalizations

The SEP entry on linear logic states that the cut rule can be eliminated from the full sequent calculus of linear logic, and that completeness still holds.
On [[proof nets|HN6WN1VE39]], cut elimination for MLL uses two local rewrite steps, and the SEP entry states that it runs in linear time.

## History

Girard introduced linear logic and its sequent calculus in the 1987 paper cited in this node.

## Explanations

### L1 human

A cut is a lemma: we prove $A$, and then we use $A$.
The theorem says that every lemma can be removed from a proof of multiplicative linear logic.
The proof without lemmas uses only pieces of the final sequent, so it is easy to search for.

### L2 human

We remove one cut by hand.

1. Take $\vdash p, q, p^{\perp} \otimes q^{\perp}$, made by $\otimes$ from $\vdash p, p^{\perp}$ and $\vdash q, q^{\perp}$, and $\vdash p \mathbin{\wp} q, p^{\perp} \otimes q^{\perp}$, made from it by $\mathbin{\wp}$.
2. Cut this with $\vdash p^{\perp} \otimes q^{\perp}, p \mathbin{\wp} q$, made in the same way, on the formula $p \mathbin{\wp} q$ and its dual $p^{\perp} \otimes q^{\perp}$.
3. The key case of the proof replaces the cut by a cut on $p$ and a cut on $q$.
4. Each of these cuts has an axiom as a premise, so it disappears, and the result is the cut-free derivation of $\vdash p^{\perp} \otimes q^{\perp}, p \mathbin{\wp} q$.

The typical use of the theorem is to show that a sequent is not derivable, by a search for cut-free derivations only.
A trap: the theorem removes cuts but not axioms on compound formulas, so $\vdash A^{\perp}, A$ with compound $A$ can stay in a cut-free derivation.
