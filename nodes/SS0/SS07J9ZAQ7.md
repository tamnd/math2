---
tag: SS07J9ZAQ7
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

A combinatorial proof shows that two expressions are equal by showing that they count the same things.
Instead of moving symbols around, you find a set of objects and explain why each side of the identity is its size.

There are two forms.
In a proof by [[double counting|0F8YBHF2W3]], one finite set is counted in two ways, and each way gives one side of the identity.
In a bijective proof, each side counts a different finite set, and an explicit [[bijection|0SNQEF7Z53]] between the two sets shows that they have the same size, by the [[bijection principle|0GV2573FP4]].

## Motivation

The identity $k\binom{n}{k} = n\binom{n-1}{k-1}$ can be checked with the factorial formula.
The algebra shows that the two sides agree, but it does not say why.
Now read both sides as counts of committees of $k$ people, chosen from $n$ people, with one member as the chair.
The left side picks the committee and then the chair, and the right side picks the chair and then the other $k - 1$ members.
Once you see this, the identity is no longer a coincidence of factorials, and you can guess and prove similar identities the same way.

Combinatorial proofs often carry more than the equation.
A bijection can keep extra features of the objects, and then it proves a whole family of identities at once.
Some results, such as [[Cayley's formula|0M2SSGSYPE]] for the number of labeled trees, have their shortest proofs in this form.

## Notation

We write $[n] = \{1, 2, \dots, n\}$.
The [[binomial coefficient|0GBZM0MT0F]] $\binom{n}{k}$ is the number of subsets of $[n]$ with $k$ elements.
A combinatorial proof uses this meaning of $\binom{n}{k}$ and never the factorial formula, so the formula $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ is a result that such proofs can derive, not a tool they use.

## Remarks

### A first proof: committees with a chair

Let $S$ be the set of pairs $(A, c)$ where $A$ is a $k$-subset of $[n]$ and $c \in A$.
Choose $A$ first in $\binom{n}{k}$ ways and then $c$ in $k$ ways, so $|S| = k\binom{n}{k}$ by the [[rule of product|0VPK4X73Q0]].
Choose $c$ first in $n$ ways and then the other $k - 1$ members from the remaining $n - 1$ people, so $|S| = n\binom{n-1}{k-1}$.
Both count $S$, so the two sides are equal.
Check with $n = 4$ and $k = 2$:
$$2 \binom{4}{2} = 2 \cdot 6 = 12 = 4 \cdot 3 = 4 \binom{3}{1}.$$
The [[full proof with a list of the twelve pairs|TTQNN6XXQN]] works the case out.

### How to find the set

The method applies when each side of an identity is a natural number with a counting meaning: a binomial coefficient, a power $m^n$, a factorial, or a sum or product of such terms.
A product suggests a sequence of choices, by the rule of product.
A sum suggests a split of a set into disjoint cases, by the [[rule of sum|0EE2V3CHFK]].
An alternating sum suggests a bijection between the objects counted with sign $+$ and those counted with sign $-$.
A proof then follows four steps.

1. Find a set $S$ that the left side counts, and say in words what one element of $S$ is.
2. Show that the left side counts $S$, by a sequence of choices or a split into cases that produces each element exactly once.
3. Count $S$ a second way that gives the right side, or find a set $T$ that the right side counts.
4. In the second case, give an explicit map $f : S \to T$ and prove that it is a bijection, usually by giving its inverse.

### More examples

[[Pascal's rule|0YRG241HQQ]], $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$, splits the $k$-subsets of $[n]$ into those that contain $n$ and those that do not.
The [[sum of binomial coefficients|0KAMF19NV8]], $\sum_{k} \binom{n}{k} = 2^n$, counts the subsets of $[n]$ by size on the left and by $n$ choices of "in or out" on the right.
[[Vandermonde's identity|01JADB9VW5]], $\binom{m+n}{r} = \sum_j \binom{m}{j}\binom{n}{r-j}$, chooses $r$ people from $m$ adults and $n$ children and sorts the choices by the number $j$ of adults.
Check with $m = n = r = 2$: $\binom{4}{2} = 6 = 1 + 4 + 1$.
For [[even and odd subsets|43EPSN2NG1]], toggling the element $1$ matches the subsets of $[n]$ of even size with those of odd size, for $n \geq 1$.
[[Prüfer sequences|900KK0PPYM]] match the labeled trees on $[n]$, for $n \geq 2$, with the sequences of length $n - 2$ in $[n]$, so there are $n^{n-2}$ trees.

### What is not a combinatorial proof

The [[algebraic proof of the committee identity|RSYQ7GQMX6]] cancels factorials.
It proves the same identity, but it names no set, so it is not a combinatorial proof.
The [[proof of Vandermonde's identity by induction|FF47MSWNER]] works with Pascal's rule as algebra, and it also gives no set that both sides count.
A map that is claimed to be a bijection but is not one proves nothing.
Sending each $2$-subset $\{a, b\}$ of $[4]$ to its smaller element is a map onto $\{1, 2, 3\}$, but it is not injective, so it does not show $\binom{4}{2} = 3$, which is false anyway since $\binom{4}{2} = 6$.

### The rules you can use

The whole logic rests on two facts: two expressions that count the same finite set are equal, and a bijection between finite sets gives equal sizes.
A double count of a relation $R \subseteq A \times B$ gives $\sum_{a \in A} d(a) = \sum_{b \in B} e(b)$, where $d(a)$ and $e(b)$ are the numbers of partners, and the handshaking lemma is the case of a graph, as in its [[proof by double counting|4M6ESXZ5B0]].
A bijection that keeps some feature, such as the size of a subset, proves one identity for each value of that feature.
An identity between two polynomials in $n$ that holds for all natural numbers $n$ holds for all real $n$, because a nonzero polynomial has finitely many roots.
So a combinatorial proof for natural $n$ can prove a polynomial identity in general.

### When the method fails

The method fails when a side has no counting meaning, for example when it has negative terms, fractions or real parameters.
Some such identities still yield after a change of form, such as moving the negative terms to the other side.
The method can also fail in practice: a true identity may have no known combinatorial proof, and then algebra or generating functions are needed.
The [[binomial theorem|0EHWPWGHB2]] gives the algebraic route, and the [[proof of symmetry from the factorial formula|GBF881BAPG]] is the algebraic counterpart of the bijection $A \mapsto [n] \setminus A$ for the [[symmetry of binomial coefficients|0R7JS3DP3W]].
[[Stars and bars|009TEMTQKH]] shows the other direction: a bijection with arrangements of symbols, [[proved by a bijection with subsets|KB70806JGH]], turns an equation count into a binomial coefficient.

### Watch out

The most common error is to count ordered choices for an unordered set.
Choosing a committee of $k$ people one at a time gives $n(n-1)\cdots(n-k+1)$, which counts each committee $k!$ times.
For $n = 4$ and $k = 2$ that is $12$ ordered choices for $6$ committees.
A second error is a split into cases that overlap, so that some element is counted twice.
A third is a map called a bijection with no proof that it is one; the inverse map is the cleanest proof.
Finally, describe the set exactly, since the proof is only as exact as that description.

### History

Leonhard Euler proved in 1748 that the partitions of a number into odd parts and into distinct parts are equally many, using generating functions.
James Glaisher gave a bijective proof of this [[partition theorem|0XFZ1BMF5Q]] in 1883, now called [[Glaisher's bijection|EZF8KV8YM6]].
Heinz Prüfer gave his bijective proof of Cayley's formula in 1918.
Arthur Benjamin and Jennifer Quinn collected many combinatorial proofs in the book "Proofs That Really Count" (2003).

### Try it

Prove $\binom{2n}{2} = 2\binom{n}{2} + n^2$ by counting.
Choose $2$ people from $n$ adults and $n$ children: two adults, two children, or one of each, giving $\binom{n}{2} + \binom{n}{2} + n \cdot n$; for $n = 3$ both sides are $15$.

Prove $\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$.
Choose $n$ people from $n$ adults and $n$ children, and sort by the number $k$ of adults: there are $\binom{n}{k}\binom{n}{n-k} = \binom{n}{k}^2$ ways for each $k$; for $n = 3$ both sides are $20$.

## Explanations

### L1 human

Suppose that a class has $n$ students and we want to form a team of $k$ students with one captain.
We can choose the team first in $\binom{n}{k}$ ways and then the captain in $k$ ways.
Or we can choose the captain first in $n$ ways and then the $k - 1$ other members from the $n - 1$ other students.
Both ways count the same teams with captains, so $k\binom{n}{k} = n\binom{n-1}{k-1}$.
For $n = 5$ and $k = 2$, both sides equal $20$.
This is a combinatorial proof: two numbers are equal because they count the same things.

### L2 human

We prove $\sum_{k=0}^{n} k\binom{n}{k} = n 2^{n-1}$ for $n \geq 1$ by double counting.
Let $S$ be the set of pairs $(A, c)$, where $A$ is any subset of $[n]$ and $c$ is an element of $A$, so $A$ is a committee of any size and $c$ is its chair.
Sort the pairs by the size $k$ of $A$: there are $\binom{n}{k}$ subsets of size $k$, each with $k$ choices of chair, so $|S| = \sum_{k} k\binom{n}{k}$.
Sort the pairs by the chair instead: there are $n$ choices of $c$, and then $A \setminus \{c\}$ is any of the $2^{n-1}$ subsets of the other $n - 1$ elements, so $|S| = n 2^{n-1}$.
Check with $n = 4$: the terms $k\binom{4}{k}$ are $0, 4, 12, 12, 4$, and
$$0 + 4 + 12 + 12 + 4 = 32 = 4 \cdot 2^3.$$
The typical use is an identity whose sum runs over a size $k$: sort a set of objects by size on one side and by another feature on the other.
Watch out for the second count without the condition $c \in A$, which gives $n 2^n$ and counts chairs who are not on the committee.

### L3 human

A bijective proof of $|A| = |B|$ is an isomorphism in the category of finite sets, and the equation of numbers is its shadow under the map that sends a set to its size.
Many bijections keep extra structure, such as a statistic on the objects, and then they prove an equality of generating functions and not only of numbers.
André Joyal's theory of combinatorial species makes this precise: a species is a functor from finite sets with bijections to finite sets, and many identities of exponential generating functions lift to isomorphisms of species.
Joyal gave a bijective proof of [[Cayley's formula|0M2SSGSYPE]] in this setting.

Alternating sums are handled by sign-reversing involutions: an involution on a signed set that reverses the sign of each element it moves shows that the signed sum equals the signed count of its fixed points.
The bijection for [[the alternating sum of binomial coefficients|0PQQGFAWSH]] is the simplest case, with no fixed points.
The involution principle of Adriano Garsia and Stephen Milne turns two such involutions into a bijection, and they used it for a bijective proof of the Rogers-Ramanujan identities.
Lattice paths, tilings and the Lindström-Gessel-Viennot lemma give combinatorial proofs of determinant identities, and [[lattice paths|040WY0TT2G]] also give the standard counting meaning of binomial coefficients.
