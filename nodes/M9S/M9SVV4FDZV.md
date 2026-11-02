---
tag: M9SVV4FDZV
kind: definition
name: Statistical learning theory
msc: [68Q32, 62H30, 68T05]
defines: 5MR9ZSC3CX
uses: [3BTG6VVCGZ, 00MRN0FARV, 0WQNRCNY3M, 56NVR0SS61, KCFXR9K3GD]
sources:
  - url: https://en.wikipedia.org/wiki/Statistical_learning_theory
---

## Definition

*Statistical learning theory* is the study of the following setting.

1. There are an input space $\mathcal X$, an output space $\mathcal Y$ and an unknown probability distribution $P$ on $\mathcal X \times \mathcal Y$.
2. A [[loss function|3BTG6VVCGZ]] $L \colon \mathcal Y \times \mathcal Y \to [0, \infty)$ measures the cost $L(f(x), y)$ of predicting $f(x)$ when the truth is $y$.
3. The *risk* of a measurable function $f \colon \mathcal X \to \mathcal Y$ is $R(f) = E[L(f(X), Y)]$, where $(X, Y)$ has law $P$.
4. A learning algorithm maps a sample $(X_1, Y_1), \dots, (X_n, Y_n)$ of [[independent and identically distributed|00MRN0FARV]] pairs with law $P$ to a function $\hat f_n$.
   Usually $\hat f_n$ lies in a fixed class $\mathcal F$.

Its questions are how fast $R(\hat f_n)$ approaches $\inf_{f \in \mathcal F} R(f)$ or the best possible risk, uniformly over the distributions $P$ in some class.

## Remarks

A central tool is the uniform deviation $\sup_{f \in \mathcal F} \abs{R_n(f) - R(f)}$, where $R_n(f) = \frac1n \sum_{i=1}^{n} L(f(X_i), Y_i)$ is the empirical risk; it controls [[empirical risk minimization|56NVR0SS61]].
For binary classification with the $0$-$1$ loss, this deviation tends to $0$ uniformly over all $P$ if and only if $\mathcal F$ has finite [[VC dimension|KCFXR9K3GD]].

Example: binary classification with $\mathcal Y = \set{0, 1}$, the $0$-$1$ loss $L(a, y) = \mathbf{1}\set{a \ne y}$ and $\mathcal F$ the half-planes in $\mathcal X = \R^2$ fits the setting; then $R(f)$ is the probability of a misclassification.

Non-example: clustering points with no labels does not fit clauses 2 and 3 as stated, since there is no output to predict.
It belongs to unsupervised learning.
