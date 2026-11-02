---
tag: 5PP333WZEK
kind: definition
name: Soundness
msc: [03B05, 03B10, 03F03]
defines: 4A84VHDTHV
uses: [1HK0VYWTV7, 1MGMQX43B8]
sources:
  - url: https://en.wikipedia.org/wiki/Soundness
---

## Definition

Let $\vdash$ be the derivability relation of a proof system, such as a [[Hilbert system|1MGMQX43B8]].
Let $\models$ be [[logical consequence|1HK0VYWTV7]] for the same language.
The proof system is *sound* if $\Gamma \vdash \varphi$ implies $\Gamma \models \varphi$, for every set of formulas $\Gamma$ and every formula $\varphi$.
It is *weakly sound* if $\vdash \varphi$ implies $\models \varphi$ for every formula $\varphi$.

## Remarks

The standard Hilbert system for propositional logic is sound.
Each axiom is a [[tautology|05006AJ7DZ]], checked by a truth table, and modus ponens preserves truth under every assignment.
Induction on the length of a derivation then gives soundness.
Adding the rule "from $\psi$ and $\varphi \to \psi$, infer $\varphi$" gives an unsound system.
With it, $\set{p \to q, \; q} \vdash p$, but the assignment $p = \mathsf{F}$, $q = \mathsf{T}$ shows $\set{p \to q, \; q} \not\models p$.
The converse property, that $\Gamma \models \varphi$ implies $\Gamma \vdash \varphi$, is completeness.
For first-order logic it is [[Gödel's completeness theorem|WQ1ZE255SF]].
