---
tag: MFV98WTF4G
kind: concept
name: Generalized quantifier
aliases: [generalized-quantifiers, quantification-linguistics, quantifiers-linguistics]
msc: ["03C80", "03B65"]
topics: [MDHDYV8QZW]
audience: grad
uses: [086QKPF0A6, 983GZBQYT4, 0GHS47PDAQ, 0MSRQHCNN9, 0EBACQFAZW]
sources:
  - wikipedia: en:7959499@r1366721445
    locator: Generalized quantifier
    note: adopted
    mention: wikipedia://en/7959499
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Generalized_quantifier
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Generalized_quantifier
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Generalized_quantifier
    locator: Conservativity
  - url: https://en.wikipedia.org/wiki/Lindström_quantifier
    locator: Generalization of first-order quantifiers
  - url: https://en.wikipedia.org/wiki/Lindström_quantifier
    locator: As precursors to Lindström's theorem
same_as:
  wikidata: Q5532504
  wikipedia: Generalized quantifier
inventory: [48E6CEX9DA]
---

## Summary

A generalized quantifier (Lindström quantifier) of type $\langle n_1, \ldots, n_k \rangle$ is a class $Q$ of [[structures|983GZBQYT4]] $(M, R_1, \ldots, R_k)$ that is closed under isomorphism.
Here $M$ is a nonempty set and $R_i \subseteq M^{n_i}$ for each $i$.
For each set $M$ we write $Q_M$ for the set of tuples $(R_1, \ldots, R_k)$ with $(M, R_1, \ldots, R_k) \in Q$.
The logic $L(Q)$ is [[first-order logic|086QKPF0A6]] with one new formation rule.
Let $\varphi_1, \ldots, \varphi_k$ be formulas, and let each $\bar{x}_i$ be a tuple of $n_i$ distinct variables.
Then $Q \bar{x}_1 \ldots \bar{x}_k \, (\varphi_1, \ldots, \varphi_k)$ is a formula that binds $\bar{x}_i$ in $\varphi_i$.
It is true in $\mathcal{M}$ under an assignment $s$ when $(\varphi_1^{\mathcal{M}, s}, \ldots, \varphi_k^{\mathcal{M}, s}) \in Q_M$, where $\varphi_i^{\mathcal{M}, s} = \{ \bar{a} \in M^{n_i} : \mathcal{M} \models \varphi_i[s(\bar{a}/\bar{x}_i)] \}$.
The [[universal quantifier|0GHS47PDAQ]] and the [[existential quantifier|0MSRQHCNN9]] are the type $\langle 1 \rangle$ quantifiers $\{ (M, M) \}$ and $\{ (M, A) : A \neq \emptyset \}$.
Generalized quantifiers give a uniform way to strengthen first-order logic, and they are the standard test cases for the comparison of logics.

## Motivation

Mathematics uses quantifier words that first-order logic cannot express.
Examples are "there are infinitely many primes", "there are uncountably many transcendental numbers" and "most graphs on $n$ vertices are connected".
Each of these words says something about the size of a set of elements, and nothing about which elements they are.
The quantifiers $\forall$ and $\exists$ have the same nature: $\exists x \, \varphi$ says that the set defined by $\varphi$ is nonempty.
This is a property of sets that does not depend on the names of the elements.
Mostowski took any property of subsets that is invariant under bijections as a quantifier.
Lindström extended the idea from sets to relations and to several arguments, which covers "equally many", "is a well-ordering" and branching quantifiers.
The resulting logics $L(Q)$ form a family in which one can test which properties of first-order logic survive the addition of one new quantifier.

## Notation

The type lists the arities of the arguments: $\langle 1 \rangle$ for one set, $\langle 1, 1 \rangle$ for two sets, $\langle 2 \rangle$ for one binary relation.
A quantifier is monadic when all $n_i = 1$ and polyadic otherwise.
The main examples have standard names:

$$Q_0 = \{ (M, A) : A \text{ is infinite} \}, \qquad Q_1 = \{ (M, A) : A \text{ is uncountable} \},$$

$$Q^{R} = \{ (M, A) : |A| > |M \setminus A| \}, \qquad \mathrm{most} = \{ (M, A, B) : |A \cap B| > |A \setminus B| \}, \qquad I = \{ (M, A, B) : |A| = |B| \}.$$

More generally $Q_\alpha$ says "at least $\aleph_\alpha$ many", $Q^R$ is the Rescher quantifier "more than half", and $I$ is the Härtig quantifier "equally many".
The logics are written $L(Q_0)$, $L(Q_1)$ or $\mathrm{FO}(Q)$, and $L(Q_1, Q_2)$ for two added quantifiers.
Some authors write $\exists^{\geq \omega}$ or $\exists^{\infty}$ for $Q_0$, and $\exists^{\geq \aleph_1}$ for $Q_1$.
In linguistics, a type $\langle 1, 1 \rangle$ quantifier is a determiner, written $D(A)(B)$ or $D_M(A, B)$.

## Remarks

### The linguistic reading

