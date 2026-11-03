---
tag: AWCMDNC1JQ
kind: definition
name: Data envelopment analysis
msc: [90C08, 90B50, 90C05]
defines: Z7SSS8G8G9
uses: [VNMXB0J2KA, XVBF9EJY10]
sources:
  - url: https://en.wikipedia.org/wiki/Data_envelopment_analysis
---

## Definition

Let $n \ge 1$ decision-making units be given.
Unit $j$ uses an input vector $x_j \in \R^m$ and produces an output vector $y_j \in \R^s$, all of whose entries are positive.
The *CCR efficiency score* of a unit $o \in \set{1, \dots, n}$ is the optimal value $\theta_o$ of the [[linear-fractional program|XVBF9EJY10]]
$$\text{maximize } \frac{w^T y_o}{v^T x_o} \quad \text{subject to} \quad \frac{w^T y_j}{v^T x_j} \le 1 \ (1 \le j \le n), \quad w \in \R^s_{\ge 0}, \ v \in \R^m_{\ge 0}, \ v \ne 0.$$
The unit $o$ is called *efficient* when $\theta_o = 1$.
*Data envelopment analysis* is the computation of these scores, and of related scores of other DEA models, for all units.

## Remarks

Since the ratios are unchanged when $w$ and $v$ are scaled together, one may fix $v^T x_o = 1$.
This gives the equivalent [[linear program|VNMXB0J2KA]]
$$\text{maximize } w^T y_o \quad \text{subject to} \quad v^T x_o = 1, \quad w^T y_j - v^T x_j \le 0 \ (1 \le j \le n), \quad w, v \ge 0.$$
The constraint for $j = o$ shows $\theta_o \le 1$.

Example: with one input and one output, the score is $\theta_o = (y_o / x_o) / \max_j (y_j / x_j)$.
Indeed the constraints say $w / v \le x_j / y_j$ for all $j$, and the objective is $(w / v)(y_o / x_o)$.
For two units with $(x_1, y_1) = (2, 4)$ and $(x_2, y_2) = (1, 1)$, unit $1$ has score $1$ and unit $2$ has score $1/2$.

Non-example: a score with fixed weights $w$ and $v$ chosen in advance, the same for all units, is an ordinary ratio index.
It is not a DEA score, since DEA chooses the weights separately for each unit.

Many texts call a unit with $\theta_o = 1$ weakly efficient and require in addition that all slacks vanish in a second-stage program for full efficiency.
Other standard models are the BCC model, which allows variable returns to scale, and output-oriented versions.
