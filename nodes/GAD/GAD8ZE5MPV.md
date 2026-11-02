---
tag: GAD8ZE5MPV
kind: definition
name: Period and index
msc: [16K50, 16K20]
defines: B5DDZHB04G
uses: [5HRKJBAY2V, 0EA5BTA0CX, NNXSP5KKAC, BEW48TA9WZ, 0WE2NHZJ7B]
sources:
  - url: https://en.wikipedia.org/wiki/Brauer_group
---

## Definition

Let $K$ be a field and let $A$ be a [[central simple algebra|5HRKJBAY2V]] over $K$.
By Wedderburn's theorem $A \cong M_m(D)$ for an integer $m \ge 1$ and a [[division ring|0EA5BTA0CX]] $D$ that is central simple over $K$, unique up to isomorphism.

1. The *index* of $A$, written $\operatorname{ind} A$, is the [[degree|NNXSP5KKAC]] of $D$.
2. The *period* (or *exponent*) of $A$, written $\operatorname{per} A$, is the [[order|0WE2NHZJ7B]] of the class $[A]$ in the [[Brauer group|BEW48TA9WZ]] $\mathrm{Br}(K)$.

## Remarks

Basic facts: $\operatorname{per} A$ divides $\operatorname{ind} A$, $\operatorname{ind} A$ divides $\deg A$, and $\operatorname{per} A$ and $\operatorname{ind} A$ have the same prime divisors.
In particular the period is finite, so $\mathrm{Br}(K)$ is a torsion group.

Example: for $\mathbb{H}$ over $\R$, $D = \mathbb{H}$ has degree $2$, so the index is $2$.
The class $[\mathbb{H}]$ is not trivial, and $\mathbb{H} \otimes_\R \mathbb{H} \cong M_4(\R)$, so the period is $2$.

Example: $A = M_n(K)$ has $D = K$, so its index and its period are both $1$.

Over local fields and over global fields, the period equals the index for every central simple algebra.
Over general fields the index can be strictly larger than the period.