In formal semantics, a noun phrase such as "every boy" denotes a set of sets: the sets $X$ with $\{ \text{boys} \} \subseteq X$.
A determiner such as "every", "some", "most" or "no" denotes a type $\langle 1, 1 \rangle$ quantifier.
This quantifier is a relation between the noun set $A$ and the predicate set $B$.
"Every boy sleeps" is true when $(A, B) \in \mathrm{every}_M$, that is, $A \subseteq B$.
This treatment gives a compositional semantics for sentences with quantifier words.
Barwise and Cooper proposed that every determiner of a natural language is conservative.
For example, "every boy sleeps" is equivalent to "every boy is a boy who sleeps".

### Examples

- $\exists^{\geq n} = \{ (M, A) : |A| \geq n \}$ ("at least $n$"). It is a generalized quantifier, but it adds nothing: $\exists^{\geq 2} x \, \varphi(x)$ is equivalent to $\exists x \, \exists y \, (x \neq y \land \varphi(x) \land \varphi(y))$.
- $Q_0$ ("infinitely many"). The sentence $Q_0 x \, (x = x)$ is true exactly in the infinite structures, and no first-order sentence has this property. [[This example|SD6TYGCEEB]] shows that $L(Q_0)$ is not compact.
- $Q_1$ ("uncountably many"). The sentence $Q_1 x \, (x = x)$ has only uncountable models, so $L(Q_1)$ fails the downward [[Löwenheim–Skolem theorem|484M0TZ1S7]].
- $\mathrm{most}$, of type $\langle 1, 1 \rangle$. The formula $\mathrm{most}\, x \, (\varphi(x), \psi(x))$ says that more elements satisfy $\varphi \land \psi$ than $\varphi \land \neg \psi$. It is not first-order definable even on finite structures; see [[this example|1C6CGH1G6A]].
- $W = \{ (M, R) : R \text{ is a well-ordering of } M \}$, of type $\langle 2 \rangle$. In $L(W)$ one sentence says that a binary relation is a well-ordering, which first-order logic cannot say.
- "There are at least two" and "more than half" are permutation invariant sets of subsets on a pure set. Each such set depends only on $|A|$ and $|M \setminus A|$, as [[this example|HPA3BKNZE1]] proves.

### Non-examples

- The family of intervals of $\mathbb{R}$ is not the $\mathbb{R}$-part of any generalized quantifier of type $\langle 1 \rangle$. A bijection of $\mathbb{R}$ maps $[0, 1]$ to a set that is not an interval; see [[this non-example|AQBW6RSRN9]].
- The family $\{ A \subseteq D : 0 \in A \}$ ("the object $0$ has the property") is not closed under permutations of $D$, because a permutation can move $0$; see [[this example|HPA3BKNZE1]].
- A set of sets that is defined on one domain only is not yet a generalized quantifier. The definition asks for a family $Q_M$ on every nonempty set $M$, with the families related by isomorphisms.

### Basic properties

