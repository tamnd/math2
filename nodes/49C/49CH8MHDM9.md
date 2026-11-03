---
tag: 49CH8MHDM9
kind: definition
name: Replica trick
msc: [82B44, 82D30]
defines: 4Y5V47G9NH
uses: [0PNRKMRC55, 0WQNRCNY3M, EHPA4B5S5W]
sources:
  - url: https://en.wikipedia.org/wiki/Replica_trick
---

## Definition

Let $Z$ be a positive [[random variable|0PNRKMRC55]] with $\mathbb{E} \abs{\log Z} < \infty$ and $\mathbb{E} Z^{\varepsilon} < \infty$ for some $\varepsilon > 0$.
Then
$$\mathbb{E} \log Z = \lim_{n \to 0^+} \frac{\mathbb{E} Z^n - 1}{n},$$
where $\mathbb{E}$ is the [[expected value|0WQNRCNY3M]].
Consider a disordered system, such as a [[spin glass|EHPA4B5S5W]], with a random Hamiltonian $H_N$ on a configuration space $\Sigma_N$.
Let $Z_N = \sum_{\sigma \in \Sigma_N} e^{-\beta H_N(\sigma)}$ be its partition function.
The *replica trick* is the following procedure.

1. For each positive integer $n$, write $\mathbb{E} Z_N^n = \mathbb{E} \sum_{\sigma^1, \dots, \sigma^n \in \Sigma_N} \exp\big( -\beta \sum_{a=1}^n H_N(\sigma^a) \big)$, a system of $n$ replicas with the same disorder.
2. Compute $\phi(n) = \lim_{N \to \infty} \frac{1}{N} \log \mathbb{E} Z_N^n$ for these integers $n$.
3. Continue $\phi$ to real $n$ near $0$ and take $\lim_{N \to \infty} \frac{1}{N} \mathbb{E} \log Z_N = \lim_{n \to 0} \phi(n) / n$.

## Remarks

The identity holds because $(Z^n - 1)/n$ decreases to $\log Z$ as $n \downarrow 0$, by convexity of $n \mapsto Z^n$, and is bounded by $(Z^\varepsilon - 1)/\varepsilon$ for $n \le \varepsilon$; monotone convergence then applies.
Step 3 is not justified in general: it exchanges the limits $N \to \infty$ and $n \to 0$, and the values of $\phi$ at the integers do not determine its continuation.

Example: let $Z = e^{\beta X}$ with $X$ standard Gaussian.
Then $\mathbb{E} Z^n = e^{n^2 \beta^2 / 2}$, and $(e^{n^2 \beta^2/2} - 1)/n \to 0 = \mathbb{E} \log Z$, as the identity claims.

Non-example: if $\log Z$ has a Cauchy law, then $\mathbb{E} Z^n = \infty$ for every $n > 0$ and $\mathbb{E} \abs{\log Z} = \infty$, so the hypotheses fail and the formula has no meaning.

In spin glass theory, the order parameter of the replicated system is the $n \times n$ overlap matrix $Q_{ab} = \frac{1}{N} \sum_i \sigma^a_i \sigma^b_i$.
The choice of its form in step 3 is called a replica symmetric or a replica symmetry breaking ansatz.
