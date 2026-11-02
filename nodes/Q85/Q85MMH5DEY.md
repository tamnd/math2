---
tag: Q85MMH5DEY
kind: definition
name: Sentence
msc: [03B10, 03C07]
defines: DKFGQTRYZE
uses: [HYJ10AF6RT, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Sentence_(mathematical_logic)
---

## Definition

Let $\sigma$ be a signature.
The set $\operatorname{FV}(\varphi)$ of *free variables* of a [[formula|HYJ10AF6RT]] $\varphi$ over $\sigma$ is defined by recursion on $\varphi$:

1. for an atomic formula, $\operatorname{FV}(\varphi)$ is the set of variables that occur in its [[terms|6D3WA7N2W4]];
2. $\operatorname{FV}(\neg \varphi) = \operatorname{FV}(\varphi)$, and $\operatorname{FV}(\varphi \ast \psi) = \operatorname{FV}(\varphi) \cup \operatorname{FV}(\psi)$ for each binary connective $\ast$;
3. $\operatorname{FV}(\forall x \, \varphi) = \operatorname{FV}(\exists x \, \varphi) = \operatorname{FV}(\varphi) \setminus \set{x}$.

A *sentence* over $\sigma$ is a formula $\varphi$ with $\operatorname{FV}(\varphi) = \emptyset$.

## Remarks

The formula $\forall x \, \exists y \, (x < y)$ is a sentence.
Indeed $\operatorname{FV}(x < y) = \set{x, y}$, removing $y$ gives $\set{x}$, and removing $x$ gives $\emptyset$.
The formula $\exists y \, (x < y)$ is not a sentence, since $x$ remains free.
Sentences are also called closed formulas.
In Mathlib sentences are `FirstOrder.Language.Sentence`.
