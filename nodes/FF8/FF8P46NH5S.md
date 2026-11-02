---
tag: FF8P46NH5S
kind: definition
name: Minimal harmonic function
msc: [31C35, 31B05]
defines: NA4BTZ6WRB
uses: [EYMQ82Z8XJ, 0DEB0JMN0W, 9ZBAX4ZPX0, TCYSWCTYYM]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_boundary
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a domain.
Let $h$ be a [[positive harmonic function|EYMQ82Z8XJ]] on $\Omega$.
The function $h$ is *minimal* if every [[harmonic function|0DEB0JMN0W]] $v$ on $\Omega$ with $0 \le v \le h$ equals $c h$ for a constant $c \in [0, 1]$.

## Remarks

Some authors also normalise $h(x_0) = 1$ at a fixed reference point $x_0$.
Example: on the unit disc $\mathbb{D}$, let $h(z) = \frac{1 - \abs{z}^2}{\abs{1 - z}^2}$, the [[Poisson kernel|TCYSWCTYYM]] with pole $1$.
If $0 \le v \le h$ is harmonic, the [[Herglotz representation theorem|9ZBAX4ZPX0]] writes $v$ and $h - v$ as Poisson integrals of positive measures $\mu$ and $\nu$ with $\mu + \nu = \delta_1$, the measure of $h$.
Then $\mu$ is a multiple of $\delta_1$, so $v$ is a multiple of $h$, and $h$ is minimal.
Non-example: $h = 1$ on the unit disc is not minimal.
The function $v(z) = \frac{1 + \operatorname{Re} z}{2}$ is harmonic with $0 \le v \le 1$ on $\mathbb{D}$, but it is not constant.
On $\R^n$ every positive harmonic function is constant, so $h = 1$ is minimal there.
The minimal functions with $h(x_0) = 1$ are the extreme points of the convex set of positive harmonic functions with value $1$ at $x_0$.
