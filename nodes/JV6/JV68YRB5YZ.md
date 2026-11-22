---
tag: JV68YRB5YZ
kind: concept
name: Abuse of notation
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
uses: [QKEX4PD029, G5S1M9, 0EPAT51DXQ, 0W95W33CMP, PZMGQMDN25]
sources:
  - url: https://en.wikipedia.org/wiki/Abuse_of_notation
    locator: Examples
---

## Summary

An abuse of notation is a shortcut that is wrong by the letter of the definitions but that every reader expands in the same correct way.
A group theory book writes "by abuse of notation we write $G$ for $(G, \cdot)$", and from then on it says "let $G$ be a group" and "let $x \in G$", though a group is a pair and $x$ lies in its set.

An *abuse of notation* is a use of a symbol that is not correct under the strict definitions, but that the context expands into exactly one correct expression.
Authors use it on purpose, because the exact form is long and the short form shows the idea.
The standard abuses name a structure by its set, name an equivalence class by one of its members, write $f(x)$ for a function $f$, and write $=$ between objects that are only isomorphic.
An abuse is acceptable only when the expansion is unique.

## Motivation

A [[group|G5S1M9]] is a pair $(G, \cdot)$ of a set and an operation, so the strict notation carries both parts everywhere.
The strict sentence reads "let $(G, \cdot)$ be a group and let $(H, \cdot|_{H \times H})$ be a subgroup of $(G, \cdot)$".
It is correct and hard to read, and every author writes "let $G$ be a group and $H$ a subgroup" instead.
The short form loses nothing, because the operation on $H$ is the one from $G$.

So mathematics accepts such shortcuts, and a reader must know which ones are standard and how to expand them.
The danger is a shortcut that looks like an abuse but has no correct expansion, and then it is an error.
The test for that danger is the idea of a [[well-defined|HNGZEBKVY2]] operation.

## Notation

Authors often flag the shortcut with the words "by abuse of notation" or "by abuse of language", the second for a word used in a loose sense.
A common example of the second kind calls a vector space $V$ a representation of a group $G$, though the representation is the homomorphism from $G$ to $\mathrm{GL}(V)$.
The pages of this site use the four standard abuses of the Summary without comment.
They avoid two others: they do not write $\sin^{-1}$ for $\arcsin$, and they do not write $f(x)$ for a function when $x$ is also a number in the same sentence.

## Remarks

### A structure named by its set

"The group $\mathbb{Z}$" names a set, but a set alone is not a group.
The reader expands it to $(\mathbb{Z}, +)$, because multiplication fails: $2m = 1$ has no integer solution $m$, so $2$ has no inverse.
[[The group Z means the integers under addition|X51H6XKCDQ]] works this through.
In the same way "the ring $\mathbb{Z}$" means $(\mathbb{Z}, +, \cdot)$, while "$\mathbb{Z}$ is countable" refers to the set alone.
The writer relies on the reader to pick the one structure that makes the sentence meaningful, and the abuse is safe when only one choice does.
This shortcut is also called suppression of parameters.

### A class named by a member

In [[integers modulo 7|03VFZ2WETT]], books write $5 + 4 = 2$, though the elements are [[equivalence classes|0W95W33CMP]].
The exact form is
$$[5] + [4] = [9] = [2], \qquad \text{since } 9 - 2 = 7.$$
The shortcut is safe because the sum does not depend on the member that names a class.
Take $12 \in [5]$ instead of $5$: then $12 + 4 = 16$, and $16 - 2 = 14$, so $[16] = [2]$ again.
[[Residue classes modulo 7 written as integers|7M3S3MNC2A]] gives the general argument.

The same shortcut breaks for a rule that does depend on the member.
"Send $[a]$ in $\mathbb{Z}/6\mathbb{Z}$ to $a$ in $\mathbb{Z}$" gives $0$ for $[0]$ and $6$ for $[6]$, though $[0] = [6]$.
[[The rule [a] ↦ a from Z/6Z to Z is not a function|XMRWZH674S]] shows that this is an error, not an abuse.

### A function named by its value

"The function $x^2$" means the [[function|0EPAT51DXQ]] $x \mapsto x^2$, and "its derivative is $2x$" means $x \mapsto 2x$.
Strictly, $x^2$ is a number once $x$ is a number, and $f(x)$ is a value of $f$, not $f$ itself.
The shortcut is safe while $x$ is a free letter.
It fails in a sentence such as "let $x = 3$; the function $x^2$ is increasing", where $x^2$ is now the number $9$.

A second shortcut of this family writes $f(A)$ for the [[image|07XF282NWH]] $\{f(a) : a \in A\}$ of a set $A$.
For $f(x) = x^2$ and $A = \{-1, 2\}$ it gives $f(A) = \{1, 4\}$.
The same letter now takes numbers and sets as inputs, and the type of the input tells you which reading holds.

### Isomorphic objects written as equal

