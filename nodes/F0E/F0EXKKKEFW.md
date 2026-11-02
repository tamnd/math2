---
tag: F0EXKKKEFW
kind: statement
role: theorem
name: Straszewicz's theorem
msc: [52A20]
uses: [0XPR1E85W0, 02AS45T3H9, 0R6EWFKRCF, 3MSGFJM2NX, VN4M72SQW5, 0QEAJB91GZ, 0FQSDC2EQ2, NT4SKSYKG9]
about: [VN4M72SQW5, 3MSGFJM2NX]
sources:
  - url: https://en.wikipedia.org/wiki/Exposed_point
---

## Statement

Let $n \ge 1$ and let $K \subseteq \R^n$ be a [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]].
Then every [[extreme point|3MSGFJM2NX]] of $K$ is a limit of [[exposed points|VN4M72SQW5]] of $K$.
That is, the set of extreme points of $K$ lies in the [[closure|0QEAJB91GZ]] of the set of exposed points of $K$.

## Remarks

Proof idea: for a point $z \in \R^n$, a point $p$ of $K$ farthest from $z$ is exposed.
Indeed, the sphere around $z$ through $p$ encloses $K$, and its tangent hyperplane at $p$ meets $K$ only in $p$.
One then shows that every extreme point can be approached by such farthest points, by choosing $z$ suitably far away in suitable directions.

Combined with the [[Minkowski–Carathéodory theorem|NT4SKSYKG9]], it follows that $K$ is the [[convex hull|0FQSDC2EQ2]] of the closure of its exposed points.

Example: let $K$ be the stadium, the convex hull of the discs of radius $1$ centred at $(-1, 0)$ and $(1, 0)$.
The four points $(\pm 1, \pm 1)$ are extreme but not exposed.
Each of them is a limit of points on the round ends, and those points are exposed.

## Explanations

### L1 human

Extreme points are corners in a broad sense, and exposed points are corners that a flat wall can touch alone.
Some corners are not exposed, such as the points where the straight sides of a stadium meet its round ends.
The theorem says these exceptions are rare: each extreme point is a limit of exposed points.

### L2 human

The theorem lets one replace extreme points by exposed points in many arguments, at the cost of a closure.
Exposed points are often easier to handle, since each comes with a linear function maximised exactly there.
It is used in the study of faces of convex bodies and in convex analysis, where exposed points correspond to directions in which the support function is differentiable.
