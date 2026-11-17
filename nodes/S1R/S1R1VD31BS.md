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
Mathematicians judge a definition by the theorems it makes true, by the exceptions it removes, and by how it behaves in larger settings.
Many definitions in current use, such as those of a prime number, a field and a polyhedron, were adjusted after their first form gave awkward theorems or failed proofs.
Lakatos described this process in *Proofs and Refutations*: a counterexample to a theorem often leads to a new definition, not to a rejected theorem.
This matters for research, because the choice of definitions decides which statements are true, and how simply they can be stated.

## Motivation

The definition of a prime number could include $1$, and many writers before the twentieth century did include it.
With this choice, the [[fundamental theorem of arithmetic|084HH1NDCB]] fails as stated: $6 = 2 \cdot 3 = 1 \cdot 2 \cdot 3$ gives two factorizations into primes.
Each statement of the theorem would then need the words "primes other than $1$".
The modern definition of a [[prime number|01826KMG2H]] excludes $1$ so that the main theorem about primes holds without exceptions.
The definition did not change because a fact about $1$ was discovered.
It changed because the theorems became simpler.

## Notation

1. When conventions differ, books state their choice, as in "in this book, $0 \in \mathbb{N}$".
2. Common signs for the two conventions are $\mathbb{N}_0 = \{0, 1, 2, \dots\}$ and $\mathbb{N}^+ = \mathbb{Z}_{>0} = \{1, 2, 3, \dots\}$.
3. Words such as "nontrivial", "proper" and "nondegenerate" in a definition usually remove a degenerate case, such as the zero ring or the empty space.

## Remarks

### Criteria for a good definition

There is no formal test, but these criteria recur in mathematical practice.

1. Clean theorems. The main theorems hold without exceptions. Excluding $1$ from the primes is the standard case.
2. Stability. The definition still works, or generalizes in one clear way, in larger settings. The divisor property of primes gives prime elements of rings, see [[equivalent definitions|NZ42PS2P1A]].
3. Invariance. The definition does not depend on choices, such as coordinates or representatives, see [[well-defined|HNGZEBKVY2]].
4. Fit with examples. The definition includes the motivating examples and excludes the cases that break the theory.
5. Good behavior under constructions. Products, quotients and limits of examples are again examples, or fail for a clear reason.

These criteria can conflict, and then different books choose differently.

### Degenerate cases

Many definitions exclude a trivial object, because it breaks a pattern.

1. A field must satisfy $0 \neq 1$. This excludes the [[zero ring|008TBCYDPX]], and it makes "$\mathbb{Z}/n\mathbb{Z}$ is a field exactly when $n$ is prime" true for each $n \geq 1$.
2. A prime ideal must be proper. So $\mathbb{Z}$ itself is not a prime ideal of $\mathbb{Z}$, and the quotient by a prime ideal is an integral domain.
3. Some authors require a connected space to be non-empty. With this choice, each space is a disjoint union of connected components in exactly one way, and the empty space has no components.

The slogan "too simple to be simple" expresses this view: the trivial object is excluded from a class whose members cannot be split, much as $1$ is excluded from the primes.

### Conventions without a winner

Some choices have no single best answer, and both conventions remain in use.

1. Whether $0$ is a natural number. Set theory, logic and computer science usually include $0$. Number theory often starts at $1$.
2. Whether "ring" requires an identity element. Most algebra books now require it, and some analysis books do not.
3. Whether "positive" includes $0$. In French usage "positif" means $\geq 0$, and in English usage "positive" means $> 0$.

In such cases, a reader must check the convention of each source before using its theorems.

### Definitions shaped by proofs and counterexamples

