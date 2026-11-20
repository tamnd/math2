---
tag: YG62F8YC0P
kind: concept
name: Pavelka logic
aliases: [pavelka-logic, rational-pavelka-logic, evaluated-syntax]
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
uses: [NFCEM44XYH, JQ713VVD0G]
sources:
  - url: https://en.wikipedia.org/wiki/Fuzzy_logic
    locator: Propositional fuzzy logics
  - url: https://en.wikipedia.org/wiki/T-norm_fuzzy_logics
    locator: Logical language
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 3. Łukasiewicz logic; 5. Other notable fuzzy logics; Bibliography
  - book: isbn:9780792352389
---

## Summary

*Pavelka logic* is fuzzy logic with graded consequence: premises and conclusions carry degrees in $[0, 1]$, not only the value "fully true".
Wikipedia calls it fuzzy logic with evaluated syntax, EVŁ, and states that its axiomatization comes from [[Łukasiewicz logic|NFCEM44XYH]].
Hájek's book gives a simpler form, *rational Pavelka logic* RPL: Łukasiewicz logic with a truth constant $\overline{r}$ for each rational $r \in [0, 1]$.
In RPL the pair "$\varphi$ to degree at least $r$" is the formula $\overline{r} \to \varphi$.
Pavelka-style completeness says that the provability degree of a formula equals its truth degree.

## Motivation

Ordinary consequence in fuzzy logic only transmits the value $1$.
But a vague premise is often true only to a degree, and a reasoner wants a degree for the conclusion.
Graded consequence answers: from premises with degrees, find the best lower bound for the degree of the conclusion.
Truth constants let the logic state such bounds inside its own language.

## Notation

A truth constant is written $\overline{r}$, with value $r$ under every evaluation.
The *truth degree* of $\varphi$ in a theory $T$ is $\lVert \varphi \rVert_T = \inf \set{e(\varphi) : e \text{ a model of } T}$.
The *provability degree* is $\lvert \varphi \rvert_T = \sup \set{r : T \vdash \overline{r} \to \varphi}$.
Strong conjunction is $\odot$, as elsewhere in this sub-area; Wikipedia writes $\&$ in the bookkeeping axioms.

## Remarks

### Examples

1. [[Graded modus ponens|820H41656Q]]: from $\varphi$ to degree $0.7$ and $\varphi \to \psi$ to degree $0.8$ follows $\psi$ to degree $0.7 \odot 0.8 = 0.5$.
2. [[Excluded middle has degree one half|NPTZAWBB8A]]: in the empty theory, $p \lor \neg p$ has truth degree $\tfrac12$.
3. A bookkeeping instance: $\overline{0.7} \odot \overline{0.8} \leftrightarrow \overline{0.5}$ is an axiom, since $\max(0, 0.7 + 0.8 - 1) = 0.5$.

### Non-examples

1. [[The minimum rule is unsound|KYG8T7KQQ9]]: in Łukasiewicz semantics, $\psi$ need not have degree $\min(0.7, 0.8)$.
2. Every graded modus ponens with a bound above $r \odot s$ is unsound, for example the product bound $0.7 \cdot 0.8 = 0.56 > 0.5$.

### Basic properties

1. RPL is Łukasiewicz logic plus bookkeeping axioms such as $(\overline{r} \odot \overline{s}) \leftrightarrow \overline{r \odot s}$ and $(\overline{r} \to \overline{s}) \leftrightarrow \overline{r \Rightarrow s}$, with $r \Rightarrow s = \min(1, 1 - r + s)$.
2. Rational constants suffice because the Łukasiewicz operations map rationals to rationals.
3. Pavelka-style completeness: $\lvert \varphi \rvert_T = \lVert \varphi \rVert_T$ for every theory $T$ and formula $\varphi$.
4. The degree $\lvert \varphi \rvert_T$ is a supremum, and it need not be attained by a single proof.
   For $T = \set{\overline{r} \to p : r \in \mathbb{Q}, r < \tfrac{\sqrt2}{2}}$, the truth degree of $p$ is the irrational number $\tfrac{\sqrt2}{2}$, and every constant is rational.
5. Wikipedia states that a generalization of Gödel's completeness theorem is provable in EVŁ.

### History

Wikipedia calls fuzzy logic with evaluated syntax "Pavelka's logic".
SEP cites Pavelka's papers "On Fuzzy Logic I, II, and III" of 1979.
Hájek's 1998 book presents rational Pavelka logic, and Wikipedia cites this book for the bookkeeping axioms.

### Common errors

1. Reading $\overline{r} \to \varphi$ as "$\varphi$ has value exactly $r$". It says that the value of $\varphi$ is at least $r$.
2. Combining degrees by $\min$. The sound combination for modus ponens is the Łukasiewicz t-norm $\odot$.
3. Expecting a single proof to reach the provability degree. The degree is a supremum over all proofs.

## Explanations

### L1 human

Pavelka logic attaches a number to each statement: how true we know it to be, at least.
Rules then compute numbers for conclusions.
The completeness theorem says these computed numbers are the best possible.

### L2 human

1. Write a graded premise "$\varphi$ to degree $r$" as $\overline{r} \to \varphi$.
2. Use modus ponens and the bookkeeping axioms to derive $\overline{s} \to \psi$.
3. The largest such $s$, over all derivations, is the provability degree of $\psi$.

A trap: the bound $s$ from one derivation can be below the truth degree; only the supremum is equal to it.

### L3 human

Pavelka-style completeness is a statement about suprema of degrees, and the continuity of the implication makes such suprema behave well.
SEP notes that Łukasiewicz logic is the only t-norm based fuzzy logic whose connectives are all continuous functions.
SEP lists truth constants $\overline{r}$ for rational $r$ among the connectives often added to fuzzy logics.
