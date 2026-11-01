---
tag: CCT8SQKHW4
kind: object
name: Levi-Civita field
msc: [12J15, 12J25]
instance_of: [0P3VCBDEE2]
sources:
  - url: https://en.wikipedia.org/wiki/Levi-Civita_field
same_as:
  wikidata: Q6535342
  wikipedia: Levi-Civita field
---

## Description

A function $a \colon \Q \to \R$ has *left-finite support* if for every $q \in \Q$ there are only finitely many $r < q$ with $a(r) \ne 0$.
The Levi-Civita field $\mathcal{R}$ is the set of such functions, written as formal sums $a = \sum_{q \in \Q} a(q)\, \varepsilon^q$.
Addition is termwise, and the product is $(ab)(q) = \sum_{r + s = q} a(r) b(s)$, a finite sum because both supports are left-finite.
For $a \ne 0$, let $q_0$ be the least $q$ with $a(q) \ne 0$; then $a > 0$ means $a(q_0) > 0$.
With these operations and this order, $\mathcal{R}$ is an [[ordered field|010JCV9J4E]] that contains $\R$ as the constant series.

## Remarks

Check that $\varepsilon = 1 \cdot \varepsilon^1$ is a positive infinitesimal: $\varepsilon > 0$ since its leading coefficient is $1$, and for each integer $n \ge 1$ the element $1/n - \varepsilon$ has leading term $\frac{1}{n} \varepsilon^0$, so it is positive.
Hence $\mathcal{R}$ is not [[Archimedean|0HQARMKEV5]], and $\varepsilon^{-1}$ is larger than every real number.
Since exponents are rational, $\varepsilon$ has roots of every order, for example $(\varepsilon^{1/2})^2 = \varepsilon$.
The field $\mathcal{R}$ is [[real closed|778KFSM09P]], and it is Cauchy complete for the topology of its order.
Adjoining a square root of $-1$ gives an algebraically closed field.

## Explanations

### L1 human

The Levi-Civita field adds to the real numbers an infinitely small positive number $\varepsilon$ and its rational powers.
Its elements are series in $\varepsilon$ such as $3 + 2\varepsilon^{1/2} - \varepsilon^{5}$, with at most finitely many terms below each power.
A number is positive when its biggest term, the one with the lowest power of $\varepsilon$, is positive.
Such fields are used to compute with infinitesimals exactly, for example in automatic differentiation.
