---
tag: FZRMYTQFRR
kind: definition
name: Theory
msc: [03C07, 03B10]
defines: 92SWXST1ZM
uses: [WDVVEYD6AT, DKFGQTRYZE, 086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_(mathematical_logic)
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]].
An $L$-theory is a set $T$ of [[sentences|DKFGQTRYZE]] of [[first-order logic|086QKPF0A6]] in the signature $L$.

## Remarks

Example: in the signature $\set{\cdot, e, {}^{-1}}$, the set of the three sentences $\forall x \, \forall y \, \forall z \, ((x \cdot y) \cdot z = x \cdot (y \cdot z))$, $\forall x \, (x \cdot e = x \land e \cdot x = x)$ and $\forall x \, (x \cdot x^{-1} = e \land x^{-1} \cdot x = e)$ is a theory, the theory of groups.
Each of its elements is a formula without free variables, so it is a set of sentences.

Non-example: the set $\set{x \cdot e = x}$ is not a theory, because the variable $x$ is free in its only formula.

Some authors require a theory to be closed under logical consequence; a set of sentences is then called a set of axioms for the theory it generates.
For an $L$-structure $\mathcal{M}$, the set $\mathrm{Th}(\mathcal{M})$ of all $L$-sentences true in $\mathcal{M}$ is the theory of $\mathcal{M}$.

## Explanations

### L1 human

A theory is any set of sentences; it may be finite or infinite, and it may even be contradictory.
The theory of groups has three sentences.
Peano arithmetic is a theory with infinitely many sentences, one induction axiom for each formula.
