---
tag: N2787BMTJW
kind: definition
name: Self-organized criticality
msc: [82C27, 82C26, 37N20]
defines: FVJ624HTV0
uses: [57789VKKAY, 0KRH5157WP]
sources:
  - url: https://en.wikipedia.org/wiki/Self-organized_criticality
---

## Definition

Consider a family of stochastic dynamical systems indexed by a system size $L$, for example a model on the box $\set{1, \dots, L}^d$.
Assume that each system is driven by a slow external input, such as adding one grain at a time.
Assume that its response to each input is a finite *avalanche* of fast internal events, with dissipation at the boundary.
Let $\pi_L$ be the [[stationary distribution|0KRH5157WP]] of the dynamics.
Let $s$ be the size of the avalanche caused by one input in the stationary state.
The systems show *self-organized criticality* if both conditions hold:

1. the stationary state is reached from typical initial states without tuning any parameter of the dynamics to a special value;
2. in the stationary state, avalanche sizes are scale invariant.
   There are $\tau > 1$ and a cutoff $s_c(L) \to \infty$ as $L \to \infty$ such that $P_{\pi_L}(s \ge k)$ behaves like $k^{1 - \tau}$ for $1 \ll k \ll s_c(L)$.

## Remarks

This is a physical notion rather than a single mathematical definition; different authors make the scale invariance precise in different ways, through avalanche sizes, durations or spatial correlations.

Example: the [[abelian sandpile model|N33S3095R5]] on a box of $\Z^d$, with grains lost at the boundary, is driven by adding single grains.
Its avalanches are the sequences of topplings.
Its stationary law is uniform on the recurrent configurations, with no free parameter.
Numerical studies show power-law avalanche statistics for it, which is the original example of the notion.

Non-example: the [[Ising model|R0KGM32QN6]] with Glauber dynamics has power-law correlations only when the temperature is tuned to the critical value, so clause 1 fails.

## Explanations

### L1 human

A system is self-organized critical when it drives itself to a state with events of every size, and nobody needs to set a knob to a special value.
