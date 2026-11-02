---
tag: XY81HRY5HP
kind: statement
role: theorem
name: Bôcher's theorem
msc: [31B05]
uses: [0DEB0JMN0W, BSJ8X2XRN9, 3H6SQA6JWM]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%B4cher%27s_theorem
same_as:
  wikidata: Q5005143
  wikipedia: Bôcher's theorem
---

## Statement

Let $n \ge 2$, let $r > 0$, and let $u$ be a positive [[harmonic function|0DEB0JMN0W]] on the punctured ball $B(0, r) \setminus \set{0}$ in $\R^n$.
Then there are a constant $b \ge 0$ and a harmonic function $v$ on the whole ball $B(0, r)$ such that, for $0 < \abs{x} < r$,
$$u(x) = v(x) + b \log \frac{1}{\abs{x}} \quad (n = 2), \qquad u(x) = v(x) + \frac{b}{\abs{x}^{n-2}} \quad (n \ge 3).$$

## Remarks

So an isolated singularity of a positive harmonic function is a nonnegative multiple of the [[fundamental solution of the Laplacian|BSJ8X2XRN9]], up to a harmonic term.
If $b = 0$, the singularity is removable, in agreement with the [[removable singularity theorem|3H6SQA6JWM]].
Proof idea: averaging $u$ over the spheres about $0$ gives a radial harmonic function on the punctured ball.
It has the form $a + b\abs{x}^{2-n}$, or $a + b \log(1/\abs{x})$ in the plane.
Positivity of $u$ is then used to show that $b \ge 0$ and that the difference of $u$ and the singular term has a removable singularity at $0$.
Positivity is needed: $u(x) = x_1 / \abs{x}^n$ is harmonic on $\R^n \setminus \set{0}$, takes both signs, and is not of the stated form, since it grows like $\abs{x}^{1-n}$ near $0$.
Example: $u(x) = 1 + \abs{x}^{2-n}$ is positive on the punctured unit ball for $n \ge 3$, with $v = 1$ and $b = 1$.

## Explanations

### L1 human

A positive harmonic function can only blow up at an isolated point in one way: like the potential of a point charge.
Every other part of it is a perfectly regular harmonic function.
So positivity forbids wild singularities such as dipoles, which take both large positive and large negative values.

### L2 human

The theorem classifies isolated singularities of positive harmonic functions, and it is the local form of the Riesz decomposition of positive superharmonic functions.
A global corollary: a positive harmonic function on $\R^n \setminus \set{0}$, $n \ge 3$, has the form $a + b\abs{x}^{2-n}$ with $a, b \ge 0$, by combining Bôcher's theorem with the Kelvin transform and Liouville's theorem.
It is also the model for the description of the Martin boundary at an isolated boundary point.
