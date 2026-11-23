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

The implicational calculus is classical logic with the single word "if ... then", and three axiom patterns are enough to prove every law that uses only that word.
For example, $(p \to q) \to q$ already says "$p$ or $q$", and Peirce's law $((p \to q) \to p) \to p$ holds classically but not intuitionistically.

The *implicational propositional calculus* is the fragment of classical propositional logic whose formulas are built from propositional variables with the connective [[implication|0NMG7W7Q11]] $\to$ only.
As a [[Hilbert system|1MGMQX43B8]] it has the rule [[modus ponens|0Y0MQYST0M]] and three axiom schemas:
$$\begin{array}{ll} \text{(K)} & \varphi \to (\psi \to \varphi), \\ \text{(S)} & (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)), \\ \text{(P)} & ((\varphi \to \psi) \to \varphi) \to \varphi. \end{array}$$
The schema P is [[Peirce's law|GMSZ75D5WE]].
The theorems of the system are exactly the [[tautologies|05006AJ7DZ]] in which $\to$ is the only connective.

## Motivation

Many arguments use only "if ... then": chains of implications, the deduction theorem, and proofs by cases on a hypothesis.
So we ask which laws of $\to$ hold, and which axioms derive them, with no help from $\neg$, $\land$ or $\lor$.
The schemas K and S are enough for the [[deduction theorem|9X08XK5RV2]], but they do not derive every classical law of $\to$.
Peirce's law is the extra axiom that closes this gap, and it plays the role of excluded middle in a language without negation.

The system is the smallest standard setting in which the classical and the intuitionistic laws of implication can be compared.
It returns in the study of [[single axioms|644XCQAC8C]] and of [[independence of axioms|729RCBPAM3]], where one connective keeps the search small.

## Notation

Formulas are written with $\to$ only, and $\to$ associates to the right: $\varphi \to \psi \to \chi$ means $\varphi \to (\psi \to \chi)$.
The names K and S come from combinatory logic, and many books call them A1 and A2, as in the system L.
Some books write $\supset$ for $\to$.
We write $\vdash$ for derivability in this system and $\models$ for truth under all truth assignments; these relations are different by definition, and completeness shows that they agree.

## Remarks

### First theorems

Every instance of K, S and P is a theorem, with a derivation of one line.
The law $\vdash \varphi \to \varphi$ has the five-line [[derivation of p → p|S8M610SGM8]], which uses only K, S and modus ponens.
The law $\vdash (\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi))$ follows with the deduction theorem, as in [[the transitivity derivation|M6ZAJFQ7E2]], since the deduction theorem holds here.
The formula $(p \to q) \to q$ has the truth table of $p \lor q$: it is $0$ only at $p = q = 0$, where it is $1 \to 0 = 0$; see [[disjunction from implication|EJMQ2P9H5B]].
The formula $((p \to q) \to q) \to ((q \to p) \to p)$ says that this disjunction is commutative, and its [[derivation|GEQWJPR0ZV]] uses Peirce's law.

### What it cannot say or prove

The formula $\neg p$ cannot be expressed, because every formula with only $\to$ takes the value $1$ when all its variables take the value $1$; see [[this non-example|PAG45X56GC]].
The formula $p \land q$ cannot be expressed either.
Each formula with only $\to$ is true whenever its rightmost variable is true, since $\alpha \to \beta$ is true when $\beta$ is true, but $p \land q$ is false both at $p = 1, q = 0$ and at $p = 0, q = 1$.
The formula $(p \to q) \to p$ is not a theorem: under $v(p) = 0$ it takes the value $1 \to 0 = 0$.
Peirce's law is not a theorem of K and S alone, since in the three-element Heyting algebra K and S always take the top value and Peirce's law does not.

### The rules you can use

The system is sound, because each axiom is a tautology and modus ponens preserves truth.
It is complete: every tautology with only $\to$ is a theorem.
Łukasiewicz found the single axiom schema $((\varphi \to \psi) \to \chi) \to ((\chi \to \varphi) \to (\theta \to \varphi))$, which with modus ponens gives the same theorems.
The Bernays-Tarski system replaces S by $(\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi))$ and has the same theorems.
Implication alone is not functionally complete, but with a constant $\bot$ for false every truth function becomes definable, since $\neg \varphi$ is $\varphi \to \bot$.

### Watch out

K and S do not derive all tautologies in $\to$: they axiomatize intuitionistic implication, and Peirce's law is missing.
Do not read $(p \to q) \to q$ as $q$: it has the value $1$ at $p = 1$, $q = 0$, where $q$ is $0$.
Do not use $\neg$ or $\bot$ in a derivation: the language has only $\to$, and the axiom A3 of L does not belong to it.

### History

Peirce's law is named after Charles Sanders Peirce, who stated it in his work on the algebra of logic.
Łukasiewicz found his single axiom for the implicational calculus in 1948.

### Try it

First, is $p \to (q \to p)$ a theorem?
Yes, it is an instance of K with $\varphi := p$ and $\psi := q$.

Second, can a formula with only $\to$ be false when all its variables are true?
No, by induction on formulas, since $\alpha \to 1 = 1$.

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
A law that is derivable from K and S alone holds intuitionistically, and this one does, since P was not used.

### L3 human

The system with K and S alone is the implicational fragment of intuitionistic logic.
Under the Curry-Howard correspondence, its theorems are the types of the closed terms of the simply typed lambda calculus.
Adding P gives the classical fragment, whose algebraic models are the implication reducts of [[Boolean algebras|0XADJKM699]], while K and S correspond to the implication reducts of [[Heyting algebras|NG943XNQWH]].
Among the sixteen truth functions of two variables, exactly six are definable with $\to$ and the variables $p$, $q$: $p$, $q$, $p \to q$, $q \to p$, $p \lor q$ and the constant $1$.
