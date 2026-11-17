---
tag: ~abb2cff1
kind: definition
name: Henkin semantics
aliases: [general-semantics, henkin-model, general-model]
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
audience: grad
defines: ~e3378781
uses: [G6X7SZSNC5, 983GZBQYT4, 2RBQPV02AS, 00E0YZCERH, ~205409ab, WQ1ZE255SF, 1NR3HAWG9D]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Semantics
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Metalogical results
  - url: https://en.wikipedia.org/wiki/Higher-order_logic
    locator: Semantics
  - book: isbn:9780122384523
    locator: Chapter 4
---

## Definition

Let $L$ be a signature of [[second-order logic|G6X7SZSNC5]].
A general structure for $L$ is a pair $\mathfrak{M} = (\mathcal{M}, (D_n)_{n \ge 1})$ with two parts.

1. $\mathcal{M}$ is an $L$-[[structure|983GZBQYT4]] with domain $M$.
2. For each $n \ge 1$, $D_n$ is a set of $n$-ary relations on $M$, that is, $D_n \subseteq \mathcal{P}(M^n)$.

An assignment $s$ sends each individual variable to an element of $M$ and each $n$-ary relation variable to an element of $D_n$.
[[Satisfaction|2RBQPV02AS]] $\mathfrak{M} \models \varphi[s]$ is defined by induction on $\varphi$ as in first-order logic, with three clauses for the new formulas.

- $\mathfrak{M} \models X(t_1, \ldots, t_n)[s]$ when the tuple of the values of $t_1, \ldots, t_n$ belongs to the relation $s(X)$.
- $\mathfrak{M} \models \forall X \, \varphi[s]$ when $\mathfrak{M} \models \varphi[s(X \mapsto R)]$ for every $R \in D_n$.
- $\mathfrak{M} \models \exists X \, \varphi[s]$ when $\mathfrak{M} \models \varphi[s(X \mapsto R)]$ for some $R \in D_n$.

A Henkin model is a general structure in which every instance of the [[comprehension schema|~205409ab]] is true:

$$\forall \bar{y} \, \forall \bar{Y} \, \exists X \, \forall x_1 \cdots \forall x_n \, \big( X(x_1, \ldots, x_n) \leftrightarrow \varphi \big),$$

for every formula $\varphi$ in which $X$ is not free, with $\bar{y}$ and $\bar{Y}$ the other free variables of $\varphi$.
The Henkin semantics is the semantics of second-order logic in which the models are the Henkin models.
A set $\Gamma$ of sentences Henkin-implies a sentence $\varphi$, written $\Gamma \models_{\mathrm{H}} \varphi$, when every Henkin model of $\Gamma$ satisfies $\varphi$.

## Notation

We write $\models_{\mathrm{H}}$ for Henkin consequence and $\models$ for consequence in the full semantics.
The general structure with $D_n = \mathcal{P}(M^n)$ for every $n$ is the full structure over $\mathcal{M}$.
The terms vary between books.
Some books call every general structure a Henkin structure, and some call a general structure that satisfies comprehension a faithful structure.
Some books also require the axiom of choice for relations, or add function variables with their own domains.

## Remarks

### Examples

- [[Every full structure is a Henkin model|~845dd993]], because the set defined by $\varphi$ is a subset of $M^n$ and so belongs to $\mathcal{P}(M^n)$.
- Every Henkin model with a finite domain is full. Comprehension with parameters gives each finite relation, through a disjunction of equations $x_j = y_{ij}$; this is also shown in the [[example on full structures|~845dd993]].
- [[Second-order Peano arithmetic has non-standard Henkin models|~3a3f15c2]], although all its full models are isomorphic to $\mathbb{N}$.

### Non-examples

- [[A general structure on two points whose family of sets omits $\set{0}$|~a74b4bb3]] is not a Henkin model: the comprehension instance for the formula $x = y$ fails.
- A first-order structure alone is not a general structure: it has no families $D_n$, so second-order quantifiers have no range.

### Completeness, compactness and Löwenheim-Skolem return

Take the deductive system with three parts.
It has the first-order rules for the individual quantifiers, the same rules for the relation quantifiers with a relation variable in place of a term, and every instance of comprehension as an axiom.
Henkin proved in 1950 that this system is complete for the Henkin semantics: $\Gamma \vdash \varphi$ exactly when $\Gamma \models_{\mathrm{H}} \varphi$.
Three consequences follow, in the same way as for first-order logic.

1. The set of Henkin-valid sentences is computably enumerable.
2. Compactness holds: if every finite subset of $\Gamma$ has a Henkin model, then $\Gamma$ has a Henkin model.
3. Löwenheim-Skolem holds: a countable set $\Gamma$ with a Henkin model has a Henkin model in which $M$ and every $D_n$ are countable.

