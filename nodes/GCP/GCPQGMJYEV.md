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

The sentence $\forall x \, \exists y \, (x < y)$ says that every $x$ has something above it.
If we give a name $f(x)$ to one such element for each $x$, the sentence becomes $\forall x \, (x < f(x))$, with no "there is" left.
Replacing each existential quantifier by a new function symbol in this way is Skolemization, and the result is in Skolem normal form.

Exactly, a [[sentence|DKFGQTRYZE]] is in Skolem normal form when it has the form $\forall x_1 \cdots \forall x_n \, \psi$ with $n \ge 0$ and $\psi$ quantifier-free, as in the [[formal definition|EZ8NCHN7SJ]].
To Skolemize a sentence in [[prenex normal form|CS82V969DE]] with distinct prefix variables, replace each $\exists y$ by a new function symbol applied to the universally quantified variables to the left of $\exists y$, and delete $\exists y$.
The result is not equivalent to the original, but it is [[equisatisfiable|B37TYWXS74]] with it: one has a model exactly when the other has one, by the [[Skolem normal form theorem|Q5H7C57VNH]].

## Motivation

An existential quantifier inside the scope of universal ones hides a dependence.
In $\forall x \, \exists y \, R(x, y)$ the choice of $y$ depends on $x$, and a function symbol makes the dependence visible, as in $\forall x \, R(x, f(x))$.
Universal sentences are simpler than general ones: they stay true in substructures, and their instances are quantifier-free.
So Skolemization turns questions of satisfiability into questions about universal sentences over a larger [[signature|WDVVEYD6AT]].

