---
tag: M4ZJ8QV3MR
kind: statement
role: theorem
name: CORDIC
msc: [65Y04, 65D20]
uses: [H313BRXEJS, 0CE768XNVP, 0HFREYRSZP]
about: [H313BRXEJS]
sources:
  - url: https://en.wikipedia.org/wiki/CORDIC
same_as:
  wikidata: Q116076
  wikipedia: CORDIC
---

## Statement

Let $n \ge 1$, let $a_i = \arctan 2^{-i}$ for $i \ge 0$ (see [[arctangent|0CE768XNVP]]), and let $K_n = \prod_{i=0}^{n-1} (1 + 2^{-2i})^{-1/2}$.
Let $\theta$ be a real number with $\abs{\theta} \le \sum_{i=0}^{n-1} a_i$.
The *CORDIC* iteration in rotation mode starts from $x_0 = K_n$, $y_0 = 0$, $z_0 = \theta$ and, for $i = 0, \ldots, n-1$, sets $\sigma_i = 1$ if $z_i \ge 0$ and $\sigma_i = -1$ otherwise, and
$$x_{i+1} = x_i - \sigma_i 2^{-i} y_i, \qquad y_{i+1} = y_i + \sigma_i 2^{-i} x_i, \qquad z_{i+1} = z_i - \sigma_i a_i.$$
Then, in exact arithmetic,

1. $x_n = \cos(\theta - z_n)$ and $y_n = \sin(\theta - z_n)$;
2. $\abs{z_n} \le a_{n-1} < 2^{-(n-1)}$;
3. hence $\abs{x_n - \cos\theta} < 2^{-(n-1)}$ and $\abs{y_n - \sin\theta} < 2^{-(n-1)}$.

## Remarks

Each step multiplies the vector $(x_i, y_i)$ by the matrix with rows $(1, -\sigma_i t)$ and $(\sigma_i t, 1)$, $t = 2^{-i}$, which is $\sqrt{1 + t^2}$ times the [[rotation|0HFREYRSZP]] by the angle $\sigma_i \arctan t$.
After $n$ steps the scale factors multiply to $1/K_n$, which cancels $x_0 = K_n$, and the total angle is $\sum_i \sigma_i a_i = \theta - z_n$; this is clause 1.
For clause 2, concavity of $\arctan$ on $[0, \infty)$ gives $a_i \le 2 a_{i+1}$, hence $a_i \le a_{i+1} + \cdots + a_{n-1} + a_{n-1}$ by induction.
With this, the bound $\abs{z_i} \le a_i + \cdots + a_{n-1} + a_{n-1}$ passes from $z_i$ to $z_{i+1} = z_i - \sigma_i a_i$, and at $i = n$ it gives $\abs{z_n} \le a_{n-1}$.
Clause 3 follows because $\cos$ and $\sin$ are $1$-Lipschitz.
Since $a_0 + a_1 + a_2 + a_3 \approx 1.618 > \pi/2$, for $n \ge 4$ the method covers all $\theta \in [-\pi/2, \pi/2]$; other angles are first reduced by symmetries.
Multiplication by $2^{-i}$ is a shift in binary, so each step needs only shifts, additions and a table lookup of $a_i$.

## Explanations

### L1 human

CORDIC computes sine and cosine without any multiplication.
It turns a vector towards the target angle by smaller and smaller fixed angles: $45°$, about $26.6°$, about $14°$, and so on.
Each turn goes to the left or to the right.
These special angles are chosen so that each turn needs only a binary shift and an addition.
Each step gains about one binary digit of accuracy.
This made it the method of choice in pocket calculators and in hardware without a multiplier.

### L2 human

The same iteration in vectoring mode drives $y$ to $0$ instead of $z$, and then computes $\arctan(y_0/x_0)$ and, up to the known constant factor, the length $\sqrt{x_0^2 + y_0^2}$.
Replacing $\arctan 2^{-i}$ by $\operatorname{artanh} 2^{-i}$ and rotations by hyperbolic rotations gives the hyperbolic functions, the exponential and the logarithm; in that case some steps must be repeated to ensure convergence.
The constant $K_n$ tends to about $0.6073$ and is applied once at the start, not at each step.
