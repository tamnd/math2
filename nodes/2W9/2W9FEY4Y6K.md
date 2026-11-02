---
tag: 2W9FEY4Y6K
kind: definition
name: Mathematical statistics
msc: [62A01]
defines: XZSA2NCATS
uses: [JZ6R7J36K5, FXCQWFY5RV, 036756NFD6, 0RWE7CPJ32]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_statistics
---

## Definition

Mathematical statistics is the study of [[statistical inference|FXCQWFY5RV]] with the methods of [[probability theory|0RWE7CPJ32]].
Its setting is a [[statistical model|JZ6R7J36K5]] $(S, \mathcal{P})$.
The data $x \in S$ are a value of a random element $X$ whose law $P$ is an unknown member of $\mathcal{P}$.
Its objects are [[statistics|036756NFD6]] $T = g(X)$ and the procedures built from them.
It judges each procedure by the laws that the procedure has under the members of $\mathcal{P}$.

## Remarks

Example: in the model of $n$ independent $\mathcal{N}(\mu, 1)$ observations with $\mu \in \R$, the sample mean $\bar{X}_n$ has law $\mathcal{N}(\mu, 1/n)$ for every $\mu$.
This law shows that $\bar{X}_n$ is unbiased for $\mu$ with variance $1/n$, a typical result of mathematical statistics.
Non-example: drawing a bar chart of one data set is descriptive statistics; it uses no model $\mathcal{P}$ and makes no claim about other possible data.
The main branches are point estimation, hypothesis testing, confidence sets and decision theory, each in a parametric or a nonparametric form.
