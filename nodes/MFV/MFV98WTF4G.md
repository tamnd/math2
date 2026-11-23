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

Words such as "infinitely many", "most" and "as many as" are quantifiers, but first-order logic has only "all" and "some".
A generalized quantifier makes such a word exact as a class of structures.
Adding one to first-order logic gives a new logic, and we can ask which first-order theorems survive.

A generalized quantifier (Lindström quantifier) of type $\langle n_1, \ldots, n_k \rangle$ is a class $Q$ of [[structures|983GZBQYT4]] $(M, R_1, \ldots, R_k)$ that is closed under isomorphism.
Here $M$ is a nonempty set and $R_i \subseteq M^{n_i}$ for each $i$.
For each set $M$, we write $Q_M$ for the set of tuples $(R_1, \ldots, R_k)$ with $(M, R_1, \ldots, R_k) \in Q$.
The logic $L(Q)$ is [[first-order logic|086QKPF0A6]] with one new formation rule.
Let $\varphi_1, \ldots, \varphi_k$ be formulas, and let each $\bar{x}_i$ be a tuple of $n_i$ distinct variables.
Then $Q \bar{x}_1 \ldots \bar{x}_k \, (\varphi_1, \ldots, \varphi_k)$ is a formula that binds $\bar{x}_i$ in $\varphi_i$.
It is true in $\mathcal{M}$ under an assignment $s$ when $(\varphi_1^{\mathcal{M}, s}, \ldots, \varphi_k^{\mathcal{M}, s}) \in Q_M$.
Here $\varphi_i^{\mathcal{M}, s} = \{ \bar{a} \in M^{n_i} : \mathcal{M} \models \varphi_i[s(\bar{a}/\bar{x}_i)] \}$ is the relation that $\varphi_i$ defines.
The [[universal quantifier|0GHS47PDAQ]] is the type $\langle 1 \rangle$ class of all $(M, M)$.
The [[existential quantifier|0MSRQHCNN9]] is the type $\langle 1 \rangle$ class of all $(M, A)$ with $A \neq \emptyset$.

## Motivation

Mathematics uses quantifier words that first-order logic cannot express.
Examples are "there are infinitely many primes", "there are uncountably many transcendental numbers" and "most graphs on $n$ vertices are connected".
Each of these words says something about the size of a set, and nothing about which elements are in it.
The quantifiers $\forall$ and $\exists$ have the same nature: $\exists x \, \varphi$ says that the set that $\varphi$ defines is nonempty.
This is a property of sets that does not depend on the names of the elements.

Mostowski took any property of subsets that is invariant under bijections as a quantifier.
Lindström extended the idea from sets to relations and to several arguments.
This covers "equally many", "is a well-ordering" and the branching quantifiers.
The logics $L(Q)$ form a family in which we can test which properties of first-order logic survive one new quantifier.
They are the standard test cases for the comparison of logics.

## Notation

The type lists the arities of the arguments: $\langle 1 \rangle$ for one set, $\langle 1, 1 \rangle$ for two sets, and $\langle 2 \rangle$ for one binary relation.
A quantifier is monadic when all $n_i = 1$, and polyadic otherwise.
The main examples have standard names:
$$Q_0 = \{ (M, A) : A \text{ is infinite} \}, \qquad Q_1 = \{ (M, A) : A \text{ is uncountable} \},$$
$$Q^{R} = \{ (M, A) : |A| > |M \setminus A| \}, \qquad \mathrm{most} = \{ (M, A, B) : |A \cap B| > |A \setminus B| \}, \qquad I = \{ (M, A, B) : |A| = |B| \}.$$
More generally, $Q_\alpha$ says "at least $\aleph_\alpha$ many".
$Q^R$ is the Rescher quantifier "more than half", and $I$ is the Härtig quantifier "equally many".
The logics are written $L(Q_0)$, $L(Q_1)$ or $\mathrm{FO}(Q)$, and $L(Q_1, Q_2)$ for two added quantifiers.
Some authors write $\exists^{\geq \omega}$ or $\exists^{\infty}$ for $Q_0$, and $\exists^{\geq \aleph_1}$ for $Q_1$.
In linguistics, a type $\langle 1, 1 \rangle$ quantifier is a determiner, written $D(A)(B)$ or $D_M(A, B)$.

