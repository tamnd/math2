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

A branching quantifier, or partially ordered quantifier prefix, is a finite set of quantifiers $\forall x_i$ and $\exists y_j$ with a strict partial order on them.
Each existential variable $y_j$ may depend only on the universal variables that come before it in the order.
The simplest case is the Henkin quantifier
$$\begin{pmatrix} \forall x_1 & \exists y_1 \\ \forall x_2 & \exists y_2 \end{pmatrix} \varphi(x_1, x_2, y_1, y_2),$$
which is true in a [[structure|983GZBQYT4]] $\mathcal{M}$ if and only if there are functions $f, g : M \to M$ with $\mathcal{M} \models \varphi(a_1, a_2, f(a_1), g(a_2))$ for all $a_1, a_2 \in M$.
So $y_1$ depends only on $x_1$, and $y_2$ depends only on $x_2$.
In general, a branching sentence is true when Skolem functions exist that take as arguments only the allowed universal variables.
Branching quantifiers matter because they extend [[first-order logic|086QKPF0A6]] by changing only the pattern of dependence, and this change already gives the full power of existential second-order logic.

## Motivation

In first-order logic the quantifiers of a prefix form a line.
In $\forall x_1 \exists y_1 \forall x_2 \exists y_2\, \varphi$, the [[Skolem normal form|GCPQGMJYEV]] replaces $y_1$ by $f(x_1)$ and $y_2$ by $g(x_1, x_2)$, so $y_2$ may depend on $x_1$.
Some statements need $y_2$ to depend on $x_2$ alone.
A natural language example of Hintikka is "some relative of each villager and some relative of each townsman hate each other".
On one reading, the relative of the villager is chosen from the villager only, and the relative of the townsman from the townsman only.
No linear order of the four quantifiers gives this pattern.
In every such order, one of $y_1$ and $y_2$ comes after both universal quantifiers, so it may depend on both.
Henkin's idea is to write the quantifiers in a partial order, so that each branch carries its own dependence.

## Notation

Henkin wrote a branching prefix as a matrix of quantifiers, with one row for each branch, as in the Summary.
The Henkin quantifier is also written $Q_H x_1 x_2 y_1 y_2\, \varphi$ or $H x_1 x_2 y_1 y_2\, \varphi$.
In [[independence-friendly logic|DPMKT2KRB8]] the same sentence is $\forall x_1 \exists y_1 \forall x_2 (\exists y_2 / \set{x_1, y_1})\, \varphi$.
In [[dependence logic|DNAPTJ98WD]] it is $\forall x_1 \exists y_1 \forall x_2 \exists y_2\, ({=}(x_2, y_2) \land \varphi)$.
The literature also uses the names "finite partially ordered quantifier" and "FPO prefix", and $\mathrm{FO}(Q_H)$ for first-order logic closed under the Henkin quantifier.

## Remarks

### Examples

- Infinity: the sentence $\exists a\, Q_H x_1 x_2 y_1 y_2\, ((x_1 = x_2 \leftrightarrow y_1 = y_2) \land y_1 \neq a)$ is true exactly in the structures with an [[infinite|0PWE3BCHVJ]] domain; see [[this example|4R3D37KQD8]].
- Comparing sizes: the sentence $Q_H x_1 x_2 y_1 y_2\, (((P(x_1) \land P(x_2)) \to (x_1 = x_2 \leftrightarrow y_1 = y_2)) \land (P(x_1) \to R(y_1)))$ says $|P| \leq |R|$; see [[this example|QWAM86B7NF]].
- Even or infinite size: the sentence $Q_H x_1 x_2 y_1 y_2\, ((x_1 = x_2 \leftrightarrow y_1 = y_2) \land y_1 \neq x_1 \land (x_2 = y_1 \to y_2 = x_1))$ says that some function without fixed points is its own inverse. A finite domain has such a function exactly when its size is even.
- Every prenex first-order sentence is a branching sentence whose order is a chain. With the axiom of choice, the Skolem reading agrees with the usual reading.

### Non-examples

- The linear sentence $\exists a\, \forall x_1 \exists y_1 \forall x_2 \exists y_2\, ((x_1 = x_2 \leftrightarrow y_1 = y_2) \land y_1 \neq a)$ uses the same matrix as the infinity sentence. It is true in every structure with at least two elements; see [[this non-example|V24R6JC19Y]].
- "The domain is finite" is not expressible by any branching sentence with a first-order matrix. Such a sentence is equivalent to an existential second-order sentence, and the [[compactness theorem|1NR3HAWG9D]] gives an infinite model to any such sentence with arbitrarily large finite models.

### Basic properties

