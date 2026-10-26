---
tag: 0JDAQHWA9N
kind: definition
name: Convergence in distribution
msc: [60F05]
defines: 0SRYJGXKR4
uses: [0MXMS3AE13, 0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_random_variables
    locator: Convergence in distribution
---

## Definition

Let $X, X_1, X_2, \dots$ be real random variables, possibly on different probability spaces, with [[cumulative distribution functions|0MXMS3AE13]] $F, F_1, F_2, \dots$.
The sequence $(X_n)$ converges in distribution to $X$ if
$$\lim_{n \to \infty} F_n(x) = F(x)$$
for each $x \in \mathbb{R}$ at which $F$ is continuous. One writes $X_n \xrightarrow{d} X$.

## Remarks

By the portmanteau theorem, an equivalent condition is $E[g(X_n)] \to E[g(X)]$ for each bounded continuous $g \colon \mathbb{R} \to \mathbb{R}$. This form extends to random variables in metric spaces.
The condition depends only on the laws. So it is the weak convergence of the laws of the $X_n$ to the law of $X$.
The restriction to continuity points is necessary. For $X_n = 1/n$ and $X = 0$, $F_n(0) = 0$ for all $n$, but $F(0) = 1$.
The central limit theorem is a result about convergence in distribution.

## Explanations

### L1 human

Convergence in distribution means that the probabilities for $X_n$ come close to those for $X$. The values of $X_n$ themselves need not come close to the values of $X$.
For example, the number of heads in $n$ tosses, after standardization, converges in distribution to a standard normal variable.
