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

Dependence logic is [[first-order logic|086QKPF0A6]] with new atomic formulas, the dependence atoms $=\!(t_1, \ldots, t_n, t)$, read "the value of $t$ is determined by the values of $t_1, \ldots, t_n$".
Its formulas are evaluated on teams.
A team over a [[structure|983GZBQYT4]] $\mathcal{M}$ is a set $X$ of assignments $s \colon V \to M$, all with the same finite domain $V$ of variables.
A first-order literal holds in $X$ when every $s \in X$ satisfies it.
The atom $=\!(t_1, \ldots, t_n, t)$ holds in $X$ when any two $s, s' \in X$ that agree on $t_1, \ldots, t_n$ also agree on $t$.
Conjunction keeps the team, and $\varphi \lor \psi$ holds in $X$ when $X = Y \cup Z$ with $Y \models \varphi$ and $Z \models \psi$.
The quantifier $\exists x$ extends each $s$ by a value chosen by a function of $s$, and $\forall x$ extends each $s$ by every value.
A sentence is true in $\mathcal{M}$ when the team $\{\emptyset\}$, whose only member is the empty assignment, satisfies it.
Dependence logic makes the dependence between variables a formula of its own, and on sentences it has exactly the expressive power of existential second-order logic.

## Motivation

In a first-order formula, a variable bound by $\exists$ may depend on every variable bound by an earlier $\forall$.
In $\forall x \, \exists y \, \forall u \, \exists v \, \varphi$, the [[Skolem functions|GCPQGMJYEV]] have the form $y = f(x)$ and $v = g(x, u)$.
First-order logic has no way to say that $v$ depends on $u$ alone.
Branching quantifiers and [[independence-friendly logic|DPMKT2KRB8]] change the quantifiers to express such patterns.
Jouko Väänänen proposed to leave the quantifiers alone and to state the dependence as an atom: $\forall x \, \exists y \, \forall u \, \exists v \, (=\!(u, v) \land \varphi)$.
A dependence is not a property of one assignment, because one row of values cannot show that $v$ is a function of $u$.
It is a property of a set of assignments, as a functional dependency in a database is a property of a whole table.
This is why the semantics uses teams.
A team can be pictured as a table whose columns are the variables and whose rows are the assignments.

## Notation

We write $\mathcal{M} \models_X \varphi$ when the team $X$ satisfies $\varphi$ in $\mathcal{M}$, and $\operatorname{dom}(X)$ for the common domain of its assignments.
For an assignment $s$, a variable $x$ and $a \in M$, the assignment $s(a/x)$ agrees with $s$ except that it sends $x$ to $a$.
For a function $F \colon X \to M$ we put $X[F/x] = \{ s(F(s)/x) : s \in X \}$, and we put $X[M/x] = \{ s(a/x) : s \in X, \ a \in M \}$.
The full clauses, for formulas in negation normal form, are these.

$$\mathcal{M} \models_X \varphi \land \psi \iff \mathcal{M} \models_X \varphi \text{ and } \mathcal{M} \models_X \psi$$

$$\mathcal{M} \models_X \varphi \lor \psi \iff X = Y \cup Z \text{ for some } Y, Z \text{ with } \mathcal{M} \models_Y \varphi \text{ and } \mathcal{M} \models_Z \psi$$

$$\mathcal{M} \models_X \exists x \, \varphi \iff \mathcal{M} \models_{X[F/x]} \varphi \text{ for some } F \colon X \to M$$

$$\mathcal{M} \models_X \forall x \, \varphi \iff \mathcal{M} \models_{X[M/x]} \varphi$$

The dependence atom is written $=\!(t_1, \ldots, t_n, t)$ by Väänänen, and also $=\!(\bar{t}, t)$ or $\operatorname{dep}(\bar{t}, t)$.
For $n = 0$ it is the constancy atom $=\!(t)$, which says that $t$ has the same value in all assignments of the team.
The logic itself is often written $\mathcal{D}$ or $\mathrm{FO}(=\!(\ldots))$.
Some authors let $F$ choose a nonempty set of values instead of one value ("lax" semantics).
For dependence logic the two versions agree, by downward closure.

## Remarks

### Examples

