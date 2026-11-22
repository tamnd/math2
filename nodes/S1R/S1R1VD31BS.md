---
tag: S1R1VD31BS
kind: concept
name: Choosing good definitions
aliases: [choice-of-definitions, proof-generated-definition, convention-in-definitions]
msc: ["00A35", "00A30"]
topics: [BP0WAF23HB]
audience: research
uses: [8ZCZ3HW91Z, NZ42PS2P1A, 01826KMG2H, 084HH1NDCB, 09HT3P35YP]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_and_Refutations
    locator: Synopsis
  - url: https://en.wikipedia.org/wiki/Prime_number
    locator: Primality of one
  - url: https://en.wikipedia.org/wiki/Natural_number
    locator: Zero as natural number
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Definition
---

## Summary

A [[definition|8ZCZ3HW91Z]] cannot be false, but it can be a bad choice.
Mathematicians judge a definition mainly by the theorems that it makes true and by the exceptions that it removes.

The standard case is the number $1$.
Nothing stops us from calling $1$ a prime, and many older authors did.
But then $6 = 2 \cdot 3 = 1 \cdot 2 \cdot 3$ would be two different factorizations into primes, and the uniqueness of prime factorization would fail.
So the modern definition of a [[prime number|01826KMG2H]] requires $p > 1$, and the [[fundamental theorem of arithmetic|084HH1NDCB]] holds with no exception.
In general, a definition is good when its main theorems hold without exceptions, when it does not depend on arbitrary choices, and when it extends cleanly to larger settings.

## Motivation

The change in the definition of a prime did not come from a new fact about $1$.
It came from the theorems: with $1$ excluded, unique factorization, the formulas for the number of divisors and for Euler's function, and the prime factorization of ideals in later algebra all hold as stated.
With $1$ included, each of them would need the words "primes other than $1$".

Many current definitions have the same kind of history.
Fields, prime ideals, connected spaces and polyhedra all have conditions that remove a case that broke a theorem.
Imre Lakatos made this process the subject of *Proofs and Refutations*: a counterexample to a theorem often leads to a new definition rather than to a rejected theorem.
For research, this matters because the choice of definitions decides which statements are true and how simply they can be stated.

## Notation

When conventions differ, a careful book states its choice, as in "in this book, $0 \in \mathbb{N}$".
Common signs that remove the doubt are $\mathbb{N}_0 = \{0, 1, 2, \dots\}$ and $\mathbb{Z}_{>0} = \{1, 2, 3, \dots\}$, but even the bare $\mathbb{N}$ means one set in some books and the other set in others.
Words such as "nontrivial", "proper" and "nondegenerate" in a definition usually remove a degenerate case, such as the zero ring or the empty space.

## Remarks

### What makes a definition good

No formal test exists, but some criteria recur in practice.
The first is clean theorems: the main results hold without exceptions, as unique factorization does once $1$ is not prime.
The second is invariance: the definition does not depend on choices of coordinates or of representatives, as a [[well-defined|HNGZEBKVY2]] operation does not.
The third is stability: the definition extends in one clear way to larger settings.
The divisor property of primes, "$p \mid ab$ implies $p \mid a$ or $p \mid b$", becomes the definition of a prime element of a ring, as [[equivalent definitions|NZ42PS2P1A]] and [[two definitions of a prime number|787PD6B171]] show.
The fourth is good behavior under constructions: products and quotients of examples are again examples, or fail for a clear reason.

These criteria can conflict.
When they do, different books choose differently, and both choices stay in use.

### Degenerate cases

Many definitions exclude a trivial object because it breaks a pattern.
A field must satisfy $0 \ne 1$.
This excludes the [[zero ring|008TBCYDPX]], and it makes "$\mathbb{Z}/n\mathbb{Z}$ is a field exactly when $n$ is prime" true for every $n \ge 1$, as the L2 explanation below checks.
A prime ideal must be a proper ideal, so $\mathbb{Z}$ is not a prime ideal of itself, and the quotient by a prime ideal is always an integral domain.

The empty space is the subtle case.
Some authors require a connected space to be nonempty.
With that choice, every space is the disjoint union of its connected components in exactly one way, and the empty space has no components at all, just as $1$ has no prime factors.
The slogan "too simple to be simple" describes the pattern: the trivial object is left out of a class of objects that cannot be split.

### Conventions without a winner

Some choices have no single best answer, and both conventions remain in use.
Whether $0$ is a natural number is the main example.
Set theory, logic and computer science usually include $0$, and many books in number theory and analysis start at $1$.
Neither choice is a fact, so a reader checks the convention of each source.

Whether a ring must have an identity element is another case.
Most algebra books now require one, and books that study rings of functions or operators without a unit often do not.
In French usage, "positif" means $\ge 0$, while in English "positive" usually means $> 0$.

### Definitions shaped by counterexamples

