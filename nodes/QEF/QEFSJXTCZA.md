---
tag: QEFSJXTCZA
kind: definition
name: Lommel function
msc: [33C10]
defines: YJ1JWF6ZDG
uses: [CZCMRDWDYW]
sources:
  - url: https://en.wikipedia.org/wiki/Lommel_function
---

## Definition

Let $\mu, \nu \in \C$ be such that neither $\mu + \nu$ nor $\mu - \nu$ is a negative odd integer, and let $z \in \C \setminus (-\infty, 0]$ with the principal branch of powers.
The *Lommel function* $s_{\mu,\nu}$ is
$$s_{\mu,\nu}(z) = \sum_{k=0}^{\infty} \frac{(-1)^k\, z^{\mu + 1 + 2k}}{\prod_{j=0}^{k} \left( (\mu + 2j + 1)^2 - \nu^2 \right)}.$$

## Remarks

The hypothesis on $\mu \pm \nu$ says exactly that no factor $(\mu + 2j + 1)^2 - \nu^2$ vanishes.
The function $s_{\mu,\nu}$ is a particular solution of
$$z^2 w'' + z w' + (z^2 - \nu^2)\, w = z^{\mu + 1}.$$
Check: the operator $w \mapsto z^2 w'' + z w' - \nu^2 w$ multiplies $z^p$ by $p^2 - \nu^2$, and $z^2 w$ shifts each term up by two powers.
So the coefficients $c_k$ of $z^{\mu + 1 + 2k}$ must satisfy $\left( (\mu + 1)^2 - \nu^2 \right) c_0 = 1$ and $\left( (\mu + 2k + 1)^2 - \nu^2 \right) c_k = -c_{k-1}$, which the series does.
Example: for $\mu = 1$ and $\nu = 0$ the first factor is $4$, so $s_{1,0}$ starts with $\frac{z^2}{4}$.
In fact $s_{1,0}$ is $1 - J_0(z)$, where $J_0$ is the [[Bessel function of the first kind|CZCMRDWDYW]].
A non-example: for $\mu = -2$ and $\nu = 1$ one has $\mu + \nu = -1$, so the factor with $j = 0$ is $(-2 + 1)^2 - 1 = 0$ and $s_{-2,1}$ is not defined by the series.
The second Lommel function $S_{\mu,\nu}$ is obtained from $s_{\mu,\nu}$ by adding a suitable combination of $J_\nu$ and $Y_\nu$ so that it has a simple asymptotic expansion at infinity.
