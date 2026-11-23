---
tag: DNAPTJ98WD
kind: concept
name: Dependence logic
aliases: [game-theoretic-semantics-for-dependence-logic, team-logic, team-semantics-for-dependence-logic]
msc: ["03B60", "03C80"]
topics: [MDHDYV8QZW]
audience: research
uses: [086QKPF0A6, 983GZBQYT4, 2RBQPV02AS, G6X7SZSNC5, GCPQGMJYEV]
sources:
  - wikipedia: en:31107554@r1355640834
    locator: Dependence logic
    note: adopted
    mention: wikipedia://en/31107554
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Dependence_logic
    locator: Semantics
  - url: https://en.wikipedia.org/wiki/Dependence_logic
    locator: Dependence logic and second-order logic
  - url: https://en.wikipedia.org/wiki/Dependence_logic
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Dependence_logic
    locator: Variants and extensions
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Semantics
same_as:
  wikidata: Q5260614
  wikipedia: Dependence logic
inventory: [SJA8Y81BP0]
---

## Summary

Dependence logic adds to [[first-order logic|086QKPF0A6]] one new kind of atomic formula, which says that the value of one variable is determined by the values of others.
Look at a table with columns $x$ and $y$ and the three rows $(0, 5)$, $(1, 7)$ and $(0, 5)$.
Whenever two rows agree on $x$, they also agree on $y$, so in this table "$y$ is a function of $x$" is true.
Add the row $(0, 6)$, and the claim becomes false, because the rows $(0, 5)$ and $(0, 6)$ agree on $x$ and not on $y$.
The claim is about the whole table and not about one row, and this is why dependence logic gives truth values to sets of assignments.

In exact terms, a team over a [[structure|983GZBQYT4]] $\mathcal{M}$ is a set $X$ of assignments $s \colon V \to M$, all with the same finite domain $V$ of variables.
The dependence atom $=\!(t_1, \ldots, t_n, t)$ holds in $X$ when any two $s, s' \in X$ that agree on $t_1, \ldots, t_n$ also agree on $t$.
A first-order literal holds in $X$ when every $s \in X$ satisfies it.
Conjunction keeps the team, and $\varphi \lor \psi$ holds in $X$ when $X = Y \cup Z$ with $Y$ satisfying $\varphi$ and $Z$ satisfying $\psi$.
The quantifier $\exists x$ extends each assignment by one value, chosen as a function of the assignment, and $\forall x$ extends each assignment by every value.
A sentence is true in $\mathcal{M}$ when the team $\{ \emptyset \}$, whose only member is the empty assignment, satisfies it.
On sentences, dependence logic has exactly the expressive power of existential [[second-order logic|G6X7SZSNC5]].

## Motivation

In a first-order formula, a variable bound by $\exists$ may depend on every variable bound by an earlier $\forall$.
In $\forall x \, \exists y \, \forall u \, \exists v \, \varphi$, the [[Skolem functions|GCPQGMJYEV]] have the form $y = f(x)$ and $v = g(x, u)$.
First-order logic has no way to say that $v$ depends on $u$ alone.
Branching quantifiers and [[independence-friendly logic|DPMKT2KRB8]] change the quantifiers to express such patterns.

Jouko Väänänen took another route: he left the quantifiers alone and stated the dependence as an atom, as in $\forall x \, \exists y \, \forall u \, \exists v \, (=\!(u, v) \land \varphi)$.
A dependence is not a property of one assignment, because one row of values cannot show that $v$ is a function of $u$.
It is a property of a set of assignments, in the same way that a functional dependency in a database is a property of a whole table.
So the semantics uses teams, and you can picture a team as a table whose columns are the variables and whose rows are the assignments.

## Notation

