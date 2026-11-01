---
tag: W1YH3YD3S4
kind: statement
role: theorem
name: Harris inequality
msc: ["60E15", 05D05, 60C05]
uses: [059TJN0NZ1, 0WQNRCNY3M, 0A7KV2WB7A]
about: [0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/FKG_inequality
---

## Statement

Let $n \ge 1$ and let $p_1, \ldots, p_n \in [0, 1]$.
Let $\Omega = \set{0, 1}^n$ with the product [[probability measure|059TJN0NZ1]] $\mu$ under which the coordinates are independent and the $i$-th coordinate equals $1$ with probability $p_i$.
Order $\Omega$ coordinatewise: $x \le y$ when $x_i \le y_i$ for all $i$.
Let $f, g \colon \Omega \to \R$ be [[increasing|0A7KV2WB7A]] functions, that is, $x \le y$ implies $f(x) \le f(y)$ and $g(x) \le g(y)$.
Then
$$\mathbb{E}[f g] \ge \mathbb{E}[f] \, \mathbb{E}[g],$$
where $\mathbb{E}$ is the [[expected value|0WQNRCNY3M]] with respect to $\mu$.

## Remarks

The proof is by induction on $n$.
For $n = 1$, the inequality is equivalent to $p_1 (1 - p_1) (f(1) - f(0)) (g(1) - g(0)) \ge 0$, which holds because both differences are nonnegative.
The induction step conditions on the last coordinate and applies the case $n = 1$ to the conditional expectations, which are again increasing.

For indicator functions of increasing events $A$ and $B$, the inequality reads $\mu(A \cap B) \ge \mu(A) \, \mu(B)$: increasing events are positively correlated.
For example, in the [[Erdős–Rényi model|6E83YKANV3]] $G(n, p)$ the events "the graph is connected" and "the graph has a triangle" are increasing, so they are positively correlated.
If $f$ is increasing and $g$ is decreasing, the inequality is reversed.
The product structure of $\mu$ matters.
For the measure giving probability $1/2$ to each of $(1, 0)$ and $(0, 1)$, the increasing events $\set{x_1 = 1}$ and $\set{x_2 = 1}$ have probability $1/2$ each but are disjoint.

## Explanations

### L1 human

Under independent coin flips, two "more is better" quantities tend to go up together.
If knowing that some coins show heads makes $f$ larger, it also makes $g$ larger, so the average of the product is at least the product of the averages.

### L2 human

The Harris inequality is the case of a product measure in the FKG inequality, which allows any measure on a distributive lattice satisfying the log-supermodularity condition.
Both follow from the [[Ahlswede–Daykin inequality|4085B8A528]].
For the uniform measure on subsets of a finite set, it is Kleitman's lemma: two up-sets $\mathcal{A}, \mathcal{B}$ of subsets of $\set{1, \ldots, n}$ satisfy $2^n |\mathcal{A} \cap \mathcal{B}| \ge |\mathcal{A}| \, |\mathcal{B}|$.
It is a standard tool in percolation theory and random graphs, often together with the [[Janson inequality|J3CT5D7FSZ]], which gives a bound in the other direction.
