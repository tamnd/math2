---
tag: 0FS3RHF6KE
kind: statement
role: theorem
name: Infinite pigeonhole principle
msc: ["05A05", "03E05"]
topics: [GB14W4SYPK]
audience: ug1
about: [01MKW4R283, 0BBTH3YSZA, 0EPAT51DXQ]
uses: [0HGVCWQGY3, 01MKW4R283, 0BBTH3YSZA]
sources:
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: Infinite sets
---

## Statement

Let $A$ be an [[infinite set|01MKW4R283]], let $B$ be a [[finite set|0BBTH3YSZA]], and let $f : A \to B$ be a function.
Then there is an element $b \in B$ such that the fibre $f^{-1}(b) = \set{a \in A : f(a) = b}$ is infinite.

In words: if infinitely many objects go into finitely many boxes, then some box receives infinitely many objects.
The [[proof|Z117P4ZE5F]] uses only the fact that a finite union of finite sets is finite.
For sequences the statement reads: a sequence $(x_m)_{m \geq 1}$ with values in a finite set $B$ has a constant [[subsequence|0R8J3ZQMJS]].

## Remarks

### Why each hypothesis is needed

- The set $B$ must be finite. For the identity map $f : \N \to \N$, each fibre $f^{-1}(b) = \set{b}$ has one element.
- The set $A$ must be infinite. If $A$ is finite, each fibre is a subset of $A$, so each fibre is finite.
- The map $f$ must be defined on all of $A$. If only the elements of a finite subset of $A$ are placed into boxes, each box receives finitely many of them.

### Consequences

- A sequence with values in a finite set has a constant subsequence. For example, the last digits of $2, 4, 8, 16, 32, 64, \ldots$ lie in $\set{0, 1, \dots, 9}$, so some digit occurs infinitely often. In fact $2, 4, 8, 6$ repeat with period $4$.
- In each infinite sequence of integers, infinitely many terms have the same remainder modulo $10$. So infinitely many pairs of terms have a difference divisible by $10$.
- The [[Bolzano-Weierstrass theorem|0KDJD249DT]] has a proof by bisection: at each step one of two halves of an interval contains $x_m$ for infinitely many indices $m$.
- The infinite form of [[Ramsey's theorem|00TQV3F5S4]] starts from this principle: one of finitely many colours is used on infinitely many edges at a vertex.

### Converse

The converse is true: if every map from $A$ to every non-empty finite set has an infinite fibre, then $A$ is infinite.
Indeed, the map from $A$ to a one-element set has the single fibre $A$, so $A$ itself is infinite.

### Generalizations

- An uncountable set split into countably many boxes has an uncountable box. The proof uses the theorem that a [[countable union of countable sets is countable|0Z8FM54P86]], which needs a weak form of the [[axiom of choice|0HTGB13FE2]].
- The finite forms are the [[pigeonhole principle|0HGVCWQGY3]] and the [[generalized pigeonhole principle|0BY7GN3449]].
- [[Ramsey theory|G5TWXV565S]] studies the many statements of the form "a large structure split into a few parts has a large part with structure".

## Explanations

### L1 human

Suppose we put infinitely many marbles into a finite number of boxes.
Then at least one box gets infinitely many marbles.
If each box got only a finite number, we could count all the marbles box by box and get a finite total.
For example, colour each whole number red or blue.
Then at least one of the two colours is used for infinitely many numbers.

### L2 human

We show that each sequence $(x_m)_{m \geq 1}$ in the interval $[0, 1]$ has a subsequence that stays in smaller and smaller intervals.

1. Split $I_0 = [0, 1]$ into the halves $[0, 1/2]$ and $[1/2, 1]$. Each index $m$ goes into a half that contains $x_m$, and the set of indices is infinite.
2. By the infinite pigeonhole principle with two boxes, one half contains $x_m$ for infinitely many $m$. Call this half $I_1$. Its length is $1/2$.
3. Repeat with $I_1$ and the infinite set of indices $m$ with $x_m \in I_1$. We get an interval $I_2 \subseteq I_1$ of length $1/4$ that contains $x_m$ for infinitely many $m$.
4. After $k$ steps we have $I_k$ of length $2^{-k}$ with infinitely many indices.
5. Choose indices $m_1 < m_2 < \cdots$ with $x_{m_k} \in I_k$. This is possible at each step, because $I_k$ has infinitely many indices, so it has one larger than $m_{k-1}$.
6. For $j \geq k$, both $x_{m_j}$ and $x_{m_k}$ lie in $I_k$, so $|x_{m_j} - x_{m_k}| \le 2^{-k}$.

The subsequence of step 5 is a Cauchy sequence, and this is the core of the bisection proof of the [[Bolzano-Weierstrass theorem|0KDJD249DT]].
A trap is to forget that the boxes must be finite in number: the bisection works because each step has only two halves.

### L3 human

In terms of cardinals, the statement says that an infinite cardinal is not a finite sum of finite cardinals.
In Mathlib it appears as `Finite.exists_infinite_fiber`.
The uncountable version, and versions for larger cardinals, depend on the cofinality of the cardinal, a subject of set theory.

The principle is the first step of compactness arguments in analysis and of infinite [[Ramsey's theorem|00TQV3F5S4]] in combinatorics.
A repeated use of it, with a diagonal choice of a subsequence, gives the [[diagonalization technique|~7da89d71]] for sequences.
König's lemma on infinite trees with finite branching is another repeated use: at each vertex one of finitely many branches has infinitely many vertices below it.
