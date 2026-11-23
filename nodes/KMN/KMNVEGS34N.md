---
tag: KMNVEGS34N
kind: concept
name: Branching quantifier
aliases: [henkin-quantifier, partially-ordered-quantifier, branching-quantification]
msc: ["03C80", "03B16"]
topics: [MDHDYV8QZW]
audience: research
uses: [086QKPF0A6, G6X7SZSNC5, GCPQGMJYEV, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Branching_quantifier
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Branching_quantifier
    locator: Definition and properties
  - url: https://en.wikipedia.org/wiki/Branching_quantifier
    locator: Relation to natural languages
  - url: https://en.wikipedia.org/wiki/Independence-friendly_logic
    locator: Model-theoretic properties
---

## Summary

In ordinary logic each choice of a witness may depend on every earlier choice.
A branching quantifier lets us say that a witness depends only on some of the earlier variables.
The simplest case is the Henkin quantifier:
$$\begin{pmatrix} \forall x_1 & \exists y_1 \\ \forall x_2 & \exists y_2 \end{pmatrix} \varphi(x_1, x_2, y_1, y_2).$$
It is true in a [[structure|983GZBQYT4]] $\mathcal{M}$ if and only if there are functions $f, g \colon M \to M$ with this property:
$$\mathcal{M} \models \varphi(a_1, a_2, f(a_1), g(a_2)) \quad \text{for all } a_1, a_2 \in M.$$
So $y_1$ depends only on $x_1$, and $y_2$ depends only on $x_2$.

In general, a branching quantifier is a finite set of quantifiers $\forall x_i$ and $\exists y_j$ with a strict partial order on them.
Each $y_j$ may depend only on the universal variables that come before it in the order.
A branching sentence is true when Skolem functions exist that take only these allowed arguments.
This one change to [[first-order logic|086QKPF0A6]] already gives the full power of existential second-order logic.

## Motivation

In first-order logic the quantifiers of a prefix form a line.
In $\forall x_1 \exists y_1 \forall x_2 \exists y_2 \, \varphi$, the [[Skolem normal form|GCPQGMJYEV]] replaces $y_1$ by $f(x_1)$ and $y_2$ by $g(x_1, x_2)$.
So $y_2$ may depend on $x_1$, and some statements forbid that.
Hintikka gave an example from English: "some relative of each villager and some relative of each townsman hate each other".
On one reading, the relative of the villager is chosen from the villager alone, and the relative of the townsman from the townsman alone.

No linear order of the four quantifiers gives this pattern.
Each $y_i$ must come after its own $x_i$, or it cannot depend on $x_i$ at all.
Then the later of $y_1$ and $y_2$ comes after both universal quantifiers, so it may depend on both.
Henkin's idea is to write the quantifiers in a partial order, so that each branch carries its own dependence.
The page on [[independence-friendly logic|DPMKT2KRB8]] and the page on [[dependence logic|DNAPTJ98WD]] continue this idea.

## Notation

Henkin wrote a branching prefix as a matrix of quantifiers, with one row for each branch, as in the Summary.
The Henkin quantifier is also written $Q_H x_1 x_2 y_1 y_2 \, \varphi$ or $H x_1 x_2 y_1 y_2 \, \varphi$.
In [[independence-friendly logic|DPMKT2KRB8]] the same sentence is $\forall x_1 \exists y_1 \forall x_2 (\exists y_2 / \set{x_1, y_1}) \, \varphi$.
In [[dependence logic|DNAPTJ98WD]] it is $\forall x_1 \exists y_1 \forall x_2 \exists y_2 \, ({=}(x_2, y_2) \land \varphi)$.
Other names are "finite partially ordered quantifier" and "FPO prefix".
We write $\mathrm{FO}(Q_H)$ for first-order logic closed under the Henkin quantifier, with the usual connectives and quantifiers.

## Remarks

### Three sentences to know

The first sentence says that the domain is [[infinite|0PWE3BCHVJ]]:
$$\exists a \, Q_H x_1 x_2 y_1 y_2 \, \big( (x_1 = x_2 \leftrightarrow y_1 = y_2) \land y_1 \neq a \big).$$
At $x_1 = x_2$ the matrix forces $f = g$, and then it forces $f$ to be one-to-one and to miss $a$.
[[This example|4R3D37KQD8]] gives the details.

The second sentence says $|P| \le |R|$ for two unary relations $P$ and $R$:
$$Q_H x_1 x_2 y_1 y_2 \, \Big( \big( (P(x_1) \land P(x_2)) \to (x_1 = x_2 \leftrightarrow y_1 = y_2) \big) \land \big( P(x_1) \to R(y_1) \big) \Big).$$
The witness is a one-to-one map from $P$ into $R$, as [[this example|QWAM86B7NF]] shows.

The third sentence $\eta$ says that the domain is even or infinite:
$$\eta := Q_H x_1 x_2 y_1 y_2 \, \big( (x_1 = x_2 \leftrightarrow y_1 = y_2) \land y_1 \neq x_1 \land (x_2 = y_1 \to y_2 = x_1) \big).$$
Its witness is a function without fixed points that is its own inverse, and the L2 explanation checks it.

Every prenex first-order sentence is also a branching sentence, with a chain as its order.

### What it is not

Put the matrix of the infinity sentence under the linear prefix $\exists a \, \forall x_1 \exists y_1 \forall x_2 \exists y_2$.
The result is true in every structure with at least two elements, as [[this non-example|V24R6JC19Y]] shows.
The order of the quantifiers, not their list, carries the meaning.

"The domain is finite" is not expressed by any branching sentence with a first-order matrix.
Such a sentence is equivalent to an existential second-order sentence.
If that sentence had arbitrarily large finite models, the [[compactness theorem|1NR3HAWG9D]] would give it an infinite model.

### Branching sentences are existential second-order

Read the Skolem functions as function variables.
Then a branching sentence with a first-order matrix becomes an existential second-order sentence.
For the Henkin quantifier it is this sentence:
$$\exists f \, \exists g \, \forall x_1 \, \forall x_2 \, \varphi(x_1, x_2, f(x_1), g(x_2)).$$
Enderton and Walkoe proved the converse.
Every $\Sigma^1_1$ sentence is equivalent to a sentence with a finite partially ordered prefix and a first-order matrix.
So the two kinds of sentences have the same expressive power, in the full semantics.

The idea of the converse is this.
First Skolemize the first-order part, so that only function variables remain.
Then give each occurrence of a function its own copy, with its own block of universal variables.
Last, add equations that force the copies to agree, as the matrix of the infinity sentence forces $f = g$.

Three facts follow from the first-order case, after the function variables become new function symbols.
A set of branching sentences has a model if each finite subset has one.
A branching sentence with an infinite model has a countable model.
By [[Fagin's theorem|BG8Q0BYSQ3]], on finite structures the branching sentences define exactly the properties in NP.

### What FO(QH) gains and loses

The logic $\mathrm{FO}(Q_H)$ allows negation and nesting, so it goes beyond $\Sigma^1_1$.
The negation of the infinity sentence says that the domain is finite.
So $\mathrm{FO}(Q_H)$ does not have the compactness property.

The Henkin quantifier also defines "there are infinitely many", and the quantifiers that compare the sizes of two definable sets.
As a Lindström [[generalized quantifier|MFV98WTF4G]], it has type $\langle 4 \rangle$: it binds four variables in one formula.

### Why FO(QH) has no complete proof system

We reduce finite validity of first-order sentences to validity in $\mathrm{FO}(Q_H)$.

1. Let $\iota$ be the infinity sentence.
   With the axiom of choice, it holds exactly in the infinite structures.
2. Let $\psi$ be a first-order sentence.
   Then $\iota \lor \psi$ is valid if and only if $\psi$ holds in every finite structure, by step 1.
3. Suppose that the valid sentences of $\mathrm{FO}(Q_H)$ form a computably enumerable set.
   Then step 2 makes the finitely valid first-order sentences a computably enumerable set.
4. [[Trakhtenbrot's theorem|XP6FW2WDWT]] says that this set is not computably enumerable, for a vocabulary with a binary relation symbol.
   So the assumption of step 3 is false.
5. A sound, complete and effective proof system would list the valid sentences.
   So no such system exists for $\mathrm{FO}(Q_H)$.

### History

Leon Henkin introduced branching quantifiers in a talk at a symposium in Warsaw in 1959, published in 1961.
Enderton and Walkoe independently proved the equivalence with $\Sigma^1_1$ in 1970.
Jaakko Hintikka proposed branching readings of English sentences in 1973.

### Watch out

Do not read the Henkin prefix as the linear prefix $\forall x_1 \exists y_1 \forall x_2 \exists y_2$.
The two differ already on finite structures, as the non-example shows.

Do not say that $\mathrm{FO}(Q_H)$ equals $\Sigma^1_1$.
Only a branching prefix followed by a first-order matrix is $\Sigma^1_1$.
Negation and nesting give more, such as finiteness of the domain.

Do not forget the axiom of choice.
The infinity sentence says that some [[injective|09NWETVTNY]] function of the domain is not [[surjective|01RVCMSN5N]].
This is Dedekind-infinity, and it agrees with infinity under the axiom of choice.

### Try it

On the domain $\set{1, 2, 3, 4}$, find witnesses $f, g$ for the sentence $\eta$.
Take $f = g$ with $f(1) = 2$, $f(2) = 1$, $f(3) = 4$ and $f(4) = 3$.

Is the infinity sentence true in a structure with one element?
No: there $f(a_1) = a$ for every $a_1$, so $y_1 \neq a$ fails.

## Explanations

### L1 human

In a normal sentence of logic, each choice may depend on all earlier choices.
A branching quantifier lets us say that a choice depends only on some of them.
Picture two players in separate rooms.
The first player hears a number $x_1$ and answers with $y_1$.
The second player hears $x_2$ and answers with $y_2$, and neither player hears the other one's number.
They win if their answers satisfy a rule that involves all four numbers.
Such a game can force the players to follow one fixed one-to-one rule.
On a finite set such a rule cannot skip an element, while on an infinite set it can.

### L2 human

We check the sentence $\eta$ of the Remarks with its Skolem form.

1. By the Skolem form, $\eta$ holds if and only if there are $f, g$ such that, for all $a_1, a_2$, three conditions hold.
   They are $(a_1 = a_2 \leftrightarrow f(a_1) = g(a_2))$, $f(a_1) \neq a_1$, and $(a_2 = f(a_1) \to g(a_2) = a_1)$.
2. Take $a_1 = a_2 = a$.
   The first condition gives $f(a) = g(a)$, so $f = g$.
3. With $f = g$, the first condition says $a_1 = a_2 \leftrightarrow f(a_1) = f(a_2)$, so $f$ is injective.
4. Take $a_2 = f(a_1)$ in the third condition.
   It gives $f(f(a_1)) = a_1$, so $f$ is its own inverse.
5. The second condition says that $f$ has no fixed point, so $f$ splits the domain into pairs $\set{a, f(a)}$.
6. On $\set{1, 2, 3}$ such a splitting would make $3$ an even number, so $\eta$ is false there.

Check: on $\set{1, 2, 3, 4}$ the swap $1 \leftrightarrow 2$, $3 \leftrightarrow 4$ satisfies all three conditions, so $\eta$ is true there.
The typical use of the Skolem form is this: we read off the functions, then use the matrix to find their properties.
Watch out for step 2: the two functions are equal only because the matrix compares $y_1$ and $y_2$ at $x_1 = x_2$.

### L3 human

Branching quantifiers mark the point where dependence becomes a logical primitive.
[[Independence-friendly logic|DPMKT2KRB8]] generalizes them by slashed quantifiers.
[[Dependence logic|DNAPTJ98WD]] puts the pattern of dependence into atoms ${=}(\vec{x}, y)$, with team semantics.
On sentences, both logics have the same expressive power as $\Sigma^1_1$.
The [[game-theoretic semantics|D45Z7HETDA]] of these logics uses games of imperfect information.
In it, the Henkin quantifier is a game for two players of one team who cannot communicate.
In abstract model theory, $\mathrm{FO}(Q_H)$ is stronger than first-order logic.
So by [[Lindström's theorem|FYZ3CJGZYV]] it must lose compactness or the downward Löwenheim-Skolem property, and it loses compactness.
