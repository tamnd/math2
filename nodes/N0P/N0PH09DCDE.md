---
tag: N0PH09DCDE
kind: definition
name: Da Costa's systems C_n
msc: ["03B53"]
topics: [NJB94B39QK]
audience: grad
defines: KN2VBRQB3Q
uses: [ET1HPME8VV, 0Y0MQYST0M, 029JBBF693, Q11N8X99FK]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 3.5
  - book: isbn:9783319332031
---

## Definition

The formulas are built from atoms with $\neg$, $\land$, $\lor$ and $\to$.
For a formula $A$, put
$$A^\circ := \neg(A \land \neg A), \quad A^1 := A^\circ, \quad A^{k+1} := (A^k)^\circ, \quad A^{(n)} := A^1 \land A^2 \land \cdots \land A^n.$$

For $1 \leq n < \omega$, the system $C_n$ is the [[Hilbert system|ET1HPME8VV]] with [[modus ponens|0Y0MQYST0M]] as its only rule and the following axiom schemes.

Positive part:

1. $A \to (B \to A)$
2. $(A \to B) \to ((A \to (B \to C)) \to (A \to C))$
3. $A \land B \to A$ and $A \land B \to B$
4. $A \to (B \to A \land B)$
5. $A \to A \lor B$ and $B \to A \lor B$
6. $(A \to C) \to ((B \to C) \to (A \lor B \to C))$
7. $A \lor (A \to B)$

[[Negation|029JBBF693]] part:

8. $A \lor \neg A$
9. $\neg\neg A \to A$
10. $B^{(n)} \to ((A \to B) \to ((A \to \neg B) \to \neg A))$
11. $A^{(n)} \land B^{(n)} \to (A \land B)^{(n)} \land (A \lor B)^{(n)} \land (A \to B)^{(n)}$

The system $C_\omega$ has axioms 1 to 6, 8 and 9, with modus ponens; it has no axiom 7, 10 or 11.
We write $\Gamma \vdash_{C_n} A$ when $A$ has a derivation from $\Gamma$ in $C_n$.
The formula $A^{(n)}$ is the *well-behavedness* formula of $C_n$.

## Notation

Many authors write $A^{\circ}$ or $\circ A$ for $A^{(1)}$, and read it "$A$ is consistent" or "$A$ is well-behaved".
Axioms 1 to 7 axiomatize positive classical logic; axioms 1 to 6 axiomatize positive [[intuitionistic logic|Q11N8X99FK]].

## Remarks

Axiom 10 is classical reductio restricted to well-behaved $B$.
Without the restriction, axioms 1 to 10 give classical propositional logic.
The SEP entry presents $C_1$ with a primitive $\circ$ and the axioms $\circ A \to (A \to (\neg A \to B))$, $(\circ A \land \circ B) \to \circ(A \land B)$ and $(\circ A \to \circ B) \to \circ(A \to B)$, over positive classical logic with double negation elimination.
The definition above follows da Costa's original form, in which $\circ A$ is the formula $\neg(A \land \neg A)$.

## Explanations

### L1 human

$C_n$ is classical logic for "and", "or" and "if", with a weaker "not".
The only classical law of "not" that is restricted is the reductio rule.
It applies to a formula $B$ only when we know that $B$ is well-behaved.

### L2 human

For $n = 1$, axiom 10 reads $\neg(B \land \neg B) \to ((A \to B) \to ((A \to \neg B) \to \neg A))$.
To use reductio on $A$ with the contradiction $B$, $\neg B$, we must first prove $\neg(B \land \neg B)$.
A trap is to think that $A^{(n)}$ grows weaker with $n$; it grows stronger, so the logics $C_n$ grow weaker.

### L3 human

The well-behavedness formulas $A^{(n)}$ are defined, not primitive, which makes $C_n$ a logic of formal inconsistency in which consistency is expressed by negation and conjunction.
The family is a descending chain $C_1 \supsetneq C_2 \supsetneq \cdots \supsetneq C_\omega$ of theorems, all below classical logic.
Da Costa and Alves gave a semantics of valuations for these systems: maps $v$ into $\set{0, 1}$ with $v(\neg A) = 1$ whenever $v(A) = 0$, but with $v(A) = v(\neg A) = 1$ allowed.
Such a valuation is not truth-functional for $\neg$, and this is the source of paraconsistency.
