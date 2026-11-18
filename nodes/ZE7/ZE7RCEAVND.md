---
tag: ZE7RCEAVND
kind: example
name: Resolution is not a Frege system
msc: ["03F20", "03B05"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: J2BAR09TPF
    note: resolution has no axioms, its lines are clauses, and it cannot derive the clause {p, q} from {p}, so it is not implicationally complete
uses: [ZDW6N1PGJ7, T3SXVH3ZZC, 6JSH907W5R]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in propositional logic
---

## Example

The [[resolution|ZDW6N1PGJ7]] rule can be written as a schematic rule with formula variables $A$, $B$ and $p$:
$$\frac{A \lor p \qquad B \lor \neg p}{A \lor B}.$$
This rule is sound.
But the system with this rule alone is not a [[Frege system|J2BAR09TPF]].

1. *No proofs from no hypotheses.* The system has no axioms, so a derivation from $\Gamma = \emptyset$ has no first line. So it proves no tautology at all, not even $p \lor \neg p$.
2. *Not implicationally complete, even on clauses.* We have $\set{p} \models \set{p, q}$. A derivation from the single [[clause|T3SXVH3ZZC]] $\set{p}$ has no pair of clauses with a complementary literal. So its only lines are copies of $\set{p}$, and $\set{p, q}$ is not derivable.
3. *Lines are clauses.* In proof complexity, resolution works on clauses, which are disjunctions of literals. They are not arbitrary formulas over a functionally complete basis.

What resolution has instead is *refutation completeness*: every unsatisfiable set of clauses derives the empty clause.

## Remarks

[[Resolution as a refutation system|6JSH907W5R]] is still a propositional proof system in the sense of Cook and Reckhow, through a CNF translation of the negated tautology.
Frege systems p-simulate resolution.
The converse fails: the [[pigeonhole formulas|RJ571F7FF0]] have polynomial-size Frege proofs and need exponential-size resolution refutations.

## Explanations

### L1 human

Resolution can only show that a list of clauses is contradictory.
It cannot prove a formula directly, and it cannot weaken a clause.
For example, from "$p$" it cannot conclude "$p$ or $q$", although this conclusion follows.

### L2 human

We check that adding one rule repairs step 2.

1. Add the weakening rule "from $A$ infer $A \lor B$".
2. From $\set{p}$, weakening gives $\set{p, q}$ in one step.
3. The repaired system is still not a Frege system, since its lines are clauses and it has no axioms.

The typical use of the example is to separate refutation systems from Frege systems.
A trap: "resolution is complete" means refutation complete, not implicationally complete.
