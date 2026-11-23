---
tag: G6X7SZSNC5
kind: concept
name: Second-order logic
msc: ["03B16", "03C85"]
topics: [MDHDYV8QZW]
audience: grad
specializes: [P1ABGYRQXH]
uses: [086QKPF0A6, 983GZBQYT4, 2RBQPV02AS, 00E0YZCERH, 47XHPD8XE2]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Semantics
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Expressive power
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: Metalogical results
  - url: https://en.wikipedia.org/wiki/Second-order_logic
    locator: History and disputed value
  - book: isbn:9780122384523
    locator: Chapter 4
same_as:
  wikidata: Q1548746
  wikipedia: Second-order logic
---

## Summary

Second-order logic is first-order logic with one new power: a formula may quantify over sets and relations of the domain, not only over its elements.
The first example to know is the induction axiom.
Over a constant $0$ and a successor function $S$, it is one sentence:
$$\forall X \, \big( (X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x) \big).$$
It says that every set that contains $0$ and is closed under $S$ contains every element.
Together with "$0$ is not a successor" and "$S$ is one-to-one", it [[pins down $(\mathbb{N}, 0, S)$ up to isomorphism|CKEG6B25AN]], and no set of first-order sentences can do that.

The [[formal definition|47XHPD8XE2]] builds the formulas over a signature $L$ like the formulas of [[first-order logic|086QKPF0A6]], with two additions.
For each $n \ge 1$ there are relation variables $X, Y, \ldots$ of arity $n$, and $X(t_1, \ldots, t_n)$ is an atomic formula for terms $t_1, \ldots, t_n$.
If $\varphi$ is a formula, then $\forall X \, \varphi$ and $\exists X \, \varphi$ are formulas.
In the full (standard) semantics, an $n$-ary relation variable ranges over all of $\mathcal{P}(M^n)$, the [[power set|00E0YZCERH]] of $M^n$, where $M$ is the domain of an $L$-[[structure|983GZBQYT4]].
In the [[Henkin semantics|KWEJFK5943]], it ranges only over a family $D_n \subseteq \mathcal{P}(M^n)$ that is part of the model.

## Motivation

Many basic properties in mathematics speak about all subsets of a structure.
Induction speaks about every set of natural numbers.
The least upper bound property says that every nonempty bounded set of real numbers has a least upper bound.
Finiteness, well-foundedness and the connectedness of a graph have the same form.

First-order logic quantifies only over elements, so it replaces such a property by a schema, with one axiom for each formula.
Then the [[compactness theorem|1NR3HAWG9D]] and the [[Löwenheim-Skolem theorem|484M0TZ1S7]] produce unintended models, such as the [[non-standard models of arithmetic|1QWN5CV4CG]].
Second-order logic states each property as one sentence, and the full semantics gives that sentence its intended meaning.
The price is high: with the full semantics, second-order logic loses the completeness, compactness and Löwenheim-Skolem theorems.
The rest of the sub-area studies this trade, and the logics that sit between first-order and full second-order logic.

## Notation

Upper case letters $X, Y, Z$ are relation variables, and lower case letters $x, y, z$ are individual variables.
Some books also allow function variables $F, G$, and a function variable can be replaced by a relation variable for its graph.
Books write the logic as SOL, $L^2$ or $L_{\mathrm{II}}$.
We write $\mathcal{M} \models \varphi$ for truth in the full semantics, and $\models_{\mathrm{H}}$ for consequence in the Henkin semantics.
A formula is $\Sigma^1_1$ when it has the form $\exists X_1 \cdots \exists X_k \, \psi$ with $\psi$ first-order, and $\Pi^1_1$ when it has the form $\forall X_1 \cdots \forall X_k \, \psi$.
The $\Sigma^1_1$ formulas form existential second-order logic, and [[monadic second-order logic|3WHQFSHR58]] (MSO) allows only relation variables of arity $1$.
The phrase "second-order logic" alone can mean either semantics, so every claim must name one.
Below, the full semantics is meant unless we say otherwise.

## Remarks

### Five things one sentence can say

