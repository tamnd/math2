---
tag: 7JZVT385PC
kind: object
name: Thue–Morse sequence
msc: [11B85, 68R15]
instance_of: [0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence
same_as:
  wikidata: Q1477120
  wikipedia: Thue–Morse sequence
---

## Description

The *Thue–Morse sequence* is the binary [[sequence|0G9EKM0E15]] $(t_n)_{n \ge 0}$ given by $t_0 = 0$, $t_{2n} = t_n$ and $t_{2n+1} = 1 - t_n$.
Equivalently, $t_n$ is $0$ if the binary expansion of $n$ has an even number of digits $1$, and $1$ otherwise.
Its first sixteen terms are
$$0110\,1001\,1001\,0110.$$

## Remarks

Check: $t_5 = 0$ because $5 = 101_2$ has two digits $1$, and $t_7 = 1$ because $7 = 111_2$ has three.

The sequence is the fixed point, starting with $0$, of the morphism $\mu$ of words with $\mu(0) = 01$ and $\mu(1) = 10$.
So the first $2^{m+1}$ terms are the first $2^m$ terms followed by their complement, where $0$ and $1$ are swapped.

The sequence is overlap-free: it has no factor of the form $a x a x a$, where $a$ is a letter and $x$ is a word.
In particular it has no factor of the form $u u u$ with $u$ nonempty.
Thue proved overlap-freeness, and it makes the sequence a basic example in [[combinatorics on words|YJ961M051W]].
It is not periodic, and it is a $2$-automatic sequence, computed by a finite automaton that reads $n$ in base $2$.

## Explanations

### L1 human

Start with $0$, and at each stage append the complement of what you have.
This gives $0$, then $01$, then $0110$, then $01101001$, and so on.
The result never repeats any block three times in a row.
It is also used as a fair order of turns: two players who pick in the order $A B B A B A A B \ldots$ share the advantage of going first.
