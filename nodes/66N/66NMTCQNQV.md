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

A many-valued logic is the consequence relation of a truth-table semantics with more than two values, which no two-valued semantics can replace.

Fix a propositional language: a set of variables and a finite set $C$ of connectives, each with an arity.
A *many-valued matrix* for $C$ is a triple $M = (V, \{f_c\}_{c \in C}, D)$ with these parts.

1. A set $V$ of truth values with at least three elements.
2. A nonempty proper subset $D \subseteq V$ of designated values.
3. For each $n$-ary connective $c$, a [[function|0EPAT51DXQ]] $f_c \colon V^n \to V$, its truth table.

A valuation is a map $v$ from the variables to $V$.
It extends to all [[formulas|TFDYXS3K1N]] by the rule below.
$$v(c(\varphi_1, \dots, \varphi_n)) = f_c(v(\varphi_1), \dots, v(\varphi_n))$$
For a set $\Gamma$ of formulas and a formula $\varphi$, we put $\Gamma \models_M \varphi$ when every valuation $v$ with $v(\gamma) \in D$ for all $\gamma \in \Gamma$ has $v(\varphi) \in D$.
A formula $\varphi$ is a *tautology* of $M$ when $\emptyset \models_M \varphi$.
The *logic* of $M$ is the relation $\models_M$.
A consequence relation is a *many-valued logic* when it is the logic of some many-valued matrix and not the logic of any matrix with two values.
It is *finitely valued* when some such $M$ is finite, and *infinite-valued* otherwise, as for a matrix on $[0, 1]$ that no finite matrix can replace.

## Notation

Common names are $\mathrm{Ł}_3$, $\mathsf{K}_3$ and $\mathsf{G}_3$ for three-valued logics, and $\mathrm{Ł}_\infty$ or $\mathrm{Ł}$ for Łukasiewicz logic on $[0, 1]$.
Some authors call only the set of tautologies "the logic".
We use the consequence relation, which carries more information, since [[strong Kleene logic|SZHA10A9X7]] has no tautologies but many valid inferences.
The general notion, with any number of values, is a [[logical matrix|P7E926JK13]].

## Remarks

Each clause has a job.
The bound $|V| \ge 3$ in clause 1 rules out the two-element matrix, whose logic with the usual tables is the classical consequence of the [[propositional calculus|09K9MWD2QQ]].
Clause 2 asks for $D$ to be nonempty and proper: with $D = V$ every formula is a tautology, and with $D = \emptyset$ every inference is valid, so in both cases the logic is trivial.
Clause 3 is truth-functionality: the value of a compound depends only on the values of its parts.
The last condition, "not the logic of any two-valued matrix", is needed because a big matrix can hide a classical logic, as [[the four-element Boolean matrix|WETMPAHWZV]] does.

For a small example, take [[Łukasiewicz's three-valued logic|F9NDCFY3GS]] with $V = \{0, \tfrac12, 1\}$, $D = \{1\}$, $\neg x = 1 - x$ and $x \to y = \min(1, 1 - x + y)$.
Then $p \to p$ is a tautology, because each row gives
$$\min(1, 1 - x + x) = 1.$$
But $p \lor \neg p$, with $\lor$ as $\max$, is a classical [[tautology|05006AJ7DZ]] that fails here, since the valuation $p \mapsto \tfrac12$ gives $\max(\tfrac12, \tfrac12) = \tfrac12 \notin D$.

Watch out: the designated set is part of the matrix.
Kleene's tables with $D = \{1\}$ give $\mathsf{K}_3$, and the same tables with $D = \{\tfrac12, 1\}$ give the logic of paradox, as [[the comparison|BJMXHXJ7QQ]] shows.
A logic can also be given by a class of matrices, with $\Gamma \models \varphi$ when the inference holds in every matrix of the class; the [[concept page|DWYCKAKXZD]] uses both forms.

## Explanations

### L1 human

A many-valued logic replaces the two truth values by a larger set and gives a table for each connective on that set.
Some values are marked as "good enough"; these are the designated values.
A formula is a law when it always gets a good value, whatever values its letters get.
An argument is valid when good values for all the premises always give a good value for the conclusion.

### L2 human

We check modus ponens, $p, p \to q \models q$, in $\mathrm{Ł}_3$ with $D = \{1\}$.
Let $v$ be a valuation with $v(p) = 1$ and $v(p \to q) = 1$.
At $x = 1$ the implication table gives
$$v(p \to q) = \min(1, 1 - 1 + v(q)) = v(q),$$
so $v(q) = 1 \in D$ and the rule is valid.
With $D = \{\tfrac12, 1\}$ the check fails at $v(p) = \tfrac12$ and $v(q) = 0$, because then $v(p \to q) = \min(1, \tfrac12) = \tfrac12$ is designated and $v(q)$ is not.
So the typical use of the definition is a finite check of all valuations, and the trap is to change $D$ without checking the rules again.
