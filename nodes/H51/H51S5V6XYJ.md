---
tag: H51S5V6XYJ
kind: definition
name: One-parameter subgroup
msc: ["22E15", 22A05]
defines: YHA64AP1HN
uses: [92700QAB5Y, 7JBRGCVJRB, 0JYTG5K9Y4, 020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/One-parameter_group
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]].
A *one-parameter subgroup* of $G$ is a continuous [[group homomorphism|0JYTG5K9Y4]] $\gamma \colon \R \to G$ from the additive group of real numbers.
So $\gamma$ is continuous and
$$\gamma(s + t) = \gamma(s)\gamma(t) \quad \text{for all } s, t \in \R.$$

## Remarks

Despite the name, a one-parameter subgroup is the map $\gamma$, not its image.

Example: for a real $n \times n$ matrix $A$, the map $\gamma(t) = e^{tA}$ into $GL_n(\R)$, given by the [[matrix exponential|020M04FN1H]], is continuous, and $e^{(s + t)A} = e^{sA} e^{tA}$ because $sA$ and $tA$ commute.

Non-example: $\gamma(t) = \begin{pmatrix} 1 & t \\ 0 & 1 + t^2 \end{pmatrix}$ is a continuous curve in $GL_2(\R)$ with $\gamma(0) = I$, but it is not a homomorphism.
The $(2,2)$ entry of $\gamma(1)\gamma(1)$ is $4$, while that of $\gamma(2)$ is $5$.

If $G$ is a [[Lie group|7JBRGCVJRB]], every one-parameter subgroup is smooth.
Then $\gamma \mapsto \gamma'(0)$ is a bijection from the one-parameter subgroups of $G$ onto the tangent space $T_eG$.
