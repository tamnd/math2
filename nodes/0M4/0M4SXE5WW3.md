---
tag: 0M4SXE5WW3
kind: statement
role: theorem
name: Extension of an independent set to a basis
aliases: [basis-extension-theorem]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6]
proofs: [SS0XKV9TAN, MEFZB7GHA9]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 2B
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Statement

An independent set can always be completed to a basis, and the new vectors can be taken from any spanning set we like.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $L \subseteq V$ be a [[linearly independent|0EVHJFTG9Z]] set.

1. There is a [[basis|0VTQTPQGAV]] $B$ of $V$ with $L \subseteq B$.
2. More precisely, if $S \subseteq V$ is a [[spanning set|0BJKVF90Z6]] of $V$ with $L \subseteq S$, then there is a basis $B$ of $V$ with $L \subseteq B \subseteq S$.

## Remarks

### Completing a set by hand

Extend $L = \{(1, 1, 0)\}$ to a basis of $\mathbb{R}^3$, using the standard basis vectors as candidates.
We walk through $e_1, e_2, e_3$ and add a vector only when it lies outside the span of what we have.
The vector $e_1 = (1, 0, 0)$ is not a multiple of $(1, 1, 0)$, so we add it.
Next, $e_2 = (0, 1, 0)$ is already in the span, because
$$(1, 1, 0) - (1, 0, 0) = (0, 1, 0),$$
so we skip it.
Every vector in the span of $(1, 1, 0)$ and $(1, 0, 0)$ has third entry $0$, so $e_3$ lies outside it, and we add it.
The result $\{(1, 1, 0), (1, 0, 0), (0, 0, 1)\}$ is independent and spans $\mathbb{R}^3$, so it is a basis that contains $L$.
This is part 2 with $S = L \cup \{e_1, e_2, e_3\}$.

The same walk works in other spaces.
In the space $P_2$ of real polynomials of degree at most $2$, take $L = \{1 + x, 1 - x\}$.
Its span contains $\tfrac12 \bigl((1 + x) + (1 - x)\bigr) = 1$ and $\tfrac12 \bigl((1 + x) - (1 - x)\bigr) = x$, so it is the span of $1$ and $x$.
The monomial $x^2$ is outside, so $\{1 + x, 1 - x, x^2\}$ is a basis of $P_2$.

### Why each hypothesis is needed

The set $L$ must be independent, because every subset of a basis is independent.
For example, $L = \{(1, 0), (2, 0)\}$ in $\mathbb{R}^2$ is dependent, so it lies in no basis.

In part 2, the condition $L \subseteq S$ is needed.
With $L = \{(1, 1)\}$ and $S = \{(1, 0), (0, 1)\}$, every $B$ with $L \subseteq B \subseteq S$ would need $(1, 1) \in S$, which is false.

The scalars must form a field.
In $\mathbb{Z}$, the set $\{2\}$ is independent, since $n \cdot 2 = 0$ forces $n = 0$.
But the only bases of $\mathbb{Z}$ are $\{1\}$ and $\{-1\}$, so no basis contains $2$.

In finite dimension the [[proof by adding vectors|SS0XKV9TAN]] uses only induction.
In general the [[proof by Zorn's lemma|MEFZB7GHA9]] uses the axiom of choice.

### What it gives you

In a space of dimension $n$, every independent set has at most $n$ vectors, because it sits inside a basis.
An independent set of exactly $n$ vectors has nothing left to add, so it is already a basis; this is half of the [[right-size criterion|096V7H13H9]].
Taking $L = \emptyset$ in part 1 gives the theorem that [[every vector space has a basis|00MS9VMQ9Z]], and taking $L = \emptyset$ in part 2 gives the theorem that [[every spanning set contains a basis|06MRNP4BNT]].

Every subspace $U$ of $V$ has a complement.
Extend a basis $B_U$ of $U$ to a basis $B$ of $V$, and let $W$ be the span of $B \setminus B_U$.
Then $U + W = V$ and $U \cap W = \{0\}$, so $V$ is the [[internal direct sum|0XYYT5KNTX]] $U \oplus W$.

The converse of part 1 holds: a subset of $V$ is independent exactly when it lies in some basis.

### Watch out

Add only vectors that lie outside the current span, not just vectors outside $L$.
For $L = \{(1, 1, 0)\}$, the vector $(2, 2, 0)$ is not in $L$, but adding it destroys independence.

The complement in the last remark depends on the choice of the extension.
For the $x$-axis $U$ in $\mathbb{R}^2$, extending by $(0, 1)$ gives the $y$-axis as $W$, and extending by $(1, 1)$ gives the diagonal line.
Both are complements of $U$, so a subspace has a complement but not a unique one.

### Try it

Extend $\{(1, 2, 3)\}$ to a basis of $\mathbb{R}^3$ with vectors from the standard basis.
One answer is $\{(1, 2, 3), e_2, e_3\}$, because their span contains $e_2$, $e_3$ and $e_1 = (1, 2, 3) - 2 e_2 - 3 e_3$, so three vectors span $\mathbb{R}^3$.
The walk in the order $e_1, e_2, e_3$ gives another answer, $\{(1, 2, 3), e_1, e_2\}$.

## Explanations

### L1 human

Suppose you have a few arrows that point in genuinely different directions.
You can always add more arrows until they reach the whole space, without spoiling the independence.
The rule is to add only arrows that the current ones cannot build.
For example, the arrow $(1, 1, 0)$ in space can be completed by $(1, 0, 0)$ and $(0, 0, 1)$.

### L2 human

Here is a typical use: find a basis of $\mathbb{R}^4$ that contains $u_1 = (1, 0, 1, 0)$ and $u_2 = (0, 1, 0, 1)$.
These two are independent, because each has a $1$ where the other has a $0$.
Try the standard basis vectors in order.
The vector $e_1$ is outside $\operatorname{span}(u_1, u_2)$, because every vector $a u_1 + b u_2 = (a, b, a, b)$ in the span has equal first and third entries.
After adding $e_1$, the span consists of the vectors $(a + c, b, a, b)$.
The vector $e_2 = (0, 1, 0, 0)$ would need $b = 1$ and $b = 0$ at once, so it is outside, and we add it.
Now we have four independent vectors in a space of dimension $4$, so $\{u_1, u_2, e_1, e_2\}$ is a basis by the right-size criterion.
The typical use is exactly this: start from vectors you care about, such as a basis of a subspace, and complete them to a basis of the whole space.

### L3 human

Parts 1 and 2 together say that the independent sets and the spanning sets of a vector space form a matroid, in which every independent set sits below a basis and every spanning set above one.
The statement holds for vector spaces over division rings by the same proofs, but it fails for free modules over $\mathbb{Z}$, as $\{2\}$ shows.
The complement that it produces is the starting point for direct sums, and it is behind the proof of the [[dimension formula for sums of subspaces|06HTJNCMPA]], which extends a basis of $U \cap W$ in two directions.
In infinite dimension the theorem depends on the axiom of choice, and [[every vector space has a basis|00MS9VMQ9Z]] explains how much of it is needed.
