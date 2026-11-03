---
tag: CHAYZAWENA
kind: definition
name: Leslie matrix
msc: [92D25, 15B48]
defines: RNVHT5BTQS
uses: [WS9M7HY0FE, JPQCCFCY8X, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Leslie_matrix
---

## Definition

Let $k \ge 2$ be the number of age classes.
Let $f_1, \ldots, f_k \ge 0$ be the fecundities, where $f_i$ is the mean number of newborns in class $1$ per individual of class $i$ in one time step.
Let $s_1, \ldots, s_{k-1} \in (0, 1]$ be the survival probabilities, where $s_i$ is the probability that an individual of class $i$ survives into class $i + 1$.
The *Leslie matrix* with these parameters is the $k \times k$ [[matrix|0VD9ZSWWJG]]
$$L = \begin{pmatrix} f_1 & f_2 & \cdots & f_{k-1} & f_k \\ s_1 & 0 & \cdots & 0 & 0 \\ 0 & s_2 & \cdots & 0 & 0 \\ \vdots & & \ddots & & \vdots \\ 0 & 0 & \cdots & s_{k-1} & 0 \end{pmatrix}.$$
The age-structured [[matrix population model|WS9M7HY0FE]] $n(t + 1) = L \, n(t)$ is the Leslie model.

## Remarks

Every Leslie matrix is a [[nonnegative matrix|JPQCCFCY8X]].
Example: $L = \begin{pmatrix} 1 & 2 \\ 0.5 & 0 \end{pmatrix}$ is a Leslie matrix with $f = (1, 2)$ and $s_1 = 0.5$; its characteristic polynomial is $\lambda^2 - \lambda - 1$, so its dominant eigenvalue is $(1 + \sqrt 5)/2 \approx 1.618$.
Non-example: $\begin{pmatrix} 1 & 2 \\ 0.5 & 0.3 \end{pmatrix}$ is not a Leslie matrix, because its entry in place $(2, 2)$ is not $0$.
Such a matrix lets individuals stay in the last class and fits a stage-structured model.
The characteristic equation of $L$ is equivalent, for $\lambda > 0$, to the Euler–Lotka equation $\sum_{i=1}^{k} f_i \, \ell_i \, \lambda^{-i} = 1$, where $\ell_1 = 1$ and $\ell_i = s_1 \cdots s_{i-1}$.
