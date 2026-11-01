---
tag: N815PEPPFA
kind: definition
name: Combinatorics on words
msc: [68R15, 05A05]
defines: YJ961M051W
uses: [0R47MAD57S, 0JKW7W7XFR]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorics_on_words
---

## Definition

Let $A$ be a finite set, the *alphabet*, whose elements are *letters*.
A finite *word* over $A$ is a finite sequence $w = a_1 a_2 \cdots a_n$ of letters, also called a string; an infinite word is a sequence $(a_i)_{i \ge 1}$.
The finite words form the free [[monoid|0R47MAD57S]] $A^*$ under concatenation, with the empty word as identity.
A *factor* of $w$ is a word $u$ with $w = x u y$ for some words $x, y$.
*Combinatorics on words* is the branch of [[combinatorics|0JKW7W7XFR]] that studies the structure of words in $A^*$ and of infinite words over $A$.
Its typical questions concern factors, repetitions, periods and morphisms of $A^*$.

## Remarks

Example: a *square* is a nonempty word of the form $u u$.
Every binary word of length at least $4$ contains a square factor.
Indeed, a square-free binary word cannot contain $aa$ or $bb$, so it alternates, and $abab$ or $baba$ is a square.

Example: the [[Thue–Morse sequence|7JZVT385PC]] is an infinite binary word with no factor of the form $a x a x a$ with $a$ a letter, so it is overlap-free.

Non-example: the word $ac$ is not a factor of $abc$.
It is only a [[subsequence|0F1PR74BRX]] of $abc$, since a factor must consist of consecutive letters.

Results of the field include the Fine–Wilf theorem on words with two periods and the existence of infinite square-free words over three letters.
