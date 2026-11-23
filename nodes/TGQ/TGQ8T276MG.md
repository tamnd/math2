---
tag: TGQ8T276MG
kind: definition
name: Monoidal t-norm based logic MTL
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
defines: PT5PHKJDYM
uses: [BHGCVPAJW0, D1R4D2HEPP, 0Y0MQYST0M, WH4SFAACAS, 0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/Monoidal_t-norm_logic
    locator: Language; Axioms; MTL-algebras; Standard semantics
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: "2. MTL: A fundamental fuzzy logic; 7. Algebraic semantics"
---

## Definition

The language of MTL has propositional variables, the binary connectives $\otimes$, $\land$ and $\to$, and the constant $\bot$.
The defined connectives are $\neg A := A \to \bot$ and $\top := \bot \to \bot$.
Weak disjunction is $A \lor B := ((A \to B) \to B) \land ((B \to A) \to A)$.

*MTL* is the Hilbert calculus with the single rule [[modus ponens|0Y0MQYST0M]] and the following ten axiom schemes.

1. (MTL1) $(A \to B) \to ((B \to C) \to (A \to C))$.
2. (MTL2) $A \otimes B \to A$.
3. (MTL3) $A \otimes B \to B \otimes A$.
4. (MTL4a) $A \land B \to A$.
5. (MTL4b) $A \land B \to B \land A$.
6. (MTL4c) $A \otimes (A \to B) \to A \land B$.
7. (MTL5a) $(A \to (B \to C)) \to (A \otimes B \to C)$.
8. (MTL5b) $(A \otimes B \to C) \to (A \to (B \to C))$.
9. (MTL6) $((A \to B) \to C) \to (((B \to A) \to C) \to C)$.
10. (MTL7) $\bot \to A$.

An *MTL-algebra* is a structure $\langle L, \land, \lor, \otimes, \Rightarrow, 0, 1 \rangle$ with four properties.
First, $\langle L, \land, \lor, 0, 1 \rangle$ is a bounded [[lattice|WH4SFAACAS]], with least element $0$ and greatest element $1$.
Second, $\langle L, \otimes, 1 \rangle$ is a commutative [[monoid|0N6R902FG1]].
Third, residuation holds: $z \otimes x \le y$ iff $z \le x \Rightarrow y$, for all $x, y, z \in L$.
Fourth, prelinearity holds: $(x \Rightarrow y) \lor (y \Rightarrow x) = 1$, for all $x, y \in L$.

It is an *MTL-chain* if its lattice order is total.
For a left-continuous [[t-norm|BHGCVPAJW0]] $*$, the *standard MTL-algebra* $[0, 1]_*$ has $\min$, $\max$, $*$, the residuum of $*$, $0$ and $1$.

An evaluation $e$ in $L$ sends each variable to an element of $L$, and it sends $\otimes$, $\land$, $\to$ and $\bot$ to $\otimes$, $\land$, $\Rightarrow$ and $0$.
We write $\Gamma \models_{\mathrm{MTL}} A$ when, for every left-continuous t-norm $*$ and every evaluation $e$ in $[0, 1]_*$ with $e(B) = 1$ for all $B \in \Gamma$, also $e(A) = 1$.

## Notation

SEP writes $\&$ for $\otimes$, and $\overline{0}$ and $\overline{1}$ for $\bot$ and $\top$.
The axiom labels follow the numbering of Hájek's axioms for BL, and MTL4a to MTL4c replace the divisibility axiom BL4.

## Remarks

The residuum in $[0, 1]_*$ exists because $*$ is left-continuous; see [[the left-continuity statement|D1R4D2HEPP]].
Residuation can be expressed by identities, so MTL-algebras form a variety.
The calculus is strongly complete for $\models_{\mathrm{MTL}}$, so $\Gamma \vdash A$ holds iff $\Gamma \models_{\mathrm{MTL}} A$.

The axioms are not independent.
MTL2 and MTL3 are derivable from the others, by results of Cintula in 2005 and Chvalovský in 2012.
SEP gives a variant list, with $(C \to A) \to ((C \to B) \to (C \to A \land B))$ in place of MTL4c.

The three MTL4 axioms make $\land$ the minimum in every standard algebra.
MTL4a and MTL4b say that $\land$ is below each argument and commutative, and MTL4c bounds the strong conjunction of $A$ and $A \to B$ by $\land$.
Adding the converse of MTL4c, in the form of divisibility, gives [[BL|FQZ04D0HH3]].

## Explanations

### L1 human

MTL is a list of ten axiom forms with the rule modus ponens.
It has two "and" connectives, a strong one from the t-norm and a weak one, the minimum.
Its theorems are the formulas that are fully true for every left-continuous t-norm.

### L2 human

To check an axiom in $[0, 1]_*$, read $\otimes$ as $*$, $\land$ as $\min$, and $\to$ as the residuum.
Use the rule that $x \Rightarrow y = 1$ iff $x \le y$.
For MTL4c, $x * (x \Rightarrow y) \le x$, and $x * (x \Rightarrow y) \le y$ by residuation, so it is at most $\min(x, y)$.
Watch out: MTL4c is only one direction of divisibility, and the other direction is what BL adds.

### L3 human

An MTL-algebra is a prelinear, commutative, bounded, integral [[residuated lattice|E337A6WVH3]].
Integral means that the monoid unit $1$ is the top element of the lattice.
