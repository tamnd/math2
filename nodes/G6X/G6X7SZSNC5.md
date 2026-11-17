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

Second-order logic over a signature $L$ is the logic whose formulas are built like the formulas of [[first-order logic|086QKPF0A6]] over $L$, with two additions (see the [[definition|47XHPD8XE2]]).
First, for each $n \ge 1$ there are relation variables $X, Y, \ldots$ of arity $n$, with atomic formulas $X(t_1, \ldots, t_n)$ for terms $t_1, \ldots, t_n$.
Second, if $\varphi$ is a formula, then $\forall X \, \varphi$ and $\exists X \, \varphi$ are formulas.
In the full (standard) semantics, a formula is evaluated in an $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ with domain $M$, and an $n$-ary relation variable ranges over all subsets of $M^n$, that is, over the whole [[power set|00E0YZCERH]] $\mathcal{P}(M^n)$.
In the [[Henkin semantics|KWEJFK5943]], it ranges only over a family $D_n \subseteq \mathcal{P}(M^n)$ that is a part of the model.
With the full semantics, second-order logic describes the natural numbers and the real numbers up to isomorphism, but it loses the completeness, compactness and Löwenheim-Skolem theorems of first-order logic.

## Motivation

Many basic properties in mathematics speak about all subsets of a structure.
Induction says that every set of natural numbers that contains $0$ and is closed under successor contains every natural number.
The least upper bound property says that every nonempty bounded set of real numbers has a least upper bound.
Finiteness, well-foundedness and the connectedness of a graph have the same form.
First-order logic can only quantify over elements, so it replaces such a property by a schema, with one axiom for each formula.
The [[compactness theorem|1NR3HAWG9D]] and the [[Löwenheim-Skolem theorem|484M0TZ1S7]] then give unintended models, for example [[non-standard models of arithmetic|1QWN5CV4CG]].
Second-order logic states each property as one sentence, and the full semantics gives the sentence its intended meaning.

## Notation

Upper case letters $X, Y, Z$ denote relation variables, and lower case letters $x, y, z$ denote individual variables.
Some books also allow function variables $F, G$; a function variable can be replaced by a relation variable for its graph.
Books write the logic as SOL, $L^2$ or $L_{\mathrm{II}}$.
We write $\mathcal{M} \models \varphi$ for truth in the full semantics, and $\models_{\mathrm{H}}$ for consequence in the Henkin semantics.
A formula is $\Sigma^1_1$ when it has the form $\exists X_1 \cdots \exists X_k \, \psi$ with $\psi$ first-order, and $\Pi^1_1$ when it has the form $\forall X_1 \cdots \forall X_k \, \psi$.
The $\Sigma^1_1$ formulas form existential second-order logic, and [[monadic second-order logic|3WHQFSHR58]] (MSO) allows only relation variables of arity $1$.
Every claim about second-order logic must name its semantics; on this page, the full semantics is meant unless we say otherwise.

## Remarks

### Examples

- Equality: the formula $\forall X \, (X(x) \to X(y))$ holds exactly when $x = y$, since the choice $X = \set{x}$ forces $y \in \set{x}$.
- Induction: with the first-order axioms $\forall x \, S(x) \neq 0$ and $\forall x \forall y \, (S(x) = S(y) \to x = y)$, the sentence $\forall X \, \big( (X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x) \big)$ gives second-order Peano arithmetic $\mathrm{PA}^2$. [[Every full model of these axioms is isomorphic to $(\mathbb{N}, 0, n \mapsto n + 1)$|CKEG6B25AN]].
- Finiteness: [[a single sentence $\mathrm{Fin}$ holds exactly in the finite structures|M4TVZVANX5]], because a set is finite exactly when every injective map from the set to itself is onto.
- Completeness of an order: with the axioms of an [[ordered field|0P3VCBDEE2]], the sentence $\forall X \, \big( (\exists x \, X(x) \land \exists b \, \forall x \, (X(x) \to x \le b)) \to \exists s \, \forall b \, (\forall x \, (X(x) \to x \le b) \leftrightarrow s \le b) \big)$ says that every nonempty set with an upper bound has a least upper bound. All full models of these axioms are isomorphic to $\mathbb{R}$, by the [[uniqueness of the complete ordered field|0G8G1TH5WK]].
- Connectedness: for a [[graph|00C0BR7D7H]] with edge relation $E$, the sentence $\forall X \, \big( (\exists x \, X(x) \land \forall x \forall y \, (X(x) \land E(x, y) \to X(y))) \to \forall x \, X(x) \big)$ says that no nonempty proper set of vertices is closed under edges, that is, the graph is connected.

### Non-examples

- A sentence with a variable for sets of subsets of the domain is not second-order; it belongs to third-order [[higher-order logic|K40YJX8K1G]].
- [[The first-order induction schema|KCZ2EVJVS2]] is not a second-order sentence: it covers only the sets that a first-order formula defines, and it has non-standard models.
- A two-sorted first-order theory with a sort for sets, such as [[second-order arithmetic|DC60FYCSPM]] in its usual first-order form, is second-order logic with the Henkin semantics, not with the full semantics.

