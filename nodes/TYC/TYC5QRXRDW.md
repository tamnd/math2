---
tag: TYC5QRXRDW
kind: proof
name: Proof that the matrix exponential solves a linear system
msc: [34A30, 15A16]
proves: 0YC8JT513J
uses: [0K665H5V1S, 0VJF99CZ0Z, 075VBY4K4X, 0PVJRACB9H, 0660QX1VPR, 002X7EK91H, 0V9A43H7WV, 0M0TKFRX2A, 003QDZ4T16]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_exponential
    locator: Linear differential equation systems
---

## Proof

We differentiate the series entry by entry, and prove uniqueness with the factor $e^{-tA}$.

1. Let $c = n \max_{i, j} \abs{A_{ij}}$. We claim $\abs{(A^k)_{ij}} \le c^k$ for all $i, j$ and $k \ge 0$. For $k = 0$, the entries of $A^0 = I$ are $0$ or $1$.
2. If the claim holds for $k$, then $\abs{(A^{k+1})_{ij}} = \abs{\sum_l (A^k)_{il} A_{lj}} \le n\, c^k \max_{l, j} \abs{A_{lj}} = c^{k+1}$. This proves the claim by induction.
3. Entry $(i, j)$ of the [[matrix exponential|0K665H5V1S]] $e^{tA}$ is the power series $\varphi_{ij}(t) = \sum_{k \ge 0} (A^k)_{ij}\, t^k / k!$. By step 1, its terms are bounded in absolute value by $(c \abs{t})^k / k!$.
4. The series $\sum_k (c \abs{t})^k / k!$ [[converges for every $t$|0PVJRACB9H]]. So $\varphi_{ij}$ converges absolutely for every $t \in \R$, and its [[radius of convergence|0660QX1VPR]] is $\infty$.
5. By [[termwise differentiation of power series|002X7EK91H]], $\varphi_{ij}$ is differentiable on $\R$ with $\varphi_{ij}'(t) = \sum_{k \ge 1} (A^k)_{ij}\, t^{k-1}/(k-1)! = \sum_{k \ge 0} (A^{k+1})_{ij}\, t^k / k!$.
6. We have $(A^{k+1})_{ij} = \sum_l A_{il} (A^k)_{lj} = \sum_l (A^k)_{il} A_{lj}$. Finite sums of convergent series may be summed termwise. So $\varphi_{ij}' = \sum_l A_{il} \varphi_{lj} = \sum_l \varphi_{il} A_{lj}$.
7. In matrix form, $\frac{d}{dt} e^{tA} = A\, e^{tA} = e^{tA} A$ for each $t \in \R$.
8. Existence. Let $x(t) = e^{tA} x_0$. Each entry of $x$ is a fixed combination of the $\varphi_{ij}$, so by step 7 $x'(t) = A e^{tA} x_0 = A x(t)$.
9. At $t = 0$ only the term $k = 0$ remains, so $e^{0 A} = I$ and $x(0) = x_0$. So $x$ solves the [[initial value problem|075VBY4K4X]] for the [[system|0VJF99CZ0Z]] $x' = A x$ on $\R$.
10. Since $(-t)^k A^k = t^k (-A)^k$, we have $e^{-tA} = e^{t(-A)}$. Step 7 for the matrix $-A$ gives $\frac{d}{dt} e^{-tA} = -A e^{-tA} = -e^{-tA} A$.
11. For differentiable matrix functions $U, V$, the entrywise [[product rule|0V9A43H7WV]] and [[linearity of differentiation|0M0TKFRX2A]] give $(U V)' = U' V + U V'$.
12. Let $Z(t) = e^{tA} e^{-tA}$. By steps 7, 10 and 11, $Z' = A e^{tA} e^{-tA} - e^{tA} A e^{-tA}$. Since $e^{tA} A = A e^{tA}$, this is $0$.
13. So each entry of $Z$ [[is constant|003QDZ4T16]], and $Z(t) = Z(0) = I$ for all $t$.
14. Uniqueness. Let $y$ be any solution on $\R$ with $y(0) = x_0$, and let $w(t) = e^{-tA} y(t)$. By steps 10 and 11, $w' = -e^{-tA} A y + e^{-tA} A y = 0$.
15. So $w$ is constant, and $w(t) = w(0) = y(0) = x_0$.
16. By step 13, $y(t) = e^{tA} e^{-tA} y(t) = e^{tA} w(t) = e^{tA} x_0$. So $x(t) = e^{tA} x_0$ is the unique solution.

## Idea

Each entry of $e^{tA}$ is a power series in $t$ with infinite radius, so it can be differentiated term by term. This shifts $A^k$ to $A^{k+1}$, which is $A e^{tA}$. For uniqueness, $e^{-tA}$ undoes the flow: it turns any solution into a constant.
