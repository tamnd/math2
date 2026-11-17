---
tag: 5SDS9T8E7J
kind: concept
name: Validity
aliases: [valid-formula, logical-validity, logical-truth]
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
uses: [2RBQPV02AS, 983GZBQYT4, K7XDVK5854, HYJ10AF6RT]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section V
    note: adopted
    mention: wikipedia://en/76765067#ERF9
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Validity_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Validity, satisfiability, and logical consequence
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
inventory: [DE9KBXJX8E]
---

## Summary

Let $L$ be a signature and let $\varphi$ be an $L$-[[formula|HYJ10AF6RT]].
The formula $\varphi$ is valid, or logically valid, written $\models \varphi$, when every $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ and every assignment $s$ in $\mathcal{M}$ give $\mathcal{M} \models \varphi[s]$, in the sense of [[satisfaction|2RBQPV02AS]].
For a sentence $\sigma$, this means that $\sigma$ is [[true|K7XDVK5854]] in every $L$-structure.
Valid formulas are the logical truths of first-order logic: they hold because of their form alone, whatever the domain and the meaning of the non-logical symbols.

## Motivation

Logic studies the forms of correct reasoning.
A sentence such as $\forall x \, \exists y \, (x < y)$ is true in $(\N, <)$, but its truth depends on the numbers, not on logic.
A sentence such as $\forall x \, P(x) \to P(c)$ is true in every structure, whatever $P$ and $c$ mean.
Validity separates the second kind from the first.
The completeness theorem then shows that the valid formulas are exactly the formulas that a proof system derives, so validity is the semantic target of every proof calculus.

## Notation

$\models \varphi$ means that $\varphi$ is valid; it is the case $\Gamma = \emptyset$ of [[logical consequence|1HK0VYWTV7]] $\Gamma \models \varphi$.
Other names are "universally valid" and "logically true"; Hilbert and Ackermann wrote "allgemeingültig".
In propositional logic the valid formulas are the [[tautologies|05006AJ7DZ]].
An argument with premises $\gamma_1, \ldots, \gamma_n$ and conclusion $\varphi$ is called valid when $\set{\gamma_1, \ldots, \gamma_n} \models \varphi$; this is a second, related use of the word.
In proof-theoretic semantics, "valid" has a different meaning, tied to rules of inference; this page does not use it.
This page uses nonempty domains; with empty domains allowed, fewer formulas are valid.

## Remarks

### Examples

1. Every instance of a propositional tautology is valid. For example $P(x) \vee \neg P(x)$ is valid, because the clause for $\neg$ makes exactly one disjunct satisfied.
2. $\forall x \, (x = x)$ is valid, because equality is interpreted as identity in every structure.
3. [[$\forall x \, P(x) \to \exists x \, P(x)$ is valid|~a95b7d53]], because every domain is nonempty.
4. The [[quantifier shift|PR3VZMWQ6B]] $\exists y \, \forall x \, R(x, y) \to \forall x \, \exists y \, R(x, y)$ is valid: one witness for all $x$ is a witness for each $x$.
5. The [[drinker paradox|~c90af64d]] $\exists x \, (D(x) \to \forall y \, D(y))$ is valid.
6. $\forall x \, \varphi \to \varphi[t/x]$ is valid when $t$ is substitutable for $x$ in $\varphi$, by the [[substitution lemma|~761225ef]].

### Non-examples

1. [[$\exists x \, P(x) \to \forall x \, P(x)$ is not valid|~88e5d7c2]]: the condition that fails is truth in every structure, and $(\set{0, 1}, P = \set{0})$ is a countermodel.
2. $\forall x \, \exists y \, (x < y)$ is true in $(\N, <)$ but not valid: it is false in the one-element structure $(\set{0}, \emptyset)$, where $<$ is empty.
3. The converse quantifier shift $\forall x \, \exists y \, R(x, y) \to \exists y \, \forall x \, R(x, y)$ is not valid: in $(\N, <)$ the antecedent is true and the consequent is false.

