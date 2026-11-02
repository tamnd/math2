---
tag: Q3X1CNXASD
kind: statement
role: theorem
name: Peetre theorem on local operators
msc: [58J99, 47F05]
uses: [F45VQ47GPV, P4DZM975BV, WWX7H5W1RP, CGBX1N9V8H]
about: [CGBX1N9V8H]
sources:
  - url: https://en.wikipedia.org/wiki/Peetre_theorem
same_as:
  wikidata: Q7160489
  wikipedia: Peetre theorem
---

## Statement

Let $M$ be a [[smooth manifold|F45VQ47GPV]] and let $E$ and $F$ be smooth real [[vector bundles|P4DZM975BV]] over $M$.
Let $\Gamma(E)$ and $\Gamma(F)$ be their spaces of smooth [[sections|WWX7H5W1RP]].
Let $D \colon \Gamma(E) \to \Gamma(F)$ be an $\R$-linear map that is local, that is,
$$\operatorname{supp}(Ds) \subseteq \operatorname{supp}(s) \quad \text{for all } s \in \Gamma(E).$$
Then every point $p \in M$ has an open neighbourhood $U$ with an integer $k \ge 0$ such that the following holds.
Over $U$, $D$ is a [[linear differential operator|CGBX1N9V8H]] of order at most $k$ with smooth coefficients.
In local coordinates and trivialisations over $U$, this means $(Ds)|_U = \sum_{\abs{\alpha} \le k} a_\alpha \, \partial^\alpha (s|_U)$ for every $s \in \Gamma(E)$, with smooth matrix-valued functions $a_\alpha$.

## Remarks

No continuity of $D$ is assumed; it is a consequence.
The idea of the proof is to show first that, near each point, $(Ds)(x)$ depends only on the $k$-jet of $s$ at $x$ for one fixed $k$.
If this failed, one could build sections with small disjoint supports accumulating at a point and add them up, and locality would force a contradiction.
Linearity then shows that $D$ is given by a linear map on $k$-jets, which is exactly a differential operator of order $k$.

Example: the exterior derivative $d \colon \Omega^j(M) \to \Omega^{j+1}(M)$ is local, and it is indeed a differential operator of order $1$.

Locality is needed.
On $M = \R$ the operator $(Df)(x) = \int_0^x f(t)\, dt$ is linear but not local, and it is not a differential operator.

The order need not be bounded on all of $M$ when $M$ is not compact.
On $\R$, let $\varphi_n$ be a smooth function with support in $(n, n + 1)$ and $\varphi_n \ne 0$.
Then $Df = \sum_{n \ge 1} \varphi_n f^{(n)}$ is a locally finite sum, so it is a local linear operator, but its order is unbounded.
If $M$ is compact, finitely many sets $U$ cover $M$, so $D$ is a differential operator of finite order.

## Explanations

### L1 human

A linear operator on functions is local if the output near a point depends only on the input near that point.
Derivatives have this property, integrals do not.
Peetre's theorem says that derivatives are the only examples: a linear local operator is a differential operator, at least near each point.

### L2 human

The theorem gives an algebraic characterisation of differential operators by their support property.
It is used to show that natural operators in differential geometry, such as those that commute with diffeomorphisms, are differential operators of finite order.
Together with invariance arguments, it leads to classification results for natural operators on bundles of tensors.
It also explains why locality is the key property of the exterior derivative, the Lie derivative and covariant derivatives.
