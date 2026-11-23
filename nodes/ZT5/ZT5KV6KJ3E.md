---
tag: ZT5KV6KJ3E
kind: statement
role: theorem
name: Ramsey's theorem for pairs in reverse mathematics
msc: ["03B30", "05D10", "03D80"]
topics: [BY8AAFN7C5]
audience: grad
about: [00TQV3F5S4, 7SQS69T17R]
uses: [00TQV3F5S4, DNXCKXZZ08, K5YPW1NTHZ, K9XG0Z2N9V, 0FS3RHF6KE]
sources:
  - url: https://en.wikipedia.org/wiki/Ramsey%27s_theorem
    locator: Reverse mathematics
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
---

## Statement

Ramsey's theorem for pairs is a plain theorem of combinatorics whose strength matches none of the Big Five: it is weaker than arithmetical comprehension, and it is incomparable with weak König's lemma.

For a set $X \subseteq \mathbb{N}$, let $[X]^2$ be the set of pairs $\{x, y\}$ with $x < y$ in $X$.
A *coloring* of pairs is a function $c \colon [\mathbb{N}]^2 \to \{0, 1\}$, coded as a set of triples.
A set $H$ is *homogeneous* for $c$ if $c$ is constant on $[H]^2$.
We write $\mathrm{RT}^2_2$ for the sentence of $L_2$ that says: for every coloring $c$ of pairs there is an infinite set $H$ that is homogeneous for $c$.
This is the infinite [[Ramsey theorem|00TQV3F5S4]] for pairs and two colors.

**Theorem.** The following hold.

1. $\mathsf{ACA}_0 \vdash \mathrm{RT}^2_2$.
2. $\mathsf{WKL}_0 \nvdash \mathrm{RT}^2_2$, and so $\mathsf{RCA}_0 \nvdash \mathrm{RT}^2_2$.
3. $\mathsf{RCA}_0 + \mathrm{RT}^2_2 \nvdash \mathsf{ACA}_0$.
4. $\mathsf{RCA}_0 + \mathrm{RT}^2_2 \nvdash \mathsf{WKL}_0$.

So over [[RCA0|DNXCKXZZ08]] the principle $\mathrm{RT}^2_2$ lies strictly between $\mathsf{RCA}_0$ and [[ACA0|K9XG0Z2N9V]], and it is incomparable with [[WKL0|K5YPW1NTHZ]].

## Remarks

### Why it fits none of the Big Five

Most theorems of countable mathematics land on one of five systems, and $\mathrm{RT}^2_2$ is the standard case that does not.
Parts 2 and 4 together say that $\mathrm{RT}^2_2$ and weak König's lemma are incomparable, so $\mathrm{RT}^2_2$ cannot be equivalent to $\mathsf{RCA}_0$ or to $\mathsf{WKL}_0$.
Part 3 says that it is not equivalent to $\mathsf{ACA}_0$, and part 1 puts it below $\mathsf{ACA}_0$, so it is also below $\mathsf{ATR}_0$ and $\Pi^1_1\text{-}\mathsf{CA}_0$.
Each negative part is proved with an $\omega$-model, that is, a family of sets closed under Turing reduction and join in which one theory holds and the other fails.
The [[proof|NKXMH6R4CX]] gives parts 1 and 2 in full and reduces parts 3 and 4 to the theorems of Seetapun and of Liu.

### Why the exponent 2 matters

The exponent counts the size of the colored sets.
For exponent $1$, $\mathrm{RT}^1_2$ is the [[infinite pigeonhole principle|0FS3RHF6KE]]: color each number red or blue, and some color is used infinitely often.
$\mathsf{RCA}_0$ proves it, as the [[proof in RCA0|9EB4DXQMWK]] shows.
For exponent $3$ and above, $\mathrm{RT}^n_2$ is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$, and the [[case of triples|5DBP11VZTF]] codes the range of a one-to-one function into a coloring of triples.
So exponent $2$ is the only one whose strength falls between the standard systems.

### Splitting the theorem

A coloring $c$ of pairs is *stable* if for each $x$ the color $c(x, y)$ is the same for all large $y$.
Cholak, Jockusch and Slaman showed that $\mathrm{RT}^2_2$ is equivalent over $\mathsf{RCA}_0$ to its restriction $\mathrm{SRT}^2_2$ to stable colorings together with the cohesiveness principle $\mathrm{COH}$.
This splitting started the study of principles below $\mathrm{RT}^2_2$, the [[reverse mathematics zoo|E3X5B175ZR]].

### First-order strength