- The team $X = \{ s_1, s_2, s_3 \}$ with $(s_i(x), s_i(y)) = (0, 5), (1, 7), (0, 5)$ satisfies $=\!(x, y)$, because the two rows with $x = 0$ both have $y = 5$. The worked team of [[this example|~dda655e0]] checks every case.
- The sentence $\forall y \, \exists x \, (=\!(x) \land R(x, y))$ is equivalent to $\exists x \, \forall y \, R(x, y)$. The constancy atom forces one value of $x$ for all values of $y$.
- The sentence $\forall x \, \exists y \, \forall u \, \exists v \, (=\!(u, v) \land \varphi)$ expresses the Henkin quantifier: there are functions $f, g$ with $\varphi(x, f(x), u, g(u))$ for all $x, u$.
- One dependence logic sentence says that the domain is infinite: it asks for an injective function that misses a point. [[This example|~7025fbde]] gives the sentence and checks it.
- In a database table with columns "employee" and "salary", the atom $=\!(\text{employee}, \text{salary})$ is the functional dependency "each employee has one salary".

### Non-examples

- The inclusion atom $x \subseteq y$ is not definable in dependence logic. It is not closed under subteams, and every dependence logic formula is; see [[this non-example|~2b375ee1]].
- The property "the domain is finite" is not defined by any dependence logic sentence. Such a sentence would be equivalent to an existential second-order sentence, and the class of finite structures is not of that form, by compactness.
- The independence atom $x \perp y$ fails downward closure: the four-row team of all pairs $(x, y) \in \{0, 1\}^2$ satisfies it, and its subteam $\{(0, 0), (1, 1)\}$ does not.

### Basic properties