- Isomorphism invariance of $Q$ makes isomorphic structures satisfy the same sentences of $L(Q)$, by induction on formulas.
- On a pure set $M$, a monadic quantifier of type $\langle 1 \rangle$ is determined by a condition on the two cardinals $|A|$ and $|M \setminus A|$.
- A type $\langle 1, 1 \rangle$ quantifier $D$ is conservative when $D_M(A, B) \iff D_M(A, A \cap B)$. The quantifiers "every", "some" and "most" are conservative; "only", with $\mathrm{only}_M(A, B) \iff B \subseteq A$, is not.
- Each type $\langle 1 \rangle$ quantifier $Q$ has a relativization $Q^{\mathrm{rel}}$ of type $\langle 1, 1 \rangle$, with $Q^{\mathrm{rel}}_M(A, B) \iff Q_A(A \cap B)$. For example $\mathrm{most} = (Q^R)^{\mathrm{rel}}$, since $|A \setminus (A \cap B)| = |A \setminus B|$.
- $L(Q_0)$ is not compact, and its set of valid sentences is not recursively enumerable.
- One sentence $\Psi$ of $L(Q_0)$ characterizes $(\mathbb{N}, <, 0, S, +, \times)$ up to isomorphism. It says that $<$ is a linear order with least element $0$, no greatest element, and finitely many elements below each element. It also states the recursion equations for $S$, $+$ and $\times$.
- So a first-order $\varphi$ is true in $\mathbb{N}$ exactly when $\Psi \to \varphi$ is valid, and true arithmetic is not recursively enumerable.
- Keisler's theorem (1970) is about a countable set of $L(Q_1)$-sentences in a countable vocabulary. The set has a model if and only if Keisler's proof system derives no contradiction from it. The axioms are those of first-order logic and a few axioms for $Q_1$.
- One of these axioms is $Q_1 x \, \exists y \, \varphi \to \exists y \, Q_1 x \, \varphi \lor Q_1 y \, \exists x \, \varphi$, which says that a countable union of countable sets is countable. Another is $\neg Q_1 x \, (x = y \lor x = z)$.
- So $L(Q_1)$ is countably compact: a countable set of sentences has a model when each finite subset has one. The reason is that a proof uses finitely many sentences.
- $L(Q_1)$ is not compact for uncountable sets of sentences. With constants $c_\alpha$ for $\alpha < \omega_1$, the set $\{ \neg Q_1 x \, (x = x) \} \cup \{ c_\alpha \neq c_\beta : \alpha < \beta < \omega_1 \}$ is finitely satisfiable and has no model.
- [[Lindström's theorem|FYZ3CJGZYV]] explains these facts. A regular logic that properly extends first-order logic cannot have both compactness and the downward Löwenheim-Skolem property. $L(Q_0)$ keeps the second property and loses compactness; $L(Q_1)$ loses the second property and keeps countable compactness.

### History

Andrzej Mostowski introduced quantifiers of type $\langle 1 \rangle$ defined by cardinality conditions in 1957.
Per Lindström gave the general definition for relations of any arity in 1966, and he proved his characterization of first-order logic in 1969.
Jerome Keisler published the completeness theorem for $L(Q_1)$ in 1970, in the paper "Logic with the quantifier 'there exist uncountably many'".
Jon Barwise and Robin Cooper applied generalized quantifiers to the semantics of natural language in 1981.

### Common errors

- To think that every new quantifier increases expressive power. The quantifiers $\exists^{\geq n}$ and "exactly $n$" are definable in first-order logic.
- To think that $L(Q_1)$ is compact. It is only countably compact; the counterexample above uses $\aleph_1$ constants.
- To confuse "most $A$ are $B$" with "most elements are $B$". The first is the type $\langle 1, 1 \rangle$ quantifier $\mathrm{most}$, and the second is the type $\langle 1 \rangle$ quantifier $Q^R$ on the whole domain.

## Explanations

### L1 human

The words "all" and "some" are quantifiers: they tell how many objects have a property.
Ordinary language has many more such words: "at least three", "infinitely many", "most", "as many as".
"Most students passed" is true when the students who passed outnumber the students who failed.
With $10$ students and $6$ passes it is true, with $5$ passes it is false.
Such a word only counts; it does not care which students passed.
A generalized quantifier is any such counting word, made exact as a property of sets.
Logicians add one of them to ordinary logic and study what the new logic can say.

### L2 human

We evaluate $\mathrm{most}\, x \, (Px, Ex)$ in the structure with domain $M = \{1, 2, \ldots, 10\}$, where $Px$ means "$x$ is prime" and $Ex$ means "$x$ is odd".

1. The set defined by $Px$ is $A = \{2, 3, 5, 7\}$.
2. The set defined by $Ex$ is $B = \{1, 3, 5, 7, 9\}$.
3. Then $A \cap B = \{3, 5, 7\}$ and $A \setminus B = \{2\}$.
4. Since $|A \cap B| = 3 > 1 = |A \setminus B|$, the pair $(A, B)$ is in $\mathrm{most}_M$, and the formula is true: most primes up to $10$ are odd.
5. The formula $Q^R x \, Ex$ asks whether $|B| = 5 > 5 = |M \setminus B|$. This is false, so "more than half of the elements are odd" fails.

The typical use is to state a property that first-order logic cannot state, and then to ask which first-order theorems still hold.
A trap is to apply first-order compactness to $L(Q_0)$.
The theory "finite, and at least $n$ elements for each $n$" is finitely satisfiable and has no model.

### L3 human

Generalized quantifiers are the simplest examples of [[abstract logical systems|RQXV7PM2WT]].
Each logic $L(Q)$ is regular, so [[Lindström's theorem|FYZ3CJGZYV]] applies: if $L(Q)$ is stronger than first-order logic, it fails compactness or the downward Löwenheim-Skolem property.
The logic $L(Q_0)$ lies inside the [[infinitary logic|PQG7VAZ1R2]] $L_{\omega_1 \omega}$, since $Q_0 x \, \varphi$ is the countable conjunction of the formulas $\exists^{\geq n} x \, \varphi$.
This is why $L(Q_0)$ keeps the downward Löwenheim-Skolem property.
The logic $L(Q_1)$ behaves like first-order logic in its proof theory, with a completeness theorem, and its model theory involves two-cardinal questions.

Lindström's definition also includes branching quantifiers.
The Henkin quantifier is the type $\langle 4 \rangle$ quantifier of all $(M, R)$ such that some functions $f, g$ satisfy $R(x, f(x), u, g(u))$ for all $x, u$.
A second-order quantifier $\exists X$ is not of this form, because it binds a relation variable and not a tuple of element variables.
Still, the quantifiers $W$ and $I$ are definable in [[second-order logic|G6X7SZSNC5]] with full semantics, so $L(W)$ and $L(I)$ are sublogics of it.
On finite structures, logics with generalized quantifiers are studied in [[finite model theory|4XRVJE0KAN]]; there the quantifier $\mathrm{most}$ is still not definable in first-order logic.
In team semantics, generalized quantifiers have also been added to [[dependence logic|DNAPTJ98WD]].
