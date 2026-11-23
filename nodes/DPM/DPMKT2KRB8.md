---
tag: DPMKT2KRB8
kind: concept
name: Independence-friendly logic
aliases: [if-logic]
msc: ["03B60", "03C80"]
topics: [MDHDYV8QZW]
audience: research
uses: [086QKPF0A6, KMNVEGS34N, D45Z7HETDA, GCPQGMJYEV, G6X7SZSNC5]
sources:
  - wikipedia: en:1974007@r1305487255
    locator: Independence-friendly logic
    note: adopted
    mention: wikipedia://en/1974007
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Semantics
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Model-theoretic properties
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Properties and critique
  - url: https://en.wikipedia.org/wiki/Branching_quantifier
    locator: Definition and properties
same_as:
  wikidata: Q17101558
  wikipedia: Independence-friendly logic
inventory: [9VWHSCKPFF]
---

## Summary

Independence-friendly logic, or IF logic, is first-order logic in which a quantifier may ignore some earlier choices.
It extends [[first-order logic|086QKPF0A6]] by slashed quantifiers $(\exists v / V)$ and $(\forall v / V)$, where $V$ is a finite set of variables.
The formula $(\exists v / V) \, \psi$ reads "there is a $v$, chosen independently of the variables in $V$, such that $\psi$".
For example, the Henkin quantifier becomes one line:
$$\forall x_1 \, \exists y_1 \, \forall x_2 \, (\exists y_2 / \set{x_1, y_1}) \, \varphi.$$

The formulas are built from first-order atomic formulas by $\neg$, $\land$, $\lor$ and slashed quantifiers.
An ordinary quantifier is a slashed quantifier with $V = \emptyset$.
A sentence is evaluated in a structure by a game of imperfect information between a verifier, Eloise, and a falsifier, Abelard.
At $(\exists v / V)$ Eloise chooses $v$ without seeing the values of the variables in $V$, and at $(\forall v / V)$ Abelard does the same.
The sentence is true if Eloise has a winning strategy that respects these limits, false if Abelard has one, and undetermined otherwise.
IF sentences express exactly the properties of existential second-order logic, $\Sigma^1_1$.

## Motivation

In first-order logic every existential choice may depend on all earlier choices.
The [[branching quantifiers|KMNVEGS34N]] of Henkin showed that other patterns of dependence add expressive power.
But their notation is a matrix of quantifiers, and it is hard to combine with the connectives.
Hintikka and Sandu wanted a linear notation in which each quantifier carries its own list of hidden information.
The slash does this, and the [[game-theoretic semantics|D45Z7HETDA]] of first-order logic extends to it with one change: the players may lack information.
This gives one framework for branching readings in natural language, for a truth predicate that applies to its own language, and for the study of dependence and independence.

## Notation

The slash set $V$ lists the hidden variables, as in $(\exists y / \set{x})$, which is often written $(\exists y / x)$.
Some authors also slash connectives: $(\lor / V)$ is a disjunction whose choice must not depend on $V$.
The negation $\neg$ of IF logic is the dual, or game, negation: it swaps the roles of the players, and some books write it $\sim$.
For a sentence $\varphi$ and a structure $\mathcal{M}$, we write $\mathcal{M} \models^{+} \varphi$ for truth and $\mathcal{M} \models^{-} \varphi$ for falsity.

Sentences have three equivalent semantics: the game semantics, the Skolem semantics, and the team semantics of Hodges.
In team semantics a formula is satisfied by a set of assignments, called a team.
Team semantics first appeared for IF logic, and [[dependence logic|DNAPTJ98WD]] took it over later.

## Remarks

### Four sentences to know

The Henkin quantifier is $\forall x_1 \exists y_1 \forall x_2 (\exists y_2 / \set{x_1, y_1}) \, \varphi$.
Both $x_1$ and $y_1$ are hidden, because otherwise $y_1$ could carry information about $x_1$.

The following sentence is true exactly in the infinite structures, as the IF form of [[this Henkin sentence|4R3D37KQD8]]:
$$\exists c \, \forall x \, \exists y \, \forall z \, (\exists w / \set{x, y}) \, \big( (x = z \leftrightarrow y = w) \land y \neq c \big).$$

The sentence $\forall x \, (\exists y / \set{x}) \, x = y$ is neither true nor false in any structure with at least two elements.
Eloise must guess $x$ without seeing it, as [[this example|Y3WXJP6FMB]] shows.

The sentence $\forall x \, \exists z \, (\exists y / \set{x}) \, x = y$ is true in every structure.
Eloise copies $x$ into $z$ and then reads $z$, which is called signaling, as [[this example|5YGHNNRVFW]] shows.

### What it cannot say

No IF sentence says "the domain is finite", as [[this non-example|3EKSGE0HWK]] shows.
So the classical negation of the infinity sentence is not an IF sentence.

No IF sentence says "the order $<$ is a well-order".
Suppose that a $\Sigma^1_1$ sentence held exactly in the well-orders.
Add new constants $c_0, c_1, c_2, \ldots$ and the axioms $c_0 > c_1 > c_2 > \cdots$.
Each finite part of this set has a model, so the [[compactness theorem|1NR3HAWG9D]] gives an ill-founded model of the sentence.

### Skolem functions and expressive power

When every slash set is empty, the game is the game of first-order logic, and truth agrees with Tarski's definition.

In the Skolem semantics, an IF sentence is true if and only if its Skolem form holds.
The Skolem function of $(\exists v / V)$ takes as arguments the variables in scope that are not in $V$.
This turns each IF sentence into a $\Sigma^1_1$ sentence, in the full semantics.
The converse also holds, by the translation of Enderton and Walkoe of $\Sigma^1_1$ into branching quantifiers.
So IF sentences and $\Sigma^1_1$ sentences define the same classes of structures.

