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

Take the [[Kripke model|NGHWZ9Y7ZV]] with one world:
$$W = \set{w}, \quad R = \set{(w, w)}, \quad V(p) = \set{w}.$$
Let $\mathrm{Th} = \set{\varphi : \mathfrak{M}, w \models \varphi}$ be the set of formulas true at $w$.
We check the closure conditions of a [[normal modal logic|D1TJYZZDCY]] one by one.

1. Each [[tautology|05006AJ7DZ]] is in $\mathrm{Th}$. At a fixed world, the connectives $\to$ and $\bot$ follow their truth tables, so every tautology is true at $w$.
2. Each instance of axiom $\mathrm{K}$ is in $\mathrm{Th}$, since $\mathrm{K}$ is true at every world of every Kripke model.
3. $\mathrm{Th}$ is closed under [[modus ponens|0Y0MQYST0M]]. If $\varphi$ and $\varphi \to \psi$ are true at $w$, then $\psi$ is true at $w$.
4. $\mathrm{Th}$ is closed under [[necessitation|G989VP2NGP]]. If $\varphi$ is true at $w$, then $\varphi$ is true at every successor of $w$, because the only successor is $w$. So $\square\varphi$ is true at $w$.
5. $p \in \mathrm{Th}$, since $w \in V(p)$.
6. Substitute $\bot$ for $p$ in the formula $p$. The result is $\bot$, and $\bot$ is false at every world. So $\bot \notin \mathrm{Th}$.
7. So $\mathrm{Th}$ is not closed under uniform substitution, and $\mathrm{Th}$ is not a [[modal logic|C3RZY20ETK]].

## Remarks

The example shows that closure under uniform substitution is a real condition, and that it separates truth in a model from validity.
The set of formulas valid on a frame $\mathfrak{F}$ is closed under substitution.
Indeed, if $\varphi$ is valid on $\mathfrak{F}$ and $V$ is a valuation, define $V'(p) = [\![ \psi ]\!]_V$.
Then $\varphi[\psi/p]$ under $V$ has the same truth set as $\varphi$ under $V'$, and that set is $W$.
If we change the valuation to $V(p) = \varnothing$, then $\neg p \in \mathrm{Th}$, and the substitution of $\top$ for $p$ gives $\neg\top \notin \mathrm{Th}$.
So no choice of $V$ repairs the example.
The set $\mathrm{Th}$ is maximal consistent, like a world of a [[canonical model|TVE4F04KME]].
No maximal consistent set is closed under substitution, since it contains $p$ or $\neg p$, and the same argument applies.

## Explanations

### L1 human

Picture one room, where the light is on.
The list of statements that are true in this room contains "the light is on".
A logic should contain only laws that hold for every possible meaning of the letters.
If the letter means "the light is off", the statement becomes false.
So a list of facts about one room is not a logic.

### L2 human

1. Take the model above and the formula $\square p$.
2. It is true at $w$, since $p$ is true at $w$ and $w$ sees only itself.
3. Substitute $\neg p$ for $p$: the instance $\square\neg p$ is false at $w$.
4. So $\square p \in \mathrm{Th}$ and $\square\neg p \notin \mathrm{Th}$.

The typical use of this example is to remember why logics are defined by validity on frames.
They are not defined by truth at a world or in a model.
A trap: the conditions on tautologies, modus ponens and necessitation hold here.
So a check of these three conditions alone does not show that a set is a normal modal logic.
