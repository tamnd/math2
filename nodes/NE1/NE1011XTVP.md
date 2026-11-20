---
tag: NE1011XTVP
kind: example
name: C1 with all well-behavedness axioms is classical logic
msc: ["03B53", "03B05"]
topics: [NJB94B39QK]
audience: grad
not_instance_of:
  - target: KN2VBRQB3Q
    note: once every formula is well-behaved, the system proves explosion and is not a logic of formal inconsistency
  - target: C7YWCR87QJ
    note: the extended system is classical propositional logic, which is explosive
uses: [N0PH09DCDE, 66YAWDDX26, 09K9MWD2QQ, ET1HPME8VV]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 3.5
  - book: isbn:9783319332031
---

## Example

Let $C_1^{+}$ be [[$C_1$|N0PH09DCDE]] with the extra axiom scheme $A^\circ$, that is $\neg(A \land \neg A)$, for every formula $A$.

1. From $B^\circ$ and axiom 10 by modus ponens, $C_1^{+}$ proves $(A \to B) \to ((A \to \neg B) \to \neg A)$ for all $A$ and $B$.
2. With axioms 1 to 6 and axiom 9, this is Kleene's axiomatization of classical [[propositional logic|09K9MWD2QQ]], which is complete.
3. Every axiom of $C_1^{+}$ is a classical tautology, and modus ponens preserves truth, so $C_1^{+}$ proves only classical tautologies.
4. So $C_1^{+}$ has exactly the classical theorems.

By [[gentle explosion|66YAWDDX26]], $A^\circ, A, \neg A \vdash C$, and $A^\circ$ is now an axiom.
So $A, \neg A \vdash_{C_1^{+}} C$ for all $A$ and $C$, and the logic is explosive.

## Remarks

The example shows why $\neg(A \land \neg A)$ cannot be a theorem of a paraconsistent C-system.
It also shows that $C_1$ is classical logic "minus" the assumption that every formula is well-behaved.
The same argument works for every $C_n$ with the axiom $A^{(n)}$.

## Explanations

### L1 human

In $C_1$, a statement must be marked well-behaved before classical reasoning about its negation applies.
If we declare every statement well-behaved, the restriction disappears.
Then $C_1$ becomes ordinary classical logic, and a contradiction proves everything again.

### L2 human

The test of a non-example is whether some contradiction stays local.
In $C_1^{+}$, the premises $p$ and $\neg p$ prove $q$ by the derivation for gentle explosion, with the axiom $p^\circ$ as an extra line.
A trap is to think that adding a classical tautology to a paraconsistent logic keeps it paraconsistent; here one tautology scheme collapses it.
