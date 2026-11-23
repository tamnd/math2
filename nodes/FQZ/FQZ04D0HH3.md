---
tag: FQZ04D0HH3
kind: definition
name: Basic fuzzy logic BL
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
defines: 3AQ5GHTXA4
uses: [BHGCVPAJW0, TGQ8T276MG, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/BL_(logic)
    locator: Language; Axioms; Semantics
  - url: https://en.wikipedia.org/wiki/Monoidal_t-norm_logic
    locator: Axioms; MTL-algebras
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 5. Other notable fuzzy logics
  - book: isbn:9780792352389
---

## Definition

The language of BL has propositional variables, the binary connectives $\otimes$ (strong conjunction) and $\to$ (implication), and the constant $\bot$.
*Basic fuzzy logic* BL is the Hilbert calculus with the single rule [[modus ponens|0Y0MQYST0M]] and the following eight axiom schemes.

1. (BL1) $(A \to B) \to ((B \to C) \to (A \to C))$.
2. (BL2) $A \otimes B \to A$.
3. (BL3) $A \otimes B \to B \otimes A$.
4. (BL4, divisibility) $A \otimes (A \to B) \to B \otimes (B \to A)$.
5. (BL5a) $(A \to (B \to C)) \to (A \otimes B \to C)$.
6. (BL5b) $(A \otimes B \to C) \to (A \to (B \to C))$.
7. (BL6, prelinearity) $((A \to B) \to C) \to (((B \to A) \to C) \to C)$.
8. (BL7) $\bot \to A$.

The defined connectives are $A \land B := A \otimes (A \to B)$, $\neg A := A \to \bot$ and $\top := \bot \to \bot$.
Weak disjunction is $A \lor B := ((A \to B) \to B) \land ((B \to A) \to A)$.

A *BL-algebra* is an [[MTL-algebra|TGQ8T276MG]] $\langle L, \land, \lor, \otimes, \Rightarrow, 0, 1 \rangle$ that satisfies divisibility, $x \land y = x \otimes (x \Rightarrow y)$ for all $x, y \in L$.
An evaluation $e$ in $L$ sends each variable to an element of $L$, and it sends $\otimes$, $\to$ and $\bot$ to $\otimes$, $\Rightarrow$ and $0$.
A formula $A$ is *valid* in $L$ if $e(A) = 1$ for every evaluation $e$.

The *standard BL-algebra* of a continuous [[t-norm|BHGCVPAJW0]] $*$ is $[0, 1]$ with $\min$, $\max$, $*$, its residuum, $0$ and $1$.

## Notation

Wikipedia writes $\otimes$ for strong conjunction and SEP writes $\&$, and in the Łukasiewicz case this sub-area writes $\odot$.
The constant $\bot$ is also written $0$ or $\overline{0}$.
The numbering BL1 to BL7, with BL5 split into two, follows Hájek.

## Remarks

Each axiom has a reading in a standard algebra.
BL1 is the transitivity of implication, BL2 says that $x * y \le x$, and BL3 is commutativity.
BL5a and BL5b together express residuation, so $\to$ is the residuum of $\otimes$.
BL7 says that $0$ is the least truth value.

Divisibility BL4 is what separates BL from MTL, which replaces it by three axioms on a primitive weak conjunction.
With weak conjunction defined, BL4 says $A \land B \to B \land A$.
In each standard BL-algebra, divisibility holds because the t-norm is continuous; see [[the divisibility example|E1M4RTRAVS]].
Prelinearity holds in the standard algebra of every left-continuous t-norm; see [[the prelinearity statement|D0ZADJFPQE]].

The axioms are not independent.
BL2 and BL3 are derivable from the others, by results of Cintula in 2005 and Chvalovský in 2012.
BL is sound and complete for all BL-algebras, for all linearly ordered BL-algebras, and for the standard BL-algebras.
The last of these, standard completeness, is due to Cignoli, Esteva, Godo and Torrens in 2000.

## Explanations

### L1 human

BL is a list of eight axiom forms and one rule, modus ponens.
The axioms describe how a fuzzy "and" and a fuzzy "if then" work together.
Each formula that BL proves is fully true for every continuous t-norm.

### L2 human

To check an axiom, read $\otimes$ as a continuous t-norm $*$ and $\to$ as its residuum, and show that it gets value $1$ for all inputs.
For BL2, $x * y \le x * 1 = x$ by monotonicity, so the residuum gives $(x * y) \Rightarrow x = 1$.
For BL4 at $x = 0.7$ and $y = 0.4$ with Łukasiewicz, both sides equal $\min(0.7, 0.4) = 0.4$, so the implication has value $1$.
Watch out: $\land$ is not a primitive connective of BL, so its meaning $\min$ comes from divisibility, not from a separate rule.

### L3 human

The residuation law, expressed by BL5a and BL5b, makes $\to$ the right adjoint of $\otimes$.
Prelinearity BL6 is the axiom behind the completeness of BL for linearly ordered algebras.
Divisibility BL4 says that $x \land y$ is a multiple $x \otimes z$ of $x$, with the witness $z = x \Rightarrow y$.
