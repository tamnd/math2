---
tag: 52XCYMK0WW
kind: definition
name: Intuitionistic logic
msc: [03B20, 03F55]
defines: Q11N8X99FK
uses: [09K9MWD2QQ, 1MGMQX43B8, 0Y0MQYST0M, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
---

## Definition

The formulas of intuitionistic propositional logic are built from propositional variables and $\bot$ with $\land$, $\lor$ and $\to$.
The negation $\neg\varphi$ abbreviates $\varphi \to \bot$.
Intuitionistic propositional logic is the set of formulas derivable in the [[Hilbert system|1MGMQX43B8]] with the following axiom schemes, for all formulas $\varphi$, $\psi$, $\chi$.

1. $\varphi \to (\psi \to \varphi)$.
2. $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$.
3. $\varphi \land \psi \to \varphi$ and $\varphi \land \psi \to \psi$.
4. $\varphi \to (\psi \to \varphi \land \psi)$.
5. $\varphi \to \varphi \lor \psi$ and $\psi \to \varphi \lor \psi$.
6. $(\varphi \to \chi) \to ((\psi \to \chi) \to (\varphi \lor \psi \to \chi))$.
7. $\bot \to \varphi$.

The only rule is [[modus ponens|0Y0MQYST0M]]: from $\varphi$ and $\varphi \to \psi$, derive $\psi$.

## Remarks

Adding the scheme $\varphi \lor \neg\varphi$, the [[law of excluded middle|0RYYK8PG4S]], gives classical [[propositional logic|09K9MWD2QQ]].
Intuitionistic first-order logic adds quantifiers with the usual axioms and rules, again without excluded middle.

Example: $\varphi \to \neg\neg\varphi$, that is, $\varphi \to ((\varphi \to \bot) \to \bot)$, is derivable.
By the deduction theorem it suffices to derive $\bot$ from $\varphi$ and $\varphi \to \bot$, which is one step of modus ponens.

Non-example: $p \lor \neg p$ is not derivable for a variable $p$.
In the Kripke model with worlds $u \le v$ and $p$ true only at $v$, neither $p$ nor $\neg p$ holds at $u$, and derivable formulas hold at every world.

Likewise $\neg\neg p \to p$ is not derivable, while $\neg\neg\neg p \to \neg p$ is.

## Explanations

### L1 human

Intuitionistic logic keeps every rule of ordinary logic except the principle that each statement is true or false.
It reads a formula as a task: to prove $A \to B$ is to give a method that turns any proof of $A$ into a proof of $B$.
