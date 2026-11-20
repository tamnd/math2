---
tag: DPMKT2KRB8
kind: concept
name: Independence-friendly logic
aliases: [if-logic, team-semantics]
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

Independence-friendly logic (IF logic) extends [[first-order logic|086QKPF0A6]] by slashed quantifiers $(\exists v / V)$ and $(\forall v / V)$, where $V$ is a finite set of variables.
The formula $(\exists v / V)\, \psi$ reads "there is a $v$, chosen independently of the variables in $V$, such that $\psi$".
Its formulas are built from first-order atomic formulas by $\neg$, $\land$, $\lor$ and slashed quantifiers, and an ordinary quantifier is a slashed quantifier with $V = \emptyset$.
A sentence $\varphi$ is evaluated in a structure $\mathcal{M}$ by a game of imperfect information between a verifier (Eloise) and a falsifier (Abelard).
At $(\exists v / V)$ Eloise chooses $v$ without seeing the current values of the variables in $V$, and at $(\forall v / V)$ Abelard does the same.
The sentence is true if Eloise has a uniform winning strategy, false if Abelard has one, and undetermined otherwise.
IF logic matters because it makes the dependence between variables explicit, and its sentences express exactly the properties of existential second-order logic ($\Sigma^1_1$).

## Motivation

In first-order logic every existential choice may depend on all earlier choices.
The [[branching quantifiers|KMNVEGS34N]] of Henkin showed that other patterns of dependence add expressive power, but their matrix notation is hard to combine with the connectives.
Hintikka and Sandu wanted a linear notation in which each quantifier carries its own list of forbidden information.
The slash does this: $\forall x_1 \exists y_1 \forall x_2 (\exists y_2 / \set{x_1, y_1})\, \varphi$ is the Henkin quantifier written in one line.
The [[game-theoretic semantics|D45Z7HETDA]] of first-order logic then extends without change, except that players may lack information.
This gives one framework for branching readings in natural language, for a self-applied truth predicate, and for the study of dependence and independence.

## Notation

The slash set $V$ lists the hidden variables, as in $(\exists y / \set{x})$, often written $(\exists y / x)$.
Some authors also slash connectives, as in $(\lor / V)$, for a disjunction whose choice must not depend on $V$.
The negation $\neg$ of IF logic is the dual (game) negation: it swaps the roles of the players, and some books write it $\sim$.
For a sentence $\varphi$ and a structure $\mathcal{M}$, we write $\mathcal{M} \models^{+} \varphi$ for truth and $\mathcal{M} \models^{-} \varphi$ for falsity.
Three equivalent semantics exist for sentences: the game semantics, the Skolem semantics, and the team semantics of Hodges, in which formulas are satisfied by sets of assignments, called teams.
Team semantics first appeared for IF logic and was later used for [[dependence logic|DNAPTJ98WD]].

## Remarks

### Examples

- The Henkin quantifier is $\forall x_1 \exists y_1 \forall x_2 (\exists y_2 / \set{x_1, y_1})\, \varphi$. Both $x_1$ and $y_1$ are hidden, because $y_1$ could otherwise carry information about $x_1$.
- Infinity: $\exists c\, \forall x \exists y \forall z (\exists w / \set{x, y})\, ((x = z \leftrightarrow y = w) \land y \neq c)$ is true exactly in the infinite structures. It is the IF form of [[this Henkin sentence|4R3D37KQD8]].
- An undetermined sentence: $\forall x (\exists y / \set{x})\, x = y$ is neither true nor false in any structure with at least two elements; see [[this example|Y3WXJP6FMB]].
- Signalling: $\forall x \exists z (\exists y / \set{x})\, x = y$ is true in every structure, because Eloise copies $x$ into $z$ and reads $z$; see [[this example|5YGHNNRVFW]].

### Non-examples

- "The domain is finite" is not expressed by any IF sentence; see [[this non-example|3EKSGE0HWK]]. So the classical negation of the infinity sentence is not an IF sentence.
- "The order $<$ is a well-order" is not expressed by any IF sentence. Suppose a $\Sigma^1_1$ sentence held exactly in the well-orders. With new constants and the axioms $c_0 > c_1 > c_2 > \cdots$ it stays finitely satisfiable, so the [[compactness theorem|1NR3HAWG9D]] gives an ill-founded model of it.

### Basic properties

