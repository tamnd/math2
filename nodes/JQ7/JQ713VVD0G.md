---
tag: JQ713VVD0G
kind: definition
name: Łukasiewicz infinite-valued logic
msc: ["03B50", "03B52"]
topics: [WZP584JQ06]
audience: research
defines: NFCEM44XYH
uses: [AJEJS6TFWP, F9NDCFY3GS, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: Axioms; Real-valued semantics
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 3. Łukasiewicz logic
  - url: https://plato.stanford.edu/entries/lukasiewicz/
    locator: 5.4 Axioms and Definitions
---

## Definition

The *standard Łukasiewicz matrix* is the [[logical matrix|AJEJS6TFWP]] $\langle [0, 1], \neg, \to, \set{1} \rangle$ with
$$\neg x = 1 - x, \qquad x \to y = \min(1, 1 - x + y).$$
*Infinite-valued Łukasiewicz logic* $\mathrm{Ł}_\infty$ is its logic: $\Gamma \models \varphi$ iff every valuation $v \colon \mathrm{Var} \to [0, 1]$ with $v(\gamma) = 1$ for all $\gamma \in \Gamma$ has $v(\varphi) = 1$.
A *tautology* of $\mathrm{Ł}_\infty$ is a formula $\varphi$ with $\emptyset \models \varphi$.

The derived connectives are
$$\varphi \oplus \psi = \neg \varphi \to \psi, \quad \varphi \odot \psi = \neg(\varphi \to \neg \psi), \quad \varphi \lor \psi = (\varphi \to \psi) \to \psi, \quad \varphi \land \psi = \neg(\neg \varphi \lor \neg \psi),$$
with values $\min(1, x + y)$, $\max(0, x + y - 1)$, $\max(x, y)$ and $\min(x, y)$.

The *Łukasiewicz axioms* are all instances of the four schemas

1. $\varphi \to (\psi \to \varphi)$,
2. $(\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi))$,
3. $((\varphi \to \psi) \to \psi) \to ((\psi \to \varphi) \to \varphi)$,
4. $(\neg \psi \to \neg \varphi) \to (\varphi \to \psi)$,

with [[modus ponens|0Y0MQYST0M]] as the only rule.

## Notation

Strong conjunction $\odot$ is also written $\otimes$, $\&$ or $\cdot$.
The logic is also written $\mathrm{Ł}$, $\mathrm{Ł}_{\aleph_0}$ or $\mathrm{Ł}_{[0,1]}$.

## Remarks

1. Example: axiom 3 is a tautology, since both $(x \to y) \to y$ and $(y \to x) \to x$ equal $\max(x, y)$; see [[the computation|DG496EV8FE]].
2. Non-example: Wajsberg's axiom $((p \to \neg p) \to p) \to p$ of $\mathrm{Ł}_3$ is not a tautology; it has value $\tfrac23$ at $p = \tfrac23$, see [[the four-valued counter-model|BK6EPGABW8]].
3. The original list of Łukasiewicz, as SEP gives it, has a fifth schema $((\varphi \to \psi) \to (\psi \to \varphi)) \to (\psi \to \varphi)$; it is derivable from the four above.
4. Using the rational points of $[0, 1]$ in place of $[0, 1]$ gives the same tautologies, by continuity of the operations.
5. The [[three-valued matrix|F9NDCFY3GS]] is the restriction to $\set{0, \tfrac12, 1}$.

## Explanations

### L1 human

The truth values are all numbers from $0$ to $1$.
Negation flips $x$ to $1 - x$.
Implication is $1$ when the antecedent is at most the consequent, and otherwise it is $1$ minus the drop.
The four axioms and modus ponens prove exactly the formulas that always get the value $1$.

### L2 human

To check that $\varphi$ is a tautology, compute its value as a function of the variables and show that it is $1$ everywhere.
For axiom 1: $\psi \to \varphi$ has value $\min(1, 1 - y + x) \ge x$, so $x \to (\psi \to \varphi) = 1$.
A trap: a formula can be $1$ on $\set{0, 1}$ and on $\set{0, \tfrac12, 1}$ and still fail on $[0, 1]$, as Wajsberg's axiom shows at $\tfrac23$.