Which sentences about numbers alone does $\mathsf{RCA}_0 + \mathrm{RT}^2_2$ prove?
Jeffry Hirst showed that it proves the bounding scheme $\mathrm{B}\Sigma^0_2$, which $\mathsf{RCA}_0$ does not prove.
Chong, Slaman and Yang showed that it does not prove the induction scheme $\mathrm{I}\Sigma^0_2$.
From above, Cholak, Jockusch and Slaman showed that $\mathsf{RCA}_0 + \mathrm{I}\Sigma^0_2 + \mathrm{RT}^2_2$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \mathrm{I}\Sigma^0_2$.
So the first-order part of $\mathrm{RT}^2_2$ lies between $\mathrm{B}\Sigma^0_2$ and $\mathrm{I}\Sigma^0_2$.
Whether $\mathsf{RCA}_0 + \mathrm{RT}^2_2$ is $\Pi^1_1$-conservative over $\mathsf{RCA}_0 + \mathrm{B}\Sigma^0_2$ is a delicate question, and it has driven much of the later work.

### Watch out

A computable coloring can have computable homogeneous sets, so one example does not show that $\mathsf{RCA}_0$ fails to prove $\mathrm{RT}^2_2$.
The coloring $c(x, y) = 0$ when $x + y$ is even and $c(x, y) = 1$ otherwise has the even numbers as a computable homogeneous set.
The failure needs one cleverly built coloring, Jockusch's, whose homogeneous sets are all noncomputable.
In the same way, part 3 does not say that $\mathrm{RT}^2_2$ is weak: it still proves $\mathrm{B}\Sigma^0_2$, which $\mathsf{WKL}_0$ does not.

### Try it

Show that $\mathrm{RT}^2_2$ implies $\mathrm{RT}^1_2$ over $\mathsf{RCA}_0$.
Answer: given $f \colon \mathbb{N} \to \{0, 1\}$, color $\{x, y\}$ with $x < y$ by $f(x)$.
Let $H$ be an infinite homogeneous set with color $d$, and let $x \in H$.
Since $H$ is infinite, some $y \in H$ has $y > x$, and then $f(x) = c(x, y) = d$.
So $f$ is constant on $H$, which is the conclusion of $\mathrm{RT}^1_2$.

## History

Carl Jockusch built, in 1972, a computable coloring of pairs with no infinite $\Sigma^0_2$ homogeneous set, which gives part 2.
Jeffry Hirst studied Ramsey's theorem in subsystems of second-order arithmetic in his thesis of 1987, and he proved there that $\mathrm{RT}^2_2$ implies $\mathrm{B}\Sigma^0_2$.
David Seetapun proved part 3 in a paper with Theodore Slaman in 1995.
Cholak, Jockusch and Slaman published the splitting into the stable and the cohesive part, and the conservation result over $\mathrm{I}\Sigma^0_2$, in 2001.
Jiayi Liu proved part 4 in 2012.

## Explanations

### L1 human

Give every pair of whole numbers one of two colors, say red or blue.
Ramsey's theorem for pairs says that some infinite set of numbers has all its pairs in one color.
Logicians ask how much set existence the proof needs.
The usual proof uses a strong axiom, arithmetical comprehension, but the theorem does not need all of it.
It is also not a consequence of weak König's lemma, and it does not imply that lemma.
So it sits in none of the five standard levels.

### L2 human

The proof of part 1 places the numbers in a tree, one at a time.
Try it with the coloring $c(x, y) = 0$ when $x$ and $y$ have the same parity and $c(x, y) = 1$ otherwise.
Start with the root $0$.
The number $1$ becomes a child of $0$, and $2$ also becomes a child of $0$, since $c(0, 2) = 0$ differs from $c(0, 1) = 1$.
The number $3$ has $c(0, 3) = 1 = c(0, 1)$, so it walks to $1$ and becomes a child of $1$.
In the same way $5$ walks $0, 1, 3$ and becomes a child of $3$.
Along the path $0, 1, 3, 5, \dots$ the color of a pair depends only on its smaller element:
$$c(0, y) = 1, \qquad c(1, y) = c(3, y) = \dots = 0 \quad \text{for later } y \text{ on the path}.$$
Dropping $0$ leaves the odd numbers, a homogeneous set of color $0$.
The typical use of the tree is to turn a two-dimensional problem into a one-dimensional one, which the pigeonhole principle solves.
The trap is that the path through the tree needs König's lemma, which is the place where arithmetical comprehension enters.

### L3 human

The negative parts are theorems about Turing degrees: an infinite homogeneous set can always be found that avoids a given kind of information, such as the halting set or a separating set for two computably inseparable sets.
This reading made $\mathrm{RT}^2_2$ a test case for the methods of computability theory, and it led to the finer measures of [[Weihrauch reducibility|4G2JQ13XZ0]].
The first-order questions connect it to the [[fragments of Peano arithmetic|T70PYM1F36]], since $\mathrm{B}\Sigma^0_2$ and $\mathrm{I}\Sigma^0_2$ are the two schemes between which its strength sits.
Exponent $2$ also appears in other principles of the zoo, such as $\mathrm{CAC}$ and $\mathrm{ADS}$, which are special cases of $\mathrm{RT}^2_2$ for colorings that come from orders.
