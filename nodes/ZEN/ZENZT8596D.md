---
tag: ZENZT8596D
kind: statement
role: lemma
name: Hartogs lemma for subharmonic functions
msc: [31B05, 32U05]
uses: [Z1MHMGFNFW, 0T3RZQXDYD, 0R6EWFKRCF, 02BH3MCBQB, S95TR54TCG, BXYQE0Q1ST]
about: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Statement

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]], and let $(u_k)_{k \ge 1}$ be a sequence of [[subharmonic functions|Z1MHMGFNFW]] on $\Omega$.
Assume that the sequence is locally uniformly bounded above: each [[compact set|0R6EWFKRCF]] $L \subseteq \Omega$ has a constant $C_L$ with $u_k \le C_L$ on $L$ for all $k$.
Let $f$ be a continuous real function on $\Omega$ with $\limsup_{k \to \infty} u_k(x) \le f(x)$ for every $x \in \Omega$.
Then for every compact set $K \subseteq \Omega$ and every $\varepsilon > 0$ there is $k_0$ such that
$$u_k(x) \le f(x) + \varepsilon \qquad \text{for all } x \in K \text{ and all } k \ge k_0.$$

## Remarks

Proof idea: fix $x_0 \in K$ and a small radius $r$ such that $f < f(x_0) + \varepsilon/3$ on a closed ball about $x_0$ inside $\Omega$.
By the [[sub-mean value property|BXYQE0Q1ST]], $u_k(y)$ is at most the mean of $u_k$ over the ball $B(y, r)$, for $y$ near $x_0$.
The uniform upper bound allows the reverse form of [[Fatou's lemma|S95TR54TCG]], which bounds the [[limit superior|0T3RZQXDYD]] of these ball means by the mean of $\limsup_k u_k \le f$.
This gives $u_k \le f(x_0) + \varepsilon$ on a neighbourhood of $x_0$ for large $k$, and compactness of $K$ finishes the proof.

The lemma upgrades a pointwise upper bound to a uniform one on compact sets, in the upward direction only.
A typical use: if $u_k \le 0$ in the limit at every point, then $\max_K u_k$ is eventually at most $\varepsilon$ on each compact $K$.
The lower bound is not upgraded in the same way, because subharmonic functions can take very negative values on small sets.

## Explanations

### L1 human

Suppose a sequence of subharmonic functions eventually stays below some continuous ceiling at every single point.
Then, on any compact piece of the domain, the whole sequence eventually stays below the ceiling plus a little, all at once.
Subharmonic functions cannot have thin upward spikes, which is why pointwise control becomes uniform control.

### L2 human

The lemma is named after Hartogs, who used an argument of this kind in his theorem on separately holomorphic functions in several complex variables.
It is a basic compactness tool for subharmonic and plurisubharmonic functions.
Typical uses are bounds on $\frac{1}{k}\log\abs{p_k}$ for sequences of polynomials $p_k$, and the study of upper envelopes of families of subharmonic functions.
