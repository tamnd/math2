---
tag: ZMVBAY7ZZD
kind: concept
name: Implicational propositional calculus
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
uses: [0NMG7W7Q11, 1MGMQX43B8, 0Y0MQYST0M, 05006AJ7DZ, GMSZ75D5WE]
sources:
  - url: https://en.wikipedia.org/wiki/Implicational_propositional_calculus
    locator: Axiom system
  - url: https://en.wikipedia.org/wiki/Implicational_propositional_calculus
    locator: Completeness
  - url: https://en.wikipedia.org/wiki/Implicational_propositional_calculus
    locator: Functional (in)completeness
same_as:
  wikidata: Q6007243
  wikipedia: Implicational propositional calculus
inventory: [PA6PVB6JNW]
---

## Summary

The *implicational propositional calculus* is the fragment of classical propositional logic whose formulas are built from propositional variables with the connective [[implication|0NMG7W7Q11]] $\to$ only.
As a [[Hilbert system|1MGMQX43B8]] it has three axiom schemas, (K) $\varphi \to (\psi \to \varphi)$, (S) $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$ and [[Peirce's law|GMSZ75D5WE]] (P) $((\varphi \to \psi) \to \varphi) \to \varphi$, and the rule [[modus ponens|0Y0MQYST0M]].
Its theorems are exactly the [[tautologies|05006AJ7DZ]] in which $\to$ is the only connective.
It is the smallest standard setting in which the classical and the intuitionistic laws of implication can be compared.

## Motivation

Many arguments use only "if ... then": chains of implications, the deduction theorem, and proofs by cases on a hypothesis.
So it is natural to ask which laws of $\to$ hold, and which axioms derive them, with no help from $\neg$, $\land$ or $\lor$.
The schemas K and S are enough for the [[deduction theorem|9X08XK5RV2]], but they do not derive every classical law of $\to$.
Peirce's law is the extra axiom that closes this gap, and it plays the role of excluded middle in a language without negation.

## Notation

Formulas are written with $\to$ only, and $\to$ associates to the right: $\varphi \to \psi \to \chi$ means $\varphi \to (\psi \to \chi)$.
The names K and S come from combinatory logic; many books call them A1 and A2, as in the system L.
Some books write $\supset$ for $\to$.
We write $\vdash$ for derivability in this system and $\models$ for truth under all truth assignments, and these relations are different by definition.

## Remarks

### Examples

- Every instance of K, S and P is a theorem, with a derivation of one line.
- $\vdash \varphi \to \varphi$: the five-line [[derivation of p → p|S8M610SGM8]] uses only K, S and modus ponens.
- $\vdash (\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi))$: the [[derivation with the deduction theorem|M6ZAJFQ7E2]] uses only modus ponens and the deduction theorem, which holds here.
- The formula $(p \to q) \to q$ has the truth table of $p \lor q$, so disjunction is definable with $\to$ alone; see [[this example|EJMQ2P9H5B]].
- The formula $((p \to q) \to q) \to ((q \to p) \to p)$, which says that this disjunction is commutative, is a theorem, and its derivation uses Peirce's law; see [[this derivation|GEQWJPR0ZV]].

### Non-examples

- The formula $\neg p$ cannot be expressed: every formula with only $\to$ takes the value $1$ when all its variables take the value $1$; see [[this non-example|PAG45X56GC]].
- The formula $p \land q$ cannot be expressed. Each formula with only $\to$ is true whenever its rightmost variable is true, since $\alpha \to \beta$ is true when $\beta$ is true. But $p \land q$ is false at $p = 1, q = 0$ and at $p = 0, q = 1$.
- The formula $(p \to q) \to p$ is not a theorem: under $v(p) = 0$ it takes the value $1 \to 0 = 0$, so it is not a tautology.
- Peirce's law is not a theorem of the system with K and S alone: in the three-element Heyting algebra, K and S always take the top value, and Peirce's law does not.

### Basic properties

- The deduction theorem holds, because its proof uses only K, S and modus ponens.
- Soundness: each axiom is a tautology, and modus ponens preserves truth, so every theorem is a tautology.
- Completeness: every tautology with only $\to$ is a theorem. The standard proof is constructive: it builds a derivation for each tautology.
- Łukasiewicz found the single axiom schema $((\varphi \to \psi) \to \chi) \to ((\chi \to \varphi) \to (\theta \to \varphi))$, which with modus ponens gives the same theorems. Sekimoto checked this with a computer search, and he proved that it is the unique smallest single axiom.
- The Bernays-Tarski system replaces S by $(\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi))$ and has the same theorems.
- Implication alone is not functionally complete. With a constant $\bot$ for false, every truth function becomes definable, since $\neg \varphi$ is $\varphi \to \bot$.

### History

Peirce's law is named after Charles Sanders Peirce, who stated it in his algebra of logic.
Łukasiewicz found his single axiom for the implicational calculus in 1948.
The Bernays-Tarski axiom system is a common alternative axiomatization.

### Common errors

- Thinking that K and S derive all tautologies in $\to$: they axiomatize intuitionistic implication, and Peirce's law is missing.
- Reading $(p \to q) \to q$ as "$q$": it has the value $1$ when $p = 1$ and $q = 0$, so it is not equivalent to $q$.
- Thinking that a formula with only $\to$ can say "$p$ is false": no such formula exists, since every formula with only $\to$ is true when all its variables are true.

## Explanations

### L1 human

This is logic with only one word: "if ... then".
We can still say a lot: "if $p$ then $p$" and "if $p$ then (if $q$ then $p$)" are always true.
We can even say "$p$ or $q$", as "if ($p$ implies $q$) then $q$".
We cannot say "not $p$": when every letter is true, every "if ... then" formula is true, so no formula can be false exactly when $p$ is true.
Three axiom patterns and modus ponens are enough to prove every always-true formula of this kind.

### L2 human

We derive $q \to (p \to p)$ in the system.

1. $p \to p$, by the five-line derivation from K, S and modus ponens.
2. $(p \to p) \to (q \to (p \to p))$, an instance of K with $\varphi := p \to p$ and $\psi := q$.
3. $q \to (p \to p)$, by modus ponens from lines 1 and 2.

The typical use of the system is to decide which laws of implication need classical logic.
A law that is derivable from K and S alone holds intuitionistically, and a law that needs P does not.
A trap is to use $\neg$ or $\bot$ in a derivation: the language has only $\to$, and the axiom A3 of L does not belong to it.

### L3 human

The system with K and S alone is the implicational fragment of intuitionistic logic.
Under the Curry-Howard correspondence, its theorems are the types of the closed terms of the simply typed lambda calculus.
Adding P gives the classical fragment, whose algebraic models are the implication reducts of [[Boolean algebras|0XADJKM699]], while K and S correspond to the implicational reducts of [[Heyting algebras|NG943XNQWH]].
Fragments with one connective are a test case for questions about axiomatization, such as [[single axioms|644XCQAC8C]] and [[independence of axioms|729RCBPAM3]].
Among the sixteen truth functions of two variables, exactly six are definable with $\to$ and the variables $p$, $q$: $p$, $q$, $p \to q$, $q \to p$, $p \lor q$ and the constant $1$.
