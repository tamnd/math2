---
tag: K9QPQH4YKY
kind: statement
role: theorem
name: Grover's algorithm
msc: [68Q12, 81P68]
uses: [E1P61VYRRD, 0XHDTE5YMZ]
about: [VP21SFE7ZA]
sources:
  - url: https://en.wikipedia.org/wiki/Grover%27s_algorithm
same_as:
  wikidata: Q1028292
  wikipedia: Grover's algorithm
---

## Statement

Let $N \ge 2$ and let $f \colon \set{0, 1, \ldots, N-1} \to \set{0, 1}$ be a [[function|0XHDTE5YMZ]] with exactly one $w$ such that $f(w) = 1$.
Suppose $f$ is given as a quantum oracle $\lvert x \rangle \mapsto (-1)^{f(x)} \lvert x \rangle$.
Let $\theta = \arcsin(1/\sqrt{N})$, and let $r$ be the integer nearest to $\pi/(4\theta) - 1/2$.
Then a quantum algorithm makes $r$ queries to the oracle and finds $w$ with probability at least $1 - 1/N$.
Here $r \le \pi \sqrt{N} / 4$.

## Remarks

The algorithm starts from the uniform superposition $\lvert s \rangle = N^{-1/2} \sum_x \lvert x \rangle$.
Each iteration applies the oracle and then the reflection $2 \lvert s \rangle\langle s \rvert - I$.
Together these two reflections rotate the state by an angle $2\theta$ in the plane spanned by $\lvert s \rangle$ and $\lvert w \rangle$.
So after $r$ iterations the state makes angle $(2r+1)\theta$ with the axis orthogonal to $\lvert w \rangle$.
The choice of $r$ makes this angle differ from $\pi/2$ by at most $\theta$, so the success probability is at least $\cos^2 \theta = 1 - 1/N$.

Example: for $N = 4$ one has $\theta = \pi / 6$, and a single iteration rotates $\lvert s \rangle$ from angle $\pi/6$ to angle $\pi/2$.
So one query finds $w$ with certainty, while a classical search needs up to three queries.

Any classical algorithm needs about $N/2$ queries on average.
Bennett, Bernstein, Brassard and Vazirani proved that every quantum algorithm needs $\Omega(\sqrt{N})$ queries, so the speedup is optimal.

## Explanations

### L1 human

Searching an unsorted list of $N$ items for one marked item takes about $N/2$ looks on average.
Lov Grover found in 1996 that a quantum computer can do it with about $\sqrt{N}$ looks.
For a million items, that is about a thousand looks instead of half a million.
The gain is quadratic, not exponential, and no quantum method can do better.

### L2 human

Grover's method is an instance of amplitude amplification: two reflections, one about the marked states and one about the start state, rotate the state toward the answer.
The same idea speeds up any algorithm that succeeds with small probability $p$, using about $1/\sqrt{p}$ repetitions instead of $1/p$.
Applied to brute-force search, it gives a quadratic speedup for NP problems such as SAT.
It does not put NP inside BQP, because $\sqrt{2^n}$ is still exponential.
