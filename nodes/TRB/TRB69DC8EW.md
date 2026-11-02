---
tag: TRB69DC8EW
kind: definition
name: Tame Fréchet space
msc: [46A61, 58C15]
defines: 7WPVZZ4YFC
uses: [N8TGDDJCFJ, 4KX81Q85DT, 0BDTTM24DP, 0S3SMRH0Z5]
sources:
  - url: https://en.wikipedia.org/wiki/Nash%E2%80%93Moser_theorem
---

## Definition

A *graded Fréchet space* is a [[Fréchet space|N8TGDDJCFJ]] $F$ with a sequence of [[seminorms|4KX81Q85DT]] $\norm{\cdot}_0 \le \norm{\cdot}_1 \le \norm{\cdot}_2 \le \cdots$ that defines its topology.
Let $L \colon F \to G$ be a [[continuous linear map|0S3SMRH0Z5]] between graded Fréchet spaces.
It is *tame* if there are integers $r, b \ge 0$ and constants $C_n$ with $\norm{L f}_n \le C_n \norm{f}_{n + r}$ for all $f \in F$ and all $n \ge b$.

For a [[Banach space|0BDTTM24DP]] $B$, let $\Sigma(B)$ be the space of sequences $f = (f_k)_{k \ge 0}$ in $B$ with
$$\norm{f}_n = \sum_{k \ge 0} e^{n k} \norm{f_k}_B < \infty \quad \text{for all } n \ge 0,$$
graded by these norms.
A graded Fréchet space $F$ is *tame* if there are a Banach space $B$ and tame linear maps $L \colon F \to \Sigma(B)$ and $M \colon \Sigma(B) \to F$ with $M \circ L = \id_F$.

## Remarks

Example: $\Sigma(B)$ itself is tame, with $L = M = \id$; the identity satisfies the estimate with $r = b = 0$ and $C_n = 1$.
Hamilton proved that $C^\infty(X)$ for a compact manifold $X$, graded by the $C^n$ norms, is tame.

Non-example of a tame map: on $\Sigma(\R)$ let $(L f)_k = f_{\floor{k/2}}$.
Then $\norm{L f}_n \le (1 + e^n) \norm{f}_{2n}$, so $L$ is continuous.
For the unit sequence $\delta_j$ one gets $\norm{L \delta_j}_n \ge e^{2nj}$ while $\norm{\delta_j}_{n+r} = e^{(n+r)j}$, so for $n > r$ no constant $C_n$ works for all $j$, and $L$ is not tame.

The grading is part of the data: equivalent gradings, with $\norm{f}_n$ and $\norm{f}'_n$ bounded by each other up to a fixed shift $r$ and constants, give the same tame maps.
