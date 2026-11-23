---
tag: Q85MMH5DEY
kind: definition
name: Sentence
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: ug2
defines: DKFGQTRYZE
uses: [HYJ10AF6RT, Y3FZTH5158, 2CHENV4DCC]
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

A sentence is a formula in which no variable is free.

Let $\sigma$ be a signature, and let $\operatorname{FV}(\varphi)$ be the set of [[free variables|Y3FZTH5158]] of a [[formula|HYJ10AF6RT]] $\varphi$ over $\sigma$.
A *sentence* over $\sigma$ is a formula $\varphi$ over $\sigma$ with $\operatorname{FV}(\varphi) = \emptyset$.

## Notation

Sentences are also called *closed formulas*.
If $\operatorname{FV}(\varphi) = \{ x_1, \ldots, x_n \}$ with $x_1, \ldots, x_n$ distinct, the sentence $\forall x_1 \cdots \forall x_n \, \varphi$ is a *universal closure* of $\varphi$, and different orders of the variables give logically equivalent sentences.
In Mathlib, `FirstOrder.Language.Sentence L` is the type of formulas of `L` whose free variables come from the empty type.
A formula there is a bounded formula with no unbound numbered variable, so a sentence has no free variable of either kind.

## Remarks

The definition has one condition, and it is a syntactic one: we compute $\operatorname{FV}(\varphi)$ by recursion on $\varphi$ and test whether it is empty.
So deciding whether a string is a sentence is a mechanical check that needs no structure.

For example, $\forall x \, \exists y \, (x < y)$ is a sentence.
We have $\operatorname{FV}(x < y) = \{ x, y \}$, then $\exists y$ removes $y$ and $\forall x$ removes $x$, which leaves $\emptyset$.

For a failing case, $\exists y \, (x < y)$ is not a sentence, since $\operatorname{FV}(\exists y \, (x < y)) = \{ x \}$.

An equivalent form: a formula is a sentence exactly when every occurrence of a variable in it is bound.
This holds because $\operatorname{FV}(\varphi)$ is the set of variables with a free occurrence.

Watch out: being a sentence is a property of the string, not of a structure.
The formula $\exists y \, (x < y)$ holds for every value of $x$ in $(\mathbb{N}, <)$, but it is still not a sentence.
The concept page [[sentence|DKFGQTRYZE]] has more examples.

## Explanations

### L1 human

A sentence is a formula in which no letter is left open.
Each letter is tied to a "for all" or a "there exists".
"For every $x$ there is a $y$ with $x < y$" is a sentence.
"There is a $y$ with $x < y$" is not, because $x$ is left open.

### L2 human

We check that the universal closure of $\varphi = (x \cdot y = y \cdot x)$ is a sentence.
First, $\operatorname{FV}(\varphi) = \operatorname{Var}(x \cdot y) \cup \operatorname{Var}(y \cdot x) = \{ x, y \}$.
Then $\operatorname{FV}(\forall y \, \varphi) = \{ x, y \} \setminus \{ y \} = \{ x \}$.
Last, $\operatorname{FV}(\forall x \, \forall y \, \varphi) = \{ x \} \setminus \{ x \} = \emptyset$.
So $\forall y \, \varphi$ alone is not a sentence, because each free variable needs its own quantifier.
