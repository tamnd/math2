---
tag: YFAQGE2ATQ
kind: statement
role: theorem
name: Isomorphism theorem for measure algebras
msc: [28A60, 28D05]
uses: [0XADJKM699, 2Z2QVWZ262, VQQM4Y550T]
about: [2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_probability_space
---

## Statement

Let $\mathfrak{A}$ be a [[Boolean algebra|0XADJKM699]] in which every countable subset has a supremum, and let $m \colon \mathfrak{A} \to [0, 1]$.
The pair $(\mathfrak{A}, m)$ is a *probability measure algebra* if three conditions hold.

1. $m(1) = 1$, and $m(a) = 0$ only for $a = 0$.
2. $m\left(\bigvee_k a_k\right) = \sum_k m(a_k)$ for every sequence of pairwise disjoint elements $a_k$.
3. The set $\mathfrak{A}$ is separable for the metric $d(a, b) = m(a \mathbin{\triangle} b)$.

Assume also that $(\mathfrak{A}, m)$ is atomless: every $a \ne 0$ has some $b \le a$ with $0 < m(b) < m(a)$.
Let $\mathfrak{L}$ be the algebra of [[Lebesgue measurable|2Z2QVWZ262]] subsets of $[0,1]$ modulo [[null sets|VQQM4Y550T]], with $\lambda$ induced by Lebesgue measure.
Then there is a Boolean algebra isomorphism $\Phi \colon \mathfrak{A} \to \mathfrak{L}$ with $\lambda(\Phi(a)) = m(a)$ for all $a \in \mathfrak{A}$.

## Remarks

Idea of proof: take a dense sequence in $\mathfrak{A}$ and the finite partitions of $1$ that it generates.
Since the algebra is atomless, $m$ takes all values between $0$ and $m(a)$ on elements below $a$.
This lets one send each partition to a partition of $[0,1]$ into finite unions of intervals with the same measures, compatibly with refinement.
The map then extends by continuity in the metric $d$.
Without atomlessness the result fails: the algebra with two atoms of measure $1/2$ has four elements, while $\mathfrak{L}$ is infinite.
Without separability it fails as well: the measure algebra of the product measure on $\set{0,1}^I$ with $I$ uncountable is atomless but not separable.
As a consequence, the measure algebra of every atomless [[standard probability space|QDDRDW9PXS]] is isomorphic to that of $[0,1]$.

## Explanations

### L1 human

Ignore sets of measure zero.
Then there is essentially only one way to spread probability evenly with no lumps, as long as the space is not too large.
Every such system of events looks like the system of measurable subsets of the unit interval with length as probability.
This is why the unit interval can serve as a model for many random experiments.

### L2 human

The theorem lets ergodic theory move between point maps and automorphisms of measure algebras.
Together with the theory of standard probability spaces, it shows that many probability spaces of analysis are isomorphic to $[0,1]$ up to null sets.
An example is $[0,1]^\N$ with the product of Lebesgue measures.
Maharam's theorem classifies the non-separable case.