### Basic properties

1. $\varphi$ is valid if and only if $\neg \varphi$ is not [[satisfiable|QN7M1JCGT9]]. Indeed $\mathcal{M} \models \neg \varphi[s]$ holds exactly when $\mathcal{M} \not\models \varphi[s]$.
2. $\varphi$ is valid if and only if its universal closure is valid, by the clause for $\forall$.
3. If $\varphi$ and $\varphi \to \psi$ are valid, then $\psi$ is valid, by the clause for $\to$; this is [[modus ponens|0Y0MQYST0M]] for validity. If $\varphi$ is valid, then $\forall x \, \varphi$ is valid.
4. For finite $\Gamma = \set{\gamma_1, \ldots, \gamma_n}$, $\Gamma \models \varphi$ holds if and only if $(\gamma_1 \wedge \cdots \wedge \gamma_n) \to \varphi$ is valid. So valid arguments reduce to valid formulas.
5. Validity does not depend on the signature: if $L \subseteq L'$, an $L$-formula is valid for $L$-structures if and only if it is valid for $L'$-structures, by the [[coincidence lemma|~7b107606]].
6. By [[soundness|4A84VHDTHV]] and the [[completeness theorem|WQ1ZE255SF]], $\varphi$ is valid if and only if $\varphi$ is provable. So the valid sentences form a computably enumerable set; by [[Church's theorem|VA6BNNY2YC]], this set is not decidable in general.

### History

Hilbert and Ackermann asked in 1928 whether every valid formula of first-order logic is provable in their calculus.
Gödel answered yes in his 1929 dissertation, published in 1930, which proved the completeness theorem.
In 1936 Church and Turing proved that no algorithm decides validity, which solved Hilbert's Entscheidungsproblem in the negative.

### Common errors

- Confusing validity with truth in one structure. A sentence true in $(\N, <)$ need not be valid; validity needs every structure.
- Thinking that every valid formula is an instance of a tautology. The formula $\forall x \, P(x) \to \exists x \, P(x)$ is valid, but propositionally its two parts are unrelated atoms.
- Forgetting the domain convention. With empty domains allowed, $\forall x \, P(x) \to \exists x \, P(x)$ and the drinker paradox are not valid.

## Explanations

### L1 human

A valid sentence is true in every possible world, whatever the objects are and whatever the words mean.
"If everything is red, then something is red" is valid, because every world has at least one thing.
"If something is red, then everything is red" is not valid: a world with one red ball and one blue ball refutes it.
Valid sentences are true because of their logical form, not because of facts about the world.

### L2 human

We prove that $\varphi = \forall x \, (P(x) \wedge Q(x)) \to \forall x \, P(x)$ is valid.

1. Let $\mathcal{M}$ be any structure and $s$ any assignment. By the clause for $\to$, we may assume $\mathcal{M} \models \forall x \, (P(x) \wedge Q(x))[s]$.
2. Let $a \in M$. By the clause for $\forall$, $s[x \mapsto a]$ satisfies $P(x) \wedge Q(x)$, so $a \in P^{\mathcal{M}}$.
3. Since $a$ was arbitrary, $\mathcal{M} \models \forall x \, P(x)[s]$.
4. So $\mathcal{M} \models \varphi[s]$ for all $\mathcal{M}$ and $s$, and $\varphi$ is valid.

The typical use of validity is to justify a logical axiom or a rule of a proof system.
A trap is to prove validity by checking a few structures; a proof must treat an arbitrary structure, while one countermodel suffices to refute validity.

### L3 human

By the completeness theorem, validity is a $\Sigma^0_1$ property of sentences, and by Church's theorem it is not decidable once the signature has a binary relation symbol.
For a signature with only unary relation symbols, validity is decidable, because a satisfiable sentence has a model of bounded finite size.
Trakhtenbrot's theorem (1950) says that validity in all finite structures is not computably enumerable, so completeness fails for finite model theory.
In second-order logic with full semantics, the valid sentences are not computably enumerable, and no complete proof system exists.
