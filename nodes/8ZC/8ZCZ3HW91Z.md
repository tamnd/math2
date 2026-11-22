---
tag: 8ZCZ3HW91Z
kind: concept
name: Mathematical definition
aliases: [definition]
msc: ["00A35", "97E40"]
topics: [BP0WAF23HB]
audience: school
uses: [0B94TKFQJX, 0S6GMNJ62Y]
sources:
  - url: https://en.wikipedia.org/wiki/Definition
    locator: In logic, mathematics and computing
  - url: https://en.wikipedia.org/wiki/Circular_definition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: lead section
---

## Summary

A mathematical definition is an agreement that gives a new word one exact meaning, so that every reader can check every use of the word.
Take the one you know best: an integer $p$ is *prime* if $p > 1$ and the only positive divisors of $p$ are $1$ and $p$.
With it, $7$ is prime, $6$ is not because $2$ divides $6$, and $1$ is not because it fails $p > 1$.

In general, a definition has two parts.
The *definiendum* is the new term, here "prime".
The *definiens* is the condition that gives its meaning, stated only in terms that are already known: primitive notions, terms defined before, and the words of logic.
After the definition, the term and the condition can replace each other in every statement and in every [[proof|0B94TKFQJX]].
A definition is a stipulation, not a claim, so it is neither true nor false.
It can only be clear or unclear, and useful or useless.

## Motivation

Everyday words have vague edges.
"A big number" or "a smooth curve" means different things to different people, and nobody can prove a statement about them.
A proof must be checkable step by step, so each term in it needs one meaning that all readers share.

Everybody "knows" what an even number is.
But to prove that the sum of two even numbers is even, we need a condition that we can calculate with.
The definition "$n$ is even if $n = 2k$ for some integer $k$" gives one, and the proof becomes one line:
$$2k + 2l = 2(k + l).$$
Each later page of the sub-area asks what else a definition needs before we may use it in this way.

## Notation

The usual form is "Let $x$ be a ... . We say that $x$ is *P* if $C(x)$", with the new term in italics or in bold type.
You will also see "$x$ is called *P* if ...", "A *P* is an object $x$ such that ...", and numbered blocks such as "Definition 3.2".
A new symbol for an object is often written with $:=$, as in $n! := 1 \cdot 2 \cdots n$, and the colon stands on the side of the new symbol.
Some books write $\overset{\text{def}}{=}$ or $\overset{\text{def}}{\iff}$, and some write $\equiv$, which has other meanings too.
A few authors write "if and only if" in every definition, but most write only "if", and the reader must read it as "if and only if".

## Remarks

### Reading a definition slowly

Go back to the prime numbers and read each part of the definiens.
The phrase "an integer $p$" fixes the kind of object, so the question "is $\tfrac{1}{2}$ prime?" gets no answer: it is outside the definition.
The condition $p > 1$ removes $0$, $1$ and the negative integers.
The condition on divisors does the main work, and you test it by trial:
$$15 = 3 \cdot 5, \qquad 13 = 1 \cdot 13 \text{ only}.$$
So $15$ is not prime and $13$ is prime.
Check: $13$ is not divisible by $2$ or $3$, and $4^2 = 16 > 13$, so no larger divisor needs a test.

A definition of a property $P$ for objects $x$ of a kind $K$ has the general form
$$\text{for each } x \text{ of kind } K: \quad x \text{ is } P \iff C(x).$$
So a definition is a [[biconditional|0S6GMNJ62Y]] that we decide to accept.
The definiens $C(x)$ may use only $x$, known terms and logic, and it must not use $P$ itself, or the definition is circular.

### The "if" that means "if and only if"

A function $f \colon \mathbb{R} \to \mathbb{R}$ is [[even|0FP31SX5EA]] if $f(-x) = f(x)$ for all real $x$.
The function $x^2$ is even, because $(-x)^2 = x^2$.
The function $x^3$ is not even, because
$$f(-1) = -1 \neq 1 = f(1).$$
But read "if" as one-way, and the definition only tells you that functions with $f(-x) = f(x)$ are even.
It would say nothing about $x^3$, and "even" would have no fixed meaning.
A definition must settle every object, so its "if" means "if and only if".

This reading belongs to the defining clause only.
In a theorem, "if $f$ and $g$ are even, then $f + g$ is even" is one-way, and its converse fails: $x^3$ and $-x^3$ are not even, but their sum $0$ is.
So the same word "if" has two uses, and you tell them apart by asking whether the sentence introduces a new term.

### More definitions to read

[[The definition of an even integer|BV6E0ZG3YN]] settles the borderline cases: $0 = 2 \cdot 0$ is even, and $-6 = 2 \cdot (-3)$ is even.
[[The definition of divisibility|73TT8GGNBM]] says that $a \mid b$ if $b = ak$ for some integer $k$, and so it makes $0 \mid 0$ true, since $0 = 0 \cdot 5$.
A set $A$ is a [[subset|0BJR9QR08E]] of $B$ if every element of $A$ is an element of $B$, so the empty set is a subset of every set: it has no element that could fail.
A [[group|G5S1M9]] is a set with an operation that is associative, has an identity element and has inverses, and an object must meet all three conditions.
In each case the definiens uses only earlier terms, and in each case it decides some case that intuition leaves open.

### What fails to be a definition

