---
tag: 0B3Q3XDM5X
kind: definition
name: Quantile function
msc: ["60E05"]
defines: 0X60VE98HN
uses: [0MXMS3AE13, 04KFTA34C5]
sources:
  - url: https://en.wikipedia.org/wiki/Quantile_function
    locator: General distribution function
---

## Definition

Let $F \colon \mathbb{R} \to [0, 1]$ be the [[cumulative distribution function|0MXMS3AE13]] of a real random variable $X$.
The quantile function of $X$ is the function $Q \colon (0, 1) \to \mathbb{R}$ with
$$Q(p) = \inf \{x \in \mathbb{R} : F(x) \ge p\}.$$
Here $\inf$ is the [[infimum|04KFTA34C5]]. The number $Q(p)$ is the $p$-quantile of $X$.

## Remarks

The set in the definition is nonempty and bounded below for $0 < p < 1$, and the infimum is a minimum because $F$ is right-continuous. So $F(Q(p)) \ge p$, and $Q(p) \le x$ if and only if $p \le F(x)$.
If $F$ is continuous and strictly increasing, then $Q = F^{-1}$.
If $U$ is uniform on $(0, 1)$, then $Q(U)$ has the cumulative distribution function $F$. This is inverse transform sampling.
$Q(1/2)$ is a [[median|08W2CW8PKW]] of $X$, and $Q(1/4)$ and $Q(3/4)$ are the lower and upper quartiles.

## Explanations

### L1 human

The quantile function answers the question "below which value does a fraction $p$ of the probability lie?".
For the exponential distribution with rate $1$, $F(x) = 1 - e^{-x}$, so $Q(p) = -\ln(1 - p)$.
