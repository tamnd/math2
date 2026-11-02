---
tag: FXCQWFY5RV
kind: definition
name: Statistical inference
msc: [62A01]
defines: JZ2S01BHJJ
uses: [JZ6R7J36K5, 036756NFD6, 0TTNRP5PFQ]
sources:
  - url: https://en.wikipedia.org/wiki/Statistical_inference
---

## Definition

Let $\mathcal{P} = \set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] on a sample space $S$.
Let $x \in S$ be an observed value of a random element $X$ whose law is $P_\theta$ for an unknown $\theta$.
*Statistical inference* is the derivation, from $x$, of statements about $\theta$ or about a function $\tau(\theta)$.
A rule of inference is a map defined on $S$ that does not depend on $\theta$; its main kinds are these.

1. A point estimate: a value $\hat{\tau}(x)$ of an [[estimator|0TTNRP5PFQ]] of $\tau(\theta)$.
2. A set estimate: a set $C(x)$ of plausible values of $\tau(\theta)$.
3. A test: a decision $\varphi(x) \in \set{0, 1}$ between a hypothesis $\theta \in \Theta_0$ and its alternative $\theta \in \Theta \setminus \Theta_0$.

## Remarks

Example: for $n$ independent $\mathcal{N}(\theta, 1)$ observations, the sample mean $\bar{x}$ is a point estimate of $\theta$, and $[\bar{x} - 1.96/\sqrt{n}, \bar{x} + 1.96/\sqrt{n}]$ is a set estimate of $\theta$.
Both are computed from the data alone, as the definition requires.
Non-example: the rule "report $\theta$" is not a rule of inference, since it uses the unknown parameter.
Inference rules are built from [[statistics|036756NFD6]] and judged either by their behaviour over repeated samples or through a posterior distribution.
