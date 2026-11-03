---
tag: T968JGCJHC
kind: statement
role: lemma
name: Shephard's lemma
msc: [91B42, 91B38, 91B16]
uses: [GZZS4MTDG9, ZFX4T69SST, Y0M5J89V2Q, 09EGC6F8PT]
about: [ZFX4T69SST]
sources:
  - url: https://en.wikipedia.org/wiki/Shephard%27s_lemma
same_as:
  wikidata: Q1536466
  wikipedia: Shephard's lemma
---

## Statement

Let $u \colon \R^n_+ \to \R$ be a continuous [[utility function|GZZS4MTDG9]], and let $v$ be a value taken by $u$.
Let $p \in \R^n$ with $p_i > 0$ for all $i$ be a price vector.
The expenditure function is $e(p, v) = \min \set{p \cdot x : x \in \R^n_+, \ u(x) \ge v}$, the value of the [[expenditure minimization problem|Y0M5J89V2Q]].
Let $h(p, v)$ be a bundle at which this minimum is attained, a [[Hicksian demand|ZFX4T69SST]].
Suppose that $e(\cdot, v)$ is differentiable at $p$.
Then for every good $i$,
$$\frac{\partial e}{\partial p_i}(p, v) = h_i(p, v).$$
In particular, the Hicksian demand at $(p, v)$ is unique.

## Remarks

Fix $\bar p$ and a minimizer $\bar x = h(\bar p, v)$.
For every $p$, the bundle $\bar x$ is still feasible, so $e(p, v) \le p \cdot \bar x$, with equality at $p = \bar p$.
So the function $p \mapsto e(p, v) - p \cdot \bar x$ has a maximum at $\bar p$, and its [[partial derivatives|09EGC6F8PT]] vanish there, which gives the formula.
This is a case of the [[envelope theorem|WK7MKDWRFF]].
In the other direction, if $u$ is continuous, represents locally nonsatiated preferences and the Hicksian demand is single-valued, then $e$ is differentiable in $p$ and the formula holds.

Example: for $u(x_1, x_2) = \sqrt{x_1 x_2}$, the expenditure function is $e(p, v) = 2 v \sqrt{p_1 p_2}$.
Its derivative in $p_1$ is $v \sqrt{p_2 / p_1}$, which is the cheapest amount of good $1$ that gives utility $v$.

The same argument in producer theory gives the producer form of the lemma.
For a cost function $c(w, y) = \min \set{w \cdot x : f(x) \ge y}$, the derivative $\partial c / \partial w_i$ is the cost-minimizing demand for input $i$.

## Explanations

### L1 human

The expenditure function says how much money is needed to reach a given level of satisfaction at given prices.
Shephard's lemma says that if one price goes up a little, the extra money needed is the price change times the amount of that good one buys.
So the rate of change of the cost of living in one price is exactly the quantity bought of that good.
This lets one read the demand off the cost function by differentiating.

### L2 human

The lemma links the expenditure function with the Hicksian demand, just as [[Roy's identity|CQ2S96993V]] links the indirect utility function with the [[Marshallian demand|EQPEPJ7QQZ]].
Differentiating it once more shows that the matrix of price derivatives of Hicksian demand is the Hessian of $e$ in $p$.
Since $e$ is concave in $p$, this matrix is symmetric and negative semidefinite, which is the key input of the [[Slutsky equation|M9P17VGSSA]].
In producer theory it plays the same role for the cost function and conditional input demands.
