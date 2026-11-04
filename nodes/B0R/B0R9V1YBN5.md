---
tag: B0R9V1YBN5
kind: proof
name: Proof of the path independence of line integrals
msc: ["26B20"]
proves: 0BFN21TF5F
uses: [05R9NF2J49, 0YS8RX87F4, 0SD237FEJD, 0FSCXYG856, 00ZEBSMNNV, 0W3W1VYWBP, 0R37DFJKFW, 0DC3MPR7C9, 03HF5PMY5T, 0D37QFPEZE, 05AXG3QRKR, 0TCBZMEYGN, 0KXSK8TEEB, 0NS2QYVC4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Conservative_vector_field
    locator: Path independence and conservative vector field
---

## Proof

We prove $1 \Rightarrow 2$, $2 \Rightarrow 3$, $3 \Rightarrow 2$ and $2 \Rightarrow 1$. All curves below are piecewise $C^1$ curves in $U$.

1. Two facts about [[line integrals|0YS8RX87F4]] of $F$ come first. If $\kappa$ is a constant curve, then every chord $\kappa(t_i) - \kappa(t_{i-1})$ is $0$, so every defining sum is $0$ and $\int_\kappa F \cdot d\mathbf{r} = 0$.
2. Let $\eta$ be a curve on $[c, d]$, let $s \in \R$, and let $\eta_s(t) = \eta(t - s)$ on $[c + s, d + s]$. Translating a partition by $s$ keeps its mesh and its chords, so the defining sums of $\eta_s$ and $\eta$ agree. Hence $\int_{\eta_s} F \cdot d\mathbf{r} = \int_\eta F \cdot d\mathbf{r}$.
3. ($1 \Rightarrow 2$.) Let $F = \nabla \phi$ with $\phi$ of class $C^1$, as in the definition of a [[conservative field|05R9NF2J49]]. Let $\gamma_1, \gamma_2$ run from $A$ to $B$. By the [[gradient theorem|0SD237FEJD]], both integrals equal $\phi(B) - \phi(A)$.
4. ($2 \Rightarrow 3$.) Let $\gamma \colon [a, b] \to U$ be closed, with $\gamma(a) = \gamma(b) = A$. The constant curve $\kappa \colon [a, b] \to \set{A}$ has the same initial and end point. By statement 2 and step 1, $\int_\gamma F \cdot d\mathbf{r} = \int_\kappa F \cdot d\mathbf{r} = 0$.
5. ($3 \Rightarrow 2$.) Let $\gamma_1 \colon [a, b] \to U$ and $\gamma_2 \colon [c, d] \to U$ both run from $A$ to $B$. Let $\gamma_2^-$ be the [[reversed curve|0FSCXYG856]] on $[c, d]$. It runs from $B$ to $A$, and $\int_{\gamma_2^-} F \cdot d\mathbf{r} = -\int_{\gamma_2} F \cdot d\mathbf{r}$.
6. Let $\eta(t) = \gamma_2^-(t - b + c)$ for $t \in [b, b + d - c]$. Then $\eta(b) = B = \gamma_1(b)$, and $\eta$ ends at $A$. By step 2, $\int_\eta F \cdot d\mathbf{r} = -\int_{\gamma_2} F \cdot d\mathbf{r}$.
7. The concatenation of $\gamma_1$ and $\eta$ is a closed curve at $A$. By statement 3 and [[additivity|00ZEBSMNNV]], $0 = \int_{\gamma_1} F \cdot d\mathbf{r} + \int_\eta F \cdot d\mathbf{r} = \int_{\gamma_1} F \cdot d\mathbf{r} - \int_{\gamma_2} F \cdot d\mathbf{r}$.
8. ($2 \Rightarrow 1$.) If $U$ is empty there is nothing to prove. Otherwise fix $p \in U$. A polygonal path is a concatenation of finitely many segments $t \mapsto y + t (z - y)$, each shifted to the right parameter interval. It is piecewise $C^1$.
9. Each [[open ball|0DC3MPR7C9]] $B(x, r)$ is convex. Indeed, for $y, z$ in it and $t \in [0, 1]$, the [[triangle inequality|03HF5PMY5T]] gives $\norm{(1 - t) y + t z - x} \le (1 - t) \norm{y - x} + t \norm{z - x} < r$.
10. Let $A$ be the set of $x \in U$ that are joined to $p$ by a polygonal path in $U$. Then $p \in A$, using a constant segment.
11. The set $A$ is open. Let $x \in A$ and choose $r > 0$ with $B(x, r) \subseteq U$. For $y \in B(x, r)$, the segment from $x$ to $y$ lies in the ball by step 9. Appending it to a path from $p$ to $x$ shows $y \in A$.
12. The set $U \setminus A$ is open. Let $x \in U \setminus A$ and $B(x, r) \subseteq U$. If some $y \in B(x, r)$ were in $A$, appending the segment from $y$ to $x$ would give $x \in A$. So $B(x, r) \subseteq U \setminus A$.
13. Since $U$ is [[connected|0R37DFJKFW]], it is not the union of two disjoint nonempty open sets. With steps 10 to 12, $A = U$.
14. For $x \in U$, let $\phi(x) = \int_\gamma F \cdot d\mathbf{r}$ for a curve $\gamma$ in $U$ from $p$ to $x$. Such a curve exists by step 13, and by statement 2 the value does not depend on the choice of $\gamma$.
15. Fix $x \in U$ and $i \in \set{1, \dots, n}$. Choose $r > 0$ with $B(x, r) \subseteq U$, and let $0 < \abs{h} < r$. Let $\gamma \colon [a, b] \to U$ run from $p$ to $x$.
16. Let $\sigma(t) = x + (t - b) h e_i$ for $t \in [b, b + 1]$, where $e_i$ is the $i$-th standard basis vector. It lies in $B(x, r)$, and the concatenation of $\gamma$ and $\sigma$ runs from $p$ to $x + h e_i$.
17. By step 14 and additivity, $\phi(x + h e_i) - \phi(x) = \int_\sigma F \cdot d\mathbf{r}$.
18. By the [[parametric formula|0W3W1VYWBP]] and the [[substitution|0D37QFPEZE]] $u = t - b$, $\int_\sigma F \cdot d\mathbf{r} = \int_b^{b+1} F(\sigma(t)) \cdot h e_i \, dt = h \int_0^1 F_i(x + u h e_i) \, du$.
19. Hence $\abs{\frac{\phi(x + h e_i) - \phi(x)}{h} - F_i(x)} \le \int_0^1 \abs{F_i(x + u h e_i) - F_i(x)} \, du$. This is at most the supremum of $\abs{F_i(w) - F_i(x)}$ over $\norm{w - x} \le \abs{h}$.
20. Since $F_i$ is continuous at $x$, this bound tends to $0$ as $h \to 0$. So the [[partial derivative|05AXG3QRKR]] $\partial \phi / \partial x_i$ exists at $x$ and equals $F_i(x)$.
21. The partial derivatives $F_1, \dots, F_n$ of $\phi$ are continuous on $U$. So $\phi$ is of [[class $C^1$|0TCBZMEYGN]], and it is differentiable by [[continuous partial derivatives imply differentiability|0KXSK8TEEB]].
22. By the coordinate form of the [[gradient|0NS2QYVC4Y]], $\nabla \phi = (F_1, \dots, F_n) = F$ on $U$. So $F$ is conservative, which is statement 1.

## Idea

A potential gives path independence by the gradient theorem. Conversely, path independence lets one define a potential as the integral from a fixed base point. A short straight last step in the direction $e_i$ then shows that the partial derivatives of this potential are the components of $F$.