Lakatos studied the history of [[Euler's polyhedron formula|09HT3P35YP]], $V - E + F = 2$.
Counterexamples appeared, such as a polyhedron with a tunnel through it, a "picture frame", for which $V - E + F = 0$.
Mathematicians answered in several ways.
Some declared the counterexample not a polyhedron, which Lakatos called "monster-barring".
Others analyzed the proof, found the step that fails, and added its hypothesis to the theorem, which he called "lemma-incorporation".
The second answer gave new concepts: simply connected surfaces and the [[Euler characteristic|RNDDWDAFJ5]].
Lakatos called concepts that arise this way "proof-generated", and he discussed uniform convergence and bounded variation as examples.

### Examples

1. The prime numbers exclude $1$, so that factorization into primes is unique up to order.
2. Fields satisfy $0 \neq 1$, so that the zero ring is not a field.
3. Uniform convergence was separated from pointwise convergence after the limit of continuous functions turned out to be discontinuous in some cases. Lakatos treats it as a proof-generated concept.
4. The open cover definition of [[compactness|0TVJZYB6SH]] replaced sequential definitions as the general one, because it behaves well for products, by [[Tychonoff's theorem|0JTRSJKCFB]].
5. Many books define $0! = 1$ and $x^0 = 1$, so that the formulas $n! = n \cdot (n - 1)!$ and $x^{m+n} = x^m x^n$ hold without exceptions.

### Non-examples

1. Defining a polyhedron as "a solid with $V - E + F = 2$" is legal, but it makes Euler's formula true by definition and says nothing about any solid.
2. Counting $1$ as a prime is legal, but it forces an exception into each statement of unique factorization.
3. Defining "continuous" by "the graph can be drawn without lifting the pen" is not a usable definition. No proof can use it, because the condition has no exact meaning.

### Basic properties

1. A change of definition changes which statements are theorems. A theorem proved under one convention may be false under another.
2. A good definition often makes a theorem into an equivalence, so that the defined class is exactly the class of objects with the desired property.
3. Two conventions that differ only on a degenerate case give theorems that differ only on that case. A translation between them is usually routine but must be checked.

### History

Many early Greek writers did not count $1$ as a number, so the question of its primality did not arise for them.
From the seventeenth century, some mathematicians listed $1$ as the first prime, and many in the nineteenth century still did.
Euler stated the polyhedron formula in the 1750s, and the counterexamples and repairs that Lakatos discusses followed in the nineteenth century.
Lakatos published *Proofs and Refutations* as four articles in 1963 and 1964, and as a book in 1976.

### Common errors

1. A student treats a convention as a fact, and argues that $0$ "really is" or "really is not" a natural number.
2. A student combines theorems from two books with different conventions, for example on whether rings have an identity.
3. A student adds hypotheses to a definition to avoid a counterexample, and does not notice that the theorem has become empty.

## Explanations

### L1 human

Mathematicians can define words in many ways, so they choose the way that makes the rules simplest.
For example, $1$ is not called a prime number.
If it were, then $6$ could be written as $2 \cdot 3$, and also as $1 \cdot 2 \cdot 3$, and also as $1 \cdot 1 \cdot 2 \cdot 3$.
The rule "each number splits into primes in only one way" would fail.
Leaving $1$ out of the primes keeps the rule simple.
So a definition is not discovered like a fact; it is chosen like a good tool.

### L2 human

We compare two definitions of a field, with and without the condition $0 \neq 1$, through the theorem "$\mathbb{Z}/n\mathbb{Z}$ is a field exactly when $n$ is prime".

1. If $n = p$ is prime, each nonzero class $[a]$ has $\gcd(a, p) = 1$. By Bézout's identity $ax + py = 1$, so $[a][x] = [1]$, and $\mathbb{Z}/p\mathbb{Z}$ is a field.
2. If $n = ab$ with $1 < a, b < n$, then $[a][b] = [0]$ with $[a] \neq [0] \neq [b]$. A field has no such pair, so $\mathbb{Z}/n\mathbb{Z}$ is not a field.
3. For $n = 1$, the ring $\mathbb{Z}/1\mathbb{Z}$ has one element, and $[0] = [1]$.
4. With the condition $0 \neq 1$, this ring is not a field, and the theorem holds for each $n \geq 1$.
5. Without the condition, each nonzero element of $\mathbb{Z}/1\mathbb{Z}$ has an inverse, because there is no nonzero element. So it would be a field, and the theorem would need the exception $n = 1$.

The typical use: when a theorem needs an exception, check whether a definition should exclude a degenerate case.
A trap is to exclude too much.
A definition that removes every counterexample by name makes the theorem empty.

### L3 human

Research mathematics often finds the right definition only after the main theorems are known.
Grothendieck's schemes include non-reduced rings, because base change and intersection theory need them, although early definitions of varieties excluded them.
The notion of a sheaf, of a topological space and of a measurable set all passed through several versions before the current one.
Lakatos's "proof-generated concepts" describe one mechanism: the hidden lemma of a proof becomes a definition, and the theorem holds for the new class by construction.
Formal libraries make conventions explicit and global.
Mathlib takes $0 \in \mathbb{N}$, sets $x / 0 = 0$, and requires fields to be nontrivial.
These are choices for convenient algebra, and each theorem records the hypotheses that the conventions do not cover.
A good definition in this sense is one under which the library's theorems need the fewest side conditions.
