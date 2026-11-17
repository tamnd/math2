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

An abuse of notation is a use of a symbol that is not correct by the strict definitions, but that the reader can expand into a correct expression without doubt.
Authors use it on purpose, because the exact expression is long and the short form makes the idea easier to see.
Typical abuses are: naming a structure by its underlying set, writing an equivalence class by one of its members, writing $f(x)$ for a function $f$, and writing $=$ between objects that are only isomorphic.
An abuse is acceptable only when the context fixes the one correct expansion.

## Motivation

A [[group|G5S1M9]] is a pair $(G, \cdot)$ of a set and a binary operation, and the strict notation must always carry both parts.
A sentence such as "let $(G, \cdot)$ be a group and let $(H, \cdot|_{H \times H})$ be a subgroup of $(G, \cdot)$" is correct but hard to read.
Every author writes "let $G$ be a group and $H$ a subgroup" instead.
The short form loses no information, because the operation on $H$ is the one from $G$.
Mathematics accepts such shortcuts, and a reader must know which ones are standard and how to expand them.

## Notation

The abuses below are standard, and this site uses them without comment.

| Short form | Exact meaning |
|---|---|
| $G$ is a group | $(G, \cdot)$ is a group, with the operation fixed by context |
| $x \in G$ | $x$ is in the underlying set of the group $G$ |
| $\mathbb{Z}$ is a ring | $(\mathbb{Z}, +, \cdot, 0, 1)$ is a ring |
| $[a]$ or $a$ in $\mathbb{Z}/n\mathbb{Z}$ | the [[equivalence class|0W95W33CMP]] $a + n\mathbb{Z}$ |
| the function $f(x)$ | the [[function|0EPAT51DXQ]] $f$, or $x \mapsto f(x)$ |
| $f(A)$ for a set $A$ | the [[image|07XF282NWH]] $\{f(a) : a \in A\}$ |
| $A = B$ for isomorphic objects | there is a chosen [[isomorphism|PZMGQMDN25]] $A \to B$ |
| $a + b + c$ | $(a + b) + c$, which equals $a + (b + c)$ by associativity |
| $1$ in a group or ring | the identity element of that structure |

This site avoids two abuses: it does not write $\sin^{-1}$ for $\arcsin$, and it does not write $f(x)$ for a function when the variable $x$ is also used as a number in the same sentence.

## Remarks

### Examples

1. [[The group Z means the integers under addition|X51H6XKCDQ]]. The symbol $\mathbb{Z}$ names the set, the additive group and the ring, and context picks one.
2. [[Residue classes modulo 7 written as integers|7M3S3MNC2A]]. Writing $5 + 4 = 2$ in $\mathbb{Z}/7\mathbb{Z}$ uses integers for classes, and it is safe because the operations do not depend on the chosen member.
3. Isomorphic objects. A text writes $\mathbb{R}^2 \times \mathbb{R} = \mathbb{R}^3$, though $((x, y), z)$ and $(x, y, z)$ are different objects; the map $((x, y), z) \mapsto (x, y, z)$ is a bijection that respects all the structure in use.
4. Function notation. The phrase "the function $x^2$" means $x \mapsto x^2$, and its derivative is written $2x$.

### Non-examples

1. [[The rule that sends a class to its member is not a function|XMRWZH674S]]. Here the short form "send the class to its member" has no single expansion, so it is an error and not an abuse.
2. A typo or a wrong formula, such as $(a + b)^2 = a^2 + b^2$. An abuse of notation has a correct expansion; a false formula does not.
3. Writing $\sin^{-1} x$ for $\arcsin x$ is a fixed alternative notation with a definition, not an abuse; it is a [[conflicting convention|CSFEP56A7D]], because another reader can take it as $(\sin x)^{-1}$.

### Basic properties

1. An abuse is safe only if the expansion is unique. For classes this means the result must be well defined, so it does not depend on the chosen member.
2. An abuse can hide a choice. Writing $V = V^{**}$ for a finite-dimensional vector space hides the [[canonical isomorphism with the double dual|0ZJM9D7NPS]], while $V = V^{*}$ would hide a choice of basis, and good texts avoid the second.
3. An abuse does not change any theorem. Each theorem stated with an abuse is a short form of a theorem stated with the exact notation.
4. In a proof assistant the abuses must be resolved. Lean resolves "a group $G$" through a type with a type class instance, and "$\mathbb{N} \subseteq \mathbb{Z}$" through a coercion map.

### History

The related phrase "abuse of language" names a word used in a loose sense, as when a vector space $V$ is called a representation of a group $G$, though the representation is the homomorphism from $G$ to $\mathrm{GL}(V)$.
The practice of naming a structure by its underlying set is also called suppression of parameters.
The detailed history of the phrases is not given here.

### Common errors

1. A student uses an integer as a class and then uses a fact about integers that does not hold for classes, such as "$3 \ne 0$" in $\mathbb{Z}/3\mathbb{Z}$, where the class of $3$ is the class of $0$.
2. A student defines a map on classes by a formula in one member and does not check that the result is the same for every member.
3. A student writes $A = B$ for isomorphic objects and then uses a property that depends on the elements, such as "$1 \in B$" when $1$ is an element of $A$ only.

## Explanations

### L1 human

Mathematicians often write a short form when the long form is clear from the context.
For example, when we work with clock time, $10 + 5$ hours is $3$ o'clock, and we write $10 + 5 = 3$.
Strictly, the numbers on a clock are not the usual numbers, but everyone knows what we mean.
This kind of shortcut is called an abuse of notation.
It is fine as long as no reader can get a second meaning from it.

### L2 human

We expand an abuse to its exact form and check that it is safe.

1. The short form: "in $\mathbb{Z}/5\mathbb{Z}$, $3 \cdot 4 = 2$".
2. The exact form: $(3 + 5\mathbb{Z}) \cdot (4 + 5\mathbb{Z}) = 12 + 5\mathbb{Z} = 2 + 5\mathbb{Z}$, since $12 - 2 = 10 = 2 \cdot 5$.
3. Other members give the same class: $8 \cdot (-1) = -8$, and $-8 - 2 = -10 = -2 \cdot 5$, so $-8 + 5\mathbb{Z} = 2 + 5\mathbb{Z}$.
4. Since the product does not depend on the members, the short form has one meaning.

The typical use of the short form is in number theory, where texts write $a^{p-1} = 1$ in $\mathbb{Z}/p\mathbb{Z}$ for $a^{p-1} \equiv 1 \pmod p$.
A trap: before an abuse is used for a new operation, the operation must be shown to be well defined.

### L3 human

In category theory, many abuses are identifications along canonical isomorphisms, such as $(A \times B) \times C = A \times (B \times C)$.
The coherence theorems of Mac Lane for monoidal categories say that such identifications are consistent, so the abuse cannot lead to a contradiction.
By contrast, an identification along a non-canonical isomorphism, such as a finite-dimensional vector space with its dual, is not compatible with all linear maps, and it can give wrong results when the maps change.
In type theory the univalence axiom makes equality of isomorphic structures part of the formal system, so some abuses become theorems.
In Lean and Mathlib, coercions and type class inference implement the standard abuses, and the formal text keeps the expansion hidden but explicit.