We write $\mathcal{M} \models_X \varphi$ when the team $X$ satisfies $\varphi$ in $\mathcal{M}$, and $\operatorname{dom}(X)$ for the common domain of its assignments.
For an assignment $s$, a variable $x$ and $a \in M$, the assignment $s(a/x)$ agrees with $s$ except that it sends $x$ to $a$.
For a function $F \colon X \to M$ we put $X[F/x] = \{ s(F(s)/x) : s \in X \}$, and we put $X[M/x] = \{ s(a/x) : s \in X, \ a \in M \}$.
For formulas in negation normal form, the clauses for the connectives and quantifiers are these:

$$\mathcal{M} \models_X \varphi \land \psi \iff \mathcal{M} \models_X \varphi \text{ and } \mathcal{M} \models_X \psi,$$

$$\mathcal{M} \models_X \varphi \lor \psi \iff X = Y \cup Z \text{ for some } Y, Z \text{ with } \mathcal{M} \models_Y \varphi \text{ and } \mathcal{M} \models_Z \psi,$$

$$\mathcal{M} \models_X \exists x \, \varphi \iff \mathcal{M} \models_{X[F/x]} \varphi \text{ for some } F \colon X \to M,$$

$$\mathcal{M} \models_X \forall x \, \varphi \iff \mathcal{M} \models_{X[M/x]} \varphi.$$

Väänänen writes the dependence atom $=\!(t_1, \ldots, t_n, t)$, and other books write $=\!(\bar{t}, t)$ or $\operatorname{dep}(\bar{t}, t)$.
For $n = 0$ it is the constancy atom $=\!(t)$, which says that $t$ has the same value in all assignments of the team.
The logic itself is often written $\mathcal{D}$ or $\mathrm{FO}(=\!(\ldots))$.
Some authors let $F$ choose a nonempty set of values instead of one value, which is the "lax" semantics, and for dependence logic the two versions agree by downward closure.

## Remarks

### A first evaluation

Take the structure with domain $\{0, 1\}$ and only equality, and the sentence $\forall x \, \exists y \, (=\!(y) \land \neg x = y)$.
The clause for $\forall x$ turns $\{ \emptyset \}$ into the team with the two rows $x = 0$ and $x = 1$.
The constancy atom forces one value $c$ of $y$ in both rows, and then the row with $x = c$ fails $\neg x = y$.
So the sentence is false, and it says the same as the first-order $\exists y \, \forall x \, \neg x = y$.
In general $\forall y \, \exists x \, (=\!(x) \land R(x, y))$ is equivalent to $\exists x \, \forall y \, R(x, y)$, because a constant witness is a witness chosen before $y$.

The atom can also express a branching pattern.
The sentence $\forall x \, \exists y \, \forall u \, \exists v \, (=\!(u, v) \land \varphi)$ holds exactly when there are functions $f$ and $g$ with $\varphi(x, f(x), u, g(u))$ for all $x$ and $u$, which is the Henkin quantifier.
In a database with columns "employee" and "salary", the atom $=\!(\text{employee}, \text{salary})$ is the functional dependency "each employee has one salary".
[[Dependence atoms on a four-row team|TYYG5A3RSV]] checks six formulas on one table, row pair by row pair.

### The closure properties

Every formula holds in the empty team, by induction on formulas: each atom holds with no pair to compare, $\emptyset = \emptyset \cup \emptyset$, and $\emptyset[F/x] = \emptyset[M/x] = \emptyset$.
Every formula is downward closed: if $\mathcal{M} \models_X \varphi$ and $Y \subseteq X$, then $\mathcal{M} \models_Y \varphi$.
The induction step for $\exists x$ restricts the function $F$ to $Y$, and the step for $\lor$ intersects both parts of the split with $Y$.

