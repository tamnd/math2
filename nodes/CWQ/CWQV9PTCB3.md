---
tag: CWQV9PTCB3
kind: definition
name: Model
msc: [03C07]
defines: MVCH6N9SNW
uses: [92SWXST1ZM, 983GZBQYT4, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
---

## Definition

Let $L$ be a signature and let $T$ be an $L$-[[theory|92SWXST1ZM]].
An $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ is a model of $T$ when $\mathcal{M} \models \varphi$ for every [[sentence|DKFGQTRYZE]] $\varphi$ in $T$.
Here $\mathcal{M} \models \varphi$ means that $\varphi$ is true in $\mathcal{M}$ under the usual inductive definition of truth.
The notation is $\mathcal{M} \models T$.

## Remarks

Example: let $T$ be the theory of groups in the signature $\set{\cdot, e, {}^{-1}}$.
The structure $(\Z, +, 0, -)$, with $\cdot$ read as $+$, $e$ as $0$ and ${}^{-1}$ as $-$, is a model of $T$.
Indeed addition of integers is associative, $0$ is neutral and $-x$ is an inverse of $x$.

Non-example: the structure $(\N, +, 0, \id)$, with ${}^{-1}$ read as the identity map, is not a model of $T$.
The sentence $\forall x \, (x \cdot x^{-1} = e)$ fails at $x = 1$, because $1 + 1 \ne 0$.

A theory is satisfiable when it has a model.
The class of all models of $T$ is often written $\mathrm{Mod}(T)$.

## Explanations

### L1 human

To check that a structure is a model of a theory, you check each sentence of the theory in the structure.
Every group is a model of the group axioms, and every model of the group axioms is a group.
