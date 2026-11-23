---
tag: VWJVAS3VE3
kind: statement
role: theorem
name: Every structural logic is determined by its Lindenbaum matrices
aliases: [wojcicki-theorem-matrix-semantics]
msc: ["03B22", "03G27", "03B50"]
topics: [WZP584JQ06]
audience: grad
about: [P7E926JK13, FCXHSC6Z4R]
uses: [AJEJS6TFWP, J78Y1M4GND]
proofs: [6R0QSZ41EE]
history:
  first_stated: "Wójcicki, 1970"
  notes: "Wójcicki's book Theory of Logical Calculi (1988) presents the result. Structural consequence relations were introduced by Łoś and Suszko in 1958."
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 3.4 Many-valuedness and rule-based approaches
  - url: https://en.wikipedia.org/wiki/Consequence_relation
    locator: lead section
---

## Statement

Every structural logic has a truth-table semantics, with formulas as truth values and theories as the sets of true formulas.

Let $\vdash$ be a structural [[consequence relation|J78Y1M4GND]] on the formula algebra $\mathrm{Fm}$.
So $\vdash$ satisfies reflexivity, monotonicity and cut, and $\Gamma \vdash \varphi$ implies $\sigma[\Gamma] \vdash \sigma(\varphi)$ for every substitution $\sigma$.
Let $\mathcal{K}$ be the class of its [[Lindenbaum matrices|AJEJS6TFWP]] $\langle \mathrm{Fm}, T \rangle$, where $T$ ranges over the closed sets of $\vdash$.

**Theorem.**

1. For all $\Gamma$ and $\varphi$, we have $\Gamma \vdash \varphi$ iff $\Gamma \models_{\mathcal{K}} \varphi$.
2. The theorems of $\vdash$ are exactly the tautologies of the single matrix $\langle \mathrm{Fm}, \mathrm{Cn}(\emptyset) \rangle$.
3. A consequence relation on $\mathrm{Fm}$ is the consequence relation of some class of [[logical matrices|P7E926JK13]] iff it is structural.

The proof is in [[the proof by the identity valuation|6R0QSZ41EE]].

## Remarks

### Why each hypothesis is needed

Structurality is the one hypothesis that a matrix semantics adds to a consequence relation.
Fix a variable $p$ and put $\Gamma \vdash \varphi$ iff $\varphi \in \Gamma \cup \{p\}$.
This relation is reflexive, monotone and closed under cut, and it has $\emptyset \vdash p$ but $\emptyset \nvdash q$.
Every matrix consequence is structural, so the substitution $p \mapsto q$ shows that no class of matrices gives $\vdash$.

Cut and monotonicity are needed because every $\models_{\mathcal{K}}$ has them.
A non-monotone relation, such as the consequence of a default logic, has no matrix semantics.
A relation without cut, such as "follows in at most one rule step", has none either, and in the proof cut is what makes $\mathrm{Cn}(\Gamma)$ closed.

### What it gives you

Every structural logic, classical or not, has a many-valued semantics in the broad sense.
So "many-valued" is a property of a semantics, not of a logic, which is the point that [[Suszko's reduction|2FQB3NQF8A]] makes from the other side.
A Hilbert system whose axioms and rules are schemes is structural, so its consequence relation has a matrix semantics.
Item 2 is the propositional form of the Lindenbaum-Tarski method, and its quotient by provable equivalence is the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] when the logic is classical.

### The converse

Item 3 is an equivalence.
Every class of matrices gives a structural consequence relation, by the remarks of [[the definition|AJEJS6TFWP]].

### Generalizations

The same method works for multiple-conclusion consequence relations, with pairs of a theory and a co-theory in place of closed sets.
Further conditions on a logic decide when one matrix suffices, and when a finite matrix suffices.

## History

Łoś and Suszko introduced structural consequence relations in 1958 and studied their matrix semantics.
Wójcicki proved in 1970 that every structural consequence relation is determined by a class of matrices, the Lindenbaum matrices of the statement.
His book "Theory of Logical Calculi" of 1988 presents the theorem and its refinements.

## Explanations

### L1 human

Many logics are given by rules of proof, not by truth tables.
The theorem says that each such logic, if its rules do not single out particular letters, also has truth tables.
The "truth values" are the formulas themselves, and "true" means "provable from the assumptions".
So truth tables exist for every reasonable logic, though they are usually infinite.

### L2 human

Take intuitionistic logic, which has no finite truth tables, as Gödel showed.
Its Lindenbaum matrix $\langle \mathrm{Fm}, \mathrm{Cn}(\emptyset) \rangle$ has the formulas as values and the intuitionistic theorems as designated values.
A formula is a tautology of this matrix iff each of its substitution instances is a theorem.
By structurality that happens iff the formula itself is a theorem, so the matrix gives exactly the intuitionistic theorems.
This is the typical use: the theorem gives some matrix semantics first, and the search for a small one comes after.
Watch out: the theorem gives infinite matrices, and it does not say that a logic has a finite matrix.

### L3 human

The theorem is the starting point of abstract algebraic logic.
You replace each Lindenbaum matrix by its quotient by the Leibniz congruence and ask when these quotients form a natural class of algebras.
For finitary algebraizable logics this class is a quasivariety, as Boolean algebras are for classical logic and [[MV-algebras|8T4M7RN9AC]] are for Łukasiewicz logic; see [[algebraic logic|QYA4H5Y7VR]].
The same idea, with theories as truth values, gives the canonical models of modal logic and the term models of first-order logic.
