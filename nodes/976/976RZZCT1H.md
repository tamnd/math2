---
tag: 976RZZCT1H
kind: concept
name: Abstraction and generalization
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: ug1
uses: [0B94TKFQJX, W48XN2MEM9, F3NNR77WKP]
sources:
  - url: https://en.wikipedia.org/wiki/Abstraction_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Generalization
    locator: lead section
  - book: isbn:9780691164076
---

## Summary

Abstraction and generalization are the two ways in which mathematics makes one argument do the work of many.
Abstraction looks at many particular cases, keeps what they share and forgets the rest, and the result is a new notion with its own definition, such as a [[group|G5S1M9]].
Generalization takes a statement or a notion and passes to a wider one that contains the original as a special case, often by dropping or weakening a [[hypothesis|W48XN2MEM9]].
For example, the [[law of cosines|060ZVZBV3E]] generalizes the [[Pythagorean theorem|0VP3A1290K]] from right triangles to all triangles.
In both cases one [[proof|0B94TKFQJX]] then covers every instance at once, and the proof is often shorter, because the general setting hides details that do not matter.

## Motivation

The integers with addition, the nonzero rational numbers with multiplication and the rotations of a square share a pattern.
In each case two elements combine to give a third, the combination is associative, there is a neutral element, and each element can be undone.
Many facts about the three structures have the same proof, such as the uniqueness of the neutral element.
It would be wasteful to prove such a fact three times, and impossible to prove it separately for every structure of this kind that will ever appear.
Abstraction names the shared pattern, here the notion of a group, and proves the fact once for all groups.

Generalization meets the same need for theorems.
The Pythagorean theorem speaks only about right triangles, and the question "what happens when the angle is not right?" leads to the law of cosines.
The idea returns throughout the area: [[examples|F3NNR77WKP]] are the raw material of abstraction, and [[classification|9HQ3TADPA8]] is often the next step after a notion has been abstracted.

## Notation

The words have no fixed technical meaning.
A statement $B$ is a *generalization* of a statement $A$ when $A$ is a special case of $B$, so that $A$ follows from $B$ by a choice of parameters or by adding hypotheses.
The reverse passage, from $B$ to $A$, is *specialization*.
Many authors use "abstraction" mainly for notions and "generalization" mainly for statements, and we follow that use.

## Remarks

### One proof for many structures

Here is a fact that abstraction lets us prove once: a group has only one identity element.
Suppose $e$ and $e'$ are both identities.
Since $e'$ is an identity, $e e' = e$, and since $e$ is an identity, $e e' = e'$.
So
$$e = e e' = e'.$$
The argument uses nothing about integers, fractions or rotations, so it holds in all three structures at once, and in every group that anyone will define later.
This is the general point: a theorem about an abstract notion holds in every instance, because its proof uses only the properties in the definition.

The same move gave many standard notions.
A [[vector space|000AYPA9AJ]] abstracts from the plane, from the polynomials and from the solutions of a linear differential equation, which all have an addition and a scaling with the same rules.
A [[metric space|0VKD1TP7F3]] keeps only the properties of distance that proofs about limits use, and a [[topological space|0CQHFPGJ45]] goes further and keeps only the open sets.

### Dropping a hypothesis

The Pythagorean theorem needs a right angle at $C$, and the law of cosines removes that hypothesis:
$$c^2 = a^2 + b^2 - 2ab \cos C.$$
At $C = 90^\circ$ the cosine is $0$, and the old theorem comes back, as [[the law of cosines example|P04BP4Y3K8]] checks with numbers.
A generalization $B$ of a theorem $A$ is stronger than $A$, so a proof of $B$ is also a proof of $A$.

