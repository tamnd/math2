---
tag: FZRMYTQFRR
kind: definition
name: First-order theory
msc: ["03C07", "03B10"]
topics: [PSRDJXRW53]
audience: ug2
defines: 92SWXST1ZM
uses: [WDVVEYD6AT, DKFGQTRYZE]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Theory
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Theory_(mathematical_logic)
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Definition

A theory is a set of sentences, and its models are the structures that make all of them true.

Let $L$ be a [[signature|WDVVEYD6AT]].
An *$L$-theory* is a set $T$ of [[sentences|DKFGQTRYZE]] of first-order logic in the signature $L$.
The elements of $T$ are its *axioms*.
A *model* of $T$ is an $L$-structure in which every sentence of $T$ is true.

## Notation

$\mathcal{M} \models T$ says that $\mathcal{M}$ is a model of $T$, and $\mathrm{Mod}(T)$ is the class of all models of $T$.
A theory is *finite* when it is a finite set, and *finitely axiomatizable* when it has the same models as a finite theory.
In Mathlib, `FirstOrder.Language.Theory L` is defined as `Set L.Sentence`, and `M ⊨ T` is notation for `FirstOrder.Language.Theory.Model`.

## Remarks

The definition asks one thing of each element: it must be a sentence.
It asks nothing of the set as a whole, so a theory may be finite or infinite, and it may even have no model.

For an example, take the signature $\{ \cdot, e, {}^{-1} \}$ and the three sentences
$$\forall x \, \forall y \, \forall z \, ((x \cdot y) \cdot z = x \cdot (y \cdot z)), \quad \forall x \, (x \cdot e = x \land e \cdot x = x), \quad \forall x \, (x \cdot x^{-1} = e \land x^{-1} \cdot x = e).$$
Each has no free variables, so the set of the three is a theory, the theory of groups.

For a non-example, the set $\{ x \cdot e = x \}$ is not a theory, because the variable $x$ is free in its only formula.

Some authors require a theory to be closed under logical consequence; a set of sentences is then called a set of axioms for the theory it generates.
Mendelson's first-order theories are given by a set of proper axioms, which may be formulas with free variables, read as their universal closures.
For an $L$-structure $\mathcal{M}$, the set $\mathrm{Th}(\mathcal{M})$ of all $L$-sentences true in $\mathcal{M}$ is the theory of $\mathcal{M}$.

## Explanations

### L1 human

A theory is any set of sentences.
It may be finite or infinite, and it may even be contradictory.
The theory of groups has three sentences.
Peano arithmetic is a theory with infinitely many sentences, one induction axiom for each formula.

### L2 human

We check that $T = \{ \forall x \, \forall y \, (x < y \to \neg (y < x)) \}$ is a theory in $\{ < \}$ and find two models.

1. The formula has no free variable, since $\forall x$ and $\forall y$ bind both variables.
   So $T$ is a set of sentences.
2. $(\mathbb{N}, <)$ is a model: if $a < b$ then not $b < a$.
3. The empty relation on any nonempty set is a model, since $x < y$ is never true.
4. The relation $\{ (0, 1), (1, 0) \}$ on $\{ 0, 1 \}$ is not a model, because $0 < 1$ and $1 < 0$ both hold.

The typical use of the definition is to separate axioms, a set of sentences, from models, a class of structures.
Watch out: $T$ does not say that $<$ is transitive, so the models of $T$ need not be orders.
