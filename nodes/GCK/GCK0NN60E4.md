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

An extension by definitions adds new symbols that only abbreviate formulas of the old language, so it changes nothing but the length of statements.
Take arithmetic in the language $\{ 0, S, +, \cdot \}$ and add a relation symbol $\le$ with the axiom $\forall x\, \forall y\, (x \le y \leftrightarrow \exists z\, (x + z = y))$.
The sentence $\forall x\, (0 \le x)$ is new, but it is only a short form of $\forall x\, \exists z\, (0 + z = x)$, and every theorem with $\le$ has such a translation.

Let $T$ be a [[theory|92SWXST1ZM]] in a first-order language $L$; as in [[formal system|439M8B4DY2]], a theory is any set of sentences.
A *definition of a relation symbol* $R$ of arity $n$ is an $L$-formula $\psi(x_1, \ldots, x_n)$, with the defining axiom $\forall \bar x\, (R(\bar x) \leftrightarrow \psi(\bar x))$.
A *definition of a [[function symbol|BXBNDHV1HW]]* $f$ of arity $n$ is an $L$-formula $\psi(\bar x, y)$ with $T \vdash \forall \bar x\, \exists ! y\, \psi(\bar x, y)$, and its defining axiom is $\forall \bar x\, \forall y\, (f(\bar x) = y \leftrightarrow \psi(\bar x, y))$.
A constant symbol is the case $n = 0$.
An *extension by definitions* of $T$ is a theory $T' = T \cup D$ in a language $L' \supseteq L$, where $D$ has exactly one defining axiom for each symbol of $L' \setminus L$.
Such an extension is [[conservative|N238J43XNE]], and each $L'$-formula is equivalent in $T'$ to an $L$-formula.

## Motivation

Mathematics never works in a bare language.
Set theory has only $\in$, but every book uses $\subseteq$, $\varnothing$, $\cup$ and ordered pairs.
Arithmetic has $0, S, +, \cdot$, but every book uses $\le$, divisibility and primes.
We want a guarantee that these abbreviations are harmless: they prove no new fact in the old language, and every statement with them has a translation without them.
Extensions by definitions give exactly this guarantee.
The condition $T \vdash \forall \bar x\, \exists ! y\, \psi$ tells us when a new function symbol is allowed.

## Notation

Definitions are often written $R(\bar x) :\leftrightarrow \psi(\bar x)$ and $f(\bar x) := \text{the unique } y \text{ with } \psi(\bar x, y)$.
The formula $\psi$ is the *definiens*, and the new symbol is the *definiendum*.
We can define several symbols one after another.
Then the definiens of a later symbol may use earlier new symbols, since each step is again an extension by definitions.
Some books call the result a *definitional extension*.

## Remarks

### Definitions in practice

In [[Peano arithmetic|0QFT7Z76N5]], the [[order relation defined from addition|GBG2F2PWJ3]] is an extension by definitions.
In group theory with the language $\{ \cdot, e \}$, the [[inverse function symbol|SZRQRQ5FE9]] can be defined, because each element has exactly one inverse.
In ZF, the constant $\varnothing$ has the definiens $\psi(y) = \forall x\, (x \notin y)$.
The axioms give a set with no elements, and extensionality makes it unique.
In ZF, $x \subseteq y$ has the definiens $\forall z\, (z \in x \to z \in y)$, and a relation symbol needs no condition.
In the theory of fields, the formula $x \cdot y = 1$ does not define a function symbol for the inverse, because $0$ has no inverse.
The definiens $(x \neq 0 \land x \cdot y = 1) \lor (x = 0 \land y = 0)$ works, with the convention $0^{-1} = 0$.

### When a definition fails

A [[square root symbol over the theory of fields|ZC5ZTHCPKH]] with the axiom $\forall x\, (s(x) \cdot s(x) = x)$ is not an extension by definitions.
Square roots need not exist, and they are not unique.
The extension proves the new $L$-sentence $\exists y\, (y \cdot y = 1 + 1)$, which fails in $\mathbb{Q}$.

Adding a constant $c$ with the axiom $c \neq 0$ to Peano arithmetic is not an extension by definitions, because no formula picks out $c$ uniquely.
It is still conservative, by the [[test with expansions of models|N238J43XNE]], but $c$ cannot be eliminated.

Existence without uniqueness can even give an inconsistent theory.
In the pure language of equality, let $T = \{ \exists x\, \exists y\, (x \neq y) \}$ and $\psi(y) = (y = y)$.
The would-be defining axiom of a constant $c$ says $\forall y\, (c = y)$, so it contradicts $T$.

