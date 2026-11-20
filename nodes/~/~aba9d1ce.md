---
tag: ~aba9d1ce
kind: example
name: The rational and real orders are elementarily equivalent
msc: ["03C07", "03C35"]
topics: [AY09KYSW81]
audience: ug2
instance_of: [P3B1V182N4]
uses: [P3B1V182N4, 2W4S2H4VYA, ZR7Y5C235P, ABN5PTXEHY, 01TQB88H4C, 0W7FBYS1F1]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementarily equivalent structures
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $L = \set{<}$.
We check that $(\Q, <) \equiv (\R, <)$, that is, that the two orders are [[elementarily equivalent|P3B1V182N4]], and that they are not isomorphic.

1. Both are dense linear orders without endpoints: between $a < b$ lies $(a + b)/2$, and $a - 1 < a < a + 1$. So both are models of the theory $\mathrm{DLO}$ of [[dense linear orders without endpoints|2W4S2H4VYA]].
2. $\mathrm{DLO}$ has no finite models, since a finite nonempty linear order has a greatest element.
3. Any two countable models of $\mathrm{DLO}$ are isomorphic, by [[Cantor's theorem|ABN5PTXEHY]].
4. By the [[Łoś-Vaught test|ZR7Y5C235P]] with $\kappa = \aleph_0$, the theory $\mathrm{DLO}$ is complete.
5. So for each $L$-sentence $\sigma$, either $\mathrm{DLO} \models \sigma$ or $\mathrm{DLO} \models \neg\sigma$. In the first case $\sigma$ holds in both orders, and in the second case it fails in both. So $(\Q, <) \equiv (\R, <)$.
6. $\Q$ is [[countable|01TQB88H4C]] and $\R$ is [[uncountable|0W7FBYS1F1]], so there is no bijection $\Q \to \R$, and the orders are not isomorphic.

## Remarks

The least upper bound property separates $(\Q, <)$ from $(\R, <)$: every nonempty subset of $\R$ with an upper bound has a least upper bound, while $\set{q \in \Q : q^2 < 2}$ has none in $\Q$.
This property quantifies over subsets, and the example shows that no set of first-order sentences in $\set{<}$ can express it.
The same argument shows that $(\Q, <)$, $(\R, <)$, $(\R \setminus \Q, <)$ and $(\Q \cap (0, 1), <)$ all satisfy the same sentences.
The pair also shows that the finiteness hypothesis is needed in [[the finite case of elementary equivalence|~906b905e]].

## Explanations

### L1 human

The fractions and the real numbers look the same to anyone who may only talk about the order "less than" with first-order sentences.
In both, there is a number between any two numbers, and there is no smallest or largest number.
Yet the real numbers are far more numerous than the fractions, so the two orders are not copies of each other.

### L2 human

We check one sentence directly in both orders: $\sigma = \forall x \, \forall y \, (x < y \to \exists z \, \exists w \, (x < z \land z < w \land w < y))$.

1. In $\Q$, for $x < y$ take $z = x + (y - x)/3$ and $w = x + 2(y - x)/3$. Both are rational, and $x < z < w < y$.
2. In $\R$, the same formulas give real numbers with $x < z < w < y$.
3. So $\sigma$ is true in both, as the example predicts.

The typical use of the example is to show that a first-order property cannot detect cardinality.
A trap is to argue that the orders differ because $\sqrt{2}$ exists in one of them; the language $\set{<}$ has no name for $\sqrt{2}$.