- Conservativity: when every slash set is empty, the game is the game of first-order logic, and truth agrees with Tarski's definition.
- Skolem semantics: an IF sentence is true if and only if its Skolem form holds. The Skolem function of $(\exists v / V)$ takes as arguments the variables in scope that are not in $V$. This turns each IF sentence into a $\Sigma^1_1$ sentence, in the full semantics.
- Expressive power: IF sentences and $\Sigma^1_1$ sentences define the same classes of structures. The direction from $\Sigma^1_1$ to IF uses the translation of Enderton and Walkoe into branching quantifiers.
- Excluded middle fails: a sentence $\varphi$ can be undetermined, and then $\varphi \lor \neg \varphi$ is not true.
- Compactness: a set of IF sentences has a model if every finite subset has one. Löwenheim-Skolem: an IF sentence with an infinite model has models of every infinite cardinality.
- Consequence is not compact: some set $T$ of IF sentences implies an IF sentence $\varphi$, while no finite subset of $T$ implies $\varphi$.
- Truth definition: Sandu proved in 1998 that there is an IF formula $\mathrm{TRUE}(x)$ in the language of arithmetic with $\mathbb{N} \models \varphi \iff \mathbb{N} \models \mathrm{TRUE}(\ulcorner \varphi \urcorner)$ for every IF sentence $\varphi$.
- This does not contradict [[Tarski's undefinability theorem|YRV6SYK2BY]]. Tarski's [[liar|KBYY281V8T]] argument needs a sentence that is true exactly when $\mathrm{TRUE}(\ulcorner \lambda \urcorner)$ is not true, and IF logic has no such contradictory negation.
- Väänänen showed in 2001 that the set of valid IF sentences is recursively isomorphic to the set of valid sentences of full [[second-order logic|G6X7SZSNC5]]. So IF logic has no complete proof system.

### History

Jaakko Hintikka and Gabriel Sandu introduced IF logic in 1989, building on Henkin's branching quantifiers of 1959 and on Hintikka's game-theoretic semantics.
Wilfrid Hodges gave a compositional semantics with sets of assignments in 1997, the origin of team semantics.
Hintikka argued in the 1990s that IF logic can define its own truth predicate, and Sandu published a proof for arithmetic in 1998.
Väänänen's later dependence logic replaced slashed quantifiers by dependence atoms and kept the team semantics.

### Common errors

- To hide only the universal variables. In $\forall x \exists z (\exists y / \set{x})$ the variable $z$ can carry the value of $x$, so the slash on $x$ alone does not make $y$ independent of $x$.
- To read $\neg$ as classical negation. The negation of IF logic swaps the players, so $\neg \varphi$ is true only when Abelard has a winning strategy for $\varphi$, and both $\varphi$ and $\neg \varphi$ can fail to be true.
- To evaluate a formula with free variables at a single assignment. Independence is a property of a strategy across many plays, so open formulas need the team semantics, not single assignments.

## Explanations

### L1 human

Ordinary logic is like a game in which the defender of a sentence sees every earlier move.
IF logic adds blindfolds: a slash tells a player which earlier moves are hidden at a given step.
For example, "for every $x$ there is a $y$, chosen blind to $x$, with $y = x$" asks a player to guess a hidden number.
On a set with two numbers, the guesser cannot always win, and the opponent cannot always win either, because the guesser may be lucky.
So the sentence is neither true nor false, and this is a new feature of the logic.
The blindfolds let the logic say things that ordinary logic cannot say, such as "the set is infinite".

### L2 human

We find the Skolem form of $\varphi = \forall x \exists y \forall z (\exists w / \set{x, y})\, \theta$ and read off its meaning.

1. The only variable in scope at $\exists y$ is $x$, and the slash set is empty, so $y = f(x)$.
2. The variables in scope at $(\exists w / \set{x, y})$ are $x$, $y$ and $z$. Removing $x$ and $y$ leaves $z$, so $w = g(z)$.
3. The Skolem form is $\exists f \exists g\, \forall x \forall z\, \theta(x, f(x), z, g(z))$.
4. This is the Skolem form of the Henkin quantifier with $x_1 = x$, $y_1 = y$, $x_2 = z$, $y_2 = w$.

The typical use of the Skolem form is to compare an IF sentence with a $\Sigma^1_1$ sentence, or to prove that a sentence is true by exhibiting functions.
A trap is step 2: the existential variable $y$ must be slashed together with $x$.
With $(\exists w / \set{x})$ only, $w = g(y, z)$ is allowed, and when $f$ is injective, $y$ carries all the information of $x$.

### L3 human

IF logic is one of a family of logics of imperfect information that all capture $\Sigma^1_1$ on sentences: [[branching quantifiers|KMNVEGS34N]], IF logic and [[dependence logic|DNAPTJ98WD]].
Their open formulas are best read in team semantics, where a formula denotes a set of teams, and the definable families of teams were characterized by Kontinen and Väänänen.
The failure of excluded middle and the lack of classical negation place IF logic between first-order logic and full [[second-order logic|G6X7SZSNC5]]: sentence by sentence it is $\Sigma^1_1$, yet its validity problem is as hard as that of second-order logic.
Hintikka proposed IF logic, with its self-applied truth predicate, as a basis for the foundations of mathematics.
Feferman argued against this proposal, on the ground that IF validity is as complex as validity in full second-order logic.
