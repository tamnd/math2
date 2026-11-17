---
tag: H8RF8WJHMA
kind: example
name: Approximate counting does not detect a single element
msc: ["03F30", "68Q15"]
topics: [RA380RWEC0]
audience: research
not_instance_of:
  - target: 65K2S22DGZ
    note: the error of the comparison is a fraction of the ambient interval, so a set with one element and the empty set have the same approximate size, and emptiness is not an approximate counting question
uses: [65K2S22DGZ, QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Theories
---

## Example

Fix $n \ge 1$, an element $x_0 < 2^n$ and an error $\varepsilon$ with $\varepsilon 2^n \ge 1$, for example $n = 4$ and $\varepsilon = 1/16$.
We compare $X = \set{x_0}$ with the empty set in the sense of [[approximate counting|65K2S22DGZ]].

1. $\emptyset \preceq_0 X$, since $\emptyset \subseteq X$ and inclusion gives a comparison with error $0$. By monotonicity in the error, $\emptyset \preceq_\varepsilon X$.
2. $X \preceq_\varepsilon \emptyset$: take $v = 1$. The set $\emptyset \sqcup [0, \varepsilon 2^n)$ is a copy of $[0, \varepsilon 2^n)$, which has at least one element.
3. The constant circuit $G$ with value $x_0$ maps this set onto $\set{x_0}$.
4. So $X \approx_\varepsilon \emptyset$: up to error $\varepsilon$, the set with one element has the size $0$.
5. The same maps give $\emptyset \approx_\varepsilon 1$ and $X \approx_\varepsilon 1$, so the approximate size does not decide whether a set is empty.
6. A smaller error does not help within the method: $\varepsilon < 2^{-n}$ gives $\varepsilon^{-1} > 2^n$, which is not of polynomial size in $n$.

## Remarks

The non-example shows what approximate counting cannot do: the error $\varepsilon 2^n$ hides every set with fewer than $\varepsilon 2^n$ elements.
This is necessary, since deciding whether a set given by a circuit is empty is the complement of circuit [[satisfiability|QN7M1JCGT9]], a $\mathrm{coNP}$-complete problem.
For a set of size about $2^{n-1}$, such as the even numbers, the same error is small compared with the set, and the method gives useful information.
The stronger theory $\mathsf{APC}_2$ counts $\mathrm{NP}$ sets with an error relative to the size of the set, but it uses an $\mathrm{NP}$ oracle in its functions.

## Explanations

### L1 human

Suppose a survey of $1000$ people may be wrong by $10$ people.
Then it cannot tell whether nobody or one person has a rare property.
Approximate counting is like such a survey: it gives sizes up to an error that is a small part of the whole range.
A set with one element is far below that error, so it looks the same as the empty set.

### L2 human

We take $n = 4$ and $\varepsilon = 1/16$, so the error is $\varepsilon 2^n = 1$.

1. The ambient interval is $[0, 16)$. Let $X = \set{5}$.
2. The padding set $[0, 1) = \set{0}$ has one element. The map $G(0) = 5$ is onto $X$, so $X \preceq_{1/16} \emptyset$.
3. $\emptyset \subseteq X$ gives $\emptyset \preceq_0 X$.
4. So $X \approx_{1/16} \emptyset$, although $X$ has one element and $\emptyset$ has none.

The typical use of this non-example is as a reminder of the scale: approximate counting estimates probabilities, not exact numbers.
A trap is to use an approximate size to conclude that a set is non-empty; the conclusion needs a size larger than the error.