### Basic properties

These properties hold for the full semantics.

1. The [[comprehension schema|5GS6DRJ5SY]] $\exists X \, \forall \bar{x} \, (X(\bar{x}) \leftrightarrow \varphi)$ is valid, since the set of tuples that satisfy $\varphi$ is a subset of $M^n$.
2. There is no effective proof system that is sound and complete for validity. The argument follows this list.
3. Compactness fails: the set $\set{\mathrm{Fin}} \cup \set{\lambda_n : n \ge 1}$, with $\lambda_n$ the first-order sentence "there are at least $n$ elements", has no model, but each finite subset has one. [[This example|M4TVZVANX5]] gives the details.
4. The downward Löwenheim-Skolem theorem fails: the second-order axioms of a complete ordered field have models, and all of them are uncountable, since they are isomorphic to $\mathbb{R}$.
5. The upward Löwenheim-Skolem theorem fails: all models of $\mathrm{PA}^2$ are countably infinite.
6. Each sentence of higher order can be reduced to a second-order sentence with the same validity; see [[higher-order logic|K40YJX8K1G]].

Here is the argument for property 2.
Add to $\mathrm{PA}^2$ the first-order recursion equations $x + 0 = x$, $x + S(y) = S(x + y)$, $x \cdot 0 = 0$ and $x \cdot S(y) = x \cdot y + x$, and call the conjunction $\mathrm{PA}^2_{+}$.

