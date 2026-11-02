---
tag: V4Q6TSY1KX
kind: definition
name: Factorial experiment
msc: [62K15]
defines: EHJ3R589ZX
uses: [2TE42ZWJ3E]
sources:
  - url: https://en.wikipedia.org/wiki/Factorial_experiment
---

## Definition

Let $k \ge 2$ and let $L_1, \dots, L_k$ be finite sets with $s_i = \abs{L_i} \ge 2$, the *levels* of factors $1, \dots, k$.
The treatments are the combinations $t = (t_1, \dots, t_k) \in L_1 \times \cdots \times L_k$.
A *full factorial experiment* is an [[experiment|2TE42ZWJ3E]] whose design applies every one of the $s_1 s_2 \cdots s_k$ combinations to at least one unit.
When every $s_i = 2$, it is a *$2^k$ factorial experiment*, and the levels are usually coded $-1$ and $+1$.

## Remarks

In a $2^k$ experiment with one run per combination and responses $y_t$, the *main effect* of factor $i$ is the mean of $y_t$ over $t_i = +1$ minus the mean over $t_i = -1$.
The *interaction* of factors $i$ and $j$ is half of the difference between the effect of factor $i$ at $t_j = +1$ and at $t_j = -1$.
Equivalently, it is the mean of $y_t$ over $t_i t_j = +1$ minus the mean over $t_i t_j = -1$.

Example: a $2^2$ experiment with factors $A$ and $B$ and responses $y_{--} = 10$, $y_{+-} = 14$, $y_{-+} = 12$, $y_{++} = 20$, where the first sign is the level of $A$.
The main effect of $A$ is $(14 + 20)/2 - (10 + 12)/2 = 6$, and that of $B$ is $(12 + 20)/2 - (10 + 14)/2 = 4$.
The interaction is $\big( (20 - 12) - (14 - 10) \big)/2 = 2$, which also equals $(10 + 20)/2 - (14 + 12)/2$.

Non-example: the runs $(-,-)$, $(+,-)$, $(-,+)$ change one factor at a time from a baseline.
The combination $(+,+)$ is missing, so this is not a full factorial experiment, and the interaction of $A$ and $B$ cannot be estimated.

The data of a factorial experiment are usually analysed by analysis of variance, with one sum of squares for each main effect and each interaction.
