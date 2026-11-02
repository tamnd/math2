---
tag: HSBWJSBH0D
kind: statement
role: theorem
name: Cochran's theorem
msc: ["62E15", 62J10]
uses: [0G558GJQMW, 0RFMMBHFTV, 0RBQS1JJCR, 0N28QN4CYA, 0EWQEYRVA8, 0E9502NT92, 0K7TD9BV2D]
about: [0RFMMBHFTV, 0RBQS1JJCR]
sources:
  - url: https://en.wikipedia.org/wiki/Cochran%27s_theorem
same_as:
  wikidata: Q599876
  wikipedia: Cochran's theorem
---

## Statement

Let $X = (X_1, \dots, X_n)^T$ be a random vector with the [[multivariate normal distribution|0G558GJQMW]] $\mathcal{N}_n(0, I_n)$, that is, $X_1, \dots, X_n$ are independent standard normal variables.
Let $A_1, \dots, A_k$ be real [[symmetric|0N28QN4CYA]] $n \times n$ matrices with $A_1 + \cdots + A_k = I_n$.
Let $r_i$ be the [[rank|0EWQEYRVA8]] of $A_i$ and let $Q_i = X^T A_i X$ be the corresponding [[quadratic form|0RBQS1JJCR]], so that $X^T X = Q_1 + \cdots + Q_k$.
Then the following are equivalent.

1. $r_1 + \cdots + r_k = n$.
2. The random variables $Q_1, \dots, Q_k$ are [[independent|0E9502NT92]], and each $Q_i$ has the [[chi-squared distribution|0RFMMBHFTV]] with $r_i$ degrees of freedom.

## Remarks

The proof of 1 implies 2 rests on a fact of linear algebra.
If symmetric matrices sum to $I_n$ and their ranks sum to $n$, then each $A_i$ is an [[idempotent matrix|0K7TD9BV2D]] and $A_i A_j = 0$ for $i \ne j$.
Then $\R^n$ is the orthogonal direct sum of the images of the $A_i$.
In an orthonormal basis adapted to this sum, each $Q_i$ is a sum of $r_i$ squares of distinct coordinates of a standard normal vector.
This gives independence and the chi-squared laws.
For 2 implies 1, the sum of the independent $Q_i$ is chi-squared with $\sum r_i$ degrees of freedom.
But $X^T X$ is chi-squared with $n$ degrees of freedom, so $\sum r_i = n$.

Example: with $J$ the $n \times n$ matrix of ones, take $A_1 = \frac{1}{n} J$ and $A_2 = I_n - \frac{1}{n} J$, of ranks $1$ and $n - 1$.
Then $Q_1 = n \bar{X}^2$ and $Q_2 = \sum_i (X_i - \bar{X})^2$ are independent, with $\chi^2$ laws with $1$ and $n - 1$ degrees of freedom.
This decomposition is the basis of the analysis of variance.

Without normality the conclusion fails: for independent variables with another distribution, the quadratic forms are in general neither chi-squared nor independent.

## Explanations

### L1 human

The squared length of a standard normal vector can be split into pieces along perpendicular subspaces, like Pythagoras' theorem.
Cochran's theorem says that the pieces are then independent, and each piece is chi-squared with as many degrees of freedom as the dimension of its subspace.
The dimensions must add up to the full dimension, and that is exactly the condition of the theorem.

### L2 human

In linear models, sums of squares such as the regression sum of squares and the residual sum of squares are quadratic forms in normal errors.
Cochran's theorem shows that they are independent chi-squared variables, so their scaled ratio has an F-distribution.
This is why F-tests in the analysis of variance and in regression have exact null distributions.
The independence of the sample mean and the sample variance of a normal sample is the case of two pieces.
