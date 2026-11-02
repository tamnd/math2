---
tag: D9AWNH60RM
kind: definition
name: Computable function
msc: [03D20, 03D10]
defines: KZSB5E471K
uses: [758EYCN27B, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Computable_function
---

## Definition

Let $k \ge 1$ and let $f \colon \N^k \rightharpoonup \N$ be a partial function, where $\N$ is the set of [[natural numbers|0MWKJ44V5A]].
Fix an encoding of tuples of natural numbers as words on the input alphabet, for example in unary separated by a marker.
The function $f$ is *computable*, or *partial computable*, if there is a [[Turing machine|758EYCN27B]] $M$ with the following property for every $\bar x \in \N^k$.

1. If $f(\bar x)$ is defined, then $M$ halts on input $\bar x$ with the code of $f(\bar x)$ on its tape.
2. If $f(\bar x)$ is undefined, then $M$ does not halt on input $\bar x$.

A *total computable function* is a computable function defined at every point of $\N^k$.

## Remarks

Example: addition $(x, y) \mapsto x + y$ is computable.
With unary codes $1^x 0 1^y$, a machine that replaces the $0$ by $1$ and erases the last $1$ halts with $1^{x+y}$ on its tape.

Non-example: the function $h(e) = 1$ if the machine with index $e$ halts on input $e$, and $h(e) = 0$ otherwise, is total but not computable.
No machine satisfies clause 1 for $h$; see the [[halting problem|Z7TN2B35B0]].

A partial function is computable if and only if it is partial [[general recursive|HBK5QHC1GC]].
The definition does not depend on the choice of a reasonable encoding or a variant of Turing machines.
