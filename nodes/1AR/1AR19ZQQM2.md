---
tag: 1AR19ZQQM2
kind: definition
name: Riesz projector
msc: [47A10, 47A60]
defines: HNW4WRSEEX
uses: [BMKATJ802A, J5YNNKSB9P, 033DA1WE8Y, 0DG10TVYPN]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz_projector
---

## Definition

Let $X$ be a complex Banach space with identity map $I$, and let $T \colon X \to X$ be a bounded operator with [[spectrum|BMKATJ802A]] $\sigma(T)$ and [[resolvent|J5YNNKSB9P]] $R(\lambda, T) = (T - \lambda I)^{-1}$.
Assume that $\sigma(T) = \sigma_1 \cup \sigma_2$, where $\sigma_1$ and $\sigma_2$ are disjoint closed sets.
Let $\Gamma$ be a finite union of positively oriented closed rectifiable curves in $\C \setminus \sigma(T)$.
Assume that $\Gamma$ has winding number $1$ around each point of $\sigma_1$ and $0$ around each point of $\sigma_2$.
The *Riesz projector* of $T$ for $\sigma_1$ is the operator
$$P_{\sigma_1} = -\frac{1}{2\pi i} \oint_\Gamma R(\lambda, T) \, d\lambda = \frac{1}{2\pi i} \oint_\Gamma (\lambda I - T)^{-1} \, d\lambda.$$

## Remarks

The integral does not depend on the choice of $\Gamma$, by the Cauchy theorem for analytic operator-valued functions.
The operator $P = P_{\sigma_1}$ is a [[projection|033DA1WE8Y]], $P^2 = P$, and it commutes with $T$.
So $X = PX \oplus (I - P)X$ with both summands closed and invariant under $T$, and the restrictions of $T$ have spectra $\sigma_1$ and $\sigma_2$.

Example: let $T = \operatorname{diag}(1, 2)$ on $\C^2$ and $\sigma_1 = \set{1}$, with $\Gamma$ the circle $\abs{\lambda - 1} = \tfrac12$.
Then $(\lambda I - T)^{-1} = \operatorname{diag}(1/(\lambda - 1), 1/(\lambda - 2))$, and [[Cauchy's integral formula|0DG10TVYPN]] gives $P_{\sigma_1} = \operatorname{diag}(1, 0)$.

Non-example: for the right shift on $\ell^2$, the spectrum is the closed unit disc, which is connected.
A subset such as the closed disc of radius $\tfrac12$ is not separated from the rest of the spectrum, so it has no Riesz projector.
Only $\sigma_1 = \emptyset$ and $\sigma_1 = \sigma(T)$ are allowed, giving $0$ and $I$.
