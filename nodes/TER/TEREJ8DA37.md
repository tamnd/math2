---
tag: TEREJ8DA37
kind: definition
name: Resolvent
msc: [47A10]
defines: J5YNNKSB9P
uses: [06GZ956657, 03TM135G0N, BMKATJ802A, CPAD5W1CGW, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Resolvent_formalism
---

## Definition

Let $X$ be a complex [[Banach space|06GZ956657]] with identity map $I$, and let $T \colon X \to X$ be a [[continuous linear map|03TM135G0N]] with [[spectrum|BMKATJ802A]] $\sigma(T)$.
The *resolvent set* of $T$ is $\rho(T) = \C \setminus \sigma(T)$.
The *resolvent* of $T$ is the function
$$R(\cdot, T) \colon \rho(T) \to \mathcal{B}(X), \qquad R(\lambda, T) = (T - \lambda I)^{-1},$$
where $\mathcal{B}(X)$ is the space of bounded operators on $X$ and the inverse is the [[bounded inverse|CPAD5W1CGW]].

## Remarks

Some authors use $(\lambda I - T)^{-1}$ instead, which changes the sign.
The resolvent set is open, and $R(\cdot, T)$ is a [[holomorphic function|0NAHXR1FRH]] with values in $\mathcal{B}(X)$.
It satisfies the *resolvent identity*
$$R(\lambda, T) - R(\mu, T) = (\lambda - \mu) R(\lambda, T) R(\mu, T) \qquad (\lambda, \mu \in \rho(T)),$$
and $\norm{R(\lambda, T)} \ge 1 / \operatorname{dist}(\lambda, \sigma(T))$.

Example: for $D(x_n) = (x_n / n)$ on $\ell^2$ and $\lambda \in \rho(D)$, $R(\lambda, D)$ is the diagonal operator with entries $1/(1/n - \lambda)$.

Non-example: $\lambda = 0$ is not in $\rho(D)$, since $D$ is not surjective.
Indeed $(1/n)$ is in $\ell^2$ but $(1)$ is not, so $(1/n)$ is not in the image of $D$.
Hence $R(0, D)$ is not defined.

The same definitions apply to closed operators, with $R(\lambda, T) \colon X \to D(T)$.
