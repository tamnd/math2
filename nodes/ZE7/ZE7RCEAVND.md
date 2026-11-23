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

Start from the single [[clause|T3SXVH3ZZC]] $\{p\}$.
It implies the clause $\{p, q\}$, since every assignment that makes $p$ true makes "$p$ or $q$" true.
But the [[resolution|ZDW6N1PGJ7]] rule cannot get there.

The rule, written as a schema with formula variables $A$, $B$ and a variable $p$, is
$$\frac{A \lor p \qquad B \lor \neg p}{A \lor B}.$$
It is a sound rule, but the system with this rule alone fails the conditions of a [[Frege system|J2BAR09TPF]], for three reasons.

1. *It proves nothing from nothing.*
   The system has no axioms, so a derivation from no hypotheses has no first line.
   So it proves no tautology at all, not even $p \lor \neg p$.
2. *It is not implicationally complete, even on clauses.*
   From the single hypothesis $\{p\}$, no two lines contain a complementary pair, so every line is a copy of $\{p\}$.
   So $\{p, q\}$ is not derivable, although $\{p\} \models \{p, q\}$.
3. *Its lines are clauses.*
   Resolution works with disjunctions of literals, not with arbitrary formulas over a functionally complete basis.

What resolution has instead is *refutation completeness*: from every unsatisfiable set of clauses it derives the empty clause.

## Remarks

The example separates two kinds of completeness.
A Frege system derives every consequence of its hypotheses, while resolution derives only the contradiction $\square$, and only from unsatisfiable inputs.
That is enough to make [[resolution as a refutation system|6JSH907W5R]] a propositional proof system in the sense of Cook and Reckhow, through a CNF of the negated tautology.

The two kinds of system also differ in strength.
Frege systems p-simulate resolution, since each resolution step is a fixed derived rule of any Frege system.
The converse fails: the [[pigeonhole formulas|RJ571F7FF0]] have polynomial-size Frege proofs and need exponential-size resolution refutations.

What if we add the weakening rule "from $A$ infer $A \lor B$"?
Then $\{p, q\}$ follows from $\{p\}$ in one step, and the system becomes implicationally complete for clauses.
It is still not a Frege system, because it has no axioms and its lines are still clauses.

## Explanations

### L1 human

Resolution can only show that a list of clauses is contradictory.
It cannot prove a formula directly, and it cannot weaken a clause.
For example, from "$p$" it cannot conclude "$p$ or $q$", although this conclusion follows.

### L2 human

We test the three clauses $\{p\}$, $\{\neg p, q\}$, $\{\neg q\}$ against both kinds of completeness.
They are unsatisfiable, and resolution refutes them: $\{p\}$ and $\{\neg p, q\}$ give $\{q\}$, and $\{q\}$ with $\{\neg q\}$ gives $\square$.
So refutation completeness works here.
Now drop $\{\neg q\}$ and ask for the consequence $\{q, r\}$ of the other two.
Resolution derives $\{q\}$ and then stops, because no pair of lines clashes.
Watch out: "resolution is complete" means refutation complete, and not implicationally complete.
