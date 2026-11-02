---
tag: G8VGTW9P4F
kind: definition
name: Modal logic
msc: [03B45]
defines: C3RZY20ETK
uses: [09K9MWD2QQ, 05006AJ7DZ, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
---

## Definition

The modal formulas are built from propositional variables $p, q, \dots$ and the constant $\bot$ with the connectives $\neg$, $\land$, $\lor$, $\to$ and the unary operator $\square$.
The formula $\lozenge\varphi$ abbreviates $\neg\square\neg\varphi$.
A normal modal logic is a set $\Lambda$ of modal formulas with these properties.

1. $\Lambda$ contains every substitution instance of a [[tautology|05006AJ7DZ]] of [[propositional logic|09K9MWD2QQ]].
2. $\Lambda$ contains every formula $\square(\varphi \to \psi) \to (\square\varphi \to \square\psi)$, the axiom $\mathrm{K}$.
3. If $\varphi \in \Lambda$ and $\varphi \to \psi \in \Lambda$, then $\psi \in \Lambda$, the rule of [[modus ponens|0Y0MQYST0M]].
4. If $\varphi \in \Lambda$, then $\square\varphi \in \Lambda$, the rule of necessitation.
5. If $\varphi \in \Lambda$, then each formula obtained from $\varphi$ by substituting formulas for its variables is in $\Lambda$.

The smallest normal modal logic is called $\mathrm{K}$.

## Remarks

Example: the logic $\mathrm{S4}$ is the smallest normal modal logic containing $\square p \to p$ and $\square p \to \square\square p$.
It satisfies the five clauses by construction, as the intersection of all normal modal logics that contain these two formulas.

Non-example: the set of all tautologies of propositional logic, read as modal formulas, is not a normal modal logic.
It fails clause 2, since $\square(p \to q) \to (\square p \to \square q)$ is not an instance of a tautology.

Other standard normal modal logics are $\mathrm{T}$, given by $\square p \to p$, and $\mathrm{S5}$, given by $\square p \to p$ and $\lozenge p \to \square\lozenge p$.
The word "modal logic" also names the whole field that studies such systems, including non-normal ones.

## Explanations

### L1 human

A modal logic is a list of the modal formulas taken as laws.
Every normal modal logic keeps all laws of classical logic and adds the rule that what is proved is necessary.
Extra axioms, such as "what is necessary is true", select the logic that fits a reading of $\square$.
