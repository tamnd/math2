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
*Basic fuzzy logic* BL is the Hilbert calculus with the single rule [[modus ponens|0Y0MQYST0M]] and these axiom schemes:

1. (BL1) $(A \to B) \to ((B \to C) \to (A \to C))$;
2. (BL2) $A \otimes B \to A$;
3. (BL3) $A \otimes B \to B \otimes A$;
4. (BL4, divisibility) $A \otimes (A \to B) \to B \otimes (B \to A)$;
5. (BL5a) $(A \to (B \to C)) \to (A \otimes B \to C)$;
6. (BL5b) $(A \otimes B \to C) \to (A \to (B \to C))$;
7. (BL6, prelinearity) $((A \to B) \to C) \to (((B \to A) \to C) \to C)$;
8. (BL7) $\bot \to A$.

The defined connectives are $A \land B := A \otimes (A \to B)$, $\neg A := A \to \bot$, $\top := \bot \to \bot$ and $A \lor B := ((A \to B) \to B) \land ((B \to A) \to A)$.

A *BL-algebra* is an [[MTL-algebra|TGQ8T276MG]] $\langle L, \land, \lor, \otimes, \Rightarrow, 0, 1 \rangle$ that satisfies divisibility: $x \land y = x \otimes (x \Rightarrow y)$ for all $x, y \in L$.
An evaluation $e$ in $L$ sends $\otimes$, $\to$ and $\bot$ to $\otimes$, $\Rightarrow$ and $0$.
A formula $A$ is *valid* in $L$ if $e(A) = 1$ for every evaluation $e$.

The *standard BL-algebra* of a continuous [[t-norm|BHGCVPAJW0]] $*$ is $[0, 1]$ with $\min$, $\max$, $*$, its residuum, $0$ and $1$.

## Notation

Wikipedia writes $\otimes$ for strong conjunction and SEP writes $\&$; in the Łukasiewicz case this sub-area writes $\odot$.
The constant $\bot$ is also written $0$ or $\overline{0}$.

## Remarks

1. The axioms BL2 and BL3 are derivable from the others, by results of Cintula (2005) and Chvalovský (2012).
2. Divisibility BL4 is what separates BL from MTL: MTL replaces it by three axioms on a primitive weak conjunction.
3. With weak conjunction defined, BL4 says $A \land B \to B \land A$.
4. Wikipedia states that BL is sound and complete for all BL-algebras, for all linearly ordered BL-algebras, and for the standard BL-algebras.
5. In each standard BL-algebra, the divisibility identity holds because the t-norm is continuous; see [[the divisibility example|E1M4RTRAVS]].
6. Prelinearity holds in every standard algebra of a left-continuous t-norm; see [[the prelinearity statement|D0ZADJFPQE]].

## Explanations

### L1 human

BL is a list of eight axiom forms and one rule, modus ponens.
The axioms describe how a fuzzy "and" and a fuzzy "if then" work together.
Each formula that BL proves is fully true for every continuous t-norm.

### L2 human

To use the definition, read $\otimes$ as a continuous t-norm $*$ and $\to$ as its residuum.
Then check that an axiom gets the value $1$ for all inputs.
For BL2: $x * y \le x$, so the residuum gives $(x * y) \Rightarrow x = 1$.
A trap: $\land$ is not a primitive connective of BL, so its meaning $\min$ comes from divisibility, not from a separate rule.

### L3 human

The residuation law, expressed by BL5a and BL5b, makes $\to$ the right adjoint of $\otimes$.
Prelinearity BL6 is the axiom behind the completeness of BL for linearly ordered algebras.
Divisibility BL4 says that $x \land y$ is a multiple $x \otimes z$ of $x$, with the witness $z = x \Rightarrow y$.