- Skolem form: a branching sentence with a first-order matrix is equivalent to an existential second-order sentence. For the Henkin quantifier it is $\exists f \exists g\, \forall x_1 \forall x_2\, \varphi(x_1, x_2, f(x_1), g(x_2))$.
- Enderton and Walkoe proved the converse: every existential second-order sentence ($\Sigma^1_1$ sentence) is equivalent to a sentence with a finite partially ordered prefix and a first-order matrix. So branching sentences and $\Sigma^1_1$ sentences have the same expressive power, in the full semantics.
- The idea of the converse: Skolemize the first-order part, so that only function variables remain. Then give each occurrence of a function its own copy, with its own block of universal variables, and add equations that force the copies to agree.
- By [[Fagin's theorem|BG8Q0BYSQ3]], on finite structures the branching sentences define exactly the properties in NP.
- A set of branching sentences has a model if each finite subset has one, and a branching sentence with an infinite model has a countable model. Both facts come from the first-order case, after the function variables become new function symbols.
- The logic $\mathrm{FO}(Q_H)$ is closed under negation. So it also expresses "the domain is finite", and it has neither the compactness property nor a complete proof system.
- The Henkin quantifier defines the quantifier "there are infinitely many", and the quantifiers that compare the sizes of two definable sets. It is itself a Lindström [[generalized quantifier|MFV98WTF4G]] of type $(4)$.

### Why FO(QH) has no complete proof system

1. Let $\iota$ be the infinity sentence of the first example. Its negation $\neg \iota$ is a sentence of $\mathrm{FO}(Q_H)$ that holds exactly in the finite structures.
2. A first-order sentence $\psi$ holds in all finite structures if and only if the sentence $\iota \lor \psi$ is valid.
3. Suppose that the valid sentences of $\mathrm{FO}(Q_H)$ form a recursively enumerable set. Then step 2 makes the set of finitely valid first-order sentences recursively enumerable.
4. Trakhtenbrot's theorem says that this set is not recursively enumerable, for a vocabulary with a binary relation symbol. So the assumption of step 3 is false.
5. A complete and effective proof system would list the valid sentences, so no such system exists for $\mathrm{FO}(Q_H)$.

### History

Leon Henkin introduced branching quantifiers in a paper given at a symposium in Warsaw in 1959 and published in 1961.
Enderton and Walkoe independently proved the equivalence with $\Sigma^1_1$ in 1970, and Hintikka proposed branching readings of English sentences in 1973.

### Common errors

- To read the Henkin prefix as the linear prefix $\forall x_1 \exists y_1 \forall x_2 \exists y_2$. The two differ already in finite structures, as the non-example shows.
- To say that $\mathrm{FO}(Q_H)$ equals $\Sigma^1_1$. Only the sentences of the form "branching prefix, then a first-order matrix" are $\Sigma^1_1$; negation and nesting give more, such as finiteness of the domain.
- To forget the axiom of choice. The infinity sentence says that some [[injective|09NWETVTNY]] function is not [[surjective|01RVCMSN5N]]. This is Dedekind-infinity, which agrees with infinity under the axiom of choice.

## Explanations

### L1 human

In a normal sentence of logic, each choice may depend on all earlier choices.
A branching quantifier lets us say that a choice depends only on some of them.
Picture two players in separate rooms.
The first player is told a number $x_1$ and answers with $y_1$; the second player is told $x_2$ and answers with $y_2$.
Neither player hears the other one's number.
They win if their answers satisfy a rule that involves all four numbers.
Such games can force the players to follow a fixed one-to-one rule, and on a finite set such a rule cannot skip an element, while on an infinite set it can.

### L2 human

We check the "even or infinite" sentence $\eta = Q_H x_1 x_2 y_1 y_2\, ((x_1 = x_2 \leftrightarrow y_1 = y_2) \land y_1 \neq x_1 \land (x_2 = y_1 \to y_2 = x_1))$.

1. By the Skolem form, $\eta$ holds if and only if there are $f, g$ with $(a_1 = a_2 \leftrightarrow f(a_1) = g(a_2))$, $f(a_1) \neq a_1$, and $(a_2 = f(a_1) \to g(a_2) = a_1)$ for all $a_1, a_2$.
2. Take $a_1 = a_2 = a$. The first condition gives $f(a) = g(a)$, so $f = g$.
3. With $f = g$, the first condition says $a_1 = a_2 \leftrightarrow f(a_1) = f(a_2)$, so $f$ is injective.
4. Take $a_2 = f(a_1)$ in the third condition. It gives $f(f(a_1)) = a_1$, so $f$ is its own inverse.
5. The second condition says that $f$ has no fixed point. So $f$ splits the domain into pairs $\set{a, f(a)}$.
6. On $\set{1, 2, 3, 4}$, the function $f$ that swaps $1$ with $2$ and $3$ with $4$, with $g = f$, satisfies all conditions, so $\eta$ is true.
7. On $\set{1, 2, 3}$, a splitting into pairs would make $3$ even, so $\eta$ is false.

The typical use of the Skolem form is this: we read off the functions, then use the matrix to derive their properties.
A trap is step 2: the two functions are equal only because the matrix compares $y_1$ and $y_2$ at $x_1 = x_2$.

### L3 human

Branching quantifiers mark the point where dependence becomes a logical primitive.
[[Independence-friendly logic|DPMKT2KRB8]] generalizes them by slashed quantifiers, and [[dependence logic|DNAPTJ98WD]] isolates the dependence pattern in atoms ${=}(\vec{x}, y)$ with team semantics; on sentences, both have the same expressive power as $\Sigma^1_1$.
The [[game-theoretic semantics|D45Z7HETDA]] of these logics uses games of imperfect information, and the Henkin quantifier corresponds to two players who cannot communicate.
In abstract model theory, $\mathrm{FO}(Q_H)$ is a logic stronger than first-order logic, so by [[Lindström's theorem|FYZ3CJGZYV]] it must lose compactness or the downward Löwenheim-Skolem property; it loses compactness.