### What a definition guarantees

The main theorem is that [[extensions by definitions are conservative|QSCE4HJEZ7]].
It has three parts.
First, every model of $T$ has exactly one expansion to a model of $T'$, because the new symbols must be read as the sets and functions that their definitions [[define|CY1TXHF6KQ]].
Second, for each $L$-sentence $\sigma$, $T' \vdash \sigma$ exactly when $T \vdash \sigma$.
Third, for each $L'$-formula $\varphi$ there is an $L$-formula $\varphi^*$ with the same free variables and $T' \vdash \varphi \leftrightarrow \varphi^*$.
The translation $\varphi \mapsto \varphi^*$ is computable.
The length of $\varphi^*$ can grow quickly when new function symbols are nested.

### Watch out

A function symbol needs a proof of existence and uniqueness in $T$ before its definition.
Without it the extension can be inconsistent or not conservative, as the failures above show.

The translation does not replace $f(t)$ by $\psi(t)$ directly, because $f(t)$ is a term and $\psi$ is a formula.
It needs a new bound variable: an atomic formula $\alpha$ that contains $f(t)$ becomes $\exists y\, (\psi(t, y) \land \alpha_y)$, where $\alpha_y$ is $\alpha$ with $y$ in place of $f(t)$.

Extensions by definitions are conservative, but most conservative extensions are not extensions by definitions.
Adding a constant with no axioms is an example.

### History

Definitions as abbreviations are as old as axiomatic mathematics, but the precise theorem needs the modern notion of a first-order theory.
Shoenfield's textbook *Mathematical Logic* of 1967 gives a syntactic proof of eliminability and conservativity.
Beth's definability theorem of 1953 gives a converse: a symbol that is implicitly determined by a theory is explicitly definable.

### Try it

In the theory of groups, translate $\forall x\, (i(x) \cdot x = e)$, where $i$ is the inverse symbol with definiens $x \cdot y = e \land y \cdot x = e$.
Answer: $\forall x\, \exists y\, (x \cdot y = e \land y \cdot x = e \land y \cdot x = e)$, which follows from the inverse axiom.

Can we add to the theory of linear orders a constant $m$ with definiens "$y$ is the least element"?
No: the theory does not prove that a least element exists, since the integers form a linear order with no least element.

## Explanations

### L1 human

In mathematics we often say "let us call a number even if it is twice a whole number".
The word "even" is new, but it adds no new facts: every sentence with "even" can be rewritten with "twice a whole number" instead.
A definition of this kind is called an extension by definitions.
For a new name of an object, such as "the empty set", we must first check that exactly one object fits the description.

### L2 human

We define a constant $1$ in arithmetic with $0$ and $S$, and translate one sentence.

1. Let $\psi(y)$ be $y = S(0)$.
   A constant needs $T \vdash \exists ! y\, \psi(y)$, and $\exists ! y\, (y = S(0))$ is a theorem of logic with equality.
2. The defining axiom is $\forall y\, (1 = y \leftrightarrow y = S(0))$.
3. Take the new sentence $\forall x\, (x + 1 = S(x))$, in which the symbol $1$ occurs once.
4. The translation is $\forall x\, \exists y\, (y = S(0) \land x + y = S(x))$.
5. In PA it is equivalent to $\forall x\, (x + S(0) = S(x))$, which follows from the axioms $x + S(y) = S(x + y)$ and $x + 0 = x$.

The typical use is that a theorem proved with abbreviations is a theorem of the original theory, and its translation can be read off.
Watch out for bound variables: if $\psi$ uses a bound variable that also occurs in $\varphi$, rename it before you substitute, or it can capture a variable of $\varphi$.

### L3 human

Extensions by definitions are the simplest kind of interpretation between theories: the identity on the domain, with each new symbol read as a formula.
Two theories with a common extension by definitions are called *definitionally equivalent*; for example, Boolean algebras and Boolean rings are definitionally equivalent.
Unique expansion of models is the semantic form of definability, and [[Beth's definability theorem|RJBDSA2ETP]] says that, for first-order logic, unique expansion implies explicit definability.
In categorical logic, a theory and its definitional extensions have equivalent syntactic categories, so they count as the same theory there.
Interpretations in general belong to [[interpretations and foundations|CXRQQZEKF8]] and to [[relative consistency proofs|X3G0RG2GPZ]].
