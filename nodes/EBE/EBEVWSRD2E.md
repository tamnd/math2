---
tag: EBEVWSRD2E
kind: statement
role: theorem
name: Plünnecke–Ruzsa inequality
msc: [11P70, 11B13]
uses: [XNBN31HQWB, 082GHNPJ53]
about: [XNBN31HQWB]
sources:
  - url: https://en.wikipedia.org/wiki/Pl%C3%BCnnecke%E2%80%93Ruzsa_inequality
same_as:
  wikidata: Q85793713
  wikipedia: Plünnecke–Ruzsa inequality
---

## Statement

Let $G$ be an [[abelian group|082GHNPJ53]], and let $A$ and $B$ be finite nonempty subsets of $G$.
Let $K \ge 1$ be a real number.
Suppose that the [[sumset|XNBN31HQWB]] satisfies $\abs{A + B} \le K \abs{A}$.
Then for all integers $m, n \ge 0$ with $m + n \ge 1$,
$$\abs{mB - nB} \le K^{m + n} \abs{A}.$$
Here $mB - nB$ is the set of all $b_1 + \dots + b_m - b'_1 - \dots - b'_n$ with all $b_i, b'_j \in B$.

## Remarks

Petridis gave a short proof.
Choose a nonempty $X \subseteq A$ that minimizes the ratio $\abs{X + B} / \abs{X}$, and call the minimum $K'$, so $K' \le K$.
He showed that $\abs{X + B + C} \le K' \abs{X + C}$ for every finite set $C$, and induction gives $\abs{X + mB} \le K^m \abs{X}$.
The [[Ruzsa triangle inequality|R7E5A4W6FJ]] then handles the differences.
With $B = A$, a set with $\abs{A + A} \le K\abs{A}$ satisfies $\abs{mA - nA} \le K^{m+n}\abs{A}$, so small doubling controls all iterated sums.
For $A = \set{1, \dots, N}$ one has $\abs{A + A} = 2N - 1 \le 2\abs{A}$, and indeed $\abs{mA - nA} \le (m + n)N \le 2^{m+n} N$.

## Explanations

### L1 human

If adding a set $B$ to a set $A$ makes it only a little larger, then adding $B$ many times, or subtracting it, also cannot make it much larger.
The growth is at most a fixed power of the first growth factor.
So a set with few sums is controlled at every later step.

### L2 human

The Plünnecke–Ruzsa inequality is a basic tool in [[additive combinatorics|3NM362A2JG]].
It is used in the proof of [[Freiman's theorem|KEPFYE6WYZ]].
It is often combined with the [[Balog–Szemerédi–Gowers theorem|W5BZZ59CVM]].
Plünnecke's original proof used a graph-theoretic argument with layered commutative graphs, and Ruzsa turned it into the form above.
