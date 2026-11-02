---
tag: 9XEXZSZSZ9
kind: definition
name: Holomorphic functional calculus
msc: [47A60, 46H30]
defines: YFKA3KVTGR
uses: [9KYWN94QDN, EH0CZ19RKP, J5YNNKSB9P, 0NAHXR1FRH, 06ZGPYTWK8]
sources:
  - url: https://en.wikipedia.org/wiki/Holomorphic_functional_calculus
---

## Definition

Let $A$ be a complex [[Banach algebra|9KYWN94QDN]] with unit $e$, and let $a \in A$ with [[spectrum|EH0CZ19RKP]] $\sigma(a)$.
Let $U \subseteq \C$ be an open set with $\sigma(a) \subseteq U$, and let $f \colon U \to \C$ be [[holomorphic|0NAHXR1FRH]].
Let $\Gamma$ be a finite union of closed piecewise smooth curves in $U \setminus \sigma(a)$.
Assume that the winding number of $\Gamma$ is $1$ around each point of $\sigma(a)$ and $0$ around each point of $\C \setminus U$.
The element $f(a) \in A$ is the [[contour integral|06ZGPYTWK8]]
$$f(a) = \frac{1}{2\pi i} \int_\Gamma f(\lambda) \, (\lambda e - a)^{-1} \, d\lambda .$$
The map $f \mapsto f(a)$, from the algebra of holomorphic functions on $U$ to $A$, is the *holomorphic functional calculus* of $a$.

## Remarks

The integrand is continuous, since $\lambda \mapsto (\lambda e - a)^{-1}$, the [[resolvent|J5YNNKSB9P]], is defined and holomorphic off $\sigma(a)$.
By Cauchy's theorem for $A$-valued holomorphic functions, $f(a)$ does not depend on the choice of $\Gamma$.
Example: for $f(\lambda) = \lambda^n$ and $\Gamma$ a large circle $\abs{\lambda} = R$ with $R > \norm{a}$, expand $(\lambda e - a)^{-1} = \sum_{k \ge 0} \lambda^{-k-1} a^k$; only the term $k = n$ survives the integral, so $f(a) = a^n$.
Non-example: $f(\lambda) = \bar\lambda$ is not holomorphic, so the definition does not apply; for non-normal operators there is no reasonable way to define $\bar a$ by this method.
The calculus is an algebra homomorphism, it is continuous for locally uniform convergence of $f$, and $\sigma(f(a)) = f(\sigma(a))$.
For a normal operator on a Hilbert space it agrees with the [[continuous functional calculus|JB7S6WPZ77]] on holomorphic functions.
When $f$ is $1$ near one closed and open part of $\sigma(a)$ and $0$ near the rest, $f(a)$ is the [[Riesz projector|1AR19ZQQM2]] of that part.
