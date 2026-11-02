---
tag: 6BQ71KQ6QT
kind: definition
name: Kripke semantics
msc: [03B45, 03B20]
defines: NGHWZ9Y7ZV
uses: [C3RZY20ETK, 05AVARPXA2, 00E0YZCERH]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
---

## Definition

A Kripke frame is a pair $(W, R)$ of a nonempty set $W$ of worlds and a [[binary relation|05AVARPXA2]] $R$ on $W$, the accessibility relation.
A Kripke model is a triple $\mathfrak{M} = (W, R, V)$ where $V$ maps each propositional variable to a subset of $W$, an element of the [[power set|00E0YZCERH]].
Truth of a [[modal formula|C3RZY20ETK]] at a world $w \in W$ is defined by induction.

1. $\mathfrak{M}, w \models p$ if and only if $w \in V(p)$, and $\mathfrak{M}, w \not\models \bot$.
2. The connectives $\neg$, $\land$, $\lor$ and $\to$ are evaluated at $w$ as in classical logic.
3. $\mathfrak{M}, w \models \square\varphi$ if and only if $\mathfrak{M}, v \models \varphi$ for every $v \in W$ with $w R v$.

A formula is valid on the frame $(W, R)$ when it is true at every world of every model $(W, R, V)$.

## Remarks

Then $\mathfrak{M}, w \models \lozenge\varphi$ if and only if some $v$ with $w R v$ has $\mathfrak{M}, v \models \varphi$.

Example: on any frame, the axiom $\square(p \to q) \to (\square p \to \square q)$ is valid.
At a world $w$ where $\square(p \to q)$ and $\square p$ hold, every $v$ with $w R v$ satisfies $p \to q$ and $p$, hence $q$.

Non-example: $\square p \to p$ is not valid on the frame $(\set{w}, \emptyset)$.
With $V(p) = \emptyset$, the formula $\square p$ holds at $w$ because no world is accessible, while $p$ fails at $w$.

The formulas valid on all frames form the logic $\mathrm{K}$.
The formulas valid on all reflexive frames form $\mathrm{T}$, and those valid on all reflexive and transitive frames form $\mathrm{S4}$.

For intuitionistic logic, the relation is a preorder, $V(p)$ is closed upward, and $\varphi \to \psi$ holds at $w$ when $\psi$ holds at every $v \ge w$ where $\varphi$ holds.

## Explanations

### L1 human

Kripke semantics reads "necessarily" as "in every world I can see".
Different conditions on the arrows between worlds give different laws of necessity.
For instance, if every world sees itself, then what is necessary is true.