Equality is definable.
The formula $\forall X \, (X(x) \to X(y))$ holds exactly when $x = y$.
If $x = y$, every set that contains $x$ contains $y$.
If the formula holds, take $X = \{ x \}$, and then $y \in \{ x \}$, so $y = x$.

Induction is one sentence, the axiom shown in the Summary.
With the axioms $\forall x \, S(x) \neq 0$ and $\forall x \forall y \, (S(x) = S(y) \to x = y)$, it gives second-order Peano arithmetic $\mathrm{PA}^2$, and [[every full model of $\mathrm{PA}^2$ is isomorphic to $(\mathbb{N}, 0, n \mapsto n + 1)$|CKEG6B25AN]].

Finiteness is one sentence.
A set is finite exactly when every one-to-one map from the set to itself is onto, and [[a sentence $\mathrm{Fin}$ says exactly that|M4TVZVANX5]].

### Five things one sentence can say, continued

Completeness of an order is one sentence.
With the axioms of an [[ordered field|0P3VCBDEE2]], the following sentence says that every nonempty set with an upper bound has a least upper bound:
$$\forall X \, \Big( \big(\exists x \, X(x) \land \exists b \, \forall x \, (X(x) \to x \le b)\big) \to \exists s \, \forall b \, \big(\forall x \, (X(x) \to x \le b) \leftrightarrow s \le b\big) \Big).$$
All full models of these axioms are isomorphic to $\mathbb{R}$, by the [[uniqueness of the complete ordered field|0G8G1TH5WK]].

Connectedness of a [[graph|00C0BR7D7H]] with edge relation $E$ is one sentence $\gamma$:
$$\forall X \, \Big( \big(\exists x \, X(x) \land \forall x \forall y \, (X(x) \land E(x, y) \to X(y))\big) \to \forall x \, X(x) \Big).$$
It says that every nonempty set of vertices that is closed under edges is the whole graph.
The L2 explanation checks $\gamma$ on two small graphs.

### What it is not

A quantifier over sets of subsets of the domain is not second-order.
No clause of the definition gives such variables, and they belong to third-order [[higher-order logic|K40YJX8K1G]].

[[The first-order induction schema|KCZ2EVJVS2]] is not the second-order axiom.
It covers only the sets that a first-order formula defines, and it has non-standard models.

A two-sorted first-order theory with a sort for sets, such as [[second-order arithmetic|DC60FYCSPM]] in its usual form, is second-order logic with the Henkin semantics, not with the full semantics.
Its set sort can miss subsets, and it has non-standard models.

### What the full semantics costs

The [[comprehension schema|5GS6DRJ5SY]] $\exists X \, \forall \bar{x} \, (X(\bar{x}) \leftrightarrow \varphi)$ is valid, because the set of tuples that satisfy $\varphi$ is a subset of $M^n$.
That is the gain.
The losses follow.

Compactness fails.
The set $\{ \mathrm{Fin} \} \cup \{ \lambda_n : n \ge 1 \}$, with $\lambda_n$ the first-order sentence "there are at least $n$ elements", has no model, but each finite subset has one, as [[the finiteness example|M4TVZVANX5]] shows.

The downward Löwenheim-Skolem theorem fails.
The second-order axioms of a complete ordered field have an infinite model, and every model is isomorphic to $\mathbb{R}$, so none is countable.

The upward Löwenheim-Skolem theorem fails.
$\mathrm{PA}^2$ has an infinite model, and every model is countable.

There is no effective proof system that is sound and complete for validity, as the next subsection shows.
Validity of sentences of any higher order reduces to validity of second-order sentences, as [[higher-order logic|K40YJX8K1G]] explains.

### Why no proof system can be complete

We reduce truth in $\mathbb{N}$ to second-order validity.
Let $\mathrm{PA}^2_{+}$ be $\mathrm{PA}^2$ together with the recursion equations $x + 0 = x$, $x + S(y) = S(x + y)$, $x \cdot 0 = 0$ and $x \cdot S(y) = x \cdot y + x$.

