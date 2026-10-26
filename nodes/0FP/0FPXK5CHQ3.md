---
tag: 0FPXK5CHQ3
kind: definition
name: Reduced word
aliases: [freely-reduced-word]
msc: ["20E05"]
defines: 0KBTP8Q2FS
sources:
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Construction
---

## Definition

Let $S$ be a set, and let $S^{-1} = \{s^{-1} : s \in S\}$ be a set of new symbols, one for each $s \in S$.
A word on $S$ is a finite string $t_1 t_2 \cdots t_n$ with $n \geq 0$ and each $t_i$ in $S \cup S^{-1}$.
A word is reduced when it contains no adjacent pair $s s^{-1}$ or $s^{-1} s$ with $s \in S$.

## Remarks

The empty word, with $n = 0$, is reduced.
Remove adjacent pairs $s s^{-1}$ and $s^{-1} s$, one at a time, until no such pair is left. The result is a reduced word.
For example, for $S = \{a, b, c\}$, the word $a b^3 c^{-1} c a^{-1} c$ reduces to $a b^3 a^{-1} c$.
A reduced word is cyclically reduced when its first and last letters are not inverse to each other.

## Explanations

### L1 human

A word is a string of letters and inverse letters.
It is reduced when you cannot cancel a letter against its inverse next to it.
Reduced words are the normal forms of the elements of a [[free group|0KTW26C80J]].
