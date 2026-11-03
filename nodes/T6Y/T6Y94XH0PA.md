---
tag: T6Y94XH0PA
kind: definition
name: EXPTIME
msc: [68Q15]
defines: T9G5S33CA0
uses: [758EYCN27B, T00W8RQT8E, ESPYW94XGR, 3QKF32ZAKN]
sources:
  - url: https://en.wikipedia.org/wiki/EXPTIME
---

## Definition

Let $t \colon \N \to \N$ be a function.
Let $\mathrm{DTIME}(t)$ be the class of languages $L \subseteq \set{0,1}^*$ decided by a deterministic multitape [[Turing machine|758EYCN27B]] with [[running time|T00W8RQT8E]] $O(t(n))$ on inputs of length $n$.
The class *EXPTIME* is
$$\mathrm{EXPTIME} = \bigcup_{k \ge 1} \mathrm{DTIME}\big(2^{n^k}\big).$$

## Remarks

Example: the [[Boolean satisfiability problem|3QKF32ZAKN]] is in EXPTIME.
A formula of length $m$ has at most $m$ variables, so it has at most $2^m$ assignments.
A machine can try them all and evaluate the formula on each in time $O(m^c)$ for a constant $c$.
The total time is $O(2^m m^c)$, which is $O(2^{m^2})$.

Non-example: by the [[time hierarchy theorem|A6D1D67GHA]] there is a language in $\mathrm{DTIME}(2^{2^n})$ that is not in $\mathrm{DTIME}(2^{n^k})$ for any $k$, so it is not in EXPTIME.

The class is also written $\mathrm{EXP}$.
The nondeterministic analogue, with nondeterministic machines, is called $\mathrm{NEXPTIME}$.