- Empty team property: $\mathcal{M} \models_\emptyset \varphi$ for every formula $\varphi$. By induction: each atom holds vacuously, $\emptyset = \emptyset \cup \emptyset$, and $\emptyset[F/x] = \emptyset[M/x] = \emptyset$.
- Downward closure: if $\mathcal{M} \models_X \varphi$ and $Y \subseteq X$, then $\mathcal{M} \models_Y \varphi$. For $\exists x$ one restricts the function $F$ to $Y$; for $\lor$ one intersects both parts with $Y$.
- Locality: if $\operatorname{dom}(X)$ contains the free variables $\bar{x}$ of $\varphi$, then $\mathcal{M} \models_X \varphi$ if and only if $\mathcal{M} \models_{X \restriction \bar{x}} \varphi$. Independence-friendly logic with Hodges's team semantics does not have this property.
- Flatness of first-order formulas: for $\varphi$ without dependence atoms, $\mathcal{M} \models_X \varphi$ if and only if $\mathcal{M} \models_s \varphi$ in the sense of [[Tarski's satisfaction|2RBQPV02AS]] for every $s \in X$.
- Conservativity: by flatness, a first-order sentence is true in $\mathcal{M}$ in dependence logic exactly when it is true in the usual sense.
- Expressive power on sentences: each dependence logic sentence is equivalent to an existential second-order sentence $\exists R_1 \ldots \exists R_k \, \psi$ with $\psi$ first-order, and conversely (Väänänen). Here the second-order logic has full semantics: each $R_i$ ranges over all relations on $M$ of its arity.
- Consequences: dependence logic is compact and satisfies the downward [[Löwenheim–Skolem theorem|484M0TZ1S7]] for sentences. By [[Fagin's theorem|BG8Q0BYSQ3]], its sentences define exactly the NP properties of finite structures.
- Expressive power on formulas (Kontinen and Väänänen): a class of teams is defined by a dependence logic formula exactly when it has three properties. It contains the empty team, it is closed under subteams, and it is definable in existential second-order logic.
- The logic is not closed under classical negation. The sentence of [[this example|~7025fbde]] says "infinite", and "finite" has no dependence logic sentence.
- Inclusion logic adds atoms $\bar{x} \subseteq \bar{y}$, true in $X$ when each value of $\bar{x}$ in $X$ is also a value of $\bar{y}$ in $X$. Its formulas are closed under unions of teams, not under subteams.
- Independence logic adds atoms $\bar{x} \perp_{\bar{z}} \bar{y}$: for $s, s' \in X$ with $s(\bar{z}) = s'(\bar{z})$ there is $s'' \in X$ that agrees with $s$ on $\bar{z}\bar{x}$ and with $s'$ on $\bar{y}$. The dependence atom $=\!(\bar{x}, y)$ is equivalent to $y \perp_{\bar{x}} y$, and on sentences independence logic again equals existential second-order logic.

### History

Wilfrid Hodges introduced team semantics in 1997 as a compositional semantics for independence-friendly logic.
Jouko Väänänen defined dependence logic in his book "Dependence Logic: A New Approach to Independence Friendly Logic" of 2007.
Kontinen and Väänänen characterized the team properties definable by dependence logic formulas in 2009.
Pietro Galliani introduced inclusion logic in 2012, and Erich Grädel and Väänänen introduced independence logic in 2013.
Galliani and Lauri Hella proved in 2013 that inclusion logic has the expressive power of positive greatest fixed point logic on sentences.

### Common errors

- To confuse the empty team $\emptyset$ with the team $\{\emptyset\}$. The empty team satisfies every formula; the team $\{\emptyset\}$ is the one that decides the truth of a sentence.
- To read $\neg$ as classical negation. In dependence logic $\neg$ is pushed to the atoms, and $\neg =\!(\bar{t}, t)$ holds only in the empty team. So $=\!(x) \lor \neg =\!(x)$ fails in every team in which $x$ takes two values.
- To think that $\varphi \lor \varphi$ is equivalent to $\varphi$. The formula $=\!(x) \lor =\!(x)$ holds in the team where $x$ takes the values $0$ and $1$, because each half is constant, but $=\!(x)$ fails there.

## Explanations

### L1 human

Think of a table with columns $x$ and $y$ and several rows.
The column $y$ depends on the column $x$ when equal entries in $x$ always come with equal entries in $y$.
For the rows $(0, 5)$, $(1, 7)$ and $(0, 5)$ this is true, but if we add the row $(0, 6)$ it is false.
Dependence logic is ordinary logic with one new kind of basic statement: "this column depends on those columns".
Such a statement is about the whole table, not about one row.
So the logic gives truth values to tables of values, which are called teams, instead of to single rows.
If we delete rows from a table, a true dependence stays true, and an empty table satisfies every statement.

### L2 human

We evaluate two sentences in the structure $\mathcal{M}$ with domain $M = \{0, 1\}$ and only equality.

1. Let $\varphi_1 = \forall x \, \exists y \, (=\!(x, y) \land \neg x = y)$. We start from the team $\{\emptyset\}$.
2. The clause for $\forall x$ gives the team $X = \{ (x \mapsto 0), (x \mapsto 1) \}$.
3. For $\exists y$ we choose $F(x \mapsto 0) = 1$ and $F(x \mapsto 1) = 0$. The new team has the rows $(x, y) = (0, 1)$ and $(1, 0)$.
4. The atom $=\!(x, y)$ holds: the two rows have different values of $x$, so there is nothing to compare.
5. The literal $\neg x = y$ holds in each row. So $\varphi_1$ is true.
6. Let $\varphi_2 = \forall x \, \exists y \, (=\!(y) \land \neg x = y)$, with the constancy atom. After step 2 we need one function $F$ with constant value $c$.
7. The row with $x = c$ then has $y = c$, and $\neg x = y$ fails in it. Both choices $c = 0$ and $c = 1$ fail, so $\varphi_2$ is false.

The sentence $\varphi_2$ says $\exists y \, \forall x \, \neg x = y$, and $\varphi_1$ says $\forall x \, \exists y \, \neg x = y$.
The typical use of the atoms is this: they fix which earlier variables a chosen value may use.
A trap is to expect $=\!(x, y)$ to add something in $\varphi_1$.
There $y$ is chosen after $x$ and may always depend on it, so the atom is redundant.
It becomes a real restriction only when it excludes some variable that comes before.

### L3 human

The equivalence with existential second-order logic is the Skolem normal form read in both directions.
A dependence atom $=\!(\bar{u}, v)$ after the quantifiers says that the Skolem function of $v$ takes only $\bar{u}$ as arguments.
Conversely, a sentence $\exists f \, \psi$ can be coded by universal quantifiers for the arguments of $f$ and existential quantifiers controlled by atoms.
So three kinds of sentences define the same classes of structures.
They are dependence logic sentences, [[independence-friendly logic|DPMKT2KRB8]] sentences, and partially ordered quantifier prefixes before a first-order formula.
Dependence logic differs in that it separates the dependence from the quantifier and has a local, compositional semantics.
The [[game-theoretic semantics|D45Z7HETDA]] behind it is a game of imperfect information; a team corresponds to a set of positions that a uniform strategy can reach.

Team semantics now carries many atoms from database theory and probability: functional dependence, inclusion, exclusion and conditional independence.
Each atom gives a logic with a typical closure property: closure under subteams for dependence, closure under unions for inclusion, neither for independence.
The same idea applies to propositional and modal logic, as in modal dependence logic.
On finite structures these logics meet descriptive complexity.
Dependence and independence logic capture NP by [[Fagin's theorem|BG8Q0BYSQ3]], and inclusion logic captures PTIME on ordered finite structures through greatest fixed points.
Inside this sub-area, dependence logic is the team-semantic form of the existential fragment of [[second-order logic|G6X7SZSNC5]].
