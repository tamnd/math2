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

One notion often has several definitions that look quite different, and a theorem tells us that they pick out the same objects.
A prime number is an integer $p > 1$ whose only positive divisors are $1$ and $p$.
It is also an integer $p > 1$ such that $p \mid ab$ always forces $p \mid a$ or $p \mid b$.
These two conditions hold for exactly the same integers, but that fact needs a proof.

In general, conditions $C_1$ and $C_2$ on objects $x$ of a kind $K$ are *equivalent definitions* when
$$C_1(x) \iff C_2(x) \qquad \text{for every } x \text{ of kind } K.$$
This is a theorem, and its [[proof|0B94TKFQJX]] needs both directions.
Authors choose one condition as the primary [[definition|8ZCZ3HW91Z]], and the others become theorems, called characterizations.

## Motivation

Each definition makes different facts easy.
The divisor definition of a prime is easy to test on $91 = 7 \cdot 13$, while the product property is what proves that $\sqrt{2}$ is irrational.
Once the two are known to agree, a proof can check one condition and use the other.

A notion also often turns up in several places before anyone sees that it is one notion.
A closed bounded interval $[a, b]$ has three useful properties: every sequence in it has a subsequence that converges in it, every cover by open sets has a finite subcover, and it is closed and bounded.
In $\mathbb{R}^n$ the three properties hold for the same sets, by the [[Heine-Borel theorem|07PFYV65MB]] and the [[Bolzano-Weierstrass theorem|0KDJD249DT]], so they are three definitions of [[compactness|0TVJZYB6SH]].
In larger settings they come apart, and that tells us which one to keep.

## Notation

"The following are equivalent", often shortened to TFAE, followed by a numbered list of conditions, announces a theorem of equivalence.
Its proof often shows a cycle (1) $\Rightarrow$ (2) $\Rightarrow \cdots \Rightarrow$ (n) $\Rightarrow$ (1).
"$C_2$ characterizes $P$" and "$P$ is characterized by $C_2$" mean that $C_2$ is equivalent to the definition of $P$.

## Remarks

### Two definitions of a prime