This trade is the starting point of [[Herbrand's theorem|VZ21F10WRS]] and of resolution theorem proving, where a computer searches for a contradiction among quantifier-free instances.
It also gives a short proof of the downward Löwenheim-Skolem theorem.

## Notation

The Skolem form of $\varphi$ is written $\varphi^S$, $\varphi_S$ or $\operatorname{Sk}(\varphi)$, and its signature $\sigma^S$.
The new function symbols are Skolem functions, and new constant symbols (arity $0$) are Skolem constants.
Some books reserve "Skolem normal form" for the result of Skolemization, and others use it for any universal prenex sentence.

## Remarks

### The rule for arguments

The arguments of a Skolem function are exactly the universally quantified variables to the left of its $\exists$.
In $\exists x \, \forall y \, R(x, y)$ nothing stands to the left of $\exists x$, so $x$ becomes a constant $c$, and the Skolem form is $\forall y \, R(c, y)$.
In [[a sentence with alternating quantifiers|PNDDPZXEW9]],
$$\forall x \, \exists y \, \forall z \, \exists w \, R(x, y, z, w) \quad \text{becomes} \quad \forall x \, \forall z \, R\big( x, f(x), z, g(x, z) \big).$$
The witness $y$ is chosen before $z$ is known, so $f$ takes only $x$.
The witness $w$ comes after both $x$ and $z$, so $g$ takes both.

### Skolem functions you already know

For the group axioms in the signature $\{ \cdot \}$, Skolemization of
$$\exists e \, \forall x \, \exists y \, (e \cdot x = x \land x \cdot e = x \land x \cdot y = e \land y \cdot x = e)$$
introduces a constant for $e$ and a unary function for $y$.
In every group these are forced to be the identity and the inverse map, as worked out in [[Skolem functions for the group axioms|WPZWBJ8FN4]].
For the density axiom of $(\mathbb{Q}, <)$ the Skolem function can be the midpoint $(x + y)/2$, but any point between $x$ and $y$ would do.

### What Skolemization does not keep

Skolemization keeps satisfiability, not meaning.
The Skolem form always implies the original sentence, because the named witness is a witness.
The converse fails, as [[a sentence and its Skolem form are not logically equivalent|BCTD7FZTSK]] shows: in a structure where $f$ is read badly, $\forall x \, \exists y \, R(x, y)$ is true and $\forall x \, R(x, f(x))$ is false.
A sentence that is not prenex, such as $\forall x \, (P(x) \to \forall y \, R(x, y))$, is not in Skolem normal form even though all its quantifiers are universal; its prenex form $\forall x \, \forall y \, (P(x) \to R(x, y))$ is.
Skolem normal form is defined for sentences, so $\forall y \, R(x, y)$, with $x$ free, does not qualify either.

### First properties

A sentence and its Skolem form are equisatisfiable.
Every model of the original sentence expands to a model of the Skolem form on the same domain, by choosing a witness for each tuple of arguments; in general this choice uses the axiom of choice.
The number of new symbols equals the number of existential quantifiers in the prefix.

### Watch out

The first slip is to give a Skolem function every universal variable, also those to the right.
In $\forall x \, \exists y \, \forall z \, R(x, y, z)$ the witness $y$ becomes $f(x)$, not $f(x, z)$; with $f(x, z)$ the sentence would become $\forall x \, \forall z \, \exists y \, R(x, y, z)$, which is weaker.
The second slip is to reuse an old symbol: each Skolem symbol must be new to the signature.
The third slip is to Skolemize before going to prenex form.
In $\neg \exists y \, P(y)$ the $\exists$ is really a $\forall$, since the formula is $\forall y \, \neg P(y)$, and it gets no Skolem function.

### History

Skolem introduced the functions now named after him in 1920, in his proof of Löwenheim's theorem on countable models.
Herbrand used them in his thesis of 1930 to reduce first-order provability to propositional questions.
Robinson's resolution method of 1965 made Skolemization a standard step in automated theorem proving.

### Try it

Skolemize $\exists u \, \forall x \, \exists y \, \forall z \, R(u, x, y, z)$.
The answer is $\forall x \, \forall z \, R(c, x, g(x), z)$, with a new constant $c$ and a new unary $g$.

Skolemize $\forall x \, \forall y \, \exists z \, (x + z = y)$, and name a Skolem function in $(\mathbb{Z}, +)$.
The Skolem form is $\forall x \, \forall y \, (x + h(x, y) = y)$, and $h(x, y) = y - x$ works.

## Explanations

### L1 human

The sentence "every person has a mother" says that for each person there is someone.
Choose a mother for each person, and write $m(x)$ for the mother of $x$.
Then the sentence becomes "every person $x$ has $m(x)$ as a mother", which has no "there is".
The new symbol $m$ is a Skolem function.

### L2 human

We Skolemize the density axiom of dense orders:
$$\forall x \, \forall y \, \big( x < y \to \exists z \, (x < z \land z < y) \big).$$
It is not prenex, because $\exists z$ sits in the consequent.
Since $z$ is not free in $x < y$, the quantifier moves out unchanged:
$$\forall x \, \forall y \, \exists z \, \big( x < y \to (x < z \land z < y) \big).$$
The $\exists z$ comes after $\forall x$ and $\forall y$, so $z$ becomes $m(x, y)$ for a new binary symbol $m$:
$$\forall x \, \forall y \, \big( x < y \to (x < m(x, y) \land m(x, y) < y) \big).$$
Check in $(\mathbb{Q}, <)$ with $m(x, y) = (x + y)/2$: if $x < y$, then $x < (x + y)/2 < y$.
The typical use is in resolution, where the matrix is next put in clause form.
Watch out that the Skolem function need not be unique, since any point between $x$ and $y$ works.

### L3 human

Skolem functions are the strategies of the existential player in the evaluation game of a prenex sentence.
In a model of a theory with built-in Skolem functions, the closure of any nonempty set under the functions is an elementary substructure.
This gives the downward Löwenheim-Skolem theorem, and it is a tool for Ehrenfeucht-Mostowski models built from indiscernibles.
Adding Skolem functions with their defining axioms is a conservative extension: a sentence of the old signature that follows from the new theory already follows from the old one.
The dual Herbrand form, with function symbols for the universal quantifiers, keeps validity instead of satisfiability.
