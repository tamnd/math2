---
tag: GCK0NN60E4
kind: concept
name: Extension by definitions
aliases: [definitional-extension, extension-by-definitions]
msc: ["03B10", "03C07"]
topics: [H8QZY0RZXZ]
audience: grad
uses: [92SWXST1ZM, WDVVEYD6AT, BXBNDHV1HW, N238J43XNE, CY1TXHF6KQ]
sources:
  - wikipedia: en:12219849@r1350903386
    locator: Extension by definition
    note: adopted
    mention: wikipedia://en/12219849
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Extension_by_definition
    locator: lead section
  - book: isbn:9780122384523
  - book: isbn:9781482237726
same_as:
  wikidata: Q5421941
  wikipedia: Extension by definition
inventory: [1W9VJE9M4M]
---

## Summary

Let $T$ be a [[theory|92SWXST1ZM]] in a first-order language $L$, a set of $L$-sentences.
A *definition of a relation symbol* $R$ of arity $n$ is an $L$-formula $\psi(x_1, \ldots, x_n)$, and its defining axiom is $\forall \bar x \, (R(\bar x) \leftrightarrow \psi(\bar x))$.
A *definition of a [[function symbol|BXBNDHV1HW]]* $f$ of arity $n$ is an $L$-formula $\psi(\bar x, y)$ with $T \vdash \forall \bar x \, \exists ! y \, \psi(\bar x, y)$, and its defining axiom is $\forall \bar x \, \forall y \, (f(\bar x) = y \leftrightarrow \psi(\bar x, y))$; a constant symbol is the case $n = 0$.
An *extension by definitions* of $T$ is a theory $T' = T \cup D$ in a language $L' \supseteq L$, where $D$ contains one defining axiom for each symbol of $L' \setminus L$.
Such an extension is [[conservative|N238J43XNE]], and each $L'$-formula is equivalent in $T'$ to an $L$-formula.
This is the logical form of the everyday practice of "introducing notation": the new symbols are abbreviations, so they shorten statements without changing the theory.

## Motivation

Mathematics never works in a bare language.
Set theory has only $\in$, but every book uses $\subseteq$, $\varnothing$, $\cup$ and ordered pairs.
Arithmetic has $0, S, +, \cdot$, but every book uses $\le$, divisibility and primes.
One wants a guarantee that these abbreviations are harmless: they should prove no new fact in the old language, and every statement with them should have a translation without them.
Extensions by definitions give exactly this guarantee, and the condition $T \vdash \forall \bar x \, \exists ! y \, \psi$ explains when a new function symbol is allowed.

## Notation

Definitions are often written $R(\bar x) :\leftrightarrow \psi(\bar x)$ and $f(\bar x) := \text{the unique } y \text{ with } \psi(\bar x, y)$.
The formula $\psi$ is the *definiens* and the new symbol is the *definiendum*.
Several symbols can be defined one after another; then $\psi$ for a later symbol may use earlier new symbols, since each step is again an extension by definitions.
Some books call the result a *definitional extension*.

## Remarks

### Examples

- In [[Peano arithmetic|0QFT7Z76N5]], the [[order relation defined from addition|GBG2F2PWJ3]] is an extension by definitions, and $\forall x \, (0 \le x)$ translates to an arithmetic sentence that PA proves.
- In group theory with the language $\set{\cdot, e}$, the [[inverse function symbol|SZRQRQ5FE9]] can be defined, because each element has exactly one inverse.
- In ZF, the constant $\varnothing$ is defined by $\psi(y) = \forall x \, (x \notin y)$; existence follows from the axioms, and uniqueness from extensionality.
- In ZF, $x \subseteq y$ is defined by $\forall z \, (z \in x \to z \in y)$; no condition is needed for a relation symbol.
- In the theory of fields, a function symbol for the multiplicative inverse cannot be defined by $x \cdot y = 1$, because $0$ has no inverse; the definiens $(x \neq 0 \land x \cdot y = 1) \lor (x = 0 \land y = 0)$ works, with the convention $0^{-1} = 0$.

### Non-examples