The general proof can be the shorter one.
[[Fermat's little theorem|0M25PRN3WQ]], $a^{p - 1} \equiv 1 \pmod p$ for a prime $p$ not dividing $a$, is a special case of [[Lagrange's theorem|3C53TD]] applied to the nonzero residues modulo $p$.
The group proof needs only that these residues form a group with $p - 1$ elements, as [[the Fermat example|ASFQ92J1RK]] shows.
The same steps with the residues coprime to $n$ give [[Euler's theorem|0VC4DVE7DQ]], so the general setting also pointed to the next generalization.

### Generalizations that fail

A generalization of a true theorem can be false, so each one needs a new proof or a counterexample.
For real numbers, $(a + b)^2 = a^2 + 2ab + b^2$.
For matrices the same formula fails, because its proof replaces $ab + ba$ by $2ab$, and matrices need not commute.
With $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ the two sides are different matrices, as [[the binomial non-example|60W7PZXBVB]] computes.

Replacing a number by a letter is a second way to fail.
The equation $2^4 = 4^2$ is true, but its "generalization" $2^x = x^2$ fails at $x = 3$, since $2^3 = 8$ and $3^2 = 9$.
The safe move is to list the facts that the old proof uses and to check each one in the new setting.

### Watch out

A common error is to carry a formula into a wider setting without checking the hypotheses its proof uses.
In an abelian group, $(ab)^{-1} = a^{-1} b^{-1}$.
In the symmetric group $S_3$, with products computed from right to left, take $a = (1\,2)$ and $b = (1\,3)$.
Then $ab = (1\,3\,2)$, so $(ab)^{-1} = (1\,2\,3)$, while $a^{-1} b^{-1} = ab = (1\,3\,2)$.
The correct rule in every group is $(ab)^{-1} = b^{-1} a^{-1}$, since $(ab)(b^{-1} a^{-1}) = a (b b^{-1}) a^{-1} = e$.

The opposite error is to study an abstract definition before you know any instance of it.
Then the definition has no content, and you cannot test any statement about it.

### History

Arthur Cayley defined a group by its operation, without a reference to permutations, in 1854.
Giuseppe Peano gave an axiomatic definition of a vector space in 1888.
Maurice Fréchet introduced metric spaces in his thesis of 1906, and Felix Hausdorff defined topological spaces by neighborhoods in 1914.
George Pólya discussed generalization, specialization and the [[inventor's paradox|FVRKDXBJF6]] in "How to Solve It" (1945).

### Try it

First, which group axioms does the proof that the identity is unique use?
It uses only the defining property of an identity, and not associativity or inverses, so it holds for any set with an operation.

Second, apply Euler's theorem with $n = 9$ and $a = 2$.
The residues coprime to $9$ are $1, 2, 4, 5, 7, 8$, so $\varphi(9) = 6$, and $2^6 = 64 = 7 \cdot 9 + 1 \equiv 1 \pmod 9$.

Third, for which pairs of matrices does $(A + B)(A - B) = A^2 - B^2$ hold?
Expanding gives $A^2 - AB + BA - B^2$, so it holds exactly when $AB = BA$.

## Explanations

### L1 human

Abstraction means to notice what many things have in common and to give it a name.
Three apples, three chairs and three days share nothing except "three", and the number three is an abstraction.
Generalization means to take a rule that works in one case and make it work in more cases.
The rule "a square with side $3$ has area $9$" generalizes to "a square with side $s$ has area $s^2$".
Each generalization must be checked, because some rules stop working in the wider setting.

### L2 human

Here is a case where a more general statement is easier to prove: we show that for every $n \ge 1$,
$$S_n = 1 + \frac{1}{4} + \frac{1}{9} + \cdots + \frac{1}{n^2} < 2.$$
A direct induction gets stuck, because $S_n < 2$ says nothing about how much room is left for the next term.
So we prove the stronger statement $S_n \le 2 - \frac{1}{n}$, which carries that information.
For $n = 1$ both sides equal $1$.
If $S_n \le 2 - \frac{1}{n}$, then, because $\frac{1}{(n + 1)^2} < \frac{1}{n(n + 1)} = \frac{1}{n} - \frac{1}{n + 1}$,
$$S_{n + 1} = S_n + \frac{1}{(n + 1)^2} < 2 - \frac{1}{n} + \frac{1}{n} - \frac{1}{n + 1} = 2 - \frac{1}{n + 1}.$$
This completes the induction, and $2 - \frac{1}{n} < 2$ gives the original claim.
Pólya called this effect the [[inventor's paradox|FVRKDXBJF6]], and [[strengthening the induction hypothesis|F94KJC2RXP]] is its most common form.
Watch out: the stronger statement must still be true, so test it first.
Check: $S_2 = 1.25 \le 1.5$ and $S_3 \approx 1.361 \le 1.667$.

### L3 human

Abstraction is the main engine of modern algebra and topology.
Emmy Noether's style of algebra replaced computations with elements by statements about ideals, modules and homomorphisms.
Category theory takes the step once more, from groups, rings and spaces to objects and morphisms, and it states theorems that hold in every category with the needed structure.
A theorem at that level, such as the uniqueness of a universal object up to unique isomorphism, has a proof of a few lines that replaces many separate proofs.

Generalization has a cost.
A general theorem can lose information that the special case has: the law of cosines says nothing special about integer side lengths, while [[Pythagorean triples|01G1WY1GVX]] have a rich arithmetic.
Good generalizations keep the features that made the original interesting.
[[Classification|9HQ3TADPA8]] lists all instances of an abstract notion, and the [[methodology of mathematics|3FJ3XMV9KD]] asks how mathematicians choose which generalizations to pursue.