1. Every full model of $\mathrm{PA}^2_{+}$ is isomorphic to $(\mathbb{N}, 0, S, +, \cdot)$.
   The map for $0$ and $S$ comes from [[the categoricity example|CKEG6B25AN]], and induction on $y$ shows that it also preserves $+$ and $\cdot$.
2. An isomorphism preserves the truth of every second-order sentence, by induction on the formula.
   So for each first-order sentence $\sigma$ of arithmetic, $\mathbb{N} \models \sigma$ holds exactly when $\mathrm{PA}^2_{+} \to \sigma$ is valid.
3. The theorems of an effective proof system form a [[computably enumerable set|TN9G24VABN]].
   If such a system were sound and complete, the valid sentences would form a computably enumerable set.
4. The map $\sigma \mapsto (\mathrm{PA}^2_{+} \to \sigma)$ is computable, so by step 2 the first-order sentences true in $\mathbb{N}$ would form a computably enumerable set.
5. That set is a consistent and complete theory that contains [[Robinson arithmetic|3K1AKGXF8A]].
   By [[Gödel's first incompleteness theorem|X9WYNYE29C]], no such theory is computably enumerable, and this contradiction ends the argument.

The same reduction shows more.
The valid second-order sentences do not even form an arithmetical set, because true arithmetic is not arithmetical, by [[Tarski's undefinability theorem|YRV6SYK2BY]].

### The full semantics depends on set theory

The full semantics uses the power set of the domain, so the truth of a sentence can depend on open questions of set theory.
Let $\rho$ be the conjunction of the second-order axioms of a complete ordered field, so every full model of $\rho$ is isomorphic to $\mathbb{R}$.
Inside such a model, the natural numbers form a definable set: the least set that contains $0$ and is closed under $x \mapsto x + 1$.
Let $\chi$ say that every subset of the domain has a one-to-one map into this set, or a one-to-one map onto the whole domain, where both maps are given as binary relations.
Then $\rho \to \chi$ is valid exactly when every set of real numbers is countable or has the cardinality of $\mathbb{R}$.
That is the [[continuum hypothesis|0MN2MER9WN]].
So the full semantics settles a sentence only as far as the set theory of the metalanguage settles it.

### Skolem's relativism

The Löwenheim-Skolem theorem gives a countable model of every countable first-order set theory that has a model.
In such a model some set is "uncountable" in the sense of the model, although only countably many elements of the model belong to it, and this is [[Skolem's paradox|68QZWDXAQ4]].
Skolem concluded that notions such as "uncountable" and "all subsets" are relative to a model.
The full semantics of second-order logic fixes these notions, and the categoricity results above depend on that.
A critic in the spirit of Skolem answers that the full semantics only moves the relativity into the set theory of the metalanguage.
The Henkin semantics accepts the relativity: its models are first-order models in disguise, and they obey the Löwenheim-Skolem theorem.

### Where it sits among logics

Full second-order logic is a proper extension of first-order logic, and [[Lindström's theorem|FYZ3CJGZYV]] explains why it must lose something.
The theorem says that a regular abstract logic that extends first-order logic and has both the compactness property and the downward Löwenheim-Skolem property expresses no more than first-order logic.
Here the downward Löwenheim-Skolem property means that every sentence with an infinite model has a countable model.
Second-order logic loses both properties.
[[Infinitary logic|PQG7VAZ1R2]] and logics with [[generalized quantifiers|MFV98WTF4G]] add less power, and each keeps some of the first-order theorems.
On finite structures, [[Fagin's theorem|BG8Q0BYSQ3]] shows that the existential second-order sentences define exactly the properties in the complexity class NP.

### Watch out

Do not say "second-order logic is incomplete" without naming the semantics.
With the Henkin semantics there is a complete proof system, and with the full semantics there is none.

Do not mix up two senses of "complete".
$\mathrm{PA}^2$ is categorical, so for each sentence $\sigma$, either $\sigma$ or $\neg \sigma$ is a consequence of $\mathrm{PA}^2$.
Yet by the argument above, no effective proof system derives all these consequences.

Do not treat the full semantics as free of set theory.
The validity of $\rho \to \chi$ above is the continuum hypothesis, which the usual axioms of set theory do not decide.

### History

Frege's logic of 1879 already quantified over concepts, which play the part of relations.
His derivation of arithmetic survives as [[Frege's theorem|J36EHBHF6J]]: the Peano axioms follow in second-order logic from Hume's principle.
Dedekind characterized the natural numbers up to isomorphism in 1888, with an argument that is a second-order categoricity proof.
Henkin introduced the general models of the Henkin semantics in 1950 and proved completeness for them.
Quine argued that second-order logic with the full semantics is set theory in disguise, and Boolos answered in 1984 with a [[plural reading|DZVEFDYYZX]] of monadic second-order quantifiers.

### Try it

Show that $\exists X \, (X(x) \land \neg X(y))$ holds exactly when $x \neq y$.
If $x \neq y$, the set $X = \{ x \}$ works, and if $x = y$, the formula asks for $X(x) \land \neg X(x)$, which no set satisfies.

Is $\forall X \, \exists x \, X(x)$ true in some structure?
No: in the full semantics $X$ can be the empty set, so the sentence is false in every structure.

Does $\mathrm{PA}^2$ have a model of cardinality $\aleph_1$?
No: every full model is isomorphic to $\mathbb{N}$, so every model is countable.

## Explanations

### L1 human

First-order logic can say "for every number $x$", but it cannot say "for every set of numbers $X$".
Second-order logic can say both.
With it, the rule of induction becomes one sentence: every set of numbers that contains $0$, and contains the next number after each of its members, contains all numbers.
For instance, such a set contains $0$, then $1$, then $2$, and so on up to $7$ and beyond.
This sentence, with two simple rules about the next number, describes the natural numbers completely, with no strange extra models.
The price is that no proof method can find all the true sentences of this logic.

### L2 human

We check the connectedness sentence $\gamma$ on two graphs with vertices $1, 2, 3$, with $E$ symmetric.

1. Take the path $P$ with edges $\{ 1, 2 \}$ and $\{ 2, 3 \}$, and let $X$ be a nonempty set of vertices that is closed under edges.
2. If $1 \in X$, then $2 \in X$ by the edge from $1$ to $2$, and then $3 \in X$ by the edge from $2$ to $3$.
3. If $2 \in X$ or $3 \in X$, the same edges give the other two vertices.
4. So every such $X$ is $\{ 1, 2, 3 \}$, and $P \models \gamma$.
5. Now take $Q$ with the single edge $\{ 1, 2 \}$.
   The set $X = \{ 3 \}$ is nonempty, and it is closed under edges, because no edge leaves $3$.
6. This $X$ does not contain $1$, so it makes the inner implication false, and $Q \not\models \gamma$.

In the full semantics, $X$ ranges over all $8$ subsets of $\{ 1, 2, 3 \}$, so step 5 may use $X = \{ 3 \}$.
A typical use of such a sentence is to define a class of structures that no first-order theory defines, and connectedness of graphs is such a class.
Watch out: in a Henkin model whose family $D_1$ omits $\{ 3 \}$ and $\{ 1, 2 \}$, the sentence $\gamma$ can be true in $Q$.

### L3 human

Second-order logic sits between first-order logic and set theory.
With the full semantics, its validities depend on the power set operation of the metatheory, and the continuum hypothesis is one of its questions.
With the [[Henkin semantics|KWEJFK5943]], it becomes a many-sorted first-order logic, and all the first-order theorems return, together with non-standard models.
Fragments behave differently.
Existential second-order logic has the same power on sentences as [[independence-friendly logic|DPMKT2KRB8]] and [[dependence logic|DNAPTJ98WD]], and it captures NP on finite structures.
The monadic second-order theory of $(\mathbb{N}, S)$ is decidable by [[Büchi's theorem|YPDXVTH5JR]], and this links MSO with automata.
In proof theory, [[second-order arithmetic|DC60FYCSPM]] and its subsystems are the Henkin side of the same language, and they are the setting of reverse mathematics.
The higher-order generalization is Church's [[simple theory of types|VQY7WX8J5C]].
