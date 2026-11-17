---
tag: NZ42PS2P1A
kind: concept
name: Equivalent definitions
aliases: [equivalent-definition, characterization]
msc: ["00A35"]
topics: [BP0WAF23HB]
audience: ug1
uses: [8ZCZ3HW91Z, 0B94TKFQJX, 0S6GMNJ62Y]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalent_definitions_of_mathematical_structures
    locator: Mathematical practice
  - url: https://en.wikipedia.org/wiki/Prime_number
    locator: Prime elements of a ring
  - url: https://en.wikipedia.org/wiki/Compact_space
    locator: Characterization
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Definition in terms of limits of sequences
---

## Summary

Two definitions of one notion are equivalent when they single out exactly the same objects of a given kind.
In symbols, conditions $C_1$ and $C_2$ on objects $x$ of a kind $K$ are equivalent when $C_1(x) \iff C_2(x)$ for each $x$ of kind $K$.
This equivalence is a theorem, and it needs a [[proof|0B94TKFQJX]] in both directions.
Authors choose one condition as the primary [[definition|8ZCZ3HW91Z]], and the others become theorems called characterizations.
Equivalent definitions matter because each one makes different facts easy to prove, and a proof may switch to the most convenient one.

## Motivation

A mathematical notion often appears in several places before anyone sees that it is one notion.
For example, a closed bounded interval $[a, b]$ has three useful properties.
Each sequence in it has a subsequence that converges to a point of the interval.
Each cover of it by open intervals has a finite subcover.
And it is closed and bounded.
In $\mathbb{R}^n$ the three properties hold for the same sets, by the [[Heine-Borel theorem|07PFYV65MB]] and the [[Bolzano-Weierstrass theorem|0KDJD249DT]].
So they are three definitions of one notion, [[compactness|0TVJZYB6SH]], and a proof can use whichever is easiest.
In general metric spaces only the first two agree, and in general topological spaces the open cover property is the one that is kept.

## Notation

1. "The following are equivalent" (TFAE), followed by a numbered list of conditions, announces a theorem of equivalence.
2. The proof of a TFAE theorem with conditions (1) to (n) often shows the cycle (1) $\Rightarrow$ (2) $\Rightarrow \cdots \Rightarrow$ (n) $\Rightarrow$ (1).
3. "$C_2$ characterizes $P$" and "$P$ is characterized by $C_2$" mean that $C_2$ is equivalent to the definition of $P$.

## Remarks

### Equivalence depends on the setting

Two conditions can be equivalent for the objects of one kind and different for the objects of a larger kind.
The words "for each $x$ of kind $K$" are part of the theorem.

1. For integers greater than $1$, "only the divisors $1$ and $p$" and "$p \mid ab$ implies $p \mid a$ or $p \mid b$" are equivalent, see [[two definitions of a prime number|787PD6B171]].
2. In the ring $\mathbb{Z}[\sqrt{-5}]$, the same two conditions [[define different classes of elements|5BM35ES8WK]].
3. For functions $\mathbb{R} \to \mathbb{R}$, the epsilon-delta and the sequential definitions of continuity are equivalent, see [[the two definitions of continuity|A4C3JY380W]]. For maps between general topological spaces they differ.
4. For metric spaces, compactness and sequential compactness are equivalent. For general topological spaces they differ.

### How an equivalence is proved

For two conditions, prove $C_1 \Rightarrow C_2$ and $C_2 \Rightarrow C_1$.
For $n$ conditions, a cycle of $n$ implications is enough, because implications compose.
Each implication must use only the hypotheses and results that do not depend on the conclusion.
A proof that uses a theorem whose proof assumed the other definition is circular.

### Choosing the primary definition

There is no rule, but authors weigh these points.

1. Generality. The definition that still works in the larger setting is often chosen. Ring theory calls an element prime when it has the divisor property, because this property gives the useful notion in general rings.
2. Ease of checking. A definition that is easy to test on examples helps beginners. School books define primes by their divisors.
3. Ease of use in proofs. Analysis books often define continuity by epsilon and delta, because estimates are then direct.
4. Tradition and formalization. Mathlib picks one definition for each notion, and it proves the others as lemmas of the form "iff".

Different books choose differently.
A reader must check which condition a book takes as the definition, because the other conditions are then theorems that need proofs.

### Examples

1. [[Two definitions of a prime number|787PD6B171]]: by divisors, and by the divisor property $p \mid ab \Rightarrow p \mid a$ or $p \mid b$.
2. [[The epsilon-delta and the sequential definitions of continuity|A4C3JY380W]] for functions $\mathbb{R} \to \mathbb{R}$.
3. Compactness of a subset of $\mathbb{R}^n$: the open cover property, the subsequence property, and "closed and bounded".
4. An $n \times n$ real matrix $A$ is [[invertible|0EB9N0S33C]] exactly when $\det A \neq 0$, exactly when $Ax = 0$ has only the solution $x = 0$, and exactly when the rank of $A$ is $n$.
5. An integer $n$ is even exactly when $n = 2k$ for an integer $k$, exactly when its remainder on division by $2$ is $0$, and exactly when $n^2$ is even. The L2 explanation below proves this.

