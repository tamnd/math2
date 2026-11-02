---
tag: XBPKCBX4EW
kind: definition
name: J-homomorphism
msc: [55Q50]
defines: YYJPRD1HYW
uses: [P976WYEFMB, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/J-homomorphism
---

## Definition

Let $r, n \ge 1$, and let $SO(n)$ be the [[special orthogonal group|0CGYNDCWRR]].
Write $S^{r+n} = \partial(D^{r+1} \times D^n) = (S^r \times D^n) \cup (D^{r+1} \times S^{n-1})$, and $S^n = D^n / \partial D^n$ with base point the image of $\partial D^n$.
For a map $f \colon S^r \to SO(n)$, define $J(f) \colon S^{r+n} \to S^n$ as follows:

1. on $S^r \times D^n$, set $J(f)(x, v) = [f(x) v]$, the class of $f(x) v \in D^n$;
2. on $D^{r+1} \times S^{n-1}$, let $J(f)$ be constant at the base point.

The *J-homomorphism* is the map $J \colon \pi_r(SO(n)) \to \pi_{r+n}(S^n)$, $[f] \mapsto [J(f)]$, on [[homotopy groups|P976WYEFMB]].

## Remarks

The two clauses agree on $S^r \times S^{n-1}$, since $f(x)$ preserves the unit sphere, so $f(x) v \in \partial D^n$.
The map $J$ is a well-defined group homomorphism.

Example: for $n = 2$ and $r = 1$, let $f \colon S^1 \to SO(2)$ send $z$ to rotation by $z$, viewing $\R^2$ as $\C$.
Then $J(f) \colon S^3 \to S^2$ is the Hopf map, up to sign and homotopy, and it generates $\pi_3(S^2) \cong \Z$.

Non-example: suppose $f(x)$ is allowed to be any invertible linear map.
Then $f(x) v$ need not lie on $\partial D^n$ for $v \in S^{n-1}$, and may even leave $D^n$, so the two clauses do not define a map.

The maps $J$ commute with the stabilisation maps $SO(n) \to SO(n+1)$ and with suspension, so they give the stable J-homomorphism $J \colon \pi_r(SO) \to \pi_r^s$.