### Equivalence with many-sorted first-order logic

The Henkin semantics is first-order logic with several sorts, written with second-order notation.
Take a sort $0$ for individuals and a sort $n$ for $n$-ary relations, with a predicate $\mathrm{Ap}_n(r, x_1, \ldots, x_n)$ that reads "$(x_1, \ldots, x_n)$ belongs to $r$".
A second-order formula translates to a many-sorted formula: $X(t_1, \ldots, t_n)$ becomes $\mathrm{Ap}_n(X, t_1, \ldots, t_n)$, and $\forall X$ becomes a quantifier over sort $n$.
A general structure gives a many-sorted structure, with $D_n$ as the sort $n$ and membership as $\mathrm{Ap}_n$.
Conversely, a many-sorted structure gives a general structure: replace each element $r$ of sort $n$ by the set $\set{\bar{a} : \mathrm{Ap}_n(r, \bar{a})}$.
The translated formulas use the elements of sort $n$ only through $\mathrm{Ap}_n$, so this replacement keeps their truth values, by induction on the formula.
So $\Gamma \models_{\mathrm{H}} \varphi$ holds exactly when the translation of $\varphi$ follows in many-sorted first-order logic from the translations of $\Gamma$ and of the comprehension instances.
This is how the completeness and compactness of the Henkin semantics follow from [[Gödel's completeness theorem|WQ1ZE255SF]] and the [[compactness theorem|1NR3HAWG9D]].

### Relation to the full semantics

Every full structure is a Henkin model, so every Henkin-valid sentence is valid in the full semantics.
The converse fails.
The Henkin-valid sentences form a computably enumerable set, and the sentences valid in the full semantics do not, as the page on [[second-order logic|G6X7SZSNC5]] shows.
So some sentence is valid in the full semantics but false in some Henkin model.
By the translation above, the models of the first-order theory [[second-order arithmetic|DC60FYCSPM]] are the Henkin models of second-order Peano arithmetic with $+$ and $\cdot$.

### History

Leon Henkin introduced general models in 1950, for the simple theory of types, and proved the completeness theorem for them.
His method of adding witnesses to a consistent set is the same method that gives his proof of Gödel's completeness theorem for first-order logic.

## Explanations

### L1 human

In second-order logic, a sentence can say "for every set of points".
The full meaning of "every set" is every set that exists.
The Henkin meaning lets each model choose a list of allowed sets, and "for every set" then means "for every set on the list".
The list must be rich enough: each set that the language can describe must be on the list.
For example, on the numbers $1$ to $5$, the set of even numbers $\set{2, 4}$ must be on the list when the language can say "even".
With this freedom, second-order logic behaves like ordinary first-order logic again, and all its usual theorems return.

### L2 human

We check that a Henkin model with a two-element domain is full.
Let $L$ be empty, $M = \set{a, b}$, and let $\mathfrak{M} = (M, (D_n))$ be a Henkin model.

1. The formula $x = y$ has the free variables $x$ and $y$. Comprehension gives $\forall y \, \exists X \, \forall x \, (X(x) \leftrightarrow x = y)$.
2. With $y = a$, some $R \in D_1$ satisfies $R = \set{a}$. With $y = b$, some $R \in D_1$ satisfies $R = \set{b}$.
3. The formula $x \neq x$ gives $\emptyset \in D_1$, and the formula $x = x$ gives $M \in D_1$.
4. So $D_1$ contains all $4$ subsets of $M$, and $D_1 = \mathcal{P}(M)$.
5. In the same way, the formula $\bigvee_{i} (x_1 = y_{i1} \land x_2 = y_{i2})$ gives each of the $16$ binary relations on $M$, so $D_2 = \mathcal{P}(M^2)$.

The typical use of the Henkin semantics is to get a complete proof system for second-order theories, at the price of non-standard models.
The trap is to forget the parameters $\bar{y}$ in comprehension: without parameters, only $\emptyset$ and $M$ are definable in the empty signature, and step 2 fails.

### L3 human

The Henkin semantics turns second-order logic into a many-sorted first-order logic, so every first-order theorem, such as interpolation and omitting types, has a Henkin version.
It is the natural semantics for [[second-order arithmetic|DC60FYCSPM]] and its subsystems, where the family of sets of numbers is a part of the model.
The models of a subsystem such as arithmetical comprehension are general structures that satisfy only a part of the comprehension schema.
In type theory, the same idea gives general models of the simple theory of types, which was Henkin's own setting.
The full semantics is the special case of the Henkin semantics in which the families are as large as possible.