- A [[square root symbol over the theory of fields|ZC5ZTHCPKH]] with the axiom $\forall x \, (s(x) \cdot s(x) = x)$ is not an extension by definitions: square roots need not exist, and they are not unique. The extension proves the new $L$-sentence $\exists y \, (y \cdot y = 1 + 1)$.
- Adding a constant $c$ with the axiom $c \neq 0$ to Peano arithmetic is not an extension by definitions, because $c$ has no unique description. It is still conservative, by the [[test with expansions of models|N238J43XNE]], but $c$ cannot be eliminated.
- A definition of $f$ with the axiom $\forall \bar x \, \forall y \, (f(\bar x) = y \leftrightarrow \psi(\bar x, y))$, when $T$ proves existence but not uniqueness, can be inconsistent. In the pure language of equality, with $T = \set{\exists x \, \exists y \, (x \neq y)}$ and $\psi(y) = (y = y)$, the axiom says $\forall y \, (c = y)$.

### Basic properties

The main theorem is that [[extensions by definitions are conservative|QSCE4HJEZ7]], with the following parts.

- Every model of $T$ has exactly one expansion to a model of $T'$: the new symbols must be interpreted by the sets and functions that their definitions [[define|CY1TXHF6KQ]].
- Conservativity: for each $L$-sentence $\sigma$, $T' \vdash \sigma$ exactly when $T \vdash \sigma$.
- Eliminability: for each $L'$-formula $\varphi$ there is an $L$-formula $\varphi^*$ with the same free variables and $T' \vdash \varphi \leftrightarrow \varphi^*$.
- The translation $\varphi \mapsto \varphi^*$ is computable, and the length of $\varphi^*$ can grow quickly when new function symbols are nested.

### History

Definitions as abbreviations are as old as axiomatic mathematics, but the precise theorem needs the modern notion of a first-order theory.
Shoenfield's textbook *Mathematical Logic* of 1967 gives a syntactic proof of eliminability and conservativity.
Beth's definability theorem of 1953 gives the converse: a symbol that is implicitly determined by a theory is explicitly definable.

### Common errors

- Defining a function symbol without proving existence and uniqueness. Without them the extension can be inconsistent or not conservative, as the non-examples show.
- Thinking that the translation $\varphi^*$ replaces $f(t)$ by $\psi(t)$ directly. The function symbol sits inside a term, so the translation needs a new bound variable: $\exists y \, (\psi(t, y) \land \ldots)$.
- Confusing an extension by definitions with any conservative extension. Extensions by definitions are conservative, but most conservative extensions, such as adding a free constant, are not extensions by definitions.

## Explanations

### L1 human

In mathematics we often say "let us call a number even if it is twice a whole number".
The word "even" is new, but it adds no new facts: every sentence with "even" can be rewritten with "twice a whole number" instead.
A definition of this kind is called an extension by definitions.
For a new name of an object, such as "the empty set", we must first check that exactly one object fits the description.

### L2 human

We define a constant $1$ in arithmetic with $0$ and $S$, and translate one sentence.

1. Let $\psi(y)$ be $y = S(0)$. A constant needs $T \vdash \exists ! y \, \psi(y)$, and $\exists ! y \, (y = S(0))$ is a theorem of logic with equality.
2. The defining axiom is $\forall y \, (1 = y \leftrightarrow y = S(0))$.
3. Take the new sentence $\forall x \, (x + 1 = S(x))$. The symbol $1$ occurs once.
4. The translation is $\forall x \, \exists y \, (y = S(0) \land x + y = S(x))$.
5. In PA it is equivalent to $\forall x \, (x + S(0) = S(x))$, which follows from the axioms $x + S(y) = S(x + y)$ and $x + 0 = x$.

The typical use is that a theorem proved with abbreviations is a theorem of the original theory, and its translation can be read off.
A trap is to forget to rename bound variables: if $\psi$ uses a bound variable that also occurs in $\varphi$, the substitution can capture it.

### L3 human

Extensions by definitions are the simplest kind of interpretation between theories: the identity on the domain, with each new symbol interpreted by a formula.
Two theories with a common extension by definitions are called *definitionally equivalent*; for example, Boolean algebras and Boolean rings are definitionally equivalent.
On the model-theoretic side, unique expansion of models is the semantic form of definability, and [[Beth's definability theorem|RJBDSA2ETP]] says that, for first-order logic, unique expansion implies explicit definability.
In categorical logic, the theory and its definitional extensions have equivalent syntactic categories, so they count as the same theory in that framework.
The study of interpretations in general belongs to [[interpretations and foundations|CXRQQZEKF8]] and to [[relative consistency proofs|X3G0RG2GPZ]].
