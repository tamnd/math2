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

Łukasiewicz infinite-valued logic takes every number in $[0, 1]$ as a truth value, with $1$ as the only designated value.
The *standard Łukasiewicz matrix* is the [[logical matrix|AJEJS6TFWP]] $\langle [0, 1], \neg, \to, \{1\} \rangle$ with the operations below.
$$\neg x = 1 - x, \qquad x \to y = \min(1, 1 - x + y)$$
*Infinite-valued Łukasiewicz logic* $\mathrm{Ł}_\infty$ is its logic: $\Gamma \models \varphi$ holds when every valuation $v \colon \mathrm{Var} \to [0, 1]$ with $v(\gamma) = 1$ for all $\gamma \in \Gamma$ has $v(\varphi) = 1$.
A *tautology* of $\mathrm{Ł}_\infty$ is a formula $\varphi$ with $\emptyset \models \varphi$.

The derived connectives are defined as follows.
$$\varphi \oplus \psi = \neg \varphi \to \psi, \quad \varphi \odot \psi = \neg(\varphi \to \neg \psi), \quad \varphi \lor \psi = (\varphi \to \psi) \to \psi, \quad \varphi \land \psi = \neg(\neg \varphi \lor \neg \psi)$$
Their values are $\min(1, x + y)$, $\max(0, x + y - 1)$, $\max(x, y)$ and $\min(x, y)$.

The *Łukasiewicz axioms* are all instances of four schemas, with [[modus ponens|0Y0MQYST0M]] as the only rule.

1. $\varphi \to (\psi \to \varphi)$
2. $(\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi))$
3. $((\varphi \to \psi) \to \psi) \to ((\psi \to \varphi) \to \varphi)$
4. $(\neg \psi \to \neg \varphi) \to (\varphi \to \psi)$

## Notation

Strong conjunction $\odot$ is also written $\otimes$, $\&$ or $\cdot$.
The logic is also written $\mathrm{Ł}$, $\mathrm{Ł}_{\aleph_0}$ or $\mathrm{Ł}_{[0,1]}$.

## Remarks

Each part of the definition has a reason.
The designated set $\{1\}$ makes "true" mean "fully true", so a tautology must get the top value everywhere.
The implication rewards a consequent that is at least as true as the antecedent, and it charges the exact drop otherwise.
For example, $0.7 \to 0.4 = \min(1, 0.7) = 0.7$, since the drop is $0.3$.

The derived connectives come out of $\neg$ and $\to$ alone.
For strong conjunction, compute $1 - \min(1, 1 - x + 1 - y) = \max(0, x + y - 1)$.
At $x = y = 0.6$ this gives $0.2$.

Axiom 3 is a tautology, since both $(x \to y) \to y$ and $(y \to x) \to x$ equal $\max(x, y)$, by [[the computation|DG496EV8FE]].
A formula that fails is Wajsberg's axiom $((p \to \neg p) \to p) \to p$ of $\mathrm{Ł}_3$.
At $p = \tfrac23$ we get $\neg p = \tfrac13$ and $p \to \neg p = \tfrac23$, then $\tfrac23 \to \tfrac23 = 1$ and $1 \to \tfrac23 = \tfrac23$; see [[the four-valued counter-model|BK6EPGABW8]].

Łukasiewicz's own list had a fifth schema, $((\varphi \to \psi) \to (\psi \to \varphi)) \to (\psi \to \varphi)$, and it is derivable from the four above.
The rational points of $[0, 1]$ give the same tautologies, because the operations are continuous.
The [[three-valued matrix|F9NDCFY3GS]] is the restriction to $\{0, \tfrac12, 1\}$.
The concept page [[Łukasiewicz infinite-valued logic|NFCEM44XYH]] works the main examples.

## Explanations

### L1 human

The truth values are all numbers from $0$ to $1$.
Negation flips $x$ to $1 - x$.
Implication is $1$ when the antecedent is at most the consequent, and otherwise it is $1$ minus the drop.
The four axioms and modus ponens prove exactly the formulas that always get the value $1$.

### L2 human

To check that $\varphi$ is a tautology, compute its value as a function of the variables and show that it is $1$ everywhere.
For axiom 1, the inner formula $\psi \to \varphi$ has the value $\min(1, 1 - y + x)$, which is at least $x$.
So the antecedent $x$ is at most the consequent, and $x \to (\psi \to \varphi) = 1$.
Watch out: a formula can be $1$ on $\{0, 1\}$ and on $\{0, \tfrac12, 1\}$ and still fail on $[0, 1]$.
Wajsberg's axiom is such a formula, and it fails at $\tfrac23$.
