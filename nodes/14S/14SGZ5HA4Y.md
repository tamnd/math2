---
tag: 14SGZ5HA4Y
kind: statement
role: theorem
name: Hales–Jewett theorem
msc: [05D10]
about: [G5TWXV565S]
sources:
  - url: https://en.wikipedia.org/wiki/Hales–Jewett_theorem
same_as:
  wikidata: Q1032886
  wikipedia: Hales–Jewett theorem
---

## Statement

Let $k \ge 1$ and $n \ge 1$ be integers, and let $[k] = \set{1, \ldots, k}$.
A *variable word* of length $n$ is a word $w \in ([k] \cup \set{*})^n$ in which the symbol $*$ occurs at least once.
For $a \in [k]$, let $w(a) \in [k]^n$ be the word obtained from $w$ by replacing every $*$ by $a$.
The set $\set{w(1), \ldots, w(k)}$ is a *combinatorial line* in $[k]^n$.

Let $k \ge 1$ and $r \ge 1$ be integers.
Then there is an integer $N$ with the following property.
For every $n \ge N$ and every colouring of $[k]^n$ with $r$ colours, some combinatorial line in $[k]^n$ is monochromatic.

## Remarks

Example: for $k = 2$ and $r = 2$ one can take $N = 2$.
The square $[2]^2$ has the five lines $\set{11, 21}$, $\set{12, 22}$, $\set{11, 12}$, $\set{21, 22}$ and $\set{11, 22}$.
In a $2$-colouring, either $11$ and $22$ have the same colour, or the word $12$ has the colour of one of them and lies on a line with it.
For $n = 1$ the only line is $\set{1, 2}$, which is not monochromatic when $1$ and $2$ get different colours.
The original proof, by induction on $k$, gives very large bounds; Shelah found a proof with primitive recursive bounds.
The theorem implies [[van der Waerden's theorem|V96FRZ2ME1]].
Use the alphabet $\set{0, \ldots, k-1}$ and map a word $w$ to $w_1 + \cdots + w_n$.
A combinatorial line goes to an arithmetic progression of length $k$ whose common difference is the number of $*$ symbols.
The density version says that, for large $n$, every set containing a fixed positive fraction of $[k]^n$ contains a combinatorial line.
It was proved by Furstenberg and Katznelson, and later by an elementary method in the Polymath project.

## Explanations

### L1 human

Think of the game of tic-tac-toe played on a cube with $k$ cells along each side and $n$ dimensions.
The theorem says that, if the dimension is large enough, any colouring of the cells with $r$ colours has a full winning line in one colour.
In particular, a game of this kind in high enough dimension cannot end in a draw.

### L2 human

The Hales–Jewett theorem is the abstract core of many Ramsey statements about arithmetic structure.
It needs no arithmetic at all: only words and substitution.
From it follow [[van der Waerden's theorem|V96FRZ2ME1]] and its multidimensional form, the Gallai–Witt theorem.
Its density version similarly implies [[Szemerédi's theorem|B23B0QEMN5]].
