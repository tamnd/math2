---
tag: 3FN2BN3GW4
kind: proof
name: Proof of the mean value property via a holomorphic function with real part u
msc: [31A05]
proves: 0HYPR64JM2
uses: [0K8SGQSV7G, 0NNQY8WCW6, 0KXSK8TEEB, 0T71SSYZ39, 0DG0Z72CQD, 02AC7JR6G6, 0ZMT1GP4KM, 0BYZTFM0DJ, 0DG10TVYPN, 0T7ABX4CWE, 00FWNP9TXY]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_conjugate
    locator: Description
---

## Proof

1. Let $U$, $u$, $c$ and $r$ be as in the statement, and let $K = \set{z : \abs{z - c} \le r} \subseteq U$.
2. Claim: there is $R' > r$ with $B = \set{z : \abs{z - c} < R'} \subseteq U$. Suppose not. Then for each $n \ge 1$ there is $w_n \notin U$ with $\abs{w_n - c} < r + 1/n$.
3. The points $w_n$ lie in the closed disc of radius $r + 1$ around $c$, which is compact. By [[sequential compactness|0K8SGQSV7G]], a subsequence converges to some $w$ with $\abs{w - c} \le r$.
4. Then $w \in K \subseteq U$. Since $U$ is open, the subsequence eventually lies in $U$. This contradicts $w_n \notin U$, which proves the claim.
5. On $B$, let $P = u_x$ and $Q = -u_y$, and let $g = P + iQ$. Since $u$ is twice continuously differentiable, $P$ and $Q$ have continuous partial derivatives.
6. So $P$ and $Q$ are differentiable on $B$, by [[continuous partial derivatives imply differentiability|0KXSK8TEEB]].
7. We have $P_x = u_{xx}$ and $Q_y = -u_{yy}$. These are equal because $u_{xx} + u_{yy} = 0$.
8. We have $P_y = u_{xy}$ and $-Q_x = u_{yx}$. These are equal by [[Schwarz's theorem|0NNQY8WCW6]].
9. By steps 6 to 8 and the [[Cauchy–Riemann equations|0T71SSYZ39]], $g$ is complex differentiable at each point of $B$. So $g$ is [[holomorphic|0DG0Z72CQD]] on $B$.
10. By [[holomorphic functions on a disc have primitives|02AC7JR6G6]], there is a holomorphic $F$ on $B$ with $F' = g$. Write $F = U_1 + i V_1$ with $U_1, V_1$ real.
11. By the Cauchy–Riemann equations for $F$, $F' = \partial_x U_1 + i \partial_x V_1$ and $\partial_x V_1 = -\partial_y U_1$. So $F' = \partial_x U_1 - i \partial_y U_1$.
12. Comparing with $g = u_x - i u_y$ gives $\partial_x U_1 = u_x$ and $\partial_y U_1 = u_y$ on $B$.
13. Let $w = U_1 - u$ on $B$. It is differentiable, since $U_1$ is (step 11) and $u$ is (step 6 applied to $u$). Its total derivative is $0$ by step 12.
14. The disc $B$ is path-connected along segments, so it is connected by [[path-connected spaces are connected|0ZMT1GP4KM]]. By [[zero derivative implies constant|0BYZTFM0DJ]], $w$ equals a real constant $k$.
15. Let $H = F - k$. Then $H$ is holomorphic on $B$, and $\operatorname{Re} H = U_1 - k = u$ on $B$.
16. The closed disc $K$ lies in $B$. By [[Cauchy's integral formula|0DG10TVYPN]] with $a = c$ and the parametrization of the [[circle integral|0T7ABX4CWE]], $$H(c) = \frac{1}{2\pi i} \int_0^{2\pi} \frac{H(c + r e^{i\theta})}{r e^{i\theta}} \, i r e^{i\theta} \, d\theta = \frac{1}{2\pi} \int_0^{2\pi} H(c + r e^{i\theta}) \, d\theta.$$
17. The integral of a complex function is defined through its real and imaginary parts, as for the [[contour integral|00FWNP9TXY]]. Taking real parts in step 16 and using step 15 gives $u(c) = \frac{1}{2\pi} \int_0^{2\pi} u(c + r e^{i\theta}) \, d\theta$.

## Idea

On a disc slightly larger than the given one, the harmonic function $u$ is the real part of a holomorphic function $H$. The function $u_x - i u_y$ is holomorphic by the Cauchy–Riemann equations, and $H$ is its primitive up to a constant. Cauchy's integral formula at the center says that $H(c)$ is the average of $H$ on the circle. Taking real parts gives the same for $u$.
