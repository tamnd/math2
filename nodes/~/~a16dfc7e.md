---
tag: ~a16dfc7e
kind: concept
name: Combinatorial and bijective proof
aliases: [combinatorial-proof]
msc: ["00A35", "05A19"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: ug1
uses: [0F8YBHF2W3, 0GV2573FP4, 0SNQEF7Z53, 0GBZM0MT0F, 0VPK4X73Q0]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bijective_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Double_counting_(proof_technique)
    locator: lead section
---

## Summary

A combinatorial proof proves an identity between two expressions by showing that both count the same finite set, or two sets of the same size.
It has two main forms.
In a proof by [[double counting|0F8YBHF2W3]], one set is counted in two ways, and each way gives one side of the identity.
In a bijective proof, each side counts a different set, and an explicit [[bijection|0SNQEF7Z53]] between the two sets shows that they have the same size, by the [[bijection principle|0GV2573FP4]].
The method matters because it explains why an identity holds, and the bijection often carries more information than the equality of numbers.

## Motivation

An identity such as $k\binom{n}{k} = n\binom{n-1}{k-1}$ can be checked by algebra with the factorial formula.
The algebra shows that the two sides are equal, but it does not say what they mean.
Both sides count the committees of $k$ people from $n$ people with one member chosen as the chair.
The left side picks the committee and then the chair; the right side picks the chair and then the other $k - 1$ members.
Once we see this, the identity is no longer a coincidence of factorials, and we can guess similar identities.
Some results, such as [[Cayley's formula|0M2SSGSYPE]], have short combinatorial proofs.

## Notation

We write $[n] = \set{1, 2, \dots, n}$.
The [[binomial coefficient|0GBZM0MT0F]] $\binom{n}{k}$ is the number of subsets of $[n]$ with $k$ elements.
A combinatorial proof uses this meaning of $\binom{n}{k}$, not the factorial formula.

## Remarks

### Examples

- [[The committee with a chair|~9956f43c]]: both $k\binom{n}{k}$ and $n\binom{n-1}{k-1}$ count the pairs (committee, chair), so they are equal.
- [[Pascal's rule|0YRG241HQQ]] $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$: split the $k$-subsets of $[n]$ into those that contain $n$ and those that do not.
- The [[sum of binomial coefficients|0KAMF19NV8]] $\sum_{k=0}^{n} \binom{n}{k} = 2^n$: both sides count the subsets of $[n]$, the left side by size and the right side by $n$ choices of "in or out".
- [[Vandermonde's identity|01JADB9VW5]] $\binom{m+n}{r} = \sum_j \binom{m}{j}\binom{n}{r-j}$: choose $r$ people from $m$ men and $n$ women, and sort the choices by the number $j$ of men.
- [[Even and odd subsets|~ea7fdbf3]]: toggling the element $1$ is a bijection between the subsets of $[n]$ of even size and those of odd size, for $n \ge 1$.
- [[Prüfer sequences|900KK0PPYM]] give, for $n \ge 2$, a bijection between the labelled trees on $[n]$ and the sequences of length $n - 2$ with entries in $[n]$, which proves that there are $n^{n-2}$ such trees.

### Non-examples

- [[The algebraic proof of the committee identity|~3f33c823]] cancels factorials. It proves the same identity, but it counts no set, so it is not a combinatorial proof.
- [[The proof of Vandermonde's identity by induction|FF47MSWNER]] proves the identity by algebra on Pascal's rule; it gives no set that both sides count.
- A map that is claimed to be a bijection but is not injective, not onto or not well defined proves nothing. Sending each $2$-subset $\set{a, b}$ of $[4]$ to its smaller element is a map onto $\set{1, 2, 3}$, and it is not injective, so it does not show $\binom{4}{2} = 3$.

### Basic properties

- If two expressions count the same finite set, they are equal. This is the whole logic of double counting.
- If $f : A \to B$ is a bijection between finite sets, then $|A| = |B|$.
- A double count of a relation $R \subseteq A \times B$ gives $\sum_{a \in A} d(a) = \sum_{b \in B} e(b)$, where $d(a)$ and $e(b)$ are the numbers of partners of $a$ and of $b$. The handshaking lemma is the case of a graph, as in the [[proof by double counting|4M6ESXZ5B0]].
- A bijective proof gives more than the equality: a bijection that preserves some property proves a refined identity, one for each value of that property.
- An identity between polynomials in $n$ that holds for all natural numbers $n$ holds for all $n$, since a nonzero polynomial has finitely many roots. So a combinatorial proof for natural $n$ can prove a polynomial identity in general.

### When it applies

The method applies when each side of an identity is a natural number with a counting meaning: a binomial coefficient, a power $m^n$, a factorial, a product or a sum of such terms.
A product suggests a sequence of choices, by the [[rule of product|0VPK4X73Q0]].
A sum suggests a split of a set into disjoint cases, by the [[rule of sum|0EE2V3CHFK]].
An alternating sum suggests a bijection between the objects counted with sign $+$ and those counted with sign $-$.

### The steps

1. Find a set $S$ that the left side counts. Write down what one element of $S$ is.
2. Show that the left side counts $S$: describe a sequence of choices, or a split into cases, that produces each element of $S$ exactly once.
3. Either count $S$ in a second way that gives the right side, or find a set $T$ that the right side counts.
4. In the second case, give an explicit map $f : S \to T$ and prove that it is a bijection, usually by giving its inverse.
5. Conclude that the two sides are equal.

### When it fails

The method fails when a side has no counting meaning, for example when it has negative terms, fractions or real parameters.
Some such identities still yield to a combinatorial proof after a change of form, such as moving negative terms to the other side.
The method can also fail in practice: an identity can be true and have no known combinatorial proof, and then algebra or generating functions are needed.

### Related methods

- [[Double counting|0F8YBHF2W3]] is the form of the method with one set counted twice.
- Algebraic proofs use formulas such as the factorial formula or the [[binomial theorem|0EHWPWGHB2]]. The [[proof of symmetry from the factorial formula|GBF881BAPG]] is the algebraic counterpart of the bijection $A \mapsto [n] \setminus A$ for the [[symmetry of binomial coefficients|0R7JS3DP3W]].
- [[Stars and bars|009TEMTQKH]] is a bijection between solutions of an equation and arrangements of symbols, [[proved by a bijection with subsets|KB70806JGH]].
- The [[pigeonhole principle|0HGVCWQGY3]] also compares the sizes of finite sets, but it proves existence and not equality.

### History

Leonhard Euler proved in 1748 that the partitions of a number into odd parts and into distinct parts are equally many, by generating functions.
James Glaisher gave a bijective proof of this [[partition theorem|0XFZ1BMF5Q]] in 1883, [[Glaisher's bijection|EZF8KV8YM6]].
Heinz Prüfer gave his bijective proof of Cayley's formula in 1918.
Arthur Benjamin and Jennifer Quinn collected many combinatorial proofs in the book "Proofs That Really Count" (2003).

### Common errors

- To count ordered choices when the set is unordered. Choosing a committee of $k$ people one at a time gives $n(n-1)\cdots(n-k+1)$, which counts each committee $k!$ times.
- To count an element twice in a split into cases, because the cases overlap.
- To give a map and call it a bijection without proving that it is injective and onto, or without giving its inverse.
- To describe the set vaguely. A combinatorial proof is only as exact as the description of the set it counts.

## Explanations

### L1 human

Suppose that a class has $n$ students and we want to form a team of $k$ students with one captain.
We can choose the team first in $\binom{n}{k}$ ways and then the captain in $k$ ways.
Or we can choose the captain first in $n$ ways and then the $k - 1$ other members from the $n - 1$ other students.
Both ways count the same teams with captains, so $k\binom{n}{k} = n\binom{n-1}{k-1}$.
For $n = 5$ and $k = 2$, both sides equal $20$.
This is a combinatorial proof: we prove that two numbers are equal by showing that they count the same things.

### L2 human

We prove $\sum_{k=0}^{n} k\binom{n}{k} = n 2^{n-1}$ for $n \ge 1$ by double counting.

1. Let $S$ be the set of pairs $(A, c)$, where $A$ is a subset of $[n]$ and $c$ is an element of $A$. Think of $A$ as a committee of any size and $c$ as its chair.
2. Sort the pairs by the size $k$ of $A$. There are $\binom{n}{k}$ subsets of size $k$, and each has $k$ choices of chair. So $|S| = \sum_{k=0}^{n} k\binom{n}{k}$.
3. Sort the pairs by the chair $c$ instead. There are $n$ choices of $c$, and then $A \setminus \set{c}$ is any subset of the other $n - 1$ elements, with $2^{n-1}$ choices. So $|S| = n 2^{n-1}$.
4. Steps 2 and 3 count the same set, so the two sums are equal.
5. Check for $n = 4$: the terms $k\binom{4}{k}$ are $0, 4, 12, 12, 4$, with sum $32$, and $4 \cdot 2^3 = 32$.

The typical use is an identity whose sum runs over a size $k$: find a set of objects and sort them by size on one side and by another feature on the other.
A trap is step 3 without the condition that $c \in A$: then the count would be $n 2^n$, which counts pairs where the chair is not on the committee.

### L3 human

A bijective proof of $|A| = |B|$ is an isomorphism in the category of finite sets, and the equation of numbers is its shadow under the map that sends a set to its size.
Many bijections preserve extra structure, such as a statistic on the objects, and then they prove an equality of generating functions and not only of numbers.
André Joyal's theory of combinatorial species makes this precise: a species is a functor from finite sets with bijections to finite sets, and many identities of exponential generating functions lift to isomorphisms of species.
Joyal gave a bijective proof of [[Cayley's formula|0M2SSGSYPE]] in this setting.

Alternating sums are handled by sign-reversing involutions: an involution on a signed set that reverses the sign of each element it moves shows that the signed sum equals the signed count of its fixed points.
The bijection for [[the alternating sum of binomial coefficients|0PQQGFAWSH]] is the simplest case, with no fixed points.
The involution principle of Adriano Garsia and Stephen Milne turns two such involutions into a bijection, and they used it for a bijective proof of the Rogers-Ramanujan identities.
Lattice paths, tilings and the Lindström-Gessel-Viennot lemma give combinatorial proofs of determinant identities, and [[lattice paths|040WY0TT2G]] also give the standard combinatorial meaning of binomial coefficients.