1. Every full model of $\mathrm{PA}^2_{+}$ is isomorphic to $(\mathbb{N}, 0, S, +, \cdot)$. The isomorphism $f$ for $0$ and $S$ comes from [[the categoricity example|CKEG6B25AN]], and induction on $y$ in $\mathbb{N}$ shows $f(x + y) = f(x) +^{\mathcal{M}} f(y)$ and $f(x \cdot y) = f(x) \cdot^{\mathcal{M}} f(y)$ from the recursion equations.
2. An isomorphism preserves the truth of every second-order sentence, by induction on the formula. So for each first-order sentence $\sigma$ of arithmetic, $\mathbb{N} \models \sigma$ holds exactly when $\mathrm{PA}^2_{+} \to \sigma$ is valid.
3. The theorems of an effective proof system form a [[computably enumerable set|TN9G24VABN]]. If such a system were sound and complete, the valid sentences would form a computably enumerable set.
4. The map $\sigma \mapsto (\mathrm{PA}^2_{+} \to \sigma)$ is computable. By step 2, the set of first-order sentences true in $\mathbb{N}$ would then be computably enumerable.
5. This set is a consistent and complete theory that contains [[Robinson arithmetic|3K1AKGXF8A]]. By [[Gödel's first incompleteness theorem|X9WYNYE29C]], such a theory is not computably enumerable. This contradiction proves property 2.

The same reduction shows that the set of valid second-order sentences is not even arithmetical, because the set of true first-order sentences of arithmetic is not arithmetical, by [[Tarski's undefinability theorem|YRV6SYK2BY]].

### The full semantics depends on set theory

The full semantics uses the power set of the domain, so the truth of a sentence can depend on questions of set theory.
Here is an instance.
Let $\rho$ be the conjunction of the second-order axioms of a complete ordered field, so that every full model of $\rho$ is isomorphic to $\mathbb{R}$.
Inside such a model, the set of natural numbers is definable as the least set that contains $0$ and is closed under $x \mapsto x + 1$.
Let $\chi$ say that every subset $X$ of the domain admits an injective relation into this set of natural numbers, or a bijective relation onto the whole domain.
Then the sentence $\rho \to \chi$ is valid exactly when every set of real numbers is countable or has the cardinality of $\mathbb{R}$, that is, exactly when the [[continuum hypothesis|0MN2MER9WN]] holds.
So the full semantics settles a sentence only as far as the set theory of the metalanguage settles it.

### Skolem's relativism

The Löwenheim-Skolem theorem gives a countable model of every countable first-order set theory that has a model.
In such a model, some set is "uncountable" in the sense of the model, although only countably many elements of the model belong to it; this is [[Skolem's paradox|68QZWDXAQ4]].
Skolem concluded that notions such as "uncountable" and "all subsets" are relative to a model.
In the full semantics of second-order logic these notions are fixed, and the categoricity results above depend on that.
A critic in the spirit of Skolem answers that the full semantics only moves the relativity to the set theory of the metalanguage.
The Henkin semantics accepts the relativity: its models are first-order models in disguise, and they satisfy the Löwenheim-Skolem theorem.

### Relation to other logics

Second-order logic with the full semantics is a proper extension of first-order logic.
By [[Lindström's theorem|FYZ3CJGZYV]], first-order logic is a maximal logic that has both the compactness property and the downward Löwenheim-Skolem property, so a proper extension must lose one of them; second-order logic loses both.
[[Fagin's theorem|BG8Q0BYSQ3]] shows that on finite structures, the existential second-order sentences define exactly the properties in the complexity class NP.
Other extensions of first-order logic, such as [[infinitary logic|PQG7VAZ1R2]] and logics with [[generalized quantifiers|MFV98WTF4G]], add less power and keep some of the first-order theorems.

### History

Frege's logic of 1879 already quantified over concepts, which play the part of relations.
Frege's derivation of arithmetic survives in [[Frege's theorem|J36EHBHF6J]]: the Peano axioms follow in second-order logic from Hume's principle.
Dedekind characterized the natural numbers up to isomorphism in 1888, with an argument that is a second-order categoricity proof.
Henkin introduced the general models of the Henkin semantics in 1950 and proved the completeness theorem for them.
Quine argued that second-order logic with the full semantics is set theory in disguise; Boolos replied in 1984 with a [[plural reading|DZVEFDYYZX]] of monadic second-order quantifiers.

### Common errors

- Saying "second-order logic is incomplete" without a semantics. With the Henkin semantics there is a complete proof system; with the full semantics there is none.
- Mixing up two senses of completeness. $\mathrm{PA}^2$ is categorical, so it decides every sentence semantically, yet no effective proof system derives all its consequences.
- Treating the full semantics as free of set theory. The validity of some sentences, such as $\rho \to \chi$ above, depends on open questions of set theory.

## Explanations

### L1 human

First-order logic can say "for every number $x$", but it cannot say "for every set of numbers $X$".
Second-order logic can say both.
With it, the rule of induction becomes one sentence: every set of numbers that contains $0$ and contains the next number after each of its members contains all numbers.
For instance, a set that contains $0$, and $1$ after $0$, and $2$ after $1$, and so on, must contain $7$.
This sentence, with two simple rules about the successor, describes the natural numbers completely, with no strange extra models.
The price is that no proof method can find all the true sentences of this logic.

### L2 human

We check that the connectedness sentence $\gamma$ of the examples is true in one graph and false in another.
The sentence is $\forall X \, \big( (\exists x \, X(x) \land \forall x \forall y \, (X(x) \land E(x, y) \to X(y))) \to \forall x \, X(x) \big)$.

1. Take the path graph $P$ with vertices $1, 2, 3$ and the edges $\set{1, 2}$ and $\set{2, 3}$, with $E$ symmetric.
2. Let $X$ be a nonempty set of vertices that is closed under edges. We show that $X = \set{1, 2, 3}$.
3. If $1 \in X$, then $2 \in X$ by the edge $(1, 2)$, and $3 \in X$ by the edge $(2, 3)$.
4. If $2 \in X$, then $1, 3 \in X$ by the edges $(2, 1)$ and $(2, 3)$. If $3 \in X$, then $2 \in X$, and then $1 \in X$.
5. So every choice of $X$ satisfies $\forall x \, X(x)$, and $P \models \gamma$.
6. Now take the graph $Q$ with vertices $1, 2, 3$ and the single edge $\set{1, 2}$.
7. The set $X = \set{3}$ is nonempty, and it is closed under edges, because no edge starts at $3$.
8. But $X$ does not contain $1$. So $X$ makes the inner implication false, and $Q \not\models \gamma$.

In the full semantics the variable $X$ ranges over all $8$ subsets of $\set{1, 2, 3}$, so the check in step 7 is allowed.
A typical use of such sentences is to define a class of structures that first-order logic cannot define; connectedness of graphs is such a class.
The trap is to forget the semantics: in a Henkin model whose family $D_1$ omits the set $\set{3}$, the sentence $\gamma$ can be true in $Q$.

### L3 human

Second-order logic sits between first-order logic and set theory.
With the full semantics, its validities depend on the power set operation of the metatheory, and the sentence $\rho \to \chi$ above shows that the continuum hypothesis is one of its questions.
With the [[Henkin semantics|KWEJFK5943]], it is a many-sorted first-order logic, and all the first-order theorems return, together with non-standard models.
[[Lindström's theorem|FYZ3CJGZYV]] explains why no logic can have both the expressive power of the full semantics and the good model theory of first-order logic.
Fragments behave differently: existential second-order logic is equivalent to [[independence-friendly logic|DPMKT2KRB8]] and to [[dependence logic|DNAPTJ98WD]] on sentences, and it captures NP on finite structures by Fagin's theorem.
Monadic second-order logic over words and trees is decidable by the theorems of Büchi and Rabin, which connect it with automata.
In proof theory, the first-order theory [[second-order arithmetic|DC60FYCSPM]] and its subsystems are the Henkin side of the same language, and they are the setting of reverse mathematics.
In type theory, the higher-order generalization is Church's simple theory of types.
