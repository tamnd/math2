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

If infinitely many objects go into finitely many boxes, then some box receives infinitely many objects.

Let $A$ be an [[infinite set|01MKW4R283]], let $B$ be a [[finite set|0BBTH3YSZA]], and let $f : A \to B$ be a function.
Then there is an element $b \in B$ whose fiber $f^{-1}(b) = \{ a \in A : f(a) = b \}$ is infinite.

For sequences the statement reads: a sequence $(x_m)_{m \geq 1}$ with values in a finite set $B$ has a constant [[subsequence|0R8J3ZQMJS]].
The [[proof|Z117P4ZE5F]] uses only the fact that a finite union of finite sets is finite.

## Remarks

### A first use: a digit that never stops

Look at the last digits of the powers of $2$:
$$2, 4, 8, 16, 32, 64, 128, 256, \ldots \quad \text{end in} \quad 2, 4, 8, 6, 2, 4, 8, 6, \ldots$$
The objects are the infinitely many powers, and the boxes are the $10$ digits.
The infinite pigeonhole principle says that some digit occurs infinitely often, before we compute anything.
Here the computation agrees: $2, 4, 8, 6$ repeat with period $4$, and each of them occurs infinitely often.
In the same way, every infinite sequence of integers has infinitely many terms with one remainder modulo $10$, so infinitely many pairs of terms have a difference divisible by $10$.

### Why each hypothesis is needed

The set $B$ of boxes must be finite.
For the identity map $f : \mathbb{N} \to \mathbb{N}$, each fiber $f^{-1}(b) = \{b\}$ has one element.

The set $A$ must be infinite.
If $A$ is finite, each fiber is a subset of $A$, so each fiber is finite.

The map $f$ must be defined on all of $A$.
If only a finite subset of $A$ is placed into boxes, each box receives finitely many objects.

### What it gives you

The [[Bolzano-Weierstrass theorem|0KDJD249DT]] has a proof by bisection: at each step one of two halves of an interval contains $x_m$ for infinitely many indices $m$, and the L2 explanation below works it out.
The infinite form of [[Ramsey's theorem|00TQV3F5S4]] starts from the principle: one of finitely many colors is used on infinitely many edges at a vertex.
König's lemma on infinite trees with finitely many branches at each vertex is a repeated use: at each vertex, one branch has infinitely many vertices below it.

### The converse

The converse is true: if every map from $A$ to a non-empty finite set has an infinite fiber, then $A$ is infinite.
The map from $A$ to a one-element set already shows this, since its only fiber is $A$ itself.

### Generalizations

An uncountable set split into countably many boxes has an uncountable box.
The proof uses the theorem that a [[countable union of countable sets is countable|0Z8FM54P86]], and that theorem needs a weak form of the [[axiom of choice|0HTGB13FE2]].
The finite forms are the [[pigeonhole principle|0HGVCWQGY3]] and the [[generalized pigeonhole principle|0BY7GN3449]].
[[Ramsey theory|G5TWXV565S]] studies the many statements of the form "a large structure split into a few parts has a large part with structure".

### Watch out

The principle finds an infinite box, but it gives no bound on when the objects in that box appear.
In the powers of $2$, the digit $6$ first occurs at $16$, and in other sequences the first repeat can come very late.
A second slip is to apply it with infinitely many boxes.
The sequence $1, 2, 3, \ldots$ has values in the infinite set $\mathbb{N}$, and it has no constant subsequence.

### Try it

Show that every infinite sequence of real numbers has infinitely many terms that are all $\geq 0$ or infinitely many terms that are all $< 0$.
Use the two boxes "$\geq 0$" and "$< 0$" for the indices, and one box receives infinitely many.

Does every map from an uncountable set to $\mathbb{N}$ have an infinite fiber, even though $\mathbb{N}$ is infinite?
Yes: by the generalization above some fiber is uncountable, and an uncountable set is infinite.

## Explanations

### L1 human

Suppose we put infinitely many marbles into a finite number of boxes.
Then at least one box gets infinitely many marbles.
If each box got only a finite number, we could count all the marbles box by box and get a finite total.
For example, color each whole number red or blue.
Then at least one of the two colors is used for infinitely many numbers.

### L2 human

We show that each sequence $(x_m)_{m \geq 1}$ in $[0, 1]$ has a subsequence whose terms crowd together.
Split $I_0 = [0, 1]$ into the halves $[0, 1/2]$ and $[1/2, 1]$, and put each index $m$ into a half that contains $x_m$.
The indices form an infinite set and there are two boxes, so one half $I_1$, of length $\tfrac{1}{2}$, contains $x_m$ for infinitely many $m$.
Repeat with $I_1$ and its infinite set of indices: one half $I_2$ of $I_1$, of length $\tfrac{1}{4}$, contains $x_m$ for infinitely many $m$.
After $k$ steps, we have an interval $I_k$ of length $2^{-k}$ with infinitely many indices.
Now choose indices $m_1 < m_2 < \cdots$ with $x_{m_k} \in I_k$, which is possible because $I_k$ has an index larger than $m_{k-1}$.
For $j \geq k$, both $x_{m_j}$ and $x_{m_k}$ lie in $I_k$, so
$$|x_{m_j} - x_{m_k}| \le 2^{-k}.$$
So the subsequence is a Cauchy sequence, and this is the core of the bisection proof of the Bolzano-Weierstrass theorem.
Each step used only two boxes, and that is why the principle applies at every step.

### L3 human

In terms of cardinals, the statement says that an infinite cardinal is not a finite sum of finite cardinals.
In Mathlib it appears as `Finite.exists_infinite_fiber`.
The uncountable version and the versions for larger cardinals depend on the cofinality of the cardinal, a subject of set theory.

The principle is the first step of compactness arguments in analysis and of the infinite [[Ramsey's theorem|00TQV3F5S4]] in combinatorics.
A repeated use, with a diagonal choice of a subsequence, gives the [[diagonalization technique|V2H30SA654]] for sequences.
