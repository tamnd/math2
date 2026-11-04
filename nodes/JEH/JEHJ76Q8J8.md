---
tag: JEHJ76Q8J8
kind: proof
name: Proof of Schwarz's theorem for C^2 functions by the mean value theorem
msc: ["26B05"]
proves: 0NNQY8WCW6
uses: [0TCBZMEYGN, 02RSXVM1ZN, 05AXG3QRKR, 0BARQY52N5, 0S9EK5MQPE]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetry_of_second_derivatives
    locator: Schwarz's theorem
---

## Proof

We apply the mean value theorem twice to a double difference.

1. Let $U \subseteq \R^n$ be open, let $f \colon U \to \R$ be of [[class C^2|0TCBZMEYGN]], and let $a \in U$. Let $i, j \in \set{1, \dots, n}$.
2. If $i = j$, the two sides of the claim are the same [[second partial derivative|02RSXVM1ZN]], so there is nothing to prove. Assume $i \ne j$.
3. Write $\partial_l$ for the [[partial derivative|05AXG3QRKR]] in the direction $x_l$, and $e_l$ for the $l$-th standard basis vector. So $\frac{\partial^2 f}{\partial x_j \, \partial x_i} = \partial_j \partial_i f$.
4. Since $U$ is open, there is $r > 0$ such that the open ball of radius $2r$ around $a$ lies in $U$.
5. For real $s, t$ with $\abs{s} < r$ and $\abs{t} < r$, the point $a + \sigma e_i + \tau e_j$ lies in that ball whenever $\abs{\sigma} \le \abs{s}$ and $\abs{\tau} \le \abs{t}$. This holds because its distance to $a$ is at most $\abs{\sigma} + \abs{\tau} < 2r$.
6. For such $s, t$ define the double difference $\Delta(s, t) = f(a + s e_i + t e_j) - f(a + s e_i) - f(a + t e_j) + f(a)$.
7. Fix $s, t$ with $0 < \abs{s} < r$ and $0 < \abs{t} < r$. Define $u(\sigma) = f(a + \sigma e_i + t e_j) - f(a + \sigma e_i)$ for $\abs{\sigma} < r$. Then $\Delta(s, t) = u(s) - u(0)$.
8. The partial derivative $\partial_i f$ exists on $U$, so $u$ is differentiable on $(-r, r)$, with $u'(\sigma) = \partial_i f(a + \sigma e_i + t e_j) - \partial_i f(a + \sigma e_i)$. In particular $u$ is continuous there.
9. By the [[mean value theorem|0BARQY52N5]] on the interval between $0$ and $s$, there is $\sigma_1$ strictly between $0$ and $s$ with $\Delta(s, t) = s \, u'(\sigma_1)$.
10. Define $v(\tau) = \partial_i f(a + \sigma_1 e_i + \tau e_j)$ for $\abs{\tau} < r$. Then $u'(\sigma_1) = v(t) - v(0)$.
11. The function $\partial_j \partial_i f$ exists on $U$, so $v$ is differentiable with $v'(\tau) = \partial_j \partial_i f(a + \sigma_1 e_i + \tau e_j)$.
12. By the mean value theorem again, there is $\tau_1$ strictly between $0$ and $t$ with $v(t) - v(0) = t \, \partial_j \partial_i f(p)$, where $p = a + \sigma_1 e_i + \tau_1 e_j$.
13. Steps 9 and 12 give $\Delta(s, t) = s t \, \partial_j \partial_i f(p)$.
14. The expression $\Delta(s, t)$ does not change if we exchange the roles of $(i, s)$ and $(j, t)$. So the same argument, with these roles exchanged, gives a point $q = a + \sigma_2 e_i + \tau_2 e_j$ with $\abs{\sigma_2} < \abs{s}$, $\abs{\tau_2} < \abs{t}$ and $\Delta(s, t) = s t \, \partial_i \partial_j f(q)$.
15. Since $s t \ne 0$, steps 13 and 14 give $\partial_j \partial_i f(p) = \partial_i \partial_j f(q)$.
16. The points $p$ and $q$ depend on $s$ and $t$, and both satisfy $\norm{p - a} \le \abs{s} + \abs{t}$ and $\norm{q - a} \le \abs{s} + \abs{t}$.
17. Take $s = t = 1/k$ for integers $k > 1/r$. Then the points $p_k$ and $q_k$ tend to $a$ as $k \to \infty$.
18. The functions $\partial_j \partial_i f$ and $\partial_i \partial_j f$ are [[continuous|0S9EK5MQPE]] at $a$, because $f$ is of class $C^2$. So $\partial_j \partial_i f(p_k) \to \partial_j \partial_i f(a)$ and $\partial_i \partial_j f(q_k) \to \partial_i \partial_j f(a)$.
19. By step 15 the two sequences are equal, so their limits are equal: $\frac{\partial^2 f}{\partial x_j \, \partial x_i}(a) = \frac{\partial^2 f}{\partial x_i \, \partial x_j}(a)$.

## Idea

The double difference $\Delta(s, t)$ is symmetric in the two directions. Two uses of the mean value theorem write it as $s t$ times a mixed partial at a nearby point, once in each order. Dividing by $s t$ and letting $s, t \to 0$, continuity of the mixed partials makes the two values meet at $a$.
