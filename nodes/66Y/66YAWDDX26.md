---
tag: 66YAWDDX26
kind: example
name: Gentle explosion in C1
msc: ["03B53"]
topics: [NJB94B39QK]
audience: grad
instance_of: [KN2VBRQB3Q]
uses: [N0PH09DCDE, TTKZGJEEK7, 0Y0MQYST0M]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 3.5
  - book: isbn:9783319332031
---

## Example

We show $A^\circ, A, \neg A \vdash_{C_1} C$ for all formulas $A$ and $C$, with the axioms of [[$C_1$|N0PH09DCDE]].

1. $A^\circ$. Premise.
2. $A$. Premise.
3. $\neg A$. Premise.
4. $A \to (\neg C \to A)$. Axiom 1.
5. $\neg C \to A$. [[Modus ponens|0Y0MQYST0M]] on 2 and 4.
6. $\neg A \to (\neg C \to \neg A)$. Axiom 1.
7. $\neg C \to \neg A$. Modus ponens on 3 and 6.
8. $A^\circ \to ((\neg C \to A) \to ((\neg C \to \neg A) \to \neg\neg C))$. Axiom 10, with $\neg C$ in the role of $A$ and $A$ in the role of $B$.
9. $(\neg C \to A) \to ((\neg C \to \neg A) \to \neg\neg C)$. Modus ponens on 1 and 8.
10. $(\neg C \to \neg A) \to \neg\neg C$. Modus ponens on 5 and 9.
11. $\neg\neg C$. Modus ponens on 7 and 10.
12. $\neg\neg C \to C$. Axiom 9.
13. $C$. Modus ponens on 11 and 12.

So a contradiction about a well-behaved formula is [[explosive|TTKZGJEEK7]] in $C_1$.
With $A^\circ$ as the consistency connective $\circ A$, this is the defining property of a logic of formal inconsistency.

## Remarks

The derivation uses only axioms 1, 9 and 10.
It works in every $C_n$ with $A^{(n)}$ in place of $A^\circ$.
Without the premise $A^\circ$, the [[three-valued model|Z54C2SK5E3]] shows that no derivation exists.

## Explanations

### L1 human

In $C_1$, a contradiction alone proves nothing new.
But if we also know that the statement is well-behaved, the contradiction proves everything, as in classical logic.
So $C_1$ behaves classically for well-behaved statements.

### L2 human

The derivation is a reductio on $\neg C$.
Assume $\neg C$ for a moment; it implies $A$ and $\neg A$, by axiom 1.
Restricted reductio, axiom 10, then refutes $\neg C$, because $A$ is well-behaved.
Double negation elimination gives $C$.
A trap is to apply axiom 10 with $C$ in the role of $B$; the well-behaved formula must be the one that is contradicted.
