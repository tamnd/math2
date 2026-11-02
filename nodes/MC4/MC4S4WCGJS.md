---
tag: MC4S4WCGJS
kind: definition
name: Gibbs measure
msc: ["37D35", "82B05", "37B10"]
defines: DG9F3W6MZM
uses: [624XDXX8FN, A1XE59ZHNM, 012PBA0FMD, B232EZ1FMB, 059TJN0NZ1, 8TD2KCVH5N, D33JK3AXRZ, 0CV69WDRXW]
sources:
  - url: https://en.wikipedia.org/wiki/Gibbs_measure
---

## Definition

Let $A$ be a $k \times k$ matrix with entries in $\set{0, 1}$.
Let $\Sigma_A \subseteq \set{1, \dots, k}^{\N}$ be the one-sided [[subshift of finite type|624XDXX8FN]] of the sequences $x = (x_0, x_1, \dots)$ with $A_{x_i x_{i+1}} = 1$ for all $i$.
Let $\sigma \colon \Sigma_A \to \Sigma_A$ be the shift, $(\sigma x)_i = x_{i+1}$.
Let $\varphi \colon \Sigma_A \to \R$ be continuous, and write $S_n \varphi(x) = \sum_{j=0}^{n-1} \varphi(\sigma^j x)$ for its [[Birkhoff sum|8TD2KCVH5N]].
For $x \in \Sigma_A$, the cylinder $[x_0 \dots x_{n-1}]$ is the set of $y \in \Sigma_A$ with $y_i = x_i$ for $0 \le i < n$.
Let $\mu$ be a $\sigma$-[[invariant|B232EZ1FMB]] [[probability measure|059TJN0NZ1]] on $\Sigma_A$.
It is a *Gibbs measure* for $\varphi$ if there are $C \ge 1$ and $P \in \R$ with
$$\frac{1}{C} \le \frac{\mu([x_0 \dots x_{n-1}])}{\exp\left(-nP + S_n \varphi(x)\right)} \le C$$
for every $x \in \Sigma_A$ and every $n \ge 1$.

## Remarks

Example: on the full shift $\set{1, \dots, k}^{\N}$ take $\varphi = 0$, and let $\mu$ be the uniform [[Bernoulli measure|D33JK3AXRZ]], under which the coordinates are independent and uniform.
Then $\mu([x_0 \dots x_{n-1}]) = k^{-n}$ and $S_n \varphi = 0$, so the ratio is $1$ with $P = \log k$, and $C = 1$ works.

Non-example: for the same shift and $\varphi = 0$, the Dirac measure at the constant sequence $(1, 1, 1, \dots)$ is invariant.
It gives measure $0$ to the cylinder $[2]$, so the lower bound fails.

The constant $P$ is then the topological pressure of $\varphi$.
For a topologically mixing $\Sigma_A$ and a [[Hölder continuous|012PBA0FMD]] $\varphi$, a Gibbs measure exists, is unique, and is the unique equilibrium state of $\varphi$ (Bowen).

In statistical mechanics, consider a finite system with states $s$ and energies $E(s)$.
The Gibbs measure at inverse temperature $\beta$ gives $s$ the probability $e^{-\beta E(s)} / Z$, where $Z = \sum_s e^{-\beta E(s)}$ is the [[partition function|0CV69WDRXW]].
For infinite lattice systems, Gibbs measures are defined instead by the Dobrushin–Lanford–Ruelle condition on conditional probabilities, and there may be several of them.
