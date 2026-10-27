---
tag: 0FPWF7TTMB
kind: statement
role: theorem
name: Lévy's continuity theorem
aliases: [levy-continuity-theorem]
msc: ["60E10", 60F05]
uses: [0MYDNRT7PP, 0JDAQHWA9N, 0T8BYAFEXX]
sources:
  - url: https://en.wikipedia.org/wiki/Lévy's_continuity_theorem
    locator: Statement
same_as:
  wikidata: Q1966978
  wikipedia: Lévy's continuity theorem
inventory: [SYT6120WS1]
---

## Statement

Let $X, X_1, X_2, \dots$ be real random variables with [[characteristic functions|0MYDNRT7PP]] $\varphi, \varphi_1, \varphi_2, \dots$.
1. If $X_n \to X$ [[in distribution|0JDAQHWA9N]], then $\varphi_n(t) \to \varphi(t)$ for each $t \in \mathbb{R}$.
2. Conversely, suppose that $\varphi_n(t)$ converges to a limit $\psi(t)$ for each $t \in \mathbb{R}$, and that $\psi$ is continuous at $0$. Then $\psi$ is the characteristic function of a random variable $Y$, and $X_n \to Y$ in distribution.

## Remarks

Part 1 follows from the definition of convergence in distribution with the bounded continuous functions $\cos(tx)$ and $\sin(tx)$.
The continuity at $0$ in part 2 is necessary. For $X_n \sim \mathcal{N}(0, n)$, $\varphi_n(t) = e^{-nt^2/2}$ tends to $1_{\{t = 0\}}$, which is not continuous at $0$, and $X_n$ does not converge in distribution.
The theorem holds in the same form for random vectors in $\mathbb{R}^k$.

## History

The theorem is named after Paul Lévy.

## Explanations

### L1 human

To show that random variables converge in distribution, it is enough to show that their characteristic functions converge.
This is often much easier, because characteristic functions of sums of independent variables are products.
