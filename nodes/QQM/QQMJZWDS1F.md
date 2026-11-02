---
tag: QQMJZWDS1F
kind: example
name: Counting measure
msc: [28A12]
instance_of: [PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Counting_measure
---

## Example

Let $X$ be a set and let $\Sigma$ be its power set.
For $A \subseteq X$, let $\mu(A)$ be the number of elements of $A$ if $A$ is finite, and $\mu(A) = \infty$ if $A$ is infinite.
Then $\mu$ is a [[measure|PR11BZQQPG]] on $(X, \Sigma)$, the counting measure.

For the check, $\mu(\varnothing) = 0$.
Let $A_1, A_2, \ldots$ be pairwise disjoint subsets of $X$ with union $A$.
Suppose all $A_n$ are finite and only finitely many are nonempty.
Then $A$ is finite, and its number of elements is the sum of those of the $A_n$.
Otherwise $A$ is infinite, and the sum $\sum_n \mu(A_n)$ is $\infty$ too, since it has a term $\infty$ or infinitely many terms at least $1$.

## Remarks

Counting measure is [[σ-finite|WEBBT18D4X]] exactly when $X$ is countable.
On $X = \N$, the integral of a non-negative function $f$ with respect to counting measure is the sum $\sum_{n} f(n)$.
So series of non-negative terms are a special case of Lebesgue integrals.

## Explanations

### L1 human

Counting measure gives each set its number of elements.
The set $\set{2, 5, 7}$ has measure $3$, and the set of even numbers has measure $\infty$.
It is the simplest measure, and it turns sums into integrals.
