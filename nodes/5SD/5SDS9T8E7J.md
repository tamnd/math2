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

A valid sentence is true in every structure, whatever the domain is and whatever the symbols mean.
Compare two sentences.
The sentence $\forall x \, P(x) \to \exists x \, P(x)$, "if everything has $P$, then something has $P$", is true in every structure, because every domain has an element.
The sentence $\forall x \, \exists y \, (x < y)$ is true in $(\mathbb{N}, <)$, but it is false in the one-element structure $(\{0\}, \emptyset)$, where nothing is below anything.
The first sentence is valid, and the second is only true in some structures.

In exact terms, let $L$ be a signature and let $\varphi$ be an $L$-[[formula|HYJ10AF6RT]].
The formula $\varphi$ is valid, written $\models \varphi$, when every $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ and every assignment $s$ in $\mathcal{M}$ give $\mathcal{M} \models \varphi[s]$, in the sense of [[satisfaction|2RBQPV02AS]].
For a sentence $\sigma$, this means that $\sigma$ is [[true|K7XDVK5854]] in every $L$-structure.
Valid formulas are the logical truths of first-order logic: they hold because of their form alone.

## Motivation

Logic studies the forms of correct reasoning.
The truth of $\forall x \, \exists y \, (x < y)$ in $(\mathbb{N}, <)$ is a fact about numbers, not about logic.
The truth of $\forall x \, P(x) \to P(c)$ in every structure is a fact about logic, because it holds whatever $P$ and $c$ mean.
Validity separates the second kind of truth from the first.
The [[completeness theorem|WQ1ZE255SF]] then shows that the valid formulas are exactly the formulas that a standard proof system derives.
So validity is the semantic target of every proof calculus.

## Notation

$\models \varphi$ means that $\varphi$ is valid.
It is the case $\Gamma = \emptyset$ of [[logical consequence|1HK0VYWTV7]] $\Gamma \models \varphi$.
Other names are "universally valid" and "logically true", and Hilbert and Ackermann wrote "allgemeingültig".
In propositional logic the valid formulas are the [[tautologies|05006AJ7DZ]].
An argument with premises $\gamma_1, \ldots, \gamma_n$ and conclusion $\varphi$ is called valid when $\{ \gamma_1, \ldots, \gamma_n \} \models \varphi$, which is a second, related use of the word.
In proof-theoretic semantics, "valid" has a different meaning, tied to rules of inference, and we do not use it here.
Domains of structures are nonempty, and with empty domains allowed, fewer formulas are valid.

## Remarks

### How to prove validity, and how to refute it

To prove that $\varphi$ is valid, fix an arbitrary structure $\mathcal{M}$ and an arbitrary assignment $s$, and show $\mathcal{M} \models \varphi[s]$ with the clauses of satisfaction.
Checking a few structures proves nothing, because there are infinitely many.
To refute validity, one countermodel is enough: one structure and one assignment that do not satisfy $\varphi$.

For example, [[$\exists x \, P(x) \to \forall x \, P(x)$ is not valid|CXT85PC672]].
In the structure with domain $\{0, 1\}$ and $P = \{0\}$, the antecedent is true at the witness $0$, and the consequent is false at $1$.
Check: the implication has a true antecedent and a false consequent, so it is false in this structure.

### Valid formulas

Every instance of a propositional tautology is valid.
For example, $P(x) \vee \neg P(x)$ is valid, because by the clause for $\neg$ exactly one disjunct is satisfied under each assignment.
The sentence $\forall x \, (x = x)$ is valid, because equality is interpreted as identity in every structure.
[[$\forall x \, P(x) \to \exists x \, P(x)$ is valid|ZAW3Q50FT3]] because every domain is nonempty, and it is not an instance of a tautology.
The [[quantifier shift|PR3VZMWQ6B]] $\exists y \, \forall x \, R(x, y) \to \forall x \, \exists y \, R(x, y)$ is valid, because one witness for all $x$ is a witness for each $x$.
The [[drinker paradox|8BMQTZZEWB]] $\exists x \, (D(x) \to \forall y \, D(y))$ is valid, although it sounds false.
The formula $\forall x \, \varphi \to \varphi[t/x]$ is valid when $t$ is substitutable for $x$ in $\varphi$, by the [[substitution lemma|A7S460KHBM]].

### Formulas that are not valid

The converse quantifier shift $\forall x \, \exists y \, R(x, y) \to \exists y \, \forall x \, R(x, y)$ is not valid.
In $(\mathbb{N}, <)$ its antecedent is true, since every number has a larger one, and its consequent is false, since no number is larger than all numbers.
A sentence that is true in one structure, such as $\forall x \, \exists y \, (x < y)$ in $(\mathbb{N}, <)$, need not be valid.
A sentence $\tau$ can be satisfiable without being valid, and $\exists x \, P(x) \to \forall x \, P(x)$ is true in every one-element structure.