## Remarks

### A first computation

We evaluate $\mathrm{most}\, x \, (Px, Ox)$ on the domain $M = \{1, 2, \ldots, 10\}$.
Here $Px$ means "$x$ is prime" and $Ox$ means "$x$ is odd".
The two formulas define the sets $A = \{2, 3, 5, 7\}$ and $B = \{1, 3, 5, 7, 9\}$.
We compare the two parts of $A$:
$$A \cap B = \{3, 5, 7\}, \qquad A \setminus B = \{2\}.$$
Since $3 > 1$, the pair $(A, B)$ is in $\mathrm{most}_M$, and the formula is true: most primes up to $10$ are odd.
Check: $|A \cap B| + |A \setminus B| = 3 + 1 = 4 = |A|$.

The formula $Q^R x \, Ox$ asks a different question, about the whole domain.
It asks whether $|B| > |M \setminus B|$, that is, whether $5 > 5$.
This is false, so "more than half of the elements are odd" fails.

### Quantifier words in language

In formal semantics, a noun phrase such as "every boy" denotes a set of sets: the sets $X$ with $\{ \text{boys} \} \subseteq X$.
A determiner such as "every", "some", "most" or "no" denotes a type $\langle 1, 1 \rangle$ quantifier.
This quantifier is a relation between the noun set $A$ and the predicate set $B$.
"Every boy sleeps" is true when $(A, B) \in \mathrm{every}_M$, that is, when $A \subseteq B$.
This treatment gives a compositional semantics for sentences with quantifier words.
Barwise and Cooper proposed that every determiner of a natural language is conservative.
For example, "every boy sleeps" says the same as "every boy is a boy who sleeps".

### Which quantifiers add power

Some generalized quantifiers add nothing to first-order logic.
"At least $n$" is the class $\exists^{\geq n} = \{ (M, A) : |A| \geq n \}$, and first-order logic already says it.
For example, $\exists^{\geq 2} x \, \varphi(x)$ is equivalent to $\exists x \, \exists y \, (x \neq y \land \varphi(x) \land \varphi(y))$.

Others add real power.
The sentence $Q_0 x \, (x = x)$ is true exactly in the infinite structures, and no first-order sentence has this property.
[[This example|SD6TYGCEEB]] shows that $L(Q_0)$ is not compact.
The sentence $Q_1 x \, (x = x)$ has only uncountable models, so $L(Q_1)$ fails the downward [[Löwenheim–Skolem theorem|484M0TZ1S7]].
The formula $\mathrm{most}\, x \, (\varphi(x), \psi(x))$ says that more elements satisfy $\varphi \land \psi$ than $\varphi \land \neg \psi$.
It is not first-order definable even on finite structures, as [[this example|1C6CGH1G6A]] shows.
The type $\langle 2 \rangle$ quantifier $W = \{ (M, R) : R \text{ is a well-ordering of } M \}$ lets one sentence say that a relation is a well-ordering.

On a pure set, a type $\langle 1 \rangle$ quantifier depends only on the two cardinals $|A|$ and $|M \setminus A|$, as [[this example|HPA3BKNZE1]] proves.
"At least two" and "more than half" are of this kind.

### What it is not

The family of intervals of $\mathbb{R}$ is not the $\mathbb{R}$-part of any type $\langle 1 \rangle$ generalized quantifier.
A bijection of $\mathbb{R}$ can map $[0, 1]$ to a set that is not an interval, as [[this non-example|AQBW6RSRN9]] shows.

The family $\{ A \subseteq D : 0 \in A \}$, "the object $0$ has the property", is not closed under permutations of $D$.
A permutation can move $0$, as [[this example|HPA3BKNZE1]] notes.

A family of sets on one domain only is not yet a generalized quantifier.
The definition asks for a family $Q_M$ on every nonempty set $M$, and isomorphisms relate the families on different sets.

### Conservativity and relativization

