---
tag: 0ETGBAK2CC
kind: statement
role: theorem
name: Existence of an algebraic closure
msc: [12F05]
uses: [0MCXX29HWY, 02HJYT53F7, 0TPWS0K1BC]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_closure
    locator: Existence of an algebraic closure and splitting fields
---

## Statement

Every [[field|0QA8CHH8MG]] $K$ has an [[algebraic closure|0MCXX29HWY]].

## Remarks

One proof: take a polynomial ring $R$ over $K$ with one variable for each root of each monic irreducible polynomial over $K$. A [[maximal ideal|02HJYT53F7]] of $R$ that contains the relations gives a field $K_1$ in which every polynomial over $K$ splits.
Repeating the step gives fields $K \subseteq K_1 \subseteq K_2 \subseteq \dots$, and their union is an algebraic closure of $K$.
The proof uses Zorn's lemma, through the existence of maximal ideals. The weaker ultrafilter lemma is enough.
For $K = \mathbb{Q}$ or $K = \mathbb{R}$, the complex numbers give a direct proof.

## Explanations

### L1 human

Every field sits inside an algebraically closed field that is algebraic over it.
The general proof needs a form of the axiom of choice, because a field can have very many polynomials.
