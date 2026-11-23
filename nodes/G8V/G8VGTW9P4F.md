---
tag: G8VGTW9P4F
kind: definition
name: Modal logic
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
defines: C3RZY20ETK
uses: [09K9MWD2QQ, 05006AJ7DZ, 0Y0MQYST0M, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Definition

We define the modal formulas, their depth, and the sets of formulas that count as a modal logic.

Fix a countable set $\Phi = \{ p_0, p_1, p_2, \dots \}$ of propositional variables.
The modal formulas are given by the following grammar:
$$\varphi ::= p \mid \bot \mid (\varphi \to \varphi) \mid \square\varphi, \qquad p \in \Phi.$$
We use the abbreviations $\neg\varphi := \varphi \to \bot$, $\top := \neg\bot$, $\varphi \vee \psi := \neg\varphi \to \psi$ and $\varphi \wedge \psi := \neg(\varphi \to \neg\psi)$.
We also put $\varphi \leftrightarrow \psi := (\varphi \to \psi) \wedge (\psi \to \varphi)$ and $\lozenge\varphi := \neg\square\neg\varphi$.

1. The set $\operatorname{Sub}(\varphi)$ of subformulas is defined by $\operatorname{Sub}(p) = \{ p \}$, $\operatorname{Sub}(\bot) = \{ \bot \}$, $\operatorname{Sub}(\varphi \to \psi) = \{ \varphi \to \psi \} \cup \operatorname{Sub}(\varphi) \cup \operatorname{Sub}(\psi)$ and $\operatorname{Sub}(\square\varphi) = \{ \square\varphi \} \cup \operatorname{Sub}(\varphi)$.
2. The modal depth is defined by $\operatorname{md}(p) = \operatorname{md}(\bot) = 0$, $\operatorname{md}(\varphi \to \psi) = \max(\operatorname{md}(\varphi), \operatorname{md}(\psi))$ and $\operatorname{md}(\square\varphi) = \operatorname{md}(\varphi) + 1$.
3. A substitution is a map $\sigma$ from $\Phi$ to formulas.
   The formula $\varphi^\sigma$ is the result of replacing each variable $p$ in $\varphi$ by $\sigma(p)$, at all its occurrences at the same time.
4. A modal logic is a set $\Lambda$ of modal formulas with three properties.
   First, $\Lambda$ contains every [[tautology|05006AJ7DZ]] of the [[propositional calculus|09K9MWD2QQ]], with modal formulas put for its variables.
   Second, if $\varphi \in \Lambda$ and $\varphi \to \psi \in \Lambda$, then $\psi \in \Lambda$ ([[modus ponens|0Y0MQYST0M]]).
   Third, if $\varphi \in \Lambda$, then $\varphi^\sigma \in \Lambda$ for every substitution $\sigma$ (uniform substitution).

## Notation

We write $\Lambda \vdash \varphi$ for $\varphi \in \Lambda$, and we call the members of $\Lambda$ its theorems.
The size $\lvert\varphi\rvert$ is the number of symbols of $\varphi$, and $\lvert\operatorname{Sub}(\varphi)\rvert \le \lvert\varphi\rvert$, because each occurrence of a subformula has its own main symbol.
Some authors take $\neg$, $\wedge$, $\vee$ and $\lozenge$ as primitive.
Then $\operatorname{md}(\lozenge\varphi) = \operatorname{md}(\varphi) + 1$ as well, and the sets of subformulas are smaller.

## Remarks

### Reading the conditions

Each clause of $\operatorname{Sub}$ and $\operatorname{md}$ is a definition by [[structural induction|12MQ2NJ29A]], and it is well defined because each formula is read in only one way.
For example, $\operatorname{md}(\square(p \to \square q) \to \square p)$ is $\max(2, 1) = 2$, since the left part has a box inside a box.

The three conditions on $\Lambda$ say what a logic must do.
The tautologies make $\Lambda$ contain all of classical logic, also for modal formulas, so $\square p \vee \neg\square p$ is in every modal logic.
Modus ponens makes $\Lambda$ closed under the one rule of the propositional calculus.
Uniform substitution makes $\Lambda$ a set of schemas: a theorem about the letter $p$ is a theorem about every formula in the place of $p$.

### A set that fails a condition

The set of formulas true at one world of one model contains all tautologies and is closed under modus ponens.
It fails substitution: in the one-world model where $p$ is true, $p$ belongs to the set and its instance $\bot$ does not.
[[The formulas true at one world|ESBQKZG00Q]] gives the details.

### What comes next

The set of all formulas is a modal logic, the inconsistent one, and every other modal logic omits $\bot$.
The intersection of modal logics is a modal logic, so each set of formulas lies in a smallest modal logic.
The normal modal logics add the axiom $\mathrm{K}$ and the [[necessitation rule|G989VP2NGP]], and [[normal modal logic K|JS8W7PA6JK]] defines them.
The idea behind the definition is told in the concept page [[modal logic|C3RZY20ETK]].

## Explanations

### L1 human

A modal formula is built like a formula of ordinary logic, with one extra symbol, the box.
The box in front of a formula means "necessarily".
The diamond means "possibly", and it is short for "not necessarily not".
The modal depth counts how many boxes are stacked inside each other.
For example, "box box $p$" has depth 2, and "box $p$ or box $q$" has depth 1.

### L2 human

We compute the depth of $\varphi = \square(p \to \square q) \to \square p$ from the inside out.
The variables have depth $0$, so $\operatorname{md}(\square q) = 1$ and $\operatorname{md}(p \to \square q) = \max(0, 1) = 1$.
One more box gives $\operatorname{md}(\square(p \to \square q)) = 2$, and $\operatorname{md}(\square p) = 1$.
So $\operatorname{md}(\varphi) = \max(2, 1) = 2$.
The typical use of the depth is an induction on formulas, for example in the proof that truth at a world depends only on the worlds near it.
Watch out: uniform substitution replaces every occurrence of a variable by the same formula, and it replaces variables only, never compound subformulas.

### L3 human

The modal formulas form the term algebra of the signature of Boolean algebras with one unary operator.
A substitution is an endomorphism of this algebra.
So a modal logic is a set closed under all endomorphisms and under modus ponens.
For normal logics this view links logics to varieties of Boolean algebras with operators, along the lines of the representation theorem of Jónsson and Tarski.
