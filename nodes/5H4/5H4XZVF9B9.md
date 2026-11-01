---
tag: 5H4XZVF9B9
kind: statement
role: theorem
name: Minkowski's second theorem
msc: [11H06]
uses: [WN9V7WSJKF, 02AS45T3H9, 0R6EWFKRCF, 0CRMGPAH83]
about: [WN9V7WSJKF]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski%27s_second_theorem
same_as:
  wikidata: Q6867853
  wikipedia: Minkowski's second theorem
---

## Statement

Let $n \ge 1$ and let $\Lambda \subset \R^n$ be a [[lattice|WN9V7WSJKF]] with covolume $\det \Lambda$.
Let $K \subset \R^n$ be a [[convex|02AS45T3H9]] [[compact|0R6EWFKRCF]] set with nonempty interior that is symmetric about the origin, that is, $-x \in K$ for all $x \in K$.
For $k = 1, \dots, n$, the $k$-th successive minimum $\lambda_k$ is the infimum of the real numbers $\lambda > 0$ such that $\lambda K$ contains $k$ [[linearly independent|0CRMGPAH83]] vectors of $\Lambda$.
Then $0 < \lambda_1 \le \lambda_2 \le \dots \le \lambda_n < \infty$ and
$$\frac{2^n}{n!} \det \Lambda \le \lambda_1 \lambda_2 \cdots \lambda_n \operatorname{vol}(K) \le 2^n \det \Lambda.$$

## Remarks

The lower bound is elementary: $K$ contains the cross-polytope spanned by $\pm v_i/\lambda_i$ for suitable independent lattice vectors $v_i$, and this cross-polytope has volume at least $2^n \det\Lambda / (n! \, \lambda_1 \cdots \lambda_n)$.
The upper bound is the deep part; Minkowski's proof compares $K$ with a body built from the successive minima and uses a packing argument.
Since $\lambda_1^n \le \lambda_1 \cdots \lambda_n$, the upper bound implies $\lambda_1^n \operatorname{vol}(K) \le 2^n \det \Lambda$; so if $\operatorname{vol}(K) \ge 2^n \det\Lambda$, then $\lambda_1 \le 1$ and $K$ contains a nonzero lattice point, which is [[Minkowski's theorem|0K387S2PKQ]].
Both bounds are sharp for $\Lambda = \Z^n$: for the cube $K = [-1, 1]^n$ all $\lambda_k = 1$ and $\operatorname{vol}(K) = 2^n$, and for the cross-polytope $\set{x : \abs{x_1} + \dots + \abs{x_n} \le 1}$ all $\lambda_k = 1$ and $\operatorname{vol}(K) = 2^n/n!$.

## Explanations

### L1 human

Blow up a symmetric convex body around the origin until it contains one lattice direction, then two independent ones, and so on.
The scaling factors needed are the successive minima.
The theorem says that their product, times the volume of the body, is about the volume of a lattice cell, up to factors that depend only on the dimension.

### L2 human

Minkowski's first theorem controls only the first minimum; the second theorem controls all of them at once.
This is what one needs to find a whole basis of short vectors.
It is used, for instance, in the reduction theory of quadratic forms and in bounds for units and ideals in number fields.
It is also the starting point of transference theorems that relate a lattice to its dual.
