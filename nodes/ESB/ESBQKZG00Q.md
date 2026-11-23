---
tag: ESBQKZG00Q
kind: example
name: The formulas true at one world do not form a modal logic
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: C3RZY20ETK
    note: the set is not closed under uniform substitution, so it is not a modal logic
uses: [C3RZY20ETK, NGHWZ9Y7ZV, D1TJYZZDCY, 05006AJ7DZ, 0Y0MQYST0M, G989VP2NGP]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: lead section
---

## Example

Take the [[Kripke model|NGHWZ9Y7ZV]] $\mathfrak{M}$ with one world that sees itself:
$$W = \{ w \}, \quad R = \{ (w, w) \}, \quad V(p) = \{ w \}.$$
Let $\mathrm{Th} = \{ \varphi : \mathfrak{M}, w \models \varphi \}$ be the set of formulas true at $w$.
We check the closure conditions of a [[normal modal logic|D1TJYZZDCY]] one by one, and we find that only substitution fails.

1. Each [[tautology|05006AJ7DZ]] is in $\mathrm{Th}$.
   At a fixed world, $\to$ and $\bot$ follow their truth tables, so every tautology is true at $w$.
2. Each instance of the axiom $\mathrm{K}$ is in $\mathrm{Th}$, because $\mathrm{K}$ is true at every world of every Kripke model.
3. $\mathrm{Th}$ is closed under [[modus ponens|0Y0MQYST0M]].
   If $\varphi$ and $\varphi \to \psi$ are true at $w$, then $\psi$ is true at $w$.
4. $\mathrm{Th}$ is closed under [[necessitation|G989VP2NGP]].
   If $\varphi$ is true at $w$, then $\varphi$ is true at every successor of $w$, because the only successor is $w$, so $\square\varphi$ is true at $w$.
5. The formula $p$ is in $\mathrm{Th}$, since $w \in V(p)$.
6. Substitute $\bot$ for $p$ in the formula $p$.
   The result is $\bot$, which is false at every world, so $\bot \notin \mathrm{Th}$.
7. So $\mathrm{Th}$ is not closed under uniform substitution, and $\mathrm{Th}$ is not a [[modal logic|C3RZY20ETK]].

## Remarks

Closure under uniform substitution is a real condition, and it is the condition that separates truth in a model from validity on a frame.

The set of formulas valid on a frame $\mathfrak{F}$ is closed under substitution.
Let $\varphi$ be valid on $\mathfrak{F}$, let $\psi$ be a formula and let $V$ be a valuation.
Define a new valuation $V'$ by $V'(p) = [\![ \psi ]\!]_V$ and $V'(q) = V(q)$ for the other variables.
Then the formula $\varphi[\psi/p]$ under $V$ has the same truth set as $\varphi$ under $V'$, by induction on $\varphi$.
That truth set is $W$, because $\varphi$ is valid on $\mathfrak{F}$.

Can another valuation repair the example?
No: if $V(p) = \varnothing$, then $\neg p \in \mathrm{Th}$, and the substitution of $\top$ for $p$ gives $\neg\top \notin \mathrm{Th}$.
In fact $\mathrm{Th}$ is maximal consistent, like a world of a [[canonical model|TVE4F04KME]].
No maximal consistent set is closed under substitution, because it contains $p$ or $\neg p$, and the argument above applies to both cases.

## Explanations

### L1 human

Picture one room where the light is on.
The list of statements that are true in this room contains "the light is on".
A logic should contain only laws that hold for every meaning of the letters.
If the letter means "the light is off", the statement becomes false.
So a list of facts about one room is not a logic.

### L2 human

Take the model above and the formula $\square p$.
It is true at $w$, since $p$ is true at $w$ and $w$ sees only itself.
Substitute $\neg p$ for $p$, and the instance $\square\neg p$ is false at $w$.
So $\square p \in \mathrm{Th}$ and $\square\neg p \notin \mathrm{Th}$.
This is why logics are defined by validity on frames, and not by truth at one world or in one model.
Watch out: the conditions on tautologies, modus ponens and necessitation all hold here, so a check of these three alone does not show that a set is a normal modal logic.
