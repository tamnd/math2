---
tag: 97VKFA0XWZ
kind: definition
name: Effective population size
msc: [92D10, 92D15]
defines: MBW183XCKH
uses: [SR4F169EKF, 007QED3E0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Effective_population_size
---

## Definition

Consider a diploid population model, and let $p_t$ be the frequency of a neutral allele in generation $t$.
Suppose that $\operatorname{Var}(p_{t+1} \mid p_t) = c \, p_t (1 - p_t)$ for a constant $c > 0$, where $\operatorname{Var}$ is the [[variance|007QED3E0Y]].
The *variance effective population size* of the model is the number $N_e$ with
$$\frac{p_t (1 - p_t)}{2 N_e} = \operatorname{Var}(p_{t+1} \mid p_t), \quad \text{that is,} \quad N_e = \frac{1}{2c}.$$
It is the number of diploid individuals in a [[Wright–Fisher model|SR4F169EKF]] with the same variance of allele frequency change.

## Remarks

Example: in the Wright–Fisher model with $2N$ gene copies, $c = 1/(2N)$, so $N_e = N$.

Non-example: a deterministic model of selection with no sampling has $\operatorname{Var}(p_{t+1} \mid p_t) = 0$.
There is no $c > 0$, so the effective size is not defined; one may think of it as infinite.

Other versions match other quantities with the Wright–Fisher model, such as the rate of loss of heterozygosity (inbreeding effective size).
In simple cases the versions agree, and the standard formulas are these.

1. With $N_m$ breeding males and $N_f$ breeding females, $N_e = 4 N_m N_f / (N_m + N_f)$.
2. With sizes $N_1, \dots, N_T$ in $T$ successive generations, $N_e$ over the $T$ generations is about the harmonic mean $T / (1/N_1 + \cdots + 1/N_T)$.

The harmonic mean is dominated by the small values, so a single bottleneck lowers $N_e$ for a long time.
