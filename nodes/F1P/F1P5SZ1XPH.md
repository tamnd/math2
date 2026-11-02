---
tag: F1P5SZ1XPH
kind: definition
name: Constructivism
msc: ["03F65", "03F55", "00A30"]
defines: G958EQ8CWW
uses: [01XM7JEKHY, 0RYYK8PG4S, 0J0XBKG64S, 0NFAGWH84K]
sources:
  - url: https://en.wikipedia.org/wiki/Constructivism_(philosophy_of_mathematics)
---

## Definition

*Constructivism* is the position in the philosophy of mathematics that consists of these two principles.

1. A mathematical object exists only if there is a method to construct it.
2. A proof of "there exists $x$ such that $P(x)$" must give a method to construct such an $x$. It must also prove $P(x)$ for this $x$.

*Constructive mathematics* is mathematics carried out under these principles.
Its logic is intuitionistic logic: classical logic without the general [[law of excluded middle|0RYYK8PG4S]] $P \vee \neg P$.

## Remarks

Example: the proof that for each natural number $n$ there is a prime $p > n$, by taking a prime factor of $n! + 1$, is constructive.
It gives a method: factor $n! + 1$ and take any prime factor $p$; then $p > n$, because no number from $2$ to $n$ divides $n! + 1$.
Non-example: the classical proof that there are irrational numbers $a, b$ with $a^b$ rational is not constructive.
It argues that either $\sqrt{2}^{\sqrt{2}}$ is rational, or it is not and then $(\sqrt{2}^{\sqrt{2}})^{\sqrt{2}} = 2$; it does not say which case holds.
It uses the law of excluded middle, which fails principle 2.
In constructive mathematics, a [[proof by contradiction|0J0XBKG64S]] proves negated statements $\neg P$, but in general does not prove $P$ from $\neg \neg P$; see the [[double negation law|0NFAGWH84K]].