### The rules for validity

A formula $\varphi$ is valid exactly when $\neg \varphi$ is not [[satisfiable|QN7M1JCGT9]], because $\mathcal{M} \models \neg \varphi[s]$ holds exactly when $\mathcal{M} \not\models \varphi[s]$.
A formula is valid exactly when its universal closure is valid, by the clause for $\forall$.
If $\varphi$ and $\varphi \to \psi$ are valid, then $\psi$ is valid, by the clause for $\to$, and this is [[modus ponens|0Y0MQYST0M]] for validity.
If $\varphi$ is valid, then $\forall x \, \varphi$ is valid.

For a finite set $\Gamma = \{ \gamma_1, \ldots, \gamma_n \}$, we have $\Gamma \models \varphi$ exactly when $(\gamma_1 \wedge \cdots \wedge \gamma_n) \to \varphi$ is valid, so valid arguments reduce to valid formulas.
Validity does not depend on the signature: if $L \subseteq L'$, an $L$-formula is valid for $L$-structures exactly when it is valid for $L'$-structures, by the [[coincidence lemma|FM580NZ9W6]].

By [[soundness|4A84VHDTHV]] and the completeness theorem, $\varphi$ is valid exactly when $\varphi$ is provable.
So the valid sentences form a computably enumerable set.
By [[Church's theorem|VA6BNNY2YC]], this set is not decidable in general.

### Watch out

Do not confuse validity with truth in one structure.
A sentence true in $(\mathbb{N}, <)$ need not be valid, because validity asks for every structure.

Not every valid formula is an instance of a tautology.
In $\forall x \, P(x) \to \exists x \, P(x)$, the two parts are unrelated atoms for propositional logic, and the validity comes from the quantifiers.

Keep the domain convention in mind.
With empty domains allowed, $\forall x \, P(x) \to \exists x \, P(x)$ and the drinker paradox are not valid.

### History

Hilbert and Ackermann asked in 1928 whether every valid formula of first-order logic is provable in their calculus.
Gödel answered yes in his 1929 dissertation, published in 1930, which proved the completeness theorem.
In 1936 Church and Turing proved that no algorithm decides validity, which solved Hilbert's Entscheidungsproblem in the negative.

### Try it

Is $\exists x \, \forall y \, R(x, y) \to \forall y \, \exists x \, R(x, y)$ valid?
Yes: a single $x$ that works for all $y$ works for each $y$.

Is $\forall x \, (P(x) \vee Q(x)) \to (\forall x \, P(x) \vee \forall x \, Q(x))$ valid?
No: take domain $\{0, 1\}$, $P = \{0\}$ and $Q = \{1\}$, where every element is in $P$ or $Q$, but neither $P$ nor $Q$ is everything.

## Explanations

### L1 human

A valid sentence is true in every possible world, whatever the objects are and whatever the words mean.
"If everything is red, then something is red" is valid, because every world has at least one thing.
"If something is red, then everything is red" is not valid, because a world with one red ball and one blue ball makes it false.
Valid sentences are true because of their logical form, not because of facts about the world.

### L2 human

We prove that $\varphi = \forall x \, (P(x) \wedge Q(x)) \to \forall x \, P(x)$ is valid.

1. Let $\mathcal{M}$ be any structure and $s$ any assignment.
   By the clause for $\to$, it is enough to treat the case $\mathcal{M} \models \forall x \, (P(x) \wedge Q(x))[s]$.
2. Let $a \in M$.
   By the clause for $\forall$, the variant $s[x \mapsto a]$ satisfies $P(x) \wedge Q(x)$, so $a \in P^{\mathcal{M}}$.
3. Since $a$ was arbitrary, $\mathcal{M} \models \forall x \, P(x)[s]$.
4. So $\mathcal{M} \models \varphi[s]$ for all $\mathcal{M}$ and $s$, and $\varphi$ is valid.

The typical use of validity is to justify a logical axiom or a rule of a proof system.
Watch out: the proof must treat an arbitrary structure, while one countermodel is enough to refute validity.

### L3 human

By the completeness theorem, validity is a $\Sigma^0_1$ property of sentences, and by Church's theorem it is not decidable once the signature has a binary relation symbol.
For a signature with only unary relation symbols and no function symbols, validity is decidable, because a satisfiable sentence has a model of bounded finite size.
Trakhtenbrot's theorem of 1950 says that the sentences true in all finite structures do not form a computably enumerable set, so completeness fails for finite model theory.
In second-order logic with full semantics, the valid sentences do not form a computably enumerable set, and no complete proof system exists.
