---
tag: 0NB31CC4SN
kind: example
name: exp(1/z) has an essential singularity at 0
aliases: [exponential-of-one-over-z]
msc: [30D30]
instance_of: [0B8837S5T3]
uses: [054VXHMCA3, 0YKDJBV26S, 0X3XD2ATB0]
sources:
  - url: https://en.wikipedia.org/wiki/Essential_singularity
    locator: Formal description
  - url: https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem
    locator: Examples
---

## Example

Let $f(z) = e^{1/z}$ for $z \in \mathbb{C} \setminus \{0\}$, where $e^w$ is the [[complex exponential|054VXHMCA3]].
The function $f$ is holomorphic on $\mathbb{C} \setminus \{0\}$, so $0$ is an isolated singularity of $f$.
Its [[Laurent series|0X3XD2ATB0]] at $0$ is
$$e^{1/z} = \sum_{n=0}^{\infty} \frac{1}{n!} z^{-n} = 1 + \frac{1}{z} + \frac{1}{2! \, z^2} + \cdots \qquad (z \neq 0).$$
It has infinitely many nonzero terms with negative powers, so $0$ is an [[essential singularity|0YKDJBV26S]] of $f$.

## Remarks

A direct check: for real $x \to 0^+$, $e^{1/x} \to \infty$, and for real $x \to 0^-$, $e^{1/x} \to 0$. So $f$ has no limit at $0$ and $|f|$ does not tend to $\infty$.
In each punctured disc $0 < |z| < \delta$, $f$ takes each value $w \neq 0$ infinitely often: the solutions of $e^{1/z} = w$ are $z = 1 / (\operatorname{Log} w + 2\pi i k)$ with $k \in \mathbb{Z}$ and $\operatorname{Log} w + 2\pi i k \neq 0$, and these points tend to $0$ as $|k| \to \infty$.
The value $0$ is never taken. This agrees with [[Picard's great theorem|08QA8QTM71]], which allows one exception.
The residue of $f$ at $0$ is the coefficient of $z^{-1}$, which is $1$.

## Explanations

### L1 human

Near $0$, the number $1/z$ is huge and can point in any direction, so $e^{1/z}$ can be huge, tiny, or anything in between.
That is why no single value or infinity describes $e^{1/z}$ near $0$.
