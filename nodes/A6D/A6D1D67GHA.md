---
tag: A6D1D67GHA
kind: statement
role: theorem
name: Time hierarchy theorem
msc: [68Q15]
uses: [T00W8RQT8E, YK3HD56R3G, GVT2NKN37K, 0TGV80E6A4]
about: [T00W8RQT8E]
sources:
  - url: https://en.wikipedia.org/wiki/Time_hierarchy_theorem
same_as:
  wikidata: Q5251122
  wikipedia: Time hierarchy theorem
---

## Statement

Let $f, g \colon \N \to \N$ be time-constructible functions.
Here $f$ is time-constructible when $f(n) \ge n$ and the binary form of $f(n)$ can be computed from $1^n$ in $O(f(n))$ steps.
Suppose that $f(n) \log f(n) = o(g(n))$, in [[big O notation|0TGV80E6A4]].
Then
$$\mathrm{DTIME}(f(n)) \subsetneq \mathrm{DTIME}(g(n)),$$
where $\mathrm{DTIME}(t(n))$ is the class of languages decided by deterministic [[multitape Turing machines|YK3HD56R3G]] in [[time|T00W8RQT8E]] $O(t(n))$.

## Remarks

The proof is a diagonalization.
A machine $D$, on input $w$, simulates the machine encoded by $w$ on input $w$ for about $g(\abs{w})$ steps and answers the opposite.
A universal machine simulates $t$ steps of any fixed multitape machine in $O(t \log t)$ steps.
So every machine running in time $O(f(n))$ is fully simulated on long enough inputs, and it cannot decide the same language as $D$.
Juris Hartmanis and Richard Stearns proved a first version of the theorem in 1965.

Consequence: [[P|GVT2NKN37K]] is strictly contained in EXPTIME, the class $\bigcup_k \mathrm{DTIME}(2^{n^k})$.
Indeed $\mathrm{P} \subseteq \mathrm{DTIME}(2^n) \subsetneq \mathrm{DTIME}(2^{2n})$.
Time-constructibility cannot be dropped: the Borodin gap theorem gives computable $f$ with $\mathrm{DTIME}(f(n)) = \mathrm{DTIME}(2^{f(n)})$.

## Explanations

### L1 human

Given more time, computers can solve more problems.
For reasonable time bounds, slightly more than a logarithmic factor of extra time already allows new problems to be solved.
So time classes form a strict ladder.

### L2 human

The theorem gives the separation $\mathrm{P} \ne \mathrm{EXPTIME}$, one of few known unconditional separations.
It says nothing about P versus NP, since NP is defined by another resource, nondeterministic time.
A version for nondeterministic time also holds, with a different and subtler proof.
Diagonalization proofs of this kind relativize, which is why the same method cannot settle P versus NP.
