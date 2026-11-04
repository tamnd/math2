---
tag: VZ4VK2YVF8
kind: proof
name: Proof that a function with zero derivative on an open interval is constant
msc: [26A24]
proves: 003QDZ4T16
uses: [0BARQY52N5, 07ZMX4ANJS, 0TK8Y3J5RW]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
---

## Proof

We compare any two values of $f$ with the mean value theorem.

1. Let $x, y \in I$ with $x < y$.
2. Since $I$ is an [[interval|0TK8Y3J5RW]], every $z$ with $x \le z \le y$ lies in $I$. So $[x, y] \subseteq I$.
3. The function $f$ is differentiable at each point of $I$. So it is [[continuous|07ZMX4ANJS]] at each point of $I$, and in particular on $[x, y]$.
4. The open interval $(x, y)$ lies in $I$, so $f$ is differentiable on $(x, y)$, with derivative $0$ there.
5. By the [[mean value theorem|0BARQY52N5]], there is $c \in (x, y)$ with $f(y) - f(x) = f'(c)(y - x)$.
6. Since $f'(c) = 0$, we get $f(y) = f(x)$.
7. So $f$ takes the same value at any two points of $I$. Fix $x_0 \in I$. Then $f(x) = f(x_0)$ for all $x \in I$, so $f$ is constant on $I$.

## Idea

The mean value theorem writes the change $f(y) - f(x)$ as a derivative times $y - x$. If the derivative is zero everywhere, every such change is zero. The interval hypothesis puts the whole segment $[x, y]$ inside the domain.
