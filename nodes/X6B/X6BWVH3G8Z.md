---
tag: X6BWVH3G8Z
kind: proof
name: Proof that C^k functions are characterised by continuous derivatives
msc: [26B05]
proves: 0TCBZMEYGN
uses: [0EY05Z9RPN, 02RSXVM1ZN, 05AXG3QRKR, 0KXSK8TEEB, 0A6PMR20N4, 0135XZZQ8M, 08EVNYZF42, 0SDMPMCN43, 03MC70ZRNR, 0C13E623WD, 0F3K4C7XYW, 0FJZMBX0ZZ]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.4.6 and Definition 8.6.1
---

## Proof

We identify each iterated derivative with the list of its values on basis vectors, and we argue by induction on the order $r$.

1. Let $U$, $f$ and $k$ be as in the statement. For $r \ge 0$, let $E_r = L^r(\mathbb{R}^n; \mathbb{R}^m)$, and let $e_1, \dots, e_n$ be the standard basis of $\mathbb{R}^n$. For a tuple $l = (l_1, \dots, l_r)$ in $\{1, \dots, n\}^r$, write $e_l = (e_{l_1}, \dots, e_{l_r})$.
2. Define $\Phi_r \colon E_r \to (\mathbb{R}^m)^{n^r} = \mathbb{R}^{N}$, with $N = m n^r$, by $\Phi_r(T) = (T(e_l))_l$. For $r = 0$, $\Phi_0$ is the identity of $\mathbb{R}^m$. The map $\Phi_r$ is linear.
3. The map $\Phi_r$ is a bijection. Write each argument $v_s = \sum_t v_{s,t} e_t$. By [[multilinearity|0SDMPMCN43]], $T(v_1, \dots, v_r) = \sum_l v_{1,l_1} \cdots v_{r,l_r} T(e_l)$, so $T$ is determined by $\Phi_r(T)$. Conversely, for any family $(y_l)$ this formula with $y_l$ in place of $T(e_l)$ defines an $r$-linear map with values $y_l$.
4. Give $E_r$ the norm $\|T\| = \|\Phi_r(T)\|$, with the Euclidean norm on $\mathbb{R}^N$. All norms on $E_r$ are [[equivalent|03MC70ZRNR]]. Equivalent norms give the same continuous maps, and they change the quotient defining a [[Fréchet derivative|08EVNYZF42]] by bounded factors only. So we may use this norm.
5. Let $G \colon U \to E_r$ and $x \in U$. Each linear map $\mathbb{R}^n \to E_r$ is bounded, by [[linear maps on finite-dimensional spaces are continuous|0C13E623WD]] and [[bounded linear maps are continuous|0F3K4C7XYW]]. Since $\Phi_r$ is a linear bijection preserving norms, $\|G(x + h) - G(x) - A h\| = \|\Phi_r G(x + h) - \Phi_r G(x) - \Phi_r A h\|$ for each linear $A \colon \mathbb{R}^n \to E_r$.
6. By step 5, $G$ is Fréchet differentiable at $x$ if and only if $\Phi_r \circ G$ is [[differentiable|0135XZZQ8M]] at $x$. For the converse direction, a derivative $L$ of $\Phi_r \circ G$ gives the linear map $A = \Phi_r^{-1} \circ L$ in step 5. Then $D(\Phi_r \circ G)(x) = \Phi_r \circ DG(x)$. Also $G$ is continuous if and only if $\Phi_r \circ G$ is continuous.
7. A map into $\mathbb{R}^N$ is continuous if and only if each coordinate is continuous. This follows from $|y_q| \le \|y\| \le |y_1| + \dots + |y_N|$ for $y \in \mathbb{R}^N$, and the [[triangle inequality|0FJZMBX0ZZ]].
8. When $D^r f$ is defined on $U$, let $c^r_{j,l}(x)$ be the $j$-th entry of $D^r f(x)(e_l)$. These functions are the coordinates of $\Phi_r \circ D^r f$.
9. For $l$ of length $r$, let $p_{j,l} = \partial^r f_j / \partial x_{l_1} \cdots \partial x_{l_r}$, where we differentiate first in $x_{l_r}$ and last in $x_{l_1}$. For $r = 0$, $p_{j,()} = f_j$. By the definition of [[higher partial derivatives|02RSXVM1ZN]], $p_{j,(i, l)} = \partial_i p_{j,l}$ whenever the right side exists. As $l$ varies, the $p_{j,l}$ are all the partial derivatives of order $r$ of $f_j$.
10. Claim: suppose that $D^r f$ is differentiable on $U$, for some $r \ge 0$. Then for all $i$, $j$, $l$ and $x \in U$, the [[partial derivative|05AXG3QRKR]] $\partial_i c^r_{j,l}(x)$ exists and equals $c^{r+1}_{j,(i,l)}(x)$.
11. Proof of the claim. By step 6, $\Phi_r \circ D^r f$ is differentiable at $x$ with derivative $\Phi_r \circ D(D^r f)(x)$. Since [[the derivative gives the directional derivatives|0A6PMR20N4]], its difference quotients in the direction $e_i$ tend to $\Phi_r\big(D(D^r f)(x)(e_i)\big)$.
12. Each coordinate of a convergent family in $\mathbb{R}^N$ converges, by step 7. Taking the coordinate with index $(j, l)$, the partial derivative $\partial_i c^r_{j,l}(x)$ exists and equals the $j$-th entry of $D(D^r f)(x)(e_i)(e_l)$.
13. By the definition of the [[iterated derivative|0EY05Z9RPN]], $D(D^r f)(x)(e_i)(e_l) = D^{r+1} f(x)(e_i, e_{l_1}, \dots, e_{l_r})$. Its $j$-th entry is $c^{r+1}_{j,(i,l)}(x)$. This proves the claim.
14. Now suppose that $f$ is of class $C^k$ in the sense of partial derivatives. We show by induction on $r \le k$ that $D^r f$ is defined on $U$ and $c^r_{j,l} = p_{j,l}$ on $U$ for all $j$ and $l$. For $r = 0$ both sides are $f_j$.
15. Suppose that this holds for some $r < k$. The coordinates of $\Phi_r \circ D^r f$ are the $p_{j,l}$. Their partial derivatives $\partial_i p_{j,l} = p_{j,(i,l)}$ have order $r + 1 \le k$, so they exist and are continuous on $U$.
16. By the theorem that [[continuous partial derivatives imply differentiability|0KXSK8TEEB]], $\Phi_r \circ D^r f$ is differentiable at each point of $U$. By step 6, $D^r f$ is differentiable on $U$. So $D^{r+1} f$ is defined on $U$.
17. By the claim and the induction hypothesis, $c^{r+1}_{j,(i,l)} = \partial_i c^r_{j,l} = \partial_i p_{j,l} = p_{j,(i,l)}$ on $U$. Each tuple of length $r + 1$ has the form $(i, l)$, so the induction step is complete.
18. Step 16 shows condition 2 for each $r < k$. For $1 \le r \le k$, the coordinates $c^r_{j,l} = p_{j,l}$ of $\Phi_r \circ D^r f$ are continuous by hypothesis. By steps 6 and 7, $D^r f$ is continuous on $U$.
19. For $r = 0$: by step 16 with $r = 0$, $f$ is differentiable at each $x \in U$. As in step 5, there is $C \ge 0$ with $\|Df(x) h\| \le C \|h\|$. The definition gives $\|f(x + h) - f(x)\| \le (C + 1) \|h\|$ for small $h$. So $f$ is continuous, and condition 1 holds.
20. Conversely, suppose that conditions 1 and 2 hold. We show by induction on $r \le k$ that each $p_{j,l}$ of order $r$ exists on $U$ and equals $c^r_{j,l}$. For $r = 0$ both sides are $f_j$.
21. Suppose that this holds for some $r < k$. By condition 2, $D^r f$ is differentiable on $U$. By the claim, $\partial_i c^r_{j,l}$ exists on $U$ and equals $c^{r+1}_{j,(i,l)}$.
22. Since $c^r_{j,l} = p_{j,l}$ on $U$, the partial derivative $p_{j,(i,l)} = \partial_i p_{j,l}$ exists on $U$ and equals $c^{r+1}_{j,(i,l)}$. This completes the induction step.
23. Let $r \le k$. By condition 1, $D^r f$ is continuous on $U$. By steps 6 and 7, each coordinate $c^r_{j,l}$ of $\Phi_r \circ D^r f$ is continuous. By step 20, each partial derivative $p_{j,l}$ of order $r$ is continuous on $U$.
24. So $f$ is of class $C^k$ on $U$. Together with steps 14 to 19, this proves the equivalence.

## Idea

The values of $D^r f(x)$ on tuples of basis vectors are exactly the partial derivatives of order $r$, with the first argument being the last variable of differentiation. So the iterated derivative and the list of partial derivatives carry the same information, and one is continuous exactly when the other is. Continuous partial derivatives give differentiability, and this lets the induction climb one order at a time.
