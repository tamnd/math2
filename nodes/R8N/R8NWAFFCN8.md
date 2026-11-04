---
tag: R8NWAFFCN8
kind: proof
name: Proof that uniform limits of holomorphic functions are holomorphic, by Morera's theorem
msc: [30A99]
proves: 0431RN0R1N
uses: [0DG0Z72CQD, 07PFYV65MB, 02AC7JR6G6, 0YQ458D7PF, 0DJMGPN8K9, 0VDD7W0EKZ, 0V4DET59NW, 0K8SGQSV7G, 0JJRENWMP6]
sources:
  - url: https://en.wikipedia.org/wiki/Morera%27s_theorem
    locator: Uniform limits
---

## Proof

1. Let $U$, $f_n$ and $f$ be as in the statement. Each $f_n$ is continuous, since a complex differentiable function is continuous at each point.
2. Claim: $f$ is continuous. Let $z \in U$ and pick $s > 0$ with the closed disc $D = \set{w : \abs{w - z} \le s} \subseteq U$. It is compact by the [[Heine–Borel theorem|07PFYV65MB]].
3. Let $\varepsilon > 0$. By uniform convergence on $D$, choose $n$ with $\abs{f_n - f} < \varepsilon/3$ on $D$. Choose $\delta \in (0, s)$ with $\abs{f_n(w) - f_n(z)} < \varepsilon/3$ for $\abs{w - z} < \delta$.
4. For $\abs{w - z} < \delta$, $\abs{f(w) - f(z)} \le \abs{f(w) - f_n(w)} + \abs{f_n(w) - f_n(z)} + \abs{f_n(z) - f(z)} < \varepsilon$. This proves the claim.
5. Let $B \subseteq U$ be an open disc, and let $T \subseteq B$ be a closed triangle with boundary path $\partial T$ of length $L$.
6. By [[holomorphic functions on a disc have primitives|02AC7JR6G6]], each $f_n$ has a primitive on $B$. By the [[fundamental theorem of contour integration|0YQ458D7PF]], $\oint_{\partial T} f_n(z) \, dz = 0$.
7. The triangle $T$ is closed and bounded, hence compact. Let $\varepsilon_n = \sup_{T} \abs{f_n - f}$. Then $\varepsilon_n \to 0$.
8. By step 6 and the [[estimation lemma|0DJMGPN8K9]], $\abs{\oint_{\partial T} f} = \abs{\oint_{\partial T} (f - f_n)} \le \varepsilon_n L$ for each $n$. So $\oint_{\partial T} f(z) \, dz = 0$.
9. By steps 4 and 8 and [[Morera's theorem|0VDD7W0EKZ]] on $B$, $f$ is [[holomorphic|0DG0Z72CQD]] on $B$.
10. Each point of $U$ lies in an open disc $B \subseteq U$. So $f$ is holomorphic on $U$.
11. Now let $K \subseteq U$ be compact. If $K$ is empty, there is nothing to prove, so let $K$ be nonempty. Claim: there is $\delta > 0$ such that $K' = \set{w : \abs{w - z} \le \delta \text{ for some } z \in K}$ is a compact subset of $U$.
12. If $U = \C$, take $\delta = 1$. Otherwise let $d(z) = \inf \set{\abs{z - w} : w \notin U}$. Then $\abs{d(z) - d(z')} \le \abs{z - z'}$, so $d$ is continuous.
13. Since $U$ is open, $d > 0$ on $K$. By [[attainment of bounds|0V4DET59NW]], $d$ has a positive minimum on $K$. Let $\delta$ be half of it. Then $K' \subseteq U$.
14. The set $K'$ is bounded since $K$ is. It is closed: if $w_j \in K'$ tends to $w$, pick $z_j \in K$ with $\abs{w_j - z_j} \le \delta$.
15. By [[sequential compactness|0K8SGQSV7G]] of $K$, a subsequence of $(z_j)$ tends to some $z \in K$. Then $\abs{w - z} \le \delta$, so $w \in K'$. By Heine–Borel, $K'$ is compact, which proves the claim.
16. Let $\eta_n = \sup_{K'} \abs{f_n - f}$. By uniform convergence on the compact set $K'$, $\eta_n \to 0$.
17. Let $z \in K$. The closed disc of radius $\delta$ around $z$ lies in $K'$, and $f_n - f$ is holomorphic on $U$ by step 10.
18. By [[Cauchy's estimates|0JJRENWMP6]] with $n = 1$ for $f_n - f$ on this disc, $\abs{f_n'(z) - f'(z)} \le \eta_n / \delta$.
19. The bound in step 18 does not depend on $z \in K$ and tends to $0$. So $f_n' \to f'$ uniformly on $K$.

## Idea

Integrals over triangles pass to the limit under uniform convergence. Each $f_n$ has zero integral over small triangles, so $f$ does too, and Morera's theorem makes $f$ holomorphic. For the derivatives, Cauchy's estimates bound $f_n' - f'$ at a point by the size of $f_n - f$ on a nearby circle.
