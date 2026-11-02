---
tag: YWX4FCFPAP
kind: statement
role: theorem
name: Smn theorem
msc: [03D20]
uses: [KZSB5E471K, MFJXPAF0R0, 5NVA2JRHPV]
about: [KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Smn_theorem
same_as:
  wikidata: Q1766814
  wikipedia: Smn theorem
---

## Statement

Fix a standard [[Gödel numbering|MFJXPAF0R0]] of programs, and let $\varphi^{(k)}_e$ be the partial [[computable function|KZSB5E471K]] of $k$ arguments computed by program $e$.
Let $m, n \ge 1$.
Then there is a [[primitive recursive|5NVA2JRHPV]] function $s^m_n \colon \N^{m+1} \to \N$ such that for all $e \in \N$, $\bar x \in \N^m$ and $\bar y \in \N^n$:
$$\varphi^{(n)}_{s^m_n(e, \bar x)}(\bar y) \simeq \varphi^{(m+n)}_e(\bar x, \bar y).$$
Here $\simeq$ means that both sides are undefined, or both are defined and equal.

## Remarks

The program $s^m_n(e, \bar x)$ first writes the fixed numbers $\bar x$ in front of its input $\bar y$, then runs program $e$.
Building this program from $e$ and $\bar x$ is a simple manipulation of codes, so $s^m_n$ is primitive recursive.

Example: let $e$ be a program for $(x, y) \mapsto x + y$.
Then $s^1_1(e, 5)$ is the number of a program for $y \mapsto 5 + y$, and $x \mapsto s^1_1(e, x)$ computes an index for "add $x$" from $x$.

The theorem is also called the parameter theorem, and it is due to Kleene.

## Explanations

### L1 human

If a program takes two inputs and you fix the first one, you get a program with one input.
The smn theorem says that the new program can be produced from the old one and the fixed input by a simple mechanical rule.
In programming terms, it is partial application, or currying, done on source code.

### L2 human

The smn theorem is used to turn a construction "uniform in a parameter" into a computable function on indices.
It is the main tool in the proof of [[Kleene's recursion theorem|F3Z30M606H]].
It is also used to build many-one reductions, for example in the proof of [[Rice's theorem|AKDR5YBBE2]].
Numberings that satisfy the smn theorem and have a universal function are called acceptable, and any two of them are computably isomorphic by a theorem of Rogers.
