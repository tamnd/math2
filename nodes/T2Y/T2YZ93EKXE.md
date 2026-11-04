---
tag: T2YZ93EKXE
kind: proof
name: Proof of the second derivative test in several variables
msc: ["49K10"]
proves: 0GYDV9FE98
uses: [0P30YYZN85, 0SCSQWXRA4, 0NNQY8WCW6, 01RBSSGMY5, 04CPG9K1C4, 00N3T18QNA, 0B5H4208Z9, 07PFYV65MB, 0V4DET59NW, 0TCBZMEYGN]
sources:
  - url: https://academicweb.nd.edu/~jdiller/teaching/archive/fall15_20850/secondderivativetest.pdf
---

## Proof

We compare $f$ near $a$ with its second-order Taylor polynomial.

1. Let $U$, $f$, $a$ and the [[Hessian matrix|0SCSQWXRA4]] $H = H_f(a)$ be as in the statement. Since $f$ is of [[class C^2|0TCBZMEYGN]], [[Schwarz's theorem|0NNQY8WCW6]] shows that $H$ is symmetric. Its quadratic form $Q(h) = h^{\mathsf{T}} H h$ is as in [[the definition of definite forms|01RBSSGMY5]].
2. Since $\nabla f(a) = 0$, the [[second-order Taylor expansion|0P30YYZN85]] gives $f(a + h) - f(a) = \tfrac{1}{2} Q(h) + R(h)$ for $a + h \in U$, with $R(h) / \norm{h}^2 \to 0$ as $h \to 0$.
3. Part 1. Assume that $H$ is positive definite. Let $S = \set{h \in \R^n : \norm{h} = 1}$ be the unit sphere. It is closed and bounded, so it is compact by the [[Heine–Borel theorem|07PFYV65MB]].
4. The function $Q$ is a polynomial in the coordinates of $h$, so it is continuous. By the [[extreme value theorem|0V4DET59NW]], there is $h_0 \in S$ with $Q(h) \ge Q(h_0)$ for all $h \in S$. Let $m = Q(h_0)$. Then $m > 0$, since $h_0 \ne 0$ and $Q$ is positive definite.
5. For $h \ne 0$, the vector $h / \norm{h}$ lies in $S$, and $Q(h) = \norm{h}^2 Q(h / \norm{h})$. So $Q(h) \ge m \norm{h}^2$ for every $h \in \R^n$.
6. By step 2, there is $\delta > 0$ such that $a + h \in U$ and $\abs{R(h)} < \tfrac{m}{4} \norm{h}^2$ whenever $0 < \norm{h} < \delta$.
7. For such $h$, steps 2, 5 and 6 give $f(a + h) - f(a) \ge \tfrac{m}{2} \norm{h}^2 - \tfrac{m}{4} \norm{h}^2 = \tfrac{m}{4} \norm{h}^2 > 0$.
8. So $f(x) > f(a)$ for all $x \in U$ with $0 < \norm{x - a} < \delta$. This means that $f$ has a strict [[local minimum|04CPG9K1C4]] at $a$.
9. Part 2. Assume that $H$ is negative definite. The function $-f$ is of class $C^2$, has gradient $0$ at $a$, and has Hessian $-H$, which is positive definite.
10. By Part 1, $-f$ has a strict local minimum at $a$. So $f$ has a strict local maximum at $a$.
11. Part 3. Let $\lambda > 0$ and $\mu < 0$ be eigenvalues of $H$. The real matrices $H - \lambda I$ and $H - \mu I$ are singular. So there are real [[eigenvectors|0B5H4208Z9]] $v, w \in \R^n$ with $H v = \lambda v$ and $H w = \mu w$. Then $Q(v) = \lambda \norm{v}^2 > 0$ and $Q(w) = \mu \norm{w}^2 < 0$.
12. For real $t \ne 0$ small enough that $a + t v \in U$, step 2 gives $\frac{f(a + t v) - f(a)}{t^2 \norm{v}^2} = \frac{\lambda}{2} + \frac{R(t v)}{\norm{t v}^2}$.
13. As $t \to 0$, the right side tends to $\lambda / 2 > 0$. So there is $\eta > 0$ with $f(a + t v) > f(a)$ for $0 < \abs{t} < \eta$.
14. In the same way, using $w$ and $\mu < 0$, there is $\eta' > 0$ with $f(a + t w) < f(a)$ for $0 < \abs{t} < \eta'$.
15. Let $\varepsilon > 0$. By steps 13 and 14, the ball of radius $\varepsilon$ around $a$ contains a point $x \in U$ with $f(x) > f(a)$. It also contains a point $y \in U$ with $f(y) < f(a)$.
16. So $a$ is neither a local maximum nor a local minimum of $f$. Since $\nabla f(a) = 0$, the point $a$ is a [[saddle point|00N3T18QNA]] of $f$.

## Idea

At a critical point the linear term of the Taylor expansion is zero, so $f(a + h) - f(a)$ is $\tfrac{1}{2} h^{\mathsf{T}} H h$ plus a remainder that is small compared to $\norm{h}^2$. A positive definite form is at least $m \norm{h}^2$, by compactness of the sphere, so it wins against the remainder. For an indefinite Hessian, moving along eigenvectors makes $f$ go up in one direction and down in another.
