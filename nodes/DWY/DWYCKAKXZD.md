---
tag: DWYCKAKXZD
kind: concept
name: Many-valued logic
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
uses: [09K9MWD2QQ, 5DYNDW9526, 05006AJ7DZ, FCXHSC6Z4R]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 1 Bivalence in question; 2 Beyond two truth values; 4.3 Are many-valued logics actually bivalent?
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
same_as:
  wikidata: Q185502
  wikipedia: Many-valued logic
---

## Summary

Give the sentence "there will be a sea battle tomorrow" the value $\tfrac12$, read "not yet decided", and give its negation the value $1 - \tfrac12 = \tfrac12$ as well.
If "or" takes the larger of two values, then "there will be a sea battle or there will not" also gets only $\tfrac12$, so excluded middle is no longer a law.
A *many-valued logic* is a logic built in this way: you keep truth tables, but the tables run over more than two truth values.

Exactly, as in [[the definition|66NMTCQNQV]], the semantics is a set $V$ of at least three truth values with a truth function on $V$ for each connective.
A nonempty proper subset $D \subseteq V$ of *designated values* plays the role of "true".
A formula $\varphi$ follows from a set $\Gamma$ when every valuation that gives designated values to all members of $\Gamma$ gives a designated value to $\varphi$.
The triple of values, operations and designated set is a [[logical matrix|P7E926JK13]].
The logic is *finitely valued* when $V$ is finite, as in [[Łukasiewicz's three-valued logic|1CE2TGM6MQ]], and *infinite-valued* when $V$ is infinite, as in [[Łukasiewicz logic on the unit interval|NFCEM44XYH]].

## Motivation

Classical [[propositional calculus|09K9MWD2QQ]] rests on [[bivalence|5DYNDW9526]]: every sentence is true or false.
Three kinds of sentence put that in doubt.
A sentence about the open future, such as the sea battle, may have no truth value yet; this was the starting point of Łukasiewicz.
A statement about a partial computation, such as "the program halts with output 0", may be undefined; this led Kleene to a value "undefined".
A vague sentence, such as "Ann is tall", seems true to a degree, so the values form a scale such as $[0, 1]$.

All three answers keep one classical idea: the value of a compound sentence is a function of the values of its parts.
They drop only the restriction to two values.
So a many-valued logic is a laboratory for the question of which classical laws depend on bivalence and which depend only on the tables.
The later pages of the sub-area follow the three motivations: three-valued logics for the future and for partiality, [[first-degree entailment|KXTP4P3GHT]] for conflicting information, and [[fuzzy logics|8DH4QM6AX8]] for degrees of truth.

## Notation

We write $V$ for the set of values, $D$ for the designated values and $\models_M$ for the consequence relation of a matrix $M$.
The values are often numbers: $\{0, \tfrac12, 1\}$ for the three-valued logics and $[0, 1]$ for the infinite-valued ones, with $1$ as "fully true" and $0$ as "fully false".
For the fuzzy logics we write $\odot$ for strong conjunction and $\oplus$ for strong disjunction.
Other books write $\otimes$ or $\&$ for $\odot$, and some use $\&$ for the weak conjunction $\min$, so check the convention before you read a formula.

## Remarks

### A first table

In [[Łukasiewicz's three-valued logic|1CE2TGM6MQ]] $\mathrm{Ł}_3$ the values are $0, \tfrac12, 1$, only $1$ is designated, negation is $1 - x$ and disjunction is $\max$.
Compute $p \lor \neg p$ for each value of $p$:
$$\max(0, 1) = 1, \qquad \max(\tfrac12, \tfrac12) = \tfrac12, \qquad \max(1, 0) = 1.$$
The middle row is not designated, so $p \lor \neg p$ is not a tautology of $\mathrm{Ł}_3$, as [[the worked case|6S872VHF67]] also shows.
Now test $\neg\neg p \to p$ with the implication $x \to y = \min(1, 1 - x + y)$.
Since $\neg\neg x = x$, every row is $\min(1, 1) = 1$, so this classical law survives.
Check: at $p = \tfrac12$ the row is $\tfrac12 \to \tfrac12 = \min(1, 1) = 1$.

### The main families

The three-valued logics differ in their tables and their designated sets.
[[Strong Kleene logic|SZHA10A9X7]] $\mathsf{K}_3$ uses Kleene's tables with $D = \{1\}$ and has no tautologies at all.
[[Weak Kleene logic|BCK5QXQXA6]] makes the middle value infectious.
[[First-degree entailment|KXTP4P3GHT]] uses four values, "true", "false", "both" and "neither", and designates two of them.
[[Post's many-valued logics|YHYSGRE7JV]] use $V = \{0, 1, \dots, m - 1\}$ with a cyclic negation.
The [[fuzzy logics|8DH4QM6AX8]], such as [[Łukasiewicz logic|NFCEM44XYH]] and [[Gödel-Dummett logic|474SGS2N0X]], take $V = [0, 1]$.

### First facts

For a matrix with $n$ values, a formula with $k$ variables has $n^k$ valuations, so tautologies of a finite matrix are decidable by a finite table.
If the tables agree with the classical tables on $\{0, 1\}$, as those of Łukasiewicz and Kleene do, then every tautology of the matrix is a classical [[tautology|05006AJ7DZ]], because the classical valuations are among the many-valued ones.
So these logics are weaker than classical logic, never stronger.
[[Wójcicki's theorem|VWJVAS3VE3]] shows that every structural consequence relation is the logic of some class of matrices.
[[Suszko's reduction|2FQB3NQF8A]] shows the other side of the coin: every such logic is also given by two-valued valuations, which are in general not truth-functional, as [[the case of Ł3|MAYHP6P8NC]] shows.

### What it is not

[[Classical logic|WETMPAHWZV]] is the logic of a four-element matrix, the Boolean algebra $\{0, 1\}^2$ with only $(1, 1)$ designated.
It is still not many-valued, since the two-element matrix gives the same logic.
Intuitionistic logic is not the logic of any finite matrix, as Gödel showed in 1932; it is many-valued only in the broad sense of infinite matrices such as [[Heyting algebras|NG943XNQWH]].
A probability assignment is not a valuation of any matrix, because [[probability is not truth-functional|EVW7FAWM68]].

### Watch out

Do not read $\tfrac12$ as a probability.
Take $p$ with value $\tfrac12$ in $\mathrm{Ł}_3$: then $p \land \neg p$ gets $\min(\tfrac12, \tfrac12) = \tfrac12$, while a probability of $p \land \neg p$ is always $0$.
Do not forget the designated set either.
Kleene's tables with $D = \{1\}$ give $\mathsf{K}_3$, and the same tables with $D = \{\tfrac12, 1\}$ give the logic of paradox, where $p \lor \neg p$ becomes a tautology.
Finally, "a logic with $n$ values" is loose talk: the number of values belongs to a matrix, and one logic can have matrices of several sizes.

### History

Łukasiewicz introduced his three-valued logic in 1920, with future contingents as his motivation.
Post introduced $m$-valued systems with a cyclic negation in 1921 and proved them functionally complete.
Kleene introduced his three-valued tables in 1938 for partial recursive predicates, and presented them again in his 1952 book.
Bochvar published his three-valued logic of meaningless sentences in 1938.
Suszko argued in 1977 that every such logic is two-valued at the level of consequence, the claim now called Suszko's thesis.

### Try it

First, in $\mathrm{Ł}_3$, is $p \to (q \to p)$ a tautology?
Yes: $q \to p \ge p$ always, because $\min(1, 1 - y + x) \ge x$, and $x \to z = 1$ whenever $z \ge x$.

Second, in $\mathrm{Ł}_3$ with $D = \{\tfrac12, 1\}$, is modus ponens valid?
No: take $p = \tfrac12$ and $q = 0$, so that $p \to q = \min(1, \tfrac12) = \tfrac12$ is designated and $p$ is designated, but $q$ is not.

## Explanations

### L1 human

Classical logic has two truth values, true and false.
A many-valued logic allows more, for example "undecided", or a degree of truth between $0$ and $1$.
In Łukasiewicz's three-valued logic the values are $0$, $\tfrac12$ and $1$, and "not $x$" has the value $1 - x$.
If "it will rain tomorrow" has the value $\tfrac12$, then "it will not rain tomorrow" also has the value $\tfrac12$.
The sentence "it will rain or it will not rain" takes the larger value, $\tfrac12$, so it is not fully true and is not a law of this logic.

### L2 human

We test modus ponens, $p, p \to q \models q$, in $\mathrm{Ł}_3$ with $D = \{1\}$.
Take a valuation with $v(p) = 1$ and $v(p \to q) = 1$.
The implication table at $x = 1$ gives
$$v(p \to q) = \min(1, 1 - 1 + v(q)) = v(q),$$
so $v(q) = 1$, which is designated, and the rule is valid.
The same check with $D = \{\tfrac12, 1\}$ fails at $v(p) = \tfrac12$, $v(q) = 0$, as in the second exercise.
This is the typical use of a matrix: a finite search either confirms a law or finds one valuation that refutes it.
The trap is to think that a law holds or fails "in three-valued logic" in general, when the answer depends on the tables and on $D$.

### L3 human

Abstractly, a many-valued logic is a structural consequence relation presented by a matrix, and by [[Wójcicki's theorem|VWJVAS3VE3]] every structural logic has such a presentation.
So "many-valued" is a property of a semantics rather than of a logic, and [[Suszko's reduction|2FQB3NQF8A]] makes the same point from the two-valued side.
The algebras of the matrices are the subject of [[algebraic logic|QYA4H5Y7VR]]: [[MV-algebras|8T4M7RN9AC]] for Łukasiewicz logic, [[Post algebras|RD2A5Z7E2B]] for Post's logics and [[residuated lattices|E337A6WVH3]] for the fuzzy logics.
The [[substructural logics|98QF5J4W16]] and the [[paraconsistent logics|NJB94B39QK]] also often use semantics with more than two values, and the logic of paradox appears there as the dual of $\mathsf{K}_3$.