[[Euclid's description of a point|FYC7X2HYBH]], "that which has no part", uses the undefined word "part", and no proof in the *Elements* uses it.
"A set is a collection, and a collection is a set" is circular: each definiens uses the other definiendum, so neither word gets a meaning.
"A number is large if it is much bigger than $1$" is vague, because "much" has no exact meaning.
"A positive integer $n$ is *good* if $n + 1$ is good" uses the definiendum in its own definiens.
It does not decide whether $1$ is good, since both "no number is good" and "every number is good" agree with it.

### A definition can hide a claim

A definition cannot be refuted, so "we call $1$ a prime" would be legal, though [[a bad choice|S1R1VD31BS]].
But many definitions contain a claim that needs a proof before the definition is legal.
A definition with "the", such as "the identity element of a group", claims that exactly one such object exists, as [[definitions that use "the"|5P955TVSS2]] explains.
A definition by representatives, such as $[a] + [b] := [a + b]$ for residues, claims that the result does not depend on the representatives, which is the subject of [[well-defined|HNGZEBKVY2]].
A recursive definition claims that the recursion has exactly one solution, as [[kinds of definitions|B60DBNF77S]] shows.
A second definition of a word that already has one claims that the two agree, which is the subject of [[equivalent definitions|NZ42PS2P1A]].
Until such a claim is proved, the "definition" is only a proposal.

### Unfolding, folding and negating

Because the term and the condition are interchangeable, a proof can replace "$x$ is $P$" by $C(x)$ at any point.
This step is called unfolding the definition, and it is the first step of most proofs.
The last step usually runs the other way: we show $C(x)$ and fold it back into "$x$ is $P$".

Negation follows the same rule: "$x$ is not $P$" means "not $C(x)$".
So $n$ is not even exactly when $n \neq 2k$ for every integer $k$, which is a statement about all $k$.
A defined term is an abbreviation, so every statement that uses it can be rewritten without it.

### Watch out

The first error is to treat the "if" of a definition as one-way and then try to prove the converse.
In "$n$ is even if $n = 2k$", both directions hold by agreement.

The second error is to argue from a picture instead of the definition.
A student may think that every function has a formula, but the definition of a [[function|0EPAT51DXQ]] asks only that each input has exactly one output.

The third error is to drop a condition of the definiens.
The number $1$ has only $1$ and itself as positive divisors, so a student who forgets $p > 1$ calls $1$ prime.

### History and Try it

Book I of [[Euclid's Elements|83WHDAV68J]] opens with 23 definitions, 5 postulates and 5 common notions, and some of the definitions, such as the one for a point, are descriptions that no proof uses.
In 1899 Hilbert built geometry on [[primitive notions|QMQEJKFEYZ]] that have no definition, with axioms that fix their use.
The Latin words "definiendum" and "definiens" mean "what is to be defined" and "what defines".

First, a function is *odd* if $f(-x) = -f(x)$ for all real $x$.
Is $f(x) = x^3 + 1$ odd?
No: $f(-1) = 0$ but $-f(1) = -2$.

Second, write out what "$a$ does not divide $b$" means.
It means that $b \neq ak$ for every integer $k$, so $3 \nmid 7$ because $3k$ is at most $6$ for $k \le 2$ and at least $9$ for $k \ge 3$.

## Explanations

### L1 human

In mathematics, a definition is a promise about how a word will be used.
It says exactly which things get the name and which do not.
Mathematicians agree that a whole number is even when it is two times some whole number.
So $14$ is even, because it is two times $7$.
And $15$ is not even, because two times $7$ is $14$ and two times $8$ is $16$, so no whole number works.
Nobody can say that the definition is wrong, because it is an agreement, not a fact.
But everybody must use the word in exactly the agreed way, and that is what makes proofs possible.

### L2 human

We prove that the sum of two odd integers is even, using nothing but the definitions.
An integer $n$ is odd if $n = 2k + 1$ for some integer $k$.

1. Let $m$ and $n$ be odd integers.
2. Unfold the definition of odd for $m$: there is an integer $k$ with $m = 2k + 1$.
3. Unfold it for $n$: there is an integer $l$ with $n = 2l + 1$.
   We need a new letter, because $n$ need not use the same $k$ as $m$.
4. Add and factor:
   $$m + n = 2k + 2l + 2 = 2(k + l + 1).$$
5. The number $j = k + l + 1$ is an integer, because sums of integers are integers.
6. So $m + n = 2j$, and we fold this back: $m + n$ is even.

Check with numbers: $7 + 9 = 16 = 2 \cdot 8$, and $k + l + 1 = 3 + 4 + 1 = 8$.
The shape of the proof is the typical use of a definition: unfold the hypotheses, calculate, and fold the conclusion.
Watch out for step 3: a student who writes $n = 2k + 1$ with the same $k$ proves the result only for $m = n$.

### L3 human

In formal logic, an explicit definition adds a new symbol $P$ and an axiom $\forall x \, (P(x) \leftrightarrow C(x))$ to a theory.
Such an extension is conservative: it proves no new statement in the old language, and each formula with $P$ is equivalent to one without $P$.
Beth's definability theorem for first-order logic goes the other way.
If the axioms fix $P$ from the old symbols in every model, then $P$ has an explicit definition, so implicit and explicit definitions have the same power there, although the [[kinds of definitions|B60DBNF77S]] look different in practice.

In a proof assistant such as Lean, a definition is a named term, and unfolding it is a reduction step that the checker performs.
Mathlib defines an element $a$ to be even when $a = r + r$ for some $r$, which agrees with the school definition because $r + r = 2r$ in every ring.
The hidden claims of a definition become proof obligations there.
Lean accepts a recursive definition only when it can check that the recursion terminates, and a function on a quotient built with `Quotient.lift` must come with a proof that it respects the relation.
