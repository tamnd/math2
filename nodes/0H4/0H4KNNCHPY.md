---
tag: 0H4KNNCHPY
kind: definition
name: Fundamental system of solutions
aliases: [fundamental-set-of-solutions]
msc: [34A30]
defines: 0DS2QFYJHE
uses: [0EQZSAB9EC, 0GK68PZ6KH]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_differential_equation
    locator: Linear differential operator
inventory: [4NZM4AFMRV]
---

## Definition

Let $I$ be an open interval and let $a_0, \dots, a_{n-1} : I \to \mathbb{R}$ be continuous. Let $S$ be the vector space of solutions on $I$ of the [[homogeneous linear equation|0EQZSAB9EC]] $y^{(n)} + a_{n-1}(x) y^{(n-1)} + \dots + a_0(x) y = 0$.
A fundamental system of solutions of the equation is a basis $(y_1, \dots, y_n)$ of $S$.

## Remarks

Since $S$ has [[dimension n|0GK68PZ6KH]], a family of $n$ solutions is a fundamental system if and only if it is linearly independent. The [[Wronskian test|0MHE4B1QCQ]] checks this.
Each solution is then $c_1 y_1 + \dots + c_n y_n$ for unique constants $c_1, \dots, c_n$.
Example: $(\cos x, \sin x)$ is a fundamental system of $y'' + y = 0$ on $\mathbb{R}$.

## Explanations

### L1 human

A fundamental system is a set of building blocks.
Each solution of the homogeneous equation is a unique combination of these $n$ solutions.