Test both conditions on $6$ and on $7$.
The number $6$ has the divisor $2$, so it fails the divisor definition.
It also fails the product property, since $6 \mid 2 \cdot 3$ but
$$6 \nmid 2, \qquad 6 \nmid 3.$$
The number $7$ has only the divisors $1$ and $7$, and it passes the product property too: $7 \mid 14 \cdot 5 = 70$, and $7 \mid 14$.
One case per number proves nothing in general, and [[two definitions of a prime number|787PD6B171]] gives the proof.
The direction from divisors to products is [[Euclid's lemma|051VYKA1EX]], and it is the harder one, because it needs Bézout's identity.

### How an equivalence is proved

For two conditions, prove $C_1 \Rightarrow C_2$ and $C_2 \Rightarrow C_1$.
For $n$ conditions a cycle of $n$ implications is enough, because implications compose.
To show that two conditions are not equivalent, one object that meets one condition and fails the other is enough.

Equivalence of conditions is reflexive, symmetric and transitive, because the [[biconditional|0S6GMNJ62Y]] is.
Once $C_1$ and $C_2$ are equivalent, every theorem proved with $C_1$ as the definition stays true with $C_2$ as the definition.
That is the whole point: a proof may switch to the condition that is most convenient at that step.

### Equivalence depends on the setting

The words "for every $x$ of kind $K$" are part of the theorem.
Two conditions can agree on the objects of one kind and differ on a larger kind.

For integers the two prime conditions agree, but in the ring $\mathbb{Z}[\sqrt{-5}]$ they [[pick out different elements|5BM35ES8WK]]: $2$ cannot be factored into non-units, yet $2 \mid (1 + \sqrt{-5})(1 - \sqrt{-5}) = 6$ while $2$ divides neither factor.
For functions $\mathbb{R} \to \mathbb{R}$, the epsilon-delta and the sequential definitions of continuity agree, as [[the two definitions of continuity|A4C3JY380W]] proves, but for maps between general topological spaces they do not.
For metric spaces, compactness and sequential compactness agree, but for general topological spaces they do not.
So when an extra hypothesis makes two conditions equivalent, that hypothesis is part of the statement.

### Choosing the primary definition

There is no rule, but authors weigh a few things.
A definition that still works in a larger setting is often preferred.
Ring theory calls an element prime when it has the product property, because that is the useful notion in general rings, and it calls the divisor property irreducible.
A definition that is easy to test helps beginners, which is why school books define primes by divisors.
A definition that makes estimates direct helps in proofs, which is why analysis books define continuity with $\varepsilon$ and $\delta$.
Mathlib picks one definition for each notion and proves the others as lemmas of the form "iff".
Different books choose differently, so check which condition a book takes as the definition before you use the others as known.

### When definitions come apart

In a general metric space "closed and bounded" is not equivalent to compactness.
Give $\mathbb{N}$ the [[discrete metric|0NA4FK7B8S]], where distinct points have distance $1$.
The whole space is closed, and it is bounded since every distance is at most $1$.
But the open balls of radius $\tfrac{1}{2}$ are the single points, and no finite set of them covers $\mathbb{N}$.

Compactness and sequential compactness come apart in topology.
The space of all functions $[0, 1] \to [0, 1]$, with the product topology, is compact by [[Tychonoff's theorem|0JTRSJKCFB]].
For $x \in [0, 1)$ let $f_n(x)$ be the $n$-th binary digit of $x$, using the expansion that does not end in all $1$s, and let $f_n(1) = 0$.
For a subsequence $(f_{n_k})$, take an $x$ whose digit number $n_k$ is $0$ for even $k$ and $1$ for odd $k$.
Then $f_{n_k}(x)$ alternates, so no subsequence converges pointwise, and the space is not sequentially compact.

### Watch out

The first error is to use a characterization outside its setting, for example "closed and bounded implies compact" in an arbitrary metric space.
The discrete metric on $\mathbb{N}$ above is the standard warning.

The second error is to prove one direction and call the definitions equivalent.
"$n = 2k$ implies $n^2$ is even" is one direction only, and the other direction needs its own proof.

The third error is a hidden circle.
If a lemma was proved with $C_2$ as the definition, it cannot be used to prove $C_1 \Rightarrow C_2$.

### History

Euclid's lemma, the main step from the divisor definition of a prime to the product property, is Proposition 30 of Book VII of the *Elements*.
In the 1840s Kummer found that unique factorization into irreducible elements fails in some rings of cyclotomic integers, and he introduced "ideal numbers" to repair it.

### Try it

First, for an $n \times n$ real matrix $A$, name two conditions equivalent to "$A$ is [[invertible|0EB9N0S33C]]".
Two of the standard ones are $\det A \neq 0$ and "$Ax = 0$ has only the solution $x = 0$".

Second, a student proves (1) $\Rightarrow$ (2), (2) $\Rightarrow$ (1) and (1) $\Rightarrow$ (3).
Are the three conditions now equivalent?
No: nothing yet shows that (3) implies (1) or (2).

## Explanations

### L1 human

Sometimes there are two ways to describe the same group of things.
An even number is a number that is two times a whole number.
It is also a number whose last digit is $0$, $2$, $4$, $6$ or $8$.
The two descriptions pick out exactly the same numbers, so they are equivalent definitions.
Someone had to prove it, because the two descriptions look quite different.
Once it is proved, we may use whichever description is more convenient.

### L2 human

We prove that three conditions on an integer $n$ are equivalent: (1) $n = 2k$ for some integer $k$, (2) the remainder of $n$ on division by $2$ is $0$, and (3) $n^2 = 2m$ for some integer $m$.

1. (1) $\Rightarrow$ (3).
   If $n = 2k$, then $n^2 = 4k^2 = 2(2k^2)$, so (3) holds with $m = 2k^2$.
2. (3) $\Rightarrow$ (2), by the contrapositive.
   By the [[division algorithm|0CHQKZFK5S]] the remainder is $0$ or $1$, so suppose it is $1$, that is, $n = 2q + 1$.
3. Square:
   $$n^2 = 4q^2 + 4q + 1 = 2(2q^2 + 2q) + 1,$$
   so the remainder of $n^2$ is $1$.
4. The remainder is unique by the division algorithm, so $n^2 \neq 2m$ for every integer $m$, and (3) fails.
5. (2) $\Rightarrow$ (1).
   If the remainder is $0$, then $n = 2q$, so (1) holds with $k = q$.

The three implications form a cycle, so each condition implies the other two.
Check with $n = 7$: (1) fails, the remainder is $1$, and $49 = 2 \cdot 24 + 1$ is odd, so all three fail together.
To prove that a number is even, prove whichever condition is easiest, and then use whichever is most useful.
Watch out: proving (1) $\Rightarrow$ (3) and (3) $\Rightarrow$ (1) would say nothing about (2).

### L3 human

For structures, "equivalent definitions" has a second meaning: two definitions with different data whose models correspond one to one.
A group can be a set with one operation for which an identity and inverses exist, or a set with an operation, a constant and an inverse map, and the two kinds of models are in bijection.
A [[matroid|PX31ZNYS3Z]] has equivalent definitions by independent sets, bases, circuits and rank functions, and such a correspondence is called a cryptomorphism.
In category theory the precise notion is an isomorphism of the categories of models that commutes with the forgetful functors.

Notions that separate in larger settings show where a theory branches.
Irreducible and prime elements separate outside unique factorization domains, and this leads to ideals and Dedekind domains.
Compactness and sequential compactness separate outside metric spaces, and nets and filters replace sequences there.
