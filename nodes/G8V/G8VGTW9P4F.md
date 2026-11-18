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

Fix a countable set $\Phi = \set{p_0, p_1, p_2, \dots}$ of propositional variables.
The modal formulas are given by the grammar
$$\varphi ::= p \mid \bot \mid (\varphi \to \varphi) \mid \square\varphi, \qquad p \in \Phi.$$
We use the abbreviations $\neg\varphi := \varphi \to \bot$, $\top := \neg\bot$, $\varphi \vee \psi := \neg\varphi \to \psi$, $\varphi \wedge \psi := \neg(\varphi \to \neg\psi)$, $\varphi \leftrightarrow \psi := (\varphi \to \psi) \wedge (\psi \to \varphi)$ and $\lozenge\varphi := \neg\square\neg\varphi$.

1. The set $\operatorname{Sub}(\varphi)$ of subformulas is defined by $\operatorname{Sub}(p) = \set{p}$, $\operatorname{Sub}(\bot) = \set{\bot}$, $\operatorname{Sub}(\varphi \to \psi) = \set{\varphi \to \psi} \cup \operatorname{Sub}(\varphi) \cup \operatorname{Sub}(\psi)$ and $\operatorname{Sub}(\square\varphi) = \set{\square\varphi} \cup \operatorname{Sub}(\varphi)$.
2. The modal depth is defined by $\operatorname{md}(p) = \operatorname{md}(\bot) = 0$, $\operatorname{md}(\varphi \to \psi) = \max(\operatorname{md}(\varphi), \operatorname{md}(\psi))$ and $\operatorname{md}(\square\varphi) = \operatorname{md}(\varphi) + 1$.
3. A substitution is a map $\sigma$ from $\Phi$ to formulas. The formula $\varphi^\sigma$ is the result of replacing each $p$ in $\varphi$ by $\sigma(p)$ at the same time.
4. A modal logic is a set $\Lambda$ of modal formulas with three properties. First, $\Lambda$ contains every [[tautology|05006AJ7DZ]] of the [[propositional calculus|09K9MWD2QQ]]. Second, if $\varphi \in \Lambda$ and $\varphi \to \psi \in \Lambda$, then $\psi \in \Lambda$ ([[modus ponens|0Y0MQYST0M]]). Third, if $\varphi \in \Lambda$, then $\varphi^\sigma \in \Lambda$ for every substitution $\sigma$ (uniform substitution).

## Notation

We write $\Lambda \vdash \varphi$ for $\varphi \in \Lambda$, and call the members of $\Lambda$ its theorems.
The size $\lvert\varphi\rvert$ is the number of symbols of $\varphi$; then $\lvert\operatorname{Sub}(\varphi)\rvert \le \lvert\varphi\rvert$.
Some authors take $\neg$, $\wedge$, $\vee$ and $\lozenge$ as primitive; then $\operatorname{md}(\lozenge\varphi) = \operatorname{md}(\varphi) + 1$ as well, and the subformula sets are slightly smaller.

## Remarks

1. Each clause of $\operatorname{Sub}$ and $\operatorname{md}$ is a definition by [[structural induction|12MQ2NJ29A]] on formulas, and each formula is read in a unique way.
2. A tautology here is a modal formula obtained from a classical tautology by a substitution of modal formulas for its variables, such as $\square p \vee \neg\square p$.
3. The set of all modal formulas is a modal logic, the inconsistent one; every other modal logic omits $\bot$.
4. The intersection of modal logics is a modal logic, so each set $\Gamma$ of formulas lies in a smallest modal logic that contains it.
5. The normal modal logics, which add the axiom $\mathrm{K}$ and the [[necessitation rule|G989VP2NGP]], are defined in [[normal modal logic K|JS8W7PA6JK]].
6. A worked count of subformulas and depth is in [[the worked example|1GQEQHQ57F]]. A set that is closed under modus ponens but not under substitution is in [[the one-world example|ESBQKZG00Q]].

## Explanations

### L1 human

A modal formula is built like a formula of ordinary logic, with one extra symbol, the box.
The box in front of a formula means "necessarily".
The diamond means "possibly", and it is short for "not necessarily not".
The modal depth counts how many boxes are stacked inside each other.
For example, "box box $p$" has depth 2, and "box $p$ or box $q$" has depth 1.

### L2 human

We compute the depth of $\varphi = \square(p \to \square q) \to \square p$.

1. $\operatorname{md}(p) = \operatorname{md}(q) = 0$.
2. $\operatorname{md}(\square q) = 1$, so $\operatorname{md}(p \to \square q) = \max(0, 1) = 1$.
3. $\operatorname{md}(\square(p \to \square q)) = 2$ and $\operatorname{md}(\square p) = 1$.
4. So $\operatorname{md}(\varphi) = \max(2, 1) = 2$.

The typical use of the depth is an induction on the formula.
An example is the proof that truth depends only on worlds near the point of evaluation.
A trap: uniform substitution replaces every occurrence of a variable by the same formula, and it replaces variables only, never compound subformulas.

### L3 human

The modal formulas form the term algebra of the signature of Boolean algebras with one unary operator.
A substitution is an endomorphism of this algebra.
A modal logic is then a set closed under all endomorphisms and under modus ponens.
For normal logics this view gives the link to varieties of Boolean algebras with operators.
This follows the line of the representation theorem of Jónsson and Tarski.
