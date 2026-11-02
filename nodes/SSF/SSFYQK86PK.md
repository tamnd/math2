---
tag: SSFYQK86PK
kind: definition
name: Inner regular measure
msc: [28C15]
defines: 28E5Q5BM69
uses: [DYR1QFNGNJ, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_measure
---

## Definition

Let $X$ be a topological space and let $\mu$ be a [[Borel measure|DYR1QFNGNJ]] on $X$.
A Borel set $A \subseteq X$ is *inner regular* for $\mu$ if
$$\mu(A) = \sup \set{\mu(K) : K \subseteq A, \ K \text{ compact and Borel}}.$$
The measure $\mu$ is *inner regular* if every Borel set is inner regular for $\mu$.

## Remarks

In a Hausdorff space every [[compact set|0R6EWFKRCF]] is closed, hence Borel, so the condition "Borel" on $K$ is automatic.

Example: counting measure on $\R$ is inner regular.
If $A$ is finite, take $K = A$; if $A$ is infinite, its finite subsets are compact and have arbitrarily large counting measure, so the supremum is $\infty = \mu(A)$.

Non-example: let $X$ be an uncountable set with the cocountable topology, whose open sets are $\emptyset$ and the complements of countable sets.
Its Borel sets are the countable sets and their complements; let $\mu$ be $0$ on countable sets and $1$ on the others.
Compact subsets of $X$ are finite, so they have measure $0$, while $\mu(X) = 1$; thus $\mu$ is not inner regular.

Variants: some authors approximate by closed sets instead of compact sets, and some ask inner regularity only for open sets.
