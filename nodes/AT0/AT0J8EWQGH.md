---
tag: AT0J8EWQGH
kind: statement
role: theorem
name: Maxwell's counting rule for frameworks
msc: [52C25, 70C20, 74K10]
uses: [E5ZHQSHB97, V5YS9BZX0N, 0ZC9YTXZRY]
about: [E5ZHQSHB97, V5YS9BZX0N]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_rigidity
---

## Statement

Let $d \ge 1$ and let $(G, p)$ be a framework in $\R^d$ with $j$ joints and $b$ bars, whose joints affinely span $\R^d$.
Let $R$ be its rigidity matrix, the $b \times dj$ matrix with one row for each bar.
The row of the bar $uv$ has $p(u) - p(v)$ in the columns of $u$, $p(v) - p(u)$ in the columns of $v$, and zeros elsewhere.
Let $s = \dim \ker R^{T}$ be the number of independent states of self-stress.
Let $m = \dim \ker R - d(d+1)/2$ be the number of independent infinitesimal mechanisms, not counting the rigid motions of $\R^d$.
Then
$$s - m = b - d j + \frac{d(d+1)}{2}.$$
In particular, if the framework is infinitesimally rigid, then $b \ge d j - d(d+1)/2$; in the plane this reads $b \ge 2j - 3$ and in space $b \ge 3j - 6$.

## Remarks

The proof is the rank–nullity theorem applied twice.
If $r$ is the [[rank|0ZC9YTXZRY]] of $R$, then $\dim \ker R = dj - r$ and $\dim \ker R^{T} = b - r$.
The infinitesimal rigid motions of $\R^d$ form a space of dimension $d(d+1)/2$ in $\ker R$ because the joints span $\R^d$ affinely.
Subtracting the two equalities gives the formula.

Example: a triangle in the plane has $j = 3$, $b = 3$ and $b - 2j + 3 = 0$; it has no mechanism and no self-stress, so $s = m = 0$.
A square of four bars has $b - 2j + 3 = -1$, and indeed it has one mechanism, the shear into a rhombus.

The count is necessary but not sufficient for rigidity.
A framework can have enough bars and still have a mechanism if some part has more bars than it needs, which then gives a state of self-stress.
In the plane, the exact combinatorial condition for generic frameworks is given by [[Laman graphs|C81JPZ51NA]].

## Explanations

### L1 human

Each joint of a framework in the plane can move in two directions, and the whole framework can slide and turn in three ways.
Each bar removes at most one way of moving.
So a rigid plane framework with $j$ joints needs at least $2j - 3$ bars.
Calladine's form of the rule says that each missing bar leaves a way to move, and each extra bar leaves a way to be pre-stressed.

### L2 human

The rigidity matrix $R$ maps joint velocities to bar length rates, and its transpose $R^{T}$ maps bar forces to the joint forces they produce.
So $\ker R$ holds the infinitesimal motions and $\ker R^{T}$ holds the self-stresses, and the theorem links the [[statically indeterminate|SKVPKD5VZN]] degree of a [[truss|E5ZHQSHB97]] with its kinematic freedom.
A framework with $s = m = 0$ is statically and kinematically determinate, which is the isostatic case used in engineering design.
