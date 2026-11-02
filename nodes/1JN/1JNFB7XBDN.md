---
tag: 1JNFB7XBDN
kind: definition
name: Collectively compact operator approximation
msc: [45L05, 47A58, 65R20]
defines: AEZE6B2XXY
uses: [06GZ956657, M2NEP1K5AE, KHJ2G2R5G7, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_operator
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]] with closed unit ball $B$.
Let $\mathcal{K}$ be a set of bounded linear operators $X \to X$.
The set $\mathcal{K}$ is *collectively compact* if
$$\set{L\psi : L \in \mathcal{K}, \ \psi \in B}$$
is relatively compact in $X$.
This means that its closure is [[compact|0R6EWFKRCF]].
A sequence $(K_n)$ of bounded linear operators on $X$ is a *collectively compact approximation* of a bounded linear operator $K$ on $X$ if:

1. $K_n \psi \to K\psi$ for every $\psi \in X$, and
2. the set $\set{K_n : n \ge 1}$ is collectively compact.

## Remarks

Every operator in a collectively compact set is [[compact|M2NEP1K5AE]], and the limit $K$ in the definition is compact as well.
The main result assumes that $K_n$ is a collectively compact approximation of $K$ and that $I - K$ is injective.
Then for large $n$ the operators $I - K_n$ are invertible with uniformly bounded inverses.
The solutions of $\varphi_n - K_n\varphi_n = f$ then satisfy $\norm{\varphi_n - \varphi} \le C \norm{K_n\varphi - K\varphi}$.
The proof uses that $\norm{(K_n - K) K} \to 0$ and $\norm{(K_n - K) K_n} \to 0$, although $\norm{K_n - K}$ need not tend to $0$.

Example: let $X = C[0, 1]$, let $k$ be continuous on $[0, 1]^2$, and let $(K_n\psi)(x) = \frac{1}{n}\sum_{j=1}^{n} k(x, \frac{j}{n}) \psi(\frac{j}{n})$.
For $\psi \in B$ one has $\abs{K_n\psi(x)} \le \max \abs{k}$ and $\abs{K_n\psi(x) - K_n\psi(x')} \le \max_t \abs{k(x, t) - k(x', t)}$, so the family is uniformly bounded and equicontinuous, hence relatively compact by the [[Arzelà–Ascoli theorem|0381S8Z5P0]].
Riemann sums converge, so $K_n\psi \to K\psi$ uniformly with $(K\psi)(x) = \int_0^1 k(x, t) \psi(t) \, dt$.
In general $\norm{K_n - K} \not\to 0$ here: for $k = 1$, functions $\psi$ in $B$ that equal $-1$ at the nodes and have integral close to $1$ show $\norm{K_n - K} = 2$ for every $n$.

Non-example: on $X = \ell^2$, let $K_n$ be the projection onto the first $n$ coordinates.
Then $K_n \psi \to \psi$ for every $\psi$, but the set $\set{K_n e_n} = \set{e_n}$ has no convergent subsequence, so clause 2 fails; indeed the limit $I$ is not compact.
