---
tag: 2CHENV4DCC
kind: definition
name: Well-formed formula
msc: [03B10, 03B05]
defines: HYJ10AF6RT
uses: [WDVVEYD6AT, 6D3WA7N2W4, QS0XVAN9BG]
sources:
  - url: https://en.wikipedia.org/wiki/Well-formed_formula
---

## Definition

Let $\sigma$ be a [[signature|WDVVEYD6AT]] and $V$ a set of variables.
The set of first-order *formulas* over $\sigma$ is the smallest set of strings such that:

1. if $t_1$ and $t_2$ are [[terms|6D3WA7N2W4]], then $t_1 = t_2$ is a formula;
2. if $R$ is a relation symbol of arity $n$ and $t_1, \dots, t_n$ are terms, then $R(t_1, \dots, t_n)$ is a formula;
3. if $\varphi$ and $\psi$ are formulas, then $\neg \varphi$, $(\varphi \land \psi)$, $(\varphi \lor \psi)$, $(\varphi \to \psi)$ and $(\varphi \leftrightarrow \psi)$ are formulas;
4. if $\varphi$ is a formula and $x \in V$, then $\forall x \, \varphi$ and $\exists x \, \varphi$ are formulas.

The formulas from clauses 1 and 2 are the *atomic formulas*.

## Remarks

In the signature of ordered sets, $\forall x \, \exists y \, (x < y)$ is a formula.
Here $x < y$ is atomic by clause 2, $\exists y \, (x < y)$ follows by clause 4, and then $\forall x$ by clause 4 again.
The string $\forall x \, (x \land y)$ is not a formula: $x$ and $y$ are terms, not formulas, so clause 3 does not apply to them.
In propositional logic the formulas are built from variables by clause 3 alone.
The [[connectives|QS0XVAN9BG]] used vary between books, since some are definable from others.
In Mathlib formulas with bounded variables are `FirstOrder.Language.BoundedFormula`.
