---
tag: Q85MMH5DEY
kind: definition
name: Sentence
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: ug2
defines: DKFGQTRYZE
uses: [HYJ10AF6RT, ~e71c5bb3, 2CHENV4DCC]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Sentence
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Sentence_(mathematical_logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Definition

Let $\sigma$ be a signature, and let $\operatorname{FV}(\varphi)$ be the set of [[free variables|~e71c5bb3]] of a [[formula|HYJ10AF6RT]] $\varphi$ over $\sigma$.
A *sentence* over $\sigma$ is a formula $\varphi$ over $\sigma$ with $\operatorname{FV}(\varphi) = \emptyset$.

## Notation

1. Sentences are also called *closed formulas*.
2. If $\operatorname{FV}(\varphi) = \set{x_1, \ldots, x_n}$ with $x_1, \ldots, x_n$ distinct, the sentence $\forall x_1 \cdots \forall x_n \, \varphi$ is a *universal closure* of $\varphi$. Different orders of the variables give logically equivalent sentences.
3. In Mathlib, `FirstOrder.Language.Sentence L` is the type of formulas of `L` whose free variables come from the empty type. A formula there is a bounded formula with no unbound numbered variable, so a sentence has no free variable of either kind.

## Remarks

Example: $\forall x \, \exists y \, (x < y)$ is a sentence.
We have $\operatorname{FV}(x < y) = \set{x, y}$, then $\exists y$ removes $y$ and $\forall x$ removes $x$, so the result is $\emptyset$.

Non-example: $\exists y \, (x < y)$ is not a sentence, since $\operatorname{FV}(\exists y \, (x < y)) = \set{x}$.

Equivalently, a formula is a sentence when every occurrence of a variable in it is bound, because $\operatorname{FV}(\varphi)$ is the set of variables with a free occurrence.
The definition gives an algorithm: compute $\operatorname{FV}(\varphi)$ by recursion on $\varphi$ and test whether it is empty.

## Explanations

### L1 human

A sentence is a formula in which no letter is left open.
Each letter is tied to a "for all" or a "there exists".
"For every $x$ there is a $y$ with $x < y$" is a sentence.
"There is a $y$ with $x < y$" is not, because $x$ is left open.

### L2 human

We check that the universal closure of $\varphi = (x \cdot y = y \cdot x)$ is a sentence.

1. $\operatorname{FV}(\varphi) = \operatorname{Var}(x \cdot y) \cup \operatorname{Var}(y \cdot x) = \set{x, y}$.
2. $\operatorname{FV}(\forall y \, \varphi) = \set{x, y} \setminus \set{y} = \set{x}$.
3. $\operatorname{FV}(\forall x \, \forall y \, \varphi) = \set{x} \setminus \set{x} = \emptyset$.

The typical use of the definition is the check that the axioms of a theory are sentences, as for the commutative law here.
The trap: $\forall x \, \varphi$ alone is not a sentence, because each free variable needs its own quantifier.
