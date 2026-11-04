---
tag: Q4PTS4BYNG
kind: proof
name: Proof of Dirichlet's approximation theorem by the pigeonhole principle
msc: [11J04]
proves: 04JAY9DGB7
uses: [0HGVCWQGY3, 0YVRNEDSVG]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_approximation_theorem
    locator: Proof by the pigeonhole principle
---

## Proof

We use the [[pigeonhole principle|0HGVCWQGY3]].

1. For $k = 0, 1, \dots, N$, put $u_k = k\alpha - \floor{k\alpha}$, where $\floor{\cdot}$ is the [[floor function|0YVRNEDSVG]]. Then $0 \le u_k < 1$, and $u_0 = 0$.
2. Put also $u_{N+1} = 1$. So we have $N + 2$ indices $0, 1, \dots, N+1$, and each $u_k$ lies in $[0, 1]$.
3. Split $[0, 1]$ into the $N + 1$ intervals $I_j = \left[\frac{j}{N+1}, \frac{j+1}{N+1}\right)$ for $0 \le j \le N - 1$ and $I_N = \left[\frac{N}{N+1}, 1\right]$. Each point of $[0, 1]$ lies in exactly one $I_j$.
4. The map that sends an index $k$ to the $j$ with $u_k \in I_j$ goes from a set of $N + 2$ elements to a set of $N + 1$ elements. By the pigeonhole principle, there are indices $i < k$ with $u_i$ and $u_k$ in the same interval.
5. Each interval has length $\frac{1}{N+1}$, so $\abs{u_k - u_i} \le \frac{1}{N+1}$.
6. Case $k \le N$. Then $u_k - u_i = (k - i)\alpha - (\floor{k\alpha} - \floor{i\alpha})$. Put $q = k - i$ and $p = \floor{k\alpha} - \floor{i\alpha}$. Then $1 \le q \le N$ and $\abs{q\alpha - p} \le \frac{1}{N+1}$.
7. Case $k = N + 1$. Then $\abs{1 - u_i} \le \frac{1}{N+1}$ with $0 \le i \le N$.
8. In step 7, $i \ne 0$: for $i = 0$ we would get $1 \le \frac{1}{N+1}$, which is false since $N \ge 1$. So $1 \le i \le N$.
9. In step 7, put $q = i$ and $p = \floor{i\alpha} + 1$. Then $q\alpha - p = u_i - 1$, so $\abs{q\alpha - p} \le \frac{1}{N+1}$ and $1 \le q \le N$.
10. In both cases we found integers $p$ and $q$ with $1 \le q \le N$ and $\abs{q\alpha - p} \le \frac{1}{N+1}$.

## Idea

The fractional parts of $0, \alpha, \dots, N\alpha$, together with the point $1$, are $N + 2$ points in $[0, 1]$.
Cut $[0,1]$ into $N + 1$ pieces; two points share a piece, so they are close.
The difference of two such multiples of $\alpha$ is then close to an integer.
