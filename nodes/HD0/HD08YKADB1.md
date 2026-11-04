---
tag: HD08YKADB1
kind: proof
name: Proof that a function with bounded derivative is Lipschitz
msc: [26A16]
proves: 0P64VE79X3
uses: [0BARQY52N5, 0QNVQ4VD9T, 0TK8Y3J5RW]
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_continuity
---

## Proof

We bound each difference quotient with the mean value theorem.

1. Let $x, y \in I$. We must show $|f(x) - f(y)| \le K |x - y|$.
2. If $x = y$, both sides are $0$. The inequality is symmetric in $x$ and $y$, so we may assume $x < y$.
3. Since $I$ is an [[interval|0TK8Y3J5RW]], every $z$ with $x \le z \le y$ lies in $I$. So $[x, y] \subseteq I$.
4. Each $z \in (x, y)$ is an interior point of $I$, because the open interval $(x, y)$ contains $z$ and lies in $I$.
5. So $f$ is differentiable on $(x, y)$, with $|f'(z)| \le K$ there. Also $f$ is continuous on $[x, y]$.
6. By the [[mean value theorem|0BARQY52N5]], there is $c \in (x, y)$ with $f(y) - f(x) = f'(c)(y - x)$.
7. Taking absolute values, $|f(y) - f(x)| = |f'(c)| \, |y - x| \le K |y - x|$, by step 5.
8. This holds for all $x, y \in I$, so $f$ is [[Lipschitz with constant $K$|0QNVQ4VD9T]].

## Idea

The mean value theorem says each chord slope of $f$ equals a value of $f'$. If every value of $f'$ has size at most $K$, every chord slope does too. That is exactly the Lipschitz condition.
