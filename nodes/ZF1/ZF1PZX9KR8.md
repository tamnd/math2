---
tag: ZF1PZX9KR8
kind: example
name: Haar measure on the circle
msc: [43A05, 28C10, 43A70]
instance_of: [VY0HXD3GC4]
uses: [04EAFVFTF7, 9T4PJJ60JE, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Example

Let $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$ be the [[circle group|04EAFVFTF7]] with complex multiplication.
Let $p \colon [0, 2\pi) \to \mathbb{T}$, $p(\theta) = e^{i\theta}$, which is a bijection.
For a Borel set $A \subseteq \mathbb{T}$ put
$$\mu(A) = \frac{1}{2\pi} \lambda\left(p^{-1}(A)\right),$$
where $\lambda$ is [[Lebesgue measure|2Z2QVWZ262]].
In integral form, $\int_{\mathbb{T}} f \, d\mu = \frac{1}{2\pi} \int_0^{2\pi} f(e^{i\theta}) \, d\theta$.

Check that $\mu$ is a Haar measure.
It is a finite Borel measure on a compact metric space, hence a Radon measure, and $\mu(\mathbb{T}) = 1$, so it is nonzero.
For $g = e^{i\alpha}$, multiplication by $g$ corresponds to $\theta \mapsto \theta + \alpha \bmod 2\pi$ on $[0, 2\pi)$.
This map cuts $[0, 2\pi)$ into two intervals and translates each of them, so it preserves Lebesgue measure.
Hence $\mu(gA) = \mu(A)$ for every $g \in \mathbb{T}$ and every Borel set $A$.

Since $\mu(\mathbb{T}) = 1$, it is the [[normalized Haar measure|9T4PJJ60JE]] of $\mathbb{T}$.
Every other Haar measure of $\mathbb{T}$ is $c\mu$ for some $c > 0$, for instance arc length $2\pi\mu$.
An arc of angle $\beta$ with $0 \le \beta \le 2\pi$ has measure $\beta / (2\pi)$.

## Explanations

### L1 human

The fair way to measure pieces of a circle is by their arc length, as a fraction of the full turn.
Rotating the circle moves arcs around but never stretches them, so this measure is invariant under the group.
A half circle has measure $1/2$ and a quarter circle has measure $1/4$, wherever they sit.
This is the measure behind the coefficients of Fourier series, which are averages over the circle.