Dependence logic is local: if $\operatorname{dom}(X)$ contains the free variables $\bar{x}$ of $\varphi$, then $\mathcal{M} \models_X \varphi$ holds exactly when $\mathcal{M} \models_{X \restriction \bar{x}} \varphi$ holds.
Independence-friendly logic with Hodges's team semantics does not have this property.
First-order formulas are flat: for $\varphi$ without dependence atoms, $\mathcal{M} \models_X \varphi$ holds exactly when every $s \in X$ satisfies $\varphi$ in the sense of [[Tarski's satisfaction|2RBQPV02AS]].
With $X = \{ \emptyset \}$ this gives conservativity: a first-order sentence is true in dependence logic exactly when it is true in the usual sense.

### Expressive power

Each dependence logic sentence is equivalent to an existential second-order sentence $\exists R_1 \ldots \exists R_k \, \psi$ with $\psi$ first-order, and each such sentence is equivalent to a dependence logic sentence.
Here each $R_i$ ranges over all relations on $M$ of its arity, as in the full semantics.
The translation reads the atoms as Skolem functions with few arguments, and back.
Since existential second-order logic is compact and satisfies the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]] for sentences, so does dependence logic.
By [[Fagin's theorem|BG8Q0BYSQ3]], its sentences define exactly the NP properties of finite structures.

The power is real: [[one sentence expresses infinity|BJMRFG9TV6]] by asking for an injective function that misses a point, and no first-order sentence does that.
The negation of that sentence, "the domain is finite", has no dependence logic sentence, because the class of finite structures is not existential second-order, by compactness.
So dependence logic is not closed under classical negation.
For formulas with free variables, Kontinen and Väänänen showed that a class of teams is defined by a formula exactly when it contains the empty team, is closed under subteams, and is definable in existential second-order logic.

### What it cannot say

The closure properties give a quick test for what lies outside the logic.
The inclusion atom $x \subseteq y$, which says that each value of $x$ in the team is also a value of $y$, holds in the team with rows $(0, 1)$ and $(1, 0)$ and fails in its subteam with the row $(0, 1)$ alone.
So it is not downward closed, and [[no dependence logic formula defines it|FM3EBN81T9]].
The independence atom $x \perp y$ fails downward closure as well.
The team of all four pairs $(x, y) \in \{0, 1\}^2$ satisfies it, but its subteam with the rows $(0, 0)$ and $(1, 1)$ does not, since no row combines $x = 0$ with $y = 1$.

### Inclusion and independence atoms

Inclusion logic adds the atoms $\bar{x} \subseteq \bar{y}$, true in $X$ when each value of $\bar{x}$ in $X$ is also a value of $\bar{y}$ in $X$.
Its formulas are closed under unions of teams, not under subteams.
Independence logic adds the atoms $\bar{x} \perp_{\bar{z}} \bar{y}$.
Such an atom holds in $X$ when for all $s, s' \in X$ with $s(\bar{z}) = s'(\bar{z})$ there is $s'' \in X$ that agrees with $s$ on $\bar{z}\bar{x}$ and with $s'$ on $\bar{y}$.
The dependence atom $=\!(\bar{x}, y)$ is equivalent to $y \perp_{\bar{x}} y$, and on sentences independence logic again equals existential second-order logic.

### Watch out

Do not confuse the empty team $\emptyset$ with the team $\{ \emptyset \}$.
The empty team satisfies every formula, while $\{ \emptyset \}$ is the team that decides the truth of a sentence.

Do not read $\neg$ as classical negation.
Negation is pushed to the atoms, and $\neg =\!(\bar{t}, t)$ holds only in the empty team.
So $=\!(x) \lor \neg =\!(x)$ fails in every team in which $x$ takes two values, and the law of excluded middle fails.

Do not expect $\varphi \lor \varphi$ to be equivalent to $\varphi$.
In the team where $x$ takes the values $0$ and $1$, the formula $=\!(x) \lor =\!(x)$ holds, since each half of the split is constant, but $=\!(x)$ fails.

### History

Wilfrid Hodges introduced team semantics in 1997 as a compositional semantics for independence-friendly logic.
Jouko Väänänen defined dependence logic in his book "Dependence Logic: A New Approach to Independence Friendly Logic" of 2007.
Kontinen and Väänänen characterized the team properties definable by dependence logic formulas in 2009.
Pietro Galliani introduced inclusion logic in 2012, and Erich Grädel and Väänänen introduced independence logic in 2013.
Galliani and Lauri Hella proved in 2013 that inclusion logic has the expressive power of positive greatest fixed point logic on sentences.

### Try it

Does the team with the rows $(x, y) = (0, 1), (1, 1), (2, 1)$ satisfy $=\!(y)$, and does it satisfy $=\!(y, x)$?
It satisfies $=\!(y)$, because $y$ is $1$ in every row, and it fails $=\!(y, x)$, because the rows agree on $y$ but not on $x$.

Is $\forall x \, \exists y \, (=\!(y) \land x = y)$ true in a one-element structure, and in a two-element structure?
It is true in the first, with $y$ equal to the only element, and false in the second, because a constant $y$ misses one value of $x$.

## Explanations

### L1 human

Think of a table with columns $x$ and $y$ and several rows.
The column $y$ depends on the column $x$ when equal entries in $x$ always come with equal entries in $y$.
For the rows $(0, 5)$, $(1, 7)$ and $(0, 5)$ this is true, but if we add the row $(0, 6)$ it is false.
Dependence logic is ordinary logic with one new kind of basic statement: "this column depends on those columns".
Such a statement is about the whole table, so the logic gives truth values to tables, called teams, instead of to single rows.
If we delete rows from a table, a true dependence stays true, and an empty table satisfies every statement.

### L2 human

We evaluate $\varphi_1 = \forall x \, \exists y \, (=\!(x, y) \land \neg x = y)$ in the structure with domain $M = \{0, 1\}$ and only equality.

1. We start from the team $\{ \emptyset \}$, and the clause for $\forall x$ gives the team with the two rows $x = 0$ and $x = 1$.
2. For $\exists y$ we choose $F$ to send the row $x = 0$ to $1$ and the row $x = 1$ to $0$.
   The new team has the rows $(x, y) = (0, 1)$ and $(1, 0)$.
3. The atom $=\!(x, y)$ holds, because the two rows have different values of $x$, so there is no pair to compare.
4. The literal $\neg x = y$ holds in each row, so $\varphi_1$ is true.

Compare $\varphi_2 = \forall x \, \exists y \, (=\!(y) \land \neg x = y)$ from the first evaluation in the remarks, which is false on the same structure.
The typical use of the atoms is this: they fix which earlier variables a chosen value may use.
Watch out: the atom $=\!(x, y)$ adds nothing in $\varphi_1$, since $y$ is chosen after $x$ and may depend on it anyway.
An atom is a real restriction only when it leaves out a variable that comes earlier, as $=\!(y)$ leaves out $x$ in $\varphi_2$.

### L3 human

The equivalence with existential second-order logic is the Skolem normal form read in both directions.
A dependence atom $=\!(\bar{u}, v)$ after the quantifiers says that the Skolem function of $v$ takes only $\bar{u}$ as arguments.
Conversely, a sentence $\exists f \, \psi$ can be coded by universal quantifiers for the arguments of $f$ and existential quantifiers controlled by atoms.
So dependence logic sentences, [[independence-friendly logic|DPMKT2KRB8]] sentences and partially ordered quantifier prefixes before a first-order formula all define the same classes of structures.
Dependence logic differs in that it separates the dependence from the quantifier and has a local, compositional semantics.
The [[game-theoretic semantics|D45Z7HETDA]] behind it is a game of imperfect information, and a team corresponds to a set of positions that a uniform strategy can reach.

Team semantics now carries many atoms from database theory and probability: functional dependence, inclusion, exclusion and conditional independence.
Each atom gives a logic with a typical closure property: closure under subteams for dependence, closure under unions for inclusion, and neither for independence.
The same idea applies to propositional and modal logic, as in modal dependence logic.
On finite structures these logics meet descriptive complexity.
Dependence and independence logic capture NP by Fagin's theorem, and inclusion logic captures PTIME on ordered finite structures through greatest fixed points.
Within the logics beyond first order, dependence logic is the team-semantic form of the existential fragment of second-order logic.
