---
tag: 9ZK07AKD4M
kind: definition
name: Kolmogorov epsilon-entropy
msc: [41A46, 46B50]
defines: 63XHDVA5FS
uses: [0VKD1TP7F3, 020Q06TYYH]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_number
---

## Definition

Let $(X, \rho)$ be a [[metric space|0VKD1TP7F3]], let $K \subseteq X$ be a nonempty [[totally bounded set|020Q06TYYH]], and let $\varepsilon > 0$.
Let $N_\varepsilon(K)$ be the least number $N$ such that $K \subseteq A_1 \cup \cdots \cup A_N$ for some subsets $A_1, \dots, A_N$ of $X$ of diameter at most $2\varepsilon$.
The *Kolmogorov $\varepsilon$-entropy* of $K$ is
$$H_\varepsilon(K) = \log_2 N_\varepsilon(K).$$

## Remarks

The number $N_\varepsilon(K)$ is finite because $K$ is totally bounded.
Covering by closed balls of radius $\varepsilon$ instead gives the covering number $N'_\varepsilon(K)$, and $N_\varepsilon(K) \le N'_\varepsilon(K) \le N_{\varepsilon/2}(K)$.
So the two versions have the same growth up to a change of $\varepsilon$ by a factor $2$.
Kolmogorov and Tikhomirov also used the $\varepsilon$-capacity, the logarithm of the largest number of points of $K$ with pairwise distances greater than $\varepsilon$.

Example: $K = [0, 1]$ in $\R$.
A set of diameter at most $2\varepsilon$ lies in an interval of length $2\varepsilon$, so at least $1/(2\varepsilon)$ of them are needed.
On the other hand, $\ceil{1/(2\varepsilon)}$ consecutive closed intervals of length $2\varepsilon$ suffice.
So $N_\varepsilon([0, 1]) = \ceil{1/(2\varepsilon)}$ and $H_\varepsilon([0, 1]) = \log_2 \ceil{1/(2\varepsilon)}$.

Non-example: $K = [0, \infty)$ is not totally bounded, and no finite family of sets of diameter $2\varepsilon$ covers it, so $H_\varepsilon(K)$ is not defined, or is $+\infty$.

For the class of functions $f$ on $[0, 1]$ with $\abs{f} \le 1$ and Lipschitz constant at most $1$, in the supremum norm, $H_\varepsilon$ is of order $1/\varepsilon$ as $\varepsilon \to 0$.
