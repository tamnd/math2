---
tag: 7MPCVNQ8SF
kind: definition
name: Ideal norm
msc: [11R04, 13F05]
defines: M54ADM0CVF
uses: [MWBDFS2KJ5, 096Z9MP2ME, 0076HWHGHQ, 02CK6QMXYD, 0HYRJF4WNQ, YB4JTB4WJN]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_norm
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_K$, and let $\mathfrak{a}$ be a nonzero [[ideal|096Z9MP2ME]] of $\mathcal{O}_K$.
The *norm* of $\mathfrak{a}$ is the [[cardinality|02CK6QMXYD]] of the [[quotient ring|0076HWHGHQ]]:
$$N(\mathfrak{a}) = \#(\mathcal{O}_K / \mathfrak{a}).$$
This number is finite.

## Remarks

Example: in $\Z[i]$, the ideal $(1 + i)$ has the classes of $0$ and $1$, so $N((1 + i)) = 2$, which equals the [[norm of the Gaussian integer|0HYRJF4WNQ]] $1 + i$, namely $1^2 + 1^2$.
Non-example: the zero ideal is excluded, since $\mathcal{O}_K / (0) \cong \mathcal{O}_K$ is infinite.
The norm is multiplicative: $N(\mathfrak{a}\mathfrak{b}) = N(\mathfrak{a}) N(\mathfrak{b})$.
For a nonzero $\alpha \in \mathcal{O}_K$, $N(\alpha \mathcal{O}_K) = \abs{N_{K/\Q}(\alpha)}$, the absolute value of the field norm.
By multiplicativity the norm extends to a group homomorphism from the nonzero [[fractional ideals|YB4JTB4WJN]] of $\mathcal{O}_K$ to $\Q_{>0}^{\times}$.
For a nonzero prime ideal $\mathfrak{p}$ lying over the prime $p$, $N(\mathfrak{p}) = p^f$, where $f$ is the residue degree.