### Non-examples

1. In $\mathbb{Z}[\sqrt{-5}]$, the element $2$ is [[irreducible but not prime|5BM35ES8WK]]. So "irreducible" and "prime" are not equivalent definitions there.
2. The space $[0, 1]^{[0,1]}$ of all functions $[0, 1] \to [0, 1]$, with the product topology, is compact by [[Tychonoff's theorem|0JTRSJKCFB]], but it is not sequentially compact. Let $f_n(x)$ be the $n$-th binary digit of $x$. For each subsequence $(n_k)$, choose $x$ whose $n_k$-th digit is $0$ for even $k$ and $1$ for odd $k$. Then $f_{n_k}(x)$ does not converge, so no subsequence of $(f_n)$ converges.
3. In a general metric space, "closed and bounded" is not equivalent to compactness. In $\mathbb{N}$ with the [[discrete metric|0NA4FK7B8S]], the whole space is closed and bounded, but the open cover by single points has no finite subcover.

### Basic properties

1. If $C_1$ and $C_2$ are equivalent, each theorem proved with $C_1$ as the definition stays true with $C_2$ as the definition.
2. Equivalence of conditions is an equivalence relation: it is reflexive, symmetric and transitive, because the [[biconditional|0S6GMNJ62Y]] has these properties.
3. To show that two conditions are not equivalent, one object that satisfies one condition and not the other is enough.
4. A weaker condition and a stronger condition can become equivalent under an extra hypothesis. Then the extra hypothesis is part of the statement, as "in a metric space" is part of "compact iff sequentially compact".

### History

[[Euclid's lemma|051VYKA1EX]], the main step from the divisor definition of a prime to the divisor property, is Proposition 30 of Book VII of Euclid's *Elements*.
In the 1840s Kummer found that unique factorization fails in some rings of cyclotomic integers, and this led to the separation of irreducible and prime elements.

### Common errors

1. A student uses a characterization outside its setting, for example "closed and bounded implies compact" in an arbitrary metric space.
2. A student proves only one direction of an equivalence and calls the definitions equivalent.
3. A student proves $C_1 \Rightarrow C_2$ with a lemma whose proof used $C_2$ as the definition, so the argument is circular.

## Explanations

### L1 human

Sometimes there are two different ways to describe the same group of things.
For example, an even number is a number that is two times a whole number.
It is also a number whose last digit is $0$, $2$, $4$, $6$ or $8$.
These two descriptions pick out exactly the same numbers, so they are equivalent definitions.
To know this, someone had to prove it, because the two descriptions look quite different.
Once it is proved, we may use whichever description is more convenient.

### L2 human

We prove that the following are equivalent for an integer $n$.
(1) $n = 2k$ for some integer $k$.
(2) The remainder of $n$ on division by $2$ is $0$.
(3) $n^2 = 2m$ for some integer $m$.

1. (1) $\Rightarrow$ (3). If $n = 2k$, then $n^2 = 4k^2 = 2(2k^2)$, so (3) holds with $m = 2k^2$.
2. (3) $\Rightarrow$ (2). We prove the contrapositive. By the [[division algorithm|0CHQKZFK5S]], the remainder is $0$ or $1$, so suppose it is $1$: $n = 2q + 1$.
3. Then $n^2 = 2(2q^2 + 2q) + 1$, so the remainder of $n^2$ is $1$.
4. The remainder is unique by the division algorithm, so $n^2 \neq 2m$ for every integer $m$, and (3) fails.
5. (2) $\Rightarrow$ (1). If the remainder is $0$, then $n = 2q + 0 = 2q$, so (1) holds with $k = q$.

The three implications form a cycle, so each condition implies each other condition.
The typical use: to prove that a number is even, prove whichever condition is easiest, and then use whichever condition is most useful.
A trap is the order of the cycle: a proof of (1) $\Rightarrow$ (3) and (3) $\Rightarrow$ (1) says nothing about (2).

### L3 human

For structures, "equivalent definitions" has a second meaning: two definitions with different data whose models correspond one to one.
A group can be a set with one operation and the existence of identity and inverses, or a set with an operation, a constant and an inverse map, and the two kinds of models are in bijection.
A [[matroid|PX31ZNYS3Z]] has equivalent definitions by independent sets, bases, circuits and rank functions; such a correspondence is called a cryptomorphism.
In category theory, the right notion is an isomorphism (or an equivalence) of the categories of models that commutes with the forgetful functors.
The notions that separate in larger settings show where a theory branches: irreducible and prime elements separate outside unique factorization domains, which leads to ideals and Dedekind domains.
Compactness and sequential compactness separate outside metric spaces, and nets and filters replace sequences there.
