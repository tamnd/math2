---
tag: B20TDZV9WW
kind: statement
role: axiom
name: Naive satisfaction schema
aliases: [unrestricted-satisfaction-schema]
msc: ["03A05", "03C40"]
topics: [6Q4JJ2MMV8]
audience: grad
about: [2RBQPV02AS]
uses: [D8SD54M5PN, MFJXPAF0R0, HYJ10AF6RT, 2RBQPV02AS]
sources:
  - url: https://plato.stanford.edu/entries/self-reference/
    locator: "Self-Reference and Paradox, 1.1 Semantic Paradoxes"
  - url: https://en.wikipedia.org/wiki/Grelling%E2%80%93Nelson_paradox
    locator: Paradox
---

## Statement

Let $\mathcal{L}_{\mathrm{Sat}}$ be the [[language of arithmetic|D8SD54M5PN]] with a new binary predicate $\mathrm{Sat}(x, y)$, read "the formula with code $x$ is true of $y$".
Fix a [[Gödel numbering|MFJXPAF0R0]].
The *naive satisfaction schema* is the set of all sentences
$$\forall y\,\bigl(\mathrm{Sat}(\ulcorner \varphi \urcorner, y) \leftrightarrow \varphi(y)\bigr),$$
where $\varphi(v)$ is any [[formula|HYJ10AF6RT]] of $\mathcal{L}_{\mathrm{Sat}}$ with exactly one free variable $v$, including formulas that contain $\mathrm{Sat}$.
The schema says that $\mathrm{Sat}$ is the [[satisfaction|2RBQPV02AS]] relation for all formulas of $\mathcal{L}_{\mathrm{Sat}}$ with one free variable.

## Remarks

### Why each hypothesis is needed

1. If $\varphi$ ranges only over formulas without $\mathrm{Sat}$, the schema is consistent with $\mathsf{PA}$. The standard model with $\mathrm{Sat}$ read as arithmetical satisfaction is a model.
2. The [[proposition on the inconsistency of the schema|TD48630JFF]] uses the formula $\neg \mathrm{Sat}(v, v)$, which contains $\mathrm{Sat}$.
3. No [[diagonal lemma|3PRW76471J]] is needed: the self-application $\mathrm{Sat}(v, v)$ already gives the paradox.

### Consequences

1. The schema is inconsistent, even with no arithmetic axioms; see the [[proposition|TD48630JFF]].
2. The informal form of the inconsistency is the [[Grelling-Nelson paradox|E1XCM5TEFD]].
3. The schema implies the [[naive truth schema|99XVFR5ZN5]] for sentences of the form $\varphi(\underline{n})$, so it is at least as strong as it.

### Converse

The schema restricted to formulas without $\mathrm{Sat}$ holds in the standard model with the intended reading.
This restriction is the satisfaction form of the first level of the [[Tarskian hierarchy|Z6MCGB0ZFX]].

### Generalizations

The [[naive definability schema|1V2GY31EAB]] is the analogous principle for definability.
In set theory, the analogue is naive comprehension, whose failure is [[Russell's paradox|0HESMMSYEG]].

## Explanations

### L1 human

A formula with one free variable expresses a property of numbers, for example "$v$ is even".
The naive satisfaction schema says that a single predicate tells, for every formula, which numbers have the property it expresses.
It also asks this for formulas that use the predicate itself.
This is the formal form of the claim that every adjective is true or not true of every thing, including of words.

### L2 human

1. Take $\varphi(v) := \exists u\,(v = u + u)$, which expresses "$v$ is even".
2. The instance of the schema is $\forall y\,(\mathrm{Sat}(\ulcorner \varphi \urcorner, y) \leftrightarrow \exists u\,(y = u + u))$.
3. So $\mathrm{Sat}(\ulcorner \varphi \urcorner, \underline{4})$ holds and $\mathrm{Sat}(\ulcorner \varphi \urcorner, \underline{3})$ fails.
4. Now take $\varphi(v) := \neg \mathrm{Sat}(v, v)$. The instance at $y = \ulcorner \varphi \urcorner$ is $\mathrm{Sat}(\ulcorner \varphi \urcorner, \ulcorner \varphi \urcorner) \leftrightarrow \neg \mathrm{Sat}(\ulcorner \varphi \urcorner, \ulcorner \varphi \urcorner)$.

The typical use is as the standard of adequacy for a satisfaction predicate.
The trap is step 4: the code of a formula is a number, so a formula can be applied to its own code.

### L3 human

The schema is the semantic analogue of naive comprehension, with formulas in place of sets and satisfaction in place of membership.
Its failure has the same diagonal form as [[Cantor's diagonal argument|0XCH8QVDCQ]].
