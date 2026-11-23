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

Take $n = 4$, so that the whole interval is $[0, 16)$, and take the error $\varepsilon = 1/16$, so that $\varepsilon 2^n = 1$.
We compare the set $X = \{5\}$ with the empty set in the sense of [[approximate counting|65K2S22DGZ]], and we find that the two sets have the same approximate size.

1. First, $\emptyset \preceq_0 X$, because $\emptyset \subseteq X$ and inclusion gives a comparison with error $0$.
   Since $\preceq_\varepsilon$ is monotone in the error, also $\emptyset \preceq_{1/16} X$.
2. Next, we show $X \preceq_{1/16} \emptyset$ with $v = 1$.
   The domain of the map is $\emptyset \sqcup [0, 1)$, a copy of $\{0\}$, which has one element.
3. The constant circuit $G$ with $G(0) = 5$ has the value $5$, so every element of $X$ is a value of $G$ on this domain.
4. Steps 1 and 3 give $X \approx_{1/16} \emptyset$.
   Up to the error $1/16$, the set with one element has size $0$.

The same argument works in general.
Fix $n \ge 1$, an element $x_0 < 2^n$ and an $\varepsilon$ with $\varepsilon 2^n \ge 1$.
The constant map with value $x_0$ covers $\{x_0\}$ from the padding $[0, \varepsilon 2^n)$, so $\{x_0\} \approx_\varepsilon \emptyset$.
The same maps give $\emptyset \approx_\varepsilon 1$ and $\{x_0\} \approx_\varepsilon 1$, so the approximate size cannot decide whether a set is empty.

A smaller error does not help within the method.
To hide nothing, we would need $\varepsilon 2^n < 1$, that is, $\varepsilon^{-1} > 2^n$.
But the method allows only errors with $\varepsilon^{-1}$ of size polynomial in $n$.

## Remarks

The non-example shows the scale of approximate counting: the error $\varepsilon 2^n$ hides every set with at most $\varepsilon 2^n$ elements.
This limit is what one expects.
Deciding whether a set given by a circuit is empty is the complement of circuit [[satisfiability|QN7M1JCGT9]], a $\mathrm{coNP}$-complete problem, so polynomial-time maps should not decide it.

For a large set the same error is harmless.
The even numbers below $2^n$ have about $2^{n-1}$ elements, and an error of $\varepsilon 2^n$ with $\varepsilon = 1/100$ changes the estimate of their fraction from $1/2$ by at most $1/100$.
The stronger theory $\mathsf{APC}_2$ counts $\mathrm{NP}$ sets with an error that is a fraction of the set itself, but its functions use an $\mathrm{NP}$ oracle.

## Explanations

### L1 human

Suppose a survey of $1000$ people may be wrong by $10$ people.
Then it cannot tell whether nobody or one person has a rare property.
Approximate counting is like such a survey: it gives sizes up to an error that is a small part of the whole range.
A set with one element is far below that error, so it looks the same as the empty set.

### L2 human

Take $n = 10$ and $\varepsilon = 1/128$, so the padding interval has $2^{10}/128 = 8$ elements.
Let $X = \{1, 2, 3\}$.
The circuit with $G(0) = 1$, $G(1) = 2$ and $G(u) = 3$ for $2 \le u < 8$ covers $X$ from the padding, so $X \preceq_{1/128} \emptyset$.
With inclusion, this gives $X \approx_{1/128} \emptyset$, although $X$ has three elements.

The typical use of this non-example is as a reminder that approximate counting estimates probabilities, not exact numbers.
Watch out: an approximate size can show that a set is non-empty only when the size is larger than the error.
