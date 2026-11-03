---
tag: RJ1PD6Z4RH
kind: definition
name: Matrix population model
msc: [92D25, 15B48, 39A60]
defines: WS9M7HY0FE
uses: [1YEMFQ1H32, JPQCCFCY8X, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_population_models
---

## Definition

Let $k \ge 1$ be a number of classes of individuals, for example age classes or life stages.
Let $A$ be a $k \times k$ [[nonnegative matrix|JPQCCFCY8X]], called the projection matrix.
The *matrix population model* with projection matrix $A$ is the discrete-time [[population model|1YEMFQ1H32]]
$$n(t + 1) = A \, n(t), \qquad t = 0, 1, 2, \ldots.$$
Here $n(t) \in \R_{\ge 0}^k$ is the vector whose entry $n_i(t)$ is the number of individuals in class $i$ at time $t$.
The entry $a_{ij}$ of $A$ is the expected contribution of one individual of class $j$ to class $i$ in one time step.
This contribution comes from survival, growth or reproduction.

## Remarks

The solution is $n(t) = A^t n(0)$.
Example: the [[matrix|0VD9ZSWWJG]] $A = \begin{pmatrix} 0 & 4 \\ 0.5 & 0.5 \end{pmatrix}$ describes juveniles that become adults with probability $0.5$, and adults that survive with probability $0.5$ and have $4$ juveniles each; from $n(0) = (0, 10)$ we get $n(1) = (40, 5)$.
Non-example: a matrix with a negative entry, such as $\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$, is not a projection matrix, since it can map nonnegative counts to negative ones.
When the classes are ages, the projection matrix is a Leslie matrix; when they are stages of different lengths, it is often called a Lefkovitch matrix.
Models in which $A$ depends on $n(t)$ or on $t$ are called density-dependent or time-varying matrix models.
