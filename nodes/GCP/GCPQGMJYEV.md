---
tag: GCPQGMJYEV
kind: concept
name: Skolem normal form
aliases: [skolemization, skolem-function]
msc: ["03B10", "03C07"]
topics: [PSRDJXRW53]
audience: ug2
uses: [CS82V969DE, DKFGQTRYZE, WDVVEYD6AT, B37TYWXS74]
sources:
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Skolem_normal_form
    locator: Examples
same_as:
  wikidata: Q1090524
  wikipedia: Skolem normal form
---

## Summary

A sentence is in Skolem normal form when it is in [[prenex normal form|CS82V969DE]] and has only universal quantifiers.
Every first-order sentence can be turned into one in Skolem normal form by replacing each existential quantifier with a new function symbol.
The new sentence is not equivalent to the old one, but it is satisfiable exactly when the old one is, by the [[Skolem normal form theorem|Q5H7C57VNH]].
This makes Skolem normal form the starting point of [[Herbrand's theorem|VZ21F10WRS]] and of resolution theorem proving.

## Motivation

An existential quantifier inside the scope of universal ones hides a dependence: in $\forall x \, \exists y \, R(x, y)$ the $y$ depends on $x$.
A function symbol $f$ makes the dependence explicit, as in $\forall x \, R(x, f(x))$.
Universal sentences are simpler than general ones.
They are preserved in substructures, and their instances are quantifier-free.
So Skolemization reduces questions of satisfiability to questions about universal sentences over a larger [[signature|WDVVEYD6AT]].

## Notation

1. The Skolem form of $\varphi$ is written $\varphi^S$, $\varphi_S$ or $\operatorname{Sk}(\varphi)$. Its signature is $\sigma^S$.
2. The new symbols are Skolem functions, and the new constants are Skolem constants.
3. In "$\exists y$ becomes $f(x_1, \dots, x_k)$", the arguments $x_1, \dots, x_k$ are the universal variables to the left of $\exists y$.

## Remarks

### Examples

1. $\forall x \, \exists y \, R(x, y)$ has the Skolem form $\forall x \, R(x, f(x))$.
2. $\exists x \, \forall y \, R(x, y)$ has the Skolem form $\forall y \, R(c, y)$ with a Skolem constant $c$.
3. [[Alternating quantifiers|PNDDPZXEW9]]: $\forall x \, \exists y \, \forall z \, \exists w \, R(x, y, z, w)$ has the Skolem form $\forall x \, \forall z \, R(x, f(x), z, g(x, z))$.
4. [[Skolem functions for the group axioms|WPZWBJ8FN4]]: the axiom of inverses gives a Skolem function that is the inverse map.

### Non-examples

1. [[A sentence and its Skolem form|BCTD7FZTSK]]: $\forall x \, \exists y \, R(x, y)$ is not in Skolem normal form, and it is not equivalent to its Skolem form.
2. $\forall x \, (P(x) \to \forall y \, R(x, y))$ has only universal quantifiers, but it is not prenex, so it is not in Skolem normal form. Its prenex form $\forall x \, \forall y \, (P(x) \to R(x, y))$ is.
3. A formula with free variables, such as $\forall y \, R(x, y)$, is not in Skolem normal form, which is defined for [[sentences|DKFGQTRYZE]].

### Basic properties

1. The Skolem form implies the original sentence, but not conversely.
2. A sentence and its Skolem form are [[equisatisfiable|B37TYWXS74]]: one has a model exactly when the other has one.
3. Each model of the original sentence expands to a model of the Skolem form on the same domain, using the axiom of choice.
4. The number of Skolem symbols equals the number of existential quantifiers in the prefix.

### History

Skolem introduced Skolem functions in 1920, in his proof of the theorem of Löwenheim on countable models.
Herbrand used them in 1930 to reduce first-order provability to propositional tautologies.
Robinson's resolution method of 1965 made Skolemization a standard step in automated theorem proving.

### Common errors

1. A student gives a Skolem function all universal variables, also those to the right. In $\forall x \, \exists y \, \forall z \, R(x, y, z)$, the witness $y$ becomes $f(x)$, not $f(x, z)$.
2. A student reuses a symbol that is already in the signature. Each Skolem symbol must be new.
3. A student Skolemizes a formula that is not in prenex form. An $\exists$ on the left of $\to$ or under $\neg$ is really a $\forall$.

## Explanations

### L1 human

The sentence "for every $x$ there is a $y$ with $R(x, y)$" says that a suitable $y$ exists for each $x$.
Choose such a $y$ for each $x$ and call it $f(x)$.
Then the sentence becomes "for every $x$, $R(x, f(x))$", which has no "there exists".
The function $f$ is called a Skolem function.

### L2 human

We Skolemize the density axiom $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \land z < y))$ of dense orders.

1. The formula is not prenex. The quantifier $\exists z$ is on the right of $\to$, and $z$ is not free in $x < y$, so it moves out: $\forall x \, \forall y \, \exists z \, (x < y \to (x < z \land z < y))$.
2. The $\exists z$ follows $\forall x$ and $\forall y$. So $z$ becomes $m(x, y)$ for a new binary symbol $m$.
3. The Skolem form is $\forall x \, \forall y \, (x < y \to (x < m(x, y) \land m(x, y) < y))$.
4. In $(\mathbb{Q}, <)$, the midpoint $m(x, y) = (x + y)/2$ is a Skolem function.

The typical use is in resolution, where the matrix is then put in clause form.
A trap: the Skolem function need not be unique.
Any choice of a point between $x$ and $y$ works.

### L3 human

Skolem functions are strategies for the existential player in the evaluation game of a prenex sentence.
In a model of a theory with built-in Skolem functions, the closure of any nonempty set under the functions is an elementary substructure.
This gives the downward Löwenheim-Skolem theorem, and the Ehrenfeucht-Mostowski models generated by indiscernibles.
In proof theory, Skolemization is conservative: a $\sigma$-sentence that follows from the Skolem axioms already follows from the original theory.
The dual Herbrand form, with function symbols for the universal quantifiers, preserves validity instead of satisfiability.
