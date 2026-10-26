---
tag: 0CZRT49QNG
kind: definition
name: Contractive sequence
msc: [40A05]
defines: 0C9CMCN9BQ
uses: [0CTV783HYT]
sources:
  - url: https://en.wikipedia.org/wiki/Contraction_mapping
    locator: lead section
---

## Definition

Let $(a_n)$ be a [[real sequence|0CTV783HYT]].
The sequence is contractive if there is a real number $C$ with $0 < C < 1$ such that
$$|a_{n+2} - a_{n+1}| \le C\, |a_{n+1} - a_n| \quad \text{for all } n \in \mathbb{N}.$$

## Remarks

Each contractive sequence is a [[Cauchy sequence|0QZMTN5AXX]]. By induction $|a_{n+1} - a_n| \le C^n |a_1 - a_0|$, and the [[geometric series|01X5CVV1Q5]] bounds $|a_m - a_n|$. So each contractive sequence converges.
If $f \colon \mathbb{R} \to \mathbb{R}$ is a contraction mapping, so that $|f(x) - f(y)| \le C|x - y|$ with $C < 1$, then each sequence $a_{n+1} = f(a_n)$ is contractive.
It is not enough that $|a_{n+2} - a_{n+1}| < |a_{n+1} - a_n|$ for all $n$. The partial sums of the harmonic series satisfy this, and they diverge.

## Explanations

### L1 human

In a contractive sequence, each step is at most a fixed fraction of the step before.
The steps shrink like a geometric sequence, so the total distance travelled is finite, and the sequence converges.