Lakatos studied the history of [[Euler's polyhedron formula|09HT3P35YP]], $V - E + F = 2$.
Counterexamples appeared, such as a "picture frame", a polyhedron with a square tunnel through it.
If the top and the bottom face of a square frame are each cut into four trapezoids, the frame has $V = 16$, $E = 32$ and $F = 16$, so
$$V - E + F = 16 - 32 + 16 = 0.$$
Some mathematicians answered that the frame is not a polyhedron, which Lakatos called "monster-barring".
Others analyzed the proof, found the step that fails, and added its hypothesis to the theorem, which he called "lemma-incorporation".
The second answer led to new concepts, such as simply connected surfaces and the [[Euler characteristic|RNDDWDAFJ5]].
Lakatos called concepts that arise this way "proof-generated", and he also discussed uniform convergence and bounded variation as examples.
[[Proofs and refutations|79P9CTRN0V]] describes his method in full.

### More cases and non-cases

Many books set $0! = 1$ and $x^0 = 1$ for $x \ne 0$.
Then $n! = n \cdot (n - 1)!$ holds for every $n \ge 1$, and $x^{m + n} = x^m x^n$ holds for all $m, n \ge 0$, with no exceptions.
For [[compact spaces|0TVJZYB6SH]], the open cover definition is the general one in topology, and it behaves well under products.
By [[Tychonoff's theorem|0JTRSJKCFB]] every product of compact spaces is compact, while a product of uncountably many sequentially compact spaces need not be sequentially compact.

Three choices are legal and bad.
Defining a polyhedron as "a solid with $V - E + F = 2$" makes Euler's formula true by definition, so the formula says nothing.
Counting $1$ as a prime forces an exception into every statement of unique factorization.
Defining "continuous" as "the graph can be drawn without lifting the pen" gives no condition that a proof can use.

### Watch out

The first error is to treat a convention as a fact and to argue that $0$ "really is" or "really is not" a natural number.
The second error is to combine theorems from two books with different conventions.
For example, a book that does not require rings to have an identity may call $2\mathbb{Z}$ a ring, and a theorem about rings with identity then does not apply to it.
The third error is to add hypotheses to a definition until a counterexample goes away, and not to notice that the theorem has become empty.

### History

Many early Greek writers did not count $1$ as a number at all, so the question of its primality did not arise for them.
From the seventeenth century, some mathematicians listed $1$ as the first prime, and many in the nineteenth century still did.
Euler stated the polyhedron formula in the 1750s, and the counterexamples and repairs that Lakatos discusses followed in the nineteenth century.
Lakatos published *Proofs and Refutations* as four articles in 1963 and 1964, and as a book in 1976.

### Try it

First, why does $x^0 = 1$ make the law $x^{m + n} = x^m x^n$ hold for $m = 0$?
The law then reads $x^n = x^0 x^n = 1 \cdot x^n$, which is true, while any other value of $x^0$ would make it false for $x \ne 0$.

Second, if the empty space counted as connected, would the decomposition into components be unique?
No: we could add any number of empty "components" to a decomposition, so the count of components would not be fixed.

## Explanations

### L1 human

Mathematicians can define a word in many ways, so they choose the way that makes the rules simplest.
For example, $1$ is not called a prime number.
If it were, then $6$ could be written as $2 \cdot 3$, as $1 \cdot 2 \cdot 3$, and as $1 \cdot 1 \cdot 2 \cdot 3$.
The rule "each number splits into primes in only one way" would fail.
Leaving $1$ out of the primes keeps the rule simple.
So a definition is not discovered like a fact; it is chosen like a good tool.

### L2 human

We compare two definitions of a field, with and without the condition $0 \ne 1$, through the theorem "$\mathbb{Z}/n\mathbb{Z}$ is a field exactly when $n$ is prime".
If $n = p$ is prime and $[a] \ne [0]$, then $\gcd(a, p) = 1$, so [[Bézout's identity|0DQVHMYAGA]] gives integers $x, y$ with $ax + py = 1$.
Then $[a][x] = [1]$, so every nonzero class has an inverse, and $\mathbb{Z}/p\mathbb{Z}$ is a field.
If $n = ab$ with $1 < a, b < n$, then
$$[a][b] = [n] = [0], \qquad [a] \ne [0], \qquad [b] \ne [0],$$
and a field has no such pair, so $\mathbb{Z}/n\mathbb{Z}$ is not a field.

That leaves $n = 1$, where $\mathbb{Z}/1\mathbb{Z}$ has one element and $[0] = [1]$.
With the condition $0 \ne 1$, it is not a field, and the theorem holds for every $n \ge 1$.
Without the condition, it would be a field, because "every nonzero element has an inverse" is vacuously true when no element is nonzero.
Then the theorem would need the exception $n = 1$.
The lesson is general: when a theorem needs an exception, ask whether the definition should exclude a degenerate case.
Watch out: a definition that removes every counterexample by name makes the theorem empty.

### L3 human

Research mathematics often finds the right definition only after the main theorems are known.
Grothendieck's schemes allow non-reduced rings, because base change and intersection theory need them, although varieties are reduced.
Lakatos's proof-generated concepts describe one mechanism: the hidden lemma of a proof becomes a definition, and the theorem holds for the new class by construction.

Formal libraries make conventions explicit and global.
Mathlib takes $0 \in \mathbb{N}$, sets $x / 0 = 0$ (the lemma `div_zero`), and builds nontriviality into the definition of a field, since `DivisionRing` extends `Nontrivial`.
These are choices that make algebra convenient, and each theorem states the hypotheses, such as $y \ne 0$, that the conventions do not cover.
A good definition in this sense is one under which the theorems need the fewest side conditions.