Isomorphism invariance of $Q$ makes isomorphic structures satisfy the same sentences of $L(Q)$, by induction on formulas.

A type $\langle 1, 1 \rangle$ quantifier $D$ is conservative when $D_M(A, B) \iff D_M(A, A \cap B)$.
The quantifiers "every", "some" and "most" are conservative.
The quantifier "only", with $\mathrm{only}_M(A, B) \iff B \subseteq A$, is not, as the L2 explanation shows.

Each type $\langle 1 \rangle$ quantifier $Q$ has a relativization $Q^{\mathrm{rel}}$ of type $\langle 1, 1 \rangle$.
It is given by $Q^{\mathrm{rel}}_M(A, B) \iff Q_A(A \cap B)$, so it applies $Q$ inside the set $A$.
For example, $\mathrm{most} = (Q^R)^{\mathrm{rel}}$, because $A \setminus (A \cap B) = A \setminus B$.
Every relativization is conservative.

### Infinitely many

The logic $L(Q_0)$ is not compact, and its set of valid sentences is not computably enumerable.
The second fact comes from one sentence $\Psi$ of $L(Q_0)$ that characterizes $(\mathbb{N}, <, 0, S, +, \times)$ up to isomorphism.
$\Psi$ says that $<$ is a linear order with least element $0$ and no greatest element.
It says that each element has only finitely many elements below it, with the formula $\neg Q_0 y \, (y < x)$.
Then the order has type $\omega$.
$\Psi$ also says that $S x$ is the next element after $x$, and it states the recursion equations for $+$ and $\times$.
So a first-order sentence $\varphi$ is true in $\mathbb{N}$ exactly when $\Psi \to \varphi$ is valid.
If the valid sentences were computably enumerable, true arithmetic would be computably enumerable, and it is not.

### Uncountably many

The logic $L(Q_1)$ behaves much more like first-order logic.
Keisler's completeness theorem is about a countable set of $L(Q_1)$-sentences in a countable vocabulary.
The set has a model if and only if Keisler's proof system derives no contradiction from it.
The axioms are those of first-order logic and a few axioms for $Q_1$.
One of them is $\neg Q_1 x \, (x = y \lor x = z)$, which says that a set with at most two elements is countable.
Another says that a countable union of countable sets is countable:
$$Q_1 x \, \exists y \, \varphi \to \big( \exists y \, Q_1 x \, \varphi \lor Q_1 y \, \exists x \, \varphi \big).$$
So $L(Q_1)$ is countably compact: a countable set of sentences has a model when each finite subset has one.
The reason is that a derivation uses only finitely many sentences.

$L(Q_1)$ is not compact for uncountable sets of sentences.
Take constants $c_\alpha$ for $\alpha < \omega_1$, and this set:
$$\{ \neg Q_1 x \, (x = x) \} \cup \{ c_\alpha \neq c_\beta : \alpha < \beta < \omega_1 \}.$$
A finite subset names only finitely many distinct constants, so a countable model satisfies it.
The whole set asks for $\aleph_1$ distinct elements in a countable domain, so it has no model.

### Where it sits among logics

