---
tag: 4ARVVS526T
kind: problem
name: Post correspondence problem
msc: [03D35, 68Q45, 68R15]
uses: [D9FCP61J44, 3J6YG01N22]
about: [YAVW1XHNFH]
sources:
  - url: https://en.wikipedia.org/wiki/Post_correspondence_problem
same_as:
  wikidata: Q798572
  wikipedia: Post correspondence problem
history:
  posed_by: "Emil Post"
  first_stated: "1946"
---

## Problem

Let $\Sigma$ be an alphabet with at least two symbols.
An instance is a finite list of pairs $(u_1, v_1), \dots, (u_n, v_n)$ of [[strings|D9FCP61J44]] over $\Sigma$.
A *match* is a finite nonempty sequence of indices $i_1, \dots, i_k \in \set{1, \dots, n}$ such that
$$u_{i_1} u_{i_2} \cdots u_{i_k} = v_{i_1} v_{i_2} \cdots v_{i_k}.$$
Is there an algorithm that decides, for every instance, whether it has a match?

## Remarks

Post proved in the paper that introduced the problem that no such algorithm exists: the set of instances with a match is not [[decidable|3J6YG01N22]].
The set is recursively enumerable, since one can try all index sequences in order of length and stop when a match appears.
The standard proof reduces the halting problem to it: the pairs are built so that a match spells out a halting computation of a given Turing machine.
Example: the instance $(a, ab), (bc, c)$ has the match $1, 2$, since $u_1 u_2 = abc = v_1 v_2$.
The instance $(ab, a)$ alone has no match, since every concatenation of $u$'s is longer than the corresponding concatenation of $v$'s.
Over a one-letter alphabet the problem is decidable, because only the lengths of the strings matter.
The problem is also decidable for instances with $n = 2$ pairs.
Because the problem is purely about strings, it is a convenient source of undecidability for questions about grammars, for example whether two context-free grammars generate languages with a common string.

## Explanations

### L1 human

Picture a stock of dominoes, each with a string on top and a string on the bottom, with as many copies of each as one likes.
The puzzle is to line up some dominoes so that the top row and the bottom row read the same string.
For some sets of dominoes this is easy, and for some it is impossible.
The surprise is that no single method can tell, for every set of dominoes, which case holds.
