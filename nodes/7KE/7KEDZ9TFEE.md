---
tag: 7KEDZ9TFEE
kind: statement
role: theorem
name: Wu's formula
msc: [57R20, 55S10]
uses: [JQCK7A210W, VR7RHP41M0, F45VQ47GPV, ZEA0PEM3B2, JX47MS1R1H]
about: [JQCK7A210W, VR7RHP41M0]
sources:
  - url: https://en.wikipedia.org/wiki/Stiefel%E2%80%93Whitney_class
---

## Statement

Let $M$ be a closed [[smooth manifold|F45VQ47GPV]] of dimension $n$, and let $[M] \in H_n(M; \Z/2\Z)$ be its mod $2$ [[fundamental class|ZEA0PEM3B2]].
For each $k \ge 0$, let $v_k \in H^k(M; \Z/2\Z)$ be the unique class such that
$$\langle v_k \smile x, [M] \rangle = \langle \operatorname{Sq}^k x, [M] \rangle \quad \text{for all } x \in H^{n-k}(M; \Z/2\Z),$$
where $\operatorname{Sq}^k$ is the $k$-th [[Steenrod square|VR7RHP41M0]] and $\smile$ is the [[cup product|JX47MS1R1H]].
Let $v = 1 + v_1 + v_2 + \cdots$ be the total Wu class.
Then the total [[Stiefel–Whitney class|JQCK7A210W]] of the tangent bundle of $M$ is
$$w(M) = \operatorname{Sq}(v), \quad \text{that is,} \quad w_k(M) = \sum_{i=0}^{k} \operatorname{Sq}^{i}(v_{k-i}).$$

## Remarks

The classes $v_k$ exist and are unique by Poincaré duality with $\Z/2\Z$ coefficients.
The proof uses the Thom class of the tangent bundle of $M$, viewed as the normal bundle of the diagonal in $M \times M$.
Steenrod squares of a Thom class give the Stiefel–Whitney classes of the bundle.

Example: for $M = \R P^2$, $H^*(M; \Z/2\Z) = (\Z/2\Z)[a]/(a^3)$.
Since $\operatorname{Sq}^1 a = a^2$, one gets $v_1 = a$, and $v_2 = 0$ because $\operatorname{Sq}^2$ vanishes on $H^0$.
So $w(\R P^2) = \operatorname{Sq}(1 + a) = 1 + a + a^2$, which agrees with $(1 + a)^3$.

Since $\operatorname{Sq}^k x = 0$ for $\deg x < k$, the class $v_k$ is $0$ for $k > n/2$.

## Explanations

### L1 human

Stiefel–Whitney classes are defined from the tangent bundle, which uses the smooth structure of the manifold.
Wu's formula computes them from the mod $2$ cohomology ring and its Steenrod squares alone.
So these classes depend only on the homotopy type of the manifold.

### L2 human

The formula has two steps: Poincaré duality turns the Steenrod squares into the Wu classes $v_k$, and then $w = \operatorname{Sq}(v)$.
It implies that Stiefel–Whitney numbers are homotopy invariants of closed manifolds, which is relevant for [[Thom's cobordism theorem|HM23BV561Z]] since these numbers decide unoriented cobordism.
For example, $w_1(M) = v_1$, so $M$ is orientable exactly when $\operatorname{Sq}^1 \colon H^{n-1}(M; \Z/2\Z) \to H^n(M; \Z/2\Z)$ is zero.