[[Lindström's theorem|FYZ3CJGZYV]] explains these facts.
A regular logic that properly extends first-order logic cannot have both compactness and the downward Löwenheim-Skolem property.
$L(Q_0)$ keeps the second property and loses compactness.
$L(Q_1)$ loses the second property and keeps countable compactness.

### Watch out

Not every new quantifier adds expressive power.
The quantifiers $\exists^{\geq n}$ and "exactly $n$" are definable in first-order logic.

Do not call $L(Q_1)$ compact.
It is only countably compact, and the counterexample above uses $\aleph_1$ constants.

Do not confuse "most $A$ are $B$" with "most elements are $B$".
The first is the type $\langle 1, 1 \rangle$ quantifier $\mathrm{most}$, and the second is the type $\langle 1 \rangle$ quantifier $Q^R$ on the whole domain.

### History

Andrzej Mostowski introduced quantifiers of type $\langle 1 \rangle$ defined by cardinality conditions in 1957.
Per Lindström gave the general definition for relations of any arity in 1966, and he proved his characterization of first-order logic in 1969.
Jerome Keisler published the completeness theorem for $L(Q_1)$ in 1970, in the paper "Logic with the quantifier 'there exist uncountably many'".
Jon Barwise and Robin Cooper applied generalized quantifiers to the semantics of natural language in 1981.

### Try it

Is "exactly two" a quantifier that adds power to first-order logic?
No: "exactly two $x$ satisfy $\varphi$" is $\exists x \, \exists y \, \big(x \neq y \land \varphi(x) \land \varphi(y) \land \forall z \, (\varphi(z) \to z = x \lor z = y)\big)$.

Is the Härtig quantifier $I$ conservative?
No: take $A = \{1\}$ and $B = \{2\}$.
Then $|A| = |B|$, but $A \cap B = \emptyset$, so $|A| \neq |A \cap B|$.

Which determiner is the relativization of $\exists$?
It is "some": $\exists^{\mathrm{rel}}_M(A, B)$ holds exactly when $A \cap B \neq \emptyset$.

## Explanations

### L1 human

The words "all" and "some" are quantifiers: they tell how many objects have a property.
Ordinary language has many more such words: "at least three", "infinitely many", "most" and "as many as".
"Most students passed" is true when the students who passed outnumber the students who failed.
With $10$ students and $6$ passes it is true, and with $5$ passes it is false.
Such a word only counts, and it does not care which students passed.
A generalized quantifier is any such counting word, made exact as a property of sets.
Logicians add one of them to ordinary logic and study what the new logic can say.

### L2 human

We show that the determiner "only" is not conservative, with $\mathrm{only}_M(A, B) \iff B \subseteq A$.

1. Take $M = \{1, 2, 3\}$, with $A = \{1, 2\}$ and $B = \{2, 3\}$.
2. Then $B \not\subseteq A$, because $3 \in B$ and $3 \notin A$, so $\mathrm{only}_M(A, B)$ is false.
3. Now replace $B$ by $A \cap B = \{2\}$.
   Since $\{2\} \subseteq \{1, 2\}$, the statement $\mathrm{only}_M(A, A \cap B)$ is true.
4. The two answers differ, so "only" is not conservative.
   Check: "only boys sleep" can be false while "only boys are boys who sleep" is always true.

The typical use of conservativity is to test whether a word can be a determiner of a natural language.
"Only" is usually analyzed as a different kind of word for this reason.
Watch out: conservativity is about the first argument $A$, so the order of the two arguments matters.

### L3 human

Generalized quantifiers give the simplest examples of [[abstract logical systems|RQXV7PM2WT]].
The logics $L(Q_0)$ and $L(Q_1)$ are regular, so [[Lindström's theorem|FYZ3CJGZYV]] applies to them.
Each of them is stronger than first-order logic, so each fails compactness or the downward Löwenheim-Skolem property.
The logic $L(Q_0)$ lies inside the [[infinitary logic|PQG7VAZ1R2]] $L_{\omega_1 \omega}$, since $Q_0 x \, \varphi$ is the countable conjunction of the formulas $\exists^{\geq n} x \, \varphi$.
This is why $L(Q_0)$ keeps the downward Löwenheim-Skolem property.
The logic $L(Q_1)$ has a completeness theorem like first-order logic, and its model theory involves two-cardinal questions.

Lindström's definition also includes branching quantifiers.
The Henkin quantifier is the type $\langle 4 \rangle$ class of all $(M, R)$ for which some functions $f, g \colon M \to M$ satisfy $R(x, f(x), u, g(u))$ for all $x, u$.
A second-order quantifier $\exists X$ is not of this form, because it binds a relation variable and not a tuple of element variables.
Still, the quantifiers $W$ and $I$ are definable in [[second-order logic|G6X7SZSNC5]] with the full semantics, so $L(W)$ and $L(I)$ are sublogics of it.
On finite structures, logics with generalized quantifiers are studied in [[finite model theory|4XRVJE0KAN]].
There the quantifier $\mathrm{most}$ is still not definable in first-order logic.
In team semantics, generalized quantifiers have also been added to [[dependence logic|DNAPTJ98WD]].