Books write $\mathbb{R}^2 \times \mathbb{R} = \mathbb{R}^3$, though $((x, y), z)$ and $(x, y, z)$ are different objects.
The map $((x, y), z) \mapsto (x, y, z)$ is a bijection that respects all the structure in use, so the equality hides an [[isomorphism|PZMGQMDN25]] that nobody has to choose.

The shortcut is safe only along such a map.
For a finite-dimensional vector space $V$, writing $V = V^{**}$ hides the [[canonical isomorphism with the double dual|0ZJM9D7NPS]], which needs no choice.
That map is an isomorphism only in finite dimension, so the shortcut fails for infinite-dimensional $V$.
Writing $V = V^{*}$ would hide a choice of basis, because no isomorphism $V \to V^*$ is canonical, and good texts avoid it.
[[Canonical and natural|F8WNADZFMM]] explains the difference.

### What is not an abuse

A false formula is not an abuse.
The line $(a + b)^2 = a^2 + b^2$ has no correct expansion, since $a = b = 1$ gives $4 \ne 2$.
An abuse always has a correct long form that the writer could have written.

A symbol with two standard meanings is not an abuse either.
The sign $\sin^{-1} x$ means $\arcsin x$ to most readers and $\frac{1}{\sin x}$ to some, so it is one of the [[conflicting conventions|CSFEP56A7D]].
The difference is that an abuse has one expansion and a conflict has two.

### Watch out

The first trap is to use a member of a class and then a fact about integers that fails for classes.
In $\mathbb{Z}/3\mathbb{Z}$ the sentence "$3 \ne 0$" is false, because the class of $3$ is the class of $0$.

The second trap is to define a map on classes by a formula in one member and never check the other members.
The formula $[a] \mapsto a$ looks harmless, and it is not a function.

The third trap is to write $A = B$ along an isomorphism that involves a choice, and then name an element.
A text writes $\mathbb{Z}/6\mathbb{Z} = \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z}$ and speaks of "the element $(0, 1)$ of $\mathbb{Z}/6\mathbb{Z}$".
Under the map $[a] \mapsto ([a]_2, [a]_3)$ that element is $[4]$, and under the map $[a] \mapsto ([5a]_2, [5a]_3)$ it is $[2]$.
Both maps are isomorphisms, so the sentence has two meanings until the text names its map.

### Try it

First, expand "in $\mathbb{Z}/5\mathbb{Z}$, $3 \cdot 4 = 2$" to its exact form and check it.
It says $[3] \cdot [4] = [12] = [2]$, which holds because $12 - 2 = 10 = 2 \cdot 5$.

Second, decide whether "$[a] \mapsto [2a]$ from $\mathbb{Z}/6\mathbb{Z}$ to $\mathbb{Z}/6\mathbb{Z}$" is an abuse or an error.
It is a safe abuse: if $6$ divides $a - b$, then $6$ divides $2a - 2b$, so the value does not depend on the member.

## Explanations

### L1 human

Mathematicians often write a short form when the long form is clear from the context.
For example, with clock time, $10$ o'clock plus $5$ hours is $3$ o'clock, and we write $10 + 5 = 3$.
Strictly, the numbers on a clock are not the usual numbers, but everyone knows what we mean.
This kind of shortcut is called an abuse of notation.
It is fine as long as no reader can get a second meaning from it.

### L2 human

Expand the shortcut "in $\mathbb{Z}/5\mathbb{Z}$, $3 \cdot 4 = 2$" and check that it is safe.
The exact form is a statement about classes:
$$(3 + 5\mathbb{Z}) \cdot (4 + 5\mathbb{Z}) = 12 + 5\mathbb{Z} = 2 + 5\mathbb{Z}, \qquad \text{since } 12 - 2 = 10.$$
Other members must give the same class.
Take $8 \in [3]$ and $-1 \in [4]$:
$$8 \cdot (-1) = -8, \qquad -8 - 2 = -10 = -2 \cdot 5,$$
so $[-8] = [2]$ again.
The product does not depend on the members, so the short form has one meaning.
Number theory uses this shortcut all the time, for example in $a^{p-1} = 1$ in $\mathbb{Z}/p\mathbb{Z}$ for $a^{p-1} \equiv 1 \pmod p$.
Watch out: before you use the shortcut for a new operation, prove that the operation is well defined.

### L3 human

In category theory, many abuses are identifications along canonical isomorphisms, such as $(A \times B) \times C = A \times (B \times C)$.
Mac Lane's coherence theorem for monoidal categories says that such identifications are consistent, so this abuse cannot lead to a contradiction.
An identification along a non-canonical isomorphism, such as a finite-dimensional vector space with its dual, does not commute with all linear maps, and it can give wrong results when the maps change.
In homotopy type theory the univalence axiom makes equality of equivalent types part of the formal system, so some abuses become theorems.
In Lean and Mathlib, coercions and type class inference carry out the standard abuses: "a group $G$" is a type with an instance, and $\mathbb{N} \subseteq \mathbb{Z}$ is a coercion map.
