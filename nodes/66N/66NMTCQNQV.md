---
tag: 66NMTCQNQV
kind: definition
name: Many-valued logic
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
defines: DWYCKAKXZD
uses: [09K9MWD2QQ, 05006AJ7DZ, 0EPAT51DXQ, P0S056MDS7, TFDYXS3K1N]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 3.2 Logical matrices and the designation-based notion of entailment
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
---

## Definition

Fix a propositional language: a set of variables and a finite set $C$ of connectives, each with an arity.
A *many-valued matrix* for $C$ is a triple $M = (V, \set{f_c}_{c \in C}, D)$ with these parts.

1. A set $V$ of truth values with at least three elements.
2. A nonempty proper subset $D \subseteq V$ of designated values.
3. For each $n$-ary connective $c$, a [[function|0EPAT51DXQ]] $f_c \colon V^n \to V$, its truth table.

A valuation is a map $v$ from the variables to $V$.
It extends to all [[formulas|TFDYXS3K1N]] by $v(c(\varphi_1, \dots, \varphi_n)) = f_c(v(\varphi_1), \dots, v(\varphi_n))$.
For a set $\Gamma$ of formulas and a formula $\varphi$, we put $\Gamma \models_M \varphi$ when every valuation $v$ with $v(\gamma) \in D$ for all $\gamma \in \Gamma$ has $v(\varphi) \in D$.
A formula $\varphi$ is a *tautology* of $M$ when $\emptyset \models_M \varphi$.
The *logic* of $M$ is the relation $\models_M$.
A consequence relation is a *many-valued logic* when it is the logic of some many-valued matrix and not the logic of any matrix with two values.
It is *finitely valued* when some such $M$ is finite, and *infinite-valued* when it is given by an infinite $V$, such as $[0, 1]$.

## Notation

Common names are $\mathrm{Ł}_3$, $\mathsf{K}_3$ and $\mathsf{G}_3$ for three-valued logics, and $\mathrm{Ł}_\infty$ or $\mathrm{Ł}$ for Łukasiewicz logic on $[0, 1]$.
Some authors call only the set of tautologies "the logic"; we use the consequence relation, which carries more information.
The general notion, with any number of values, is a [[logical matrix|~d80767f3]].

## Remarks

1. With $V = \set{0, 1}$, $D = \set{1}$ and the usual tables, $\models_M$ is classical consequence of the [[propositional calculus|09K9MWD2QQ]]; clause 1 excludes this two-valued case.
2. Example: [[Łukasiewicz's three-valued logic|~09f1e8d9]] has $V = \set{0, \tfrac12, 1}$, $D = \set{1}$, $\neg x = 1 - x$ and $x \to y = \min(1, 1 - x + y)$. Then $p \to p$ is a tautology, since $\min(1, 1 - x + x) = 1$.
3. Non-example of a tautology: $p \lor \neg p$ with $x \lor y = \max(x, y)$ is a classical [[tautology|05006AJ7DZ]] but not a tautology of $\mathrm{Ł}_3$. The valuation $p \mapsto \tfrac12$ gives $\tfrac12 \notin D$.
4. Two matrices with the same tables and different designated sets give different logics. Kleene's tables with $D = \set{1}$ give $\mathsf{K}_3$, and with $D = \set{\tfrac12, 1}$ they give the logic of paradox; see [[the comparison|~89c152fd]].
5. A logic can be given by a class of matrices instead of one matrix: $\Gamma \models \varphi$ holds when it holds in every matrix of the class.
6. Consequence and tautologies can differ in strength. In [[Strong Kleene logic|SZHA10A9X7]] there are no tautologies, but $p \land q \models p$ holds.

## Explanations

### L1 human

A many-valued logic replaces the two truth values by a larger set and gives a table for each connective on that set.
Some values are marked as "good enough", the designated values.
A formula is a law when it always gets a good value, whatever values its letters get.
An argument is valid when good values for the premises always give a good value for the conclusion.

### L2 human

We check $p, p \to q \models q$ in $\mathrm{Ł}_3$ with $D = \set{1}$.

1. Let $v$ be a valuation with $v(p) = 1$ and $v(p \to q) = 1$.
2. Then $\min(1, 1 - 1 + v(q)) = v(q)$, so $v(p \to q) = v(q)$.
3. Hence $v(q) = 1 \in D$, and modus ponens is valid in $\mathrm{Ł}_3$.

The typical use of the definition is a finite check of all valuations, or a search for one valuation that refutes a law.
A trap: with $D = \set{\tfrac12, 1}$, the same check fails for $v(p) = \tfrac12$ and $v(q) = 0$, since $\tfrac12 \to 0 = \tfrac12$.