Two first-order theorems survive through this translation.
A set of IF sentences has a model if each finite subset has one.
An IF sentence with an infinite model has models of every infinite cardinality, for a countable vocabulary.

Consequence is not compact, however.
Let $T$ contain the first-order sentences "there are at least $n$ elements" for all $n \ge 1$, and let $\varphi$ be the infinity sentence.
Every model of $T$ is infinite, so $T$ implies $\varphi$.
A finite subset of $T$ has a finite model, where $\varphi$ is not true, so no finite subset implies $\varphi$.

### Truth, negation and validity

Excluded middle fails.
A sentence $\varphi$ can be undetermined, and then $\varphi \lor \neg \varphi$ is not true.

Sandu proved in 1998 that arithmetic has an IF truth predicate.
There is an IF formula $\mathrm{TRUE}(x)$ such that $\mathbb{N} \models \varphi$ if and only if $\mathbb{N} \models \mathrm{TRUE}(\ulcorner \varphi \urcorner)$, for every IF sentence $\varphi$.
This does not contradict [[Tarski's undefinability theorem|YRV6SYK2BY]].
Tarski's [[liar|KBYY281V8T]] argument needs a sentence that is true exactly when $\mathrm{TRUE}(\ulcorner \lambda \urcorner)$ is not true.
IF logic has no such contradictory negation.

Väänänen showed that the set of valid IF sentences is recursively isomorphic to the set of valid sentences of full [[second-order logic|G6X7SZSNC5]].
So IF logic has no complete proof system.

### History

Jaakko Hintikka and Gabriel Sandu introduced IF logic in 1989.
They built on the branching quantifiers that Henkin introduced in 1959, and on the game-theoretic semantics of Hintikka.
Wilfrid Hodges gave a compositional semantics with sets of assignments in 1997, and this was the origin of team semantics.
In the 1990s Hintikka argued that IF logic can define its own truth predicate, and Sandu published a proof for arithmetic in 1998.
Väänänen's dependence logic, from his 2007 book "Dependence Logic", replaced slashed quantifiers by dependence atoms and kept the team semantics.

### Watch out

Do not hide only the universal variables.
In $\forall x \, \exists z \, (\exists y / \set{x})$ the variable $z$ can carry the value of $x$, so the slash on $x$ alone does not make $y$ independent of $x$.

Do not read $\neg$ as classical negation.
The negation of IF logic swaps the players, so $\neg \varphi$ is true only when Abelard has a winning strategy for $\varphi$.
Both $\varphi$ and $\neg \varphi$ can fail to be true.

Do not evaluate a formula with free variables at a single assignment.
Independence is a property of a strategy across many plays, so open formulas need the team semantics.

### Try it

Find the Skolem form of $\forall x \, (\exists y / \set{x}) \, x = y$.
The Skolem function of $y$ has no arguments, so the Skolem form is $\exists c \, \forall x \, x = c$, which holds exactly in the one-element structures.

Is $\forall x \, \exists y \, (\exists z / \set{x}) \, z = x$ true in $\set{0, 1}$?
Yes: Eloise plays $y = x$ and then $z = y$, since $y$ is not hidden.

## Explanations

### L1 human

Ordinary logic is like a game in which the defender of a sentence sees every earlier move.
IF logic adds blindfolds: a slash tells a player which earlier moves are hidden at a given step.
For example, "for every $x$ there is a $y$, chosen blind to $x$, with $y = x$" asks a player to guess a hidden number.
On a set with two numbers, the guesser cannot always win.
The opponent cannot always win either, because the guesser may be lucky.
So the sentence is neither true nor false, and this is a new feature of the logic.
The blindfolds let the logic say things that ordinary logic cannot say, such as "the set is infinite".

### L2 human

We find the Skolem form of $\varphi = \forall x \, \exists y \, \forall z \, (\exists w / \set{x, y}) \, \theta$ and read off its meaning.

1. The only variable in scope at $\exists y$ is $x$, and the slash set is empty, so $y = f(x)$.
2. The variables in scope at $(\exists w / \set{x, y})$ are $x$, $y$ and $z$.
   Removing $x$ and $y$ leaves $z$, so $w = g(z)$.
3. So the Skolem form is this sentence:
   $$\exists f \, \exists g \, \forall x \, \forall z \, \theta(x, f(x), z, g(z)).$$
4. This is the Skolem form of the Henkin quantifier, with $x_1 = x$, $y_1 = y$, $x_2 = z$ and $y_2 = w$.

Check: each Skolem function has exactly the arguments of the matching branch of the Henkin quantifier, $f$ with $x_1$ and $g$ with $x_2$.
The typical use of the Skolem form is to compare an IF sentence with a $\Sigma^1_1$ sentence, or to prove a sentence true by giving functions.
Watch out for step 2: the existential variable $y$ must be slashed together with $x$.
With $(\exists w / \set{x})$ alone, $w = g(y, z)$ is allowed, and when $f$ is injective, $y$ carries all the information of $x$.

### L3 human

Three logics of imperfect information capture $\Sigma^1_1$ on sentences: [[branching quantifiers|KMNVEGS34N]], IF logic and [[dependence logic|DNAPTJ98WD]].
Their open formulas are best read in team semantics, where a formula denotes a set of teams.
Kontinen and Väänänen characterized the families of teams that these formulas define.
IF logic lacks excluded middle and classical negation.
Sentence by sentence it is $\Sigma^1_1$, yet its validity problem is as hard as that of full [[second-order logic|G6X7SZSNC5]].
Hintikka proposed IF logic, with its own truth predicate, as a basis for the foundations of mathematics.
Feferman argued against this proposal, because IF validity is as complex as validity in full second-order logic.
