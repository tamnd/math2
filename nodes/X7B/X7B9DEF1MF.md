---
tag: X7B9DEF1MF
kind: definition
name: Multiplier ideal
msc: [14F18, 32U05, 32U25]
defines: BKM0TQSCD9
uses: [FF2P7ER3QT, JSGWAN2RJV, 7PJ8KVZZCQ, N3PGYJJQ7W]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplier_ideal
---

## Definition

Let $X$ be a complex manifold.
Let $\varphi$ be a [[plurisubharmonic function|FF2P7ER3QT]] on $X$, or more generally a function that is locally a plurisubharmonic function plus a smooth function.
The *multiplier ideal sheaf* $\mathcal{I}(\varphi) \subseteq \mathcal{O}_X$ is the subsheaf of $\mathcal{O}_X$ defined as follows.
Its stalk at $x \in X$ is the set of [[germs|7PJ8KVZZCQ]] $f \in \mathcal{O}_{X,x}$ that satisfy the following condition.
There is a coordinate neighbourhood $U$ of $x$ with $\int_U \abs{f}^2 e^{-2\varphi} \, dV < \infty$, where $dV$ is Lebesgue measure in the coordinates of $U$.

## Remarks

The condition does not depend on the coordinates, since a change of coordinates multiplies $dV$ by a smooth positive function.
The stalks are ideals, so $\mathcal{I}(\varphi)$ is an [[ideal sheaf|N3PGYJJQ7W]]; Nadel's theorem says it is coherent.
Example: $X = \C$, $\varphi = c \log\abs{z}$ with $c > 0$.
In polar coordinates, $\int_{\abs{z} < r} \abs{z}^{2k} \abs{z}^{-2c} \, dV = 2\pi \int_0^r t^{2k - 2c + 1} \, dt$, which is finite exactly when $k > c - 1$.
So the stalk at $0$ is $(z^{\floor{c}})$; for example $\mathcal{I}(\log\abs{z})_0 = (z)$.
Non-example: for $\varphi = \log\abs{z}$, the germ $f = 1$ is not in the stalk at $0$, since $\int \abs{z}^{-2} \, dV$ diverges near $0$.
If $\varphi$ is locally bounded, then $\mathcal{I}(\varphi) = \mathcal{O}_X$.
Algebraic form: for an ideal $\mathfrak{a} = (g_1, \dots, g_k)$ and a real $c > 0$, $\mathcal{J}(c \cdot \mathfrak{a}) = \mathcal{I}\left(\tfrac{c}{2} \log \sum_i \abs{g_i}^2\right)$, the germs with $\abs{f}^2 / (\sum_i \abs{g_i}^2)^c$ locally integrable.
Some authors use the weight $e^{-\varphi}$ instead of $e^{-2\varphi}$.
