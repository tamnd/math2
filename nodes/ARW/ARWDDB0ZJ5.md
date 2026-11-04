---
tag: ARWDDB0ZJ5
kind: proof
name: Proof of the Tietze extension theorem by successive approximation
msc: [54C20]
proves: 0X52TNMTCJ
uses: [0AJ646N339, 01EY3VR7ZD, 0SY9ECQ19Q, 0D2MXBV21T, 0G5AV9Q4RR, 0D5YHQGDJY, 0CNQXVBHCX, 0A26X79RTB, 0B2305GNAZ, 0B8GPXFSP7, 065J822CKN, 05NK26G0DR, 0C9S13WKMF, 0GR2APWTAC, 0W8YHHGCJG, 05APWSX53S, E3CPZNJZNG, 0N32V0E3XJ]
sources:
  - url: https://proofwiki.org/wiki/Tietze_Extension_Theorem
---

## Proof

We first treat bounded $f$ by a series of Urysohn functions, then reduce the general case to it.

1. Notation: $X$ is a [[normal space|0AJ646N339]], $A \subseteq X$ is [[closed|0G5AV9Q4RR]], and $A$ has the [[subspace topology|0D5YHQGDJY]]. "Continuous" means [[continuous|0SY9ECQ19Q]] as a map of topological spaces.
2. Criterion (C). Let $Z$ be a topological space and $h \colon Z \to \mathbb{R}$. Then $h$ is continuous if and only if for each $z_0 \in Z$ and $\varepsilon > 0$ there is an open $W \ni z_0$ with $|h(z) - h(z_0)| < \varepsilon$ for all $z \in W$.
3. Proof of (C). If $h$ is continuous, take $W = h^{-1}((h(z_0) - \varepsilon, h(z_0) + \varepsilon))$, the preimage of an [[open ball|0B2305GNAZ]].
4. Conversely, let $V \subseteq \mathbb{R}$ be open and $z_0 \in h^{-1}(V)$. By [[the ball criterion|0A26X79RTB]], some $(h(z_0) - \varepsilon, h(z_0) + \varepsilon)$ lies in $V$. The set $W$ for this $\varepsilon$ lies in $h^{-1}(V)$.
5. So $h^{-1}(V)$ is a union of open sets, hence open by the [[axioms of a topology|0CNQXVBHCX]].
6. By (C), if $g, h \colon Z \to \mathbb{R}$ are continuous, then $g + h$ and $g - h$ are continuous. Given $\varepsilon$, intersect the two sets $W$ for $\varepsilon / 2$.
7. The restriction to $A$ of a continuous $g \colon X \to \mathbb{R}$ is continuous. It is $g \circ \iota$ with $\iota$ the [[inclusion|065J822CKN]], and [[compositions are continuous|05NK26G0DR]].
8. If $B \subseteq A$ is closed in $A$, then $B$ is closed in $X$. Indeed $A \setminus B = A \cap U$ with $U$ open in $X$, so $X \setminus B = (X \setminus A) \cup U$ is open.
9. Lemma. Let $r > 0$ and let $h \colon A \to \mathbb{R}$ be continuous with $|h| \le r$ on $A$. Then there is a continuous $g \colon X \to [-r/3, r/3]$ with $|h - g| \le 2r/3$ on $A$.
10. Proof of the lemma. Let $B = h^{-1}([-r, -r/3])$ and $D = h^{-1}([r/3, r])$. They are closed in $A$ by [[continuity via closed sets|0B8GPXFSP7]], so closed in $X$ by step 8. They are disjoint.
11. By [[Urysohn's lemma|01EY3VR7ZD]] there is a continuous $u \colon X \to [0, 1]$ with $u = 0$ on $B$ and $u = 1$ on $D$. Let $g = (r/3)(2u - 1)$, which is continuous by (C) and takes values in $[-r/3, r/3]$.
12. On $B$: $g = -r/3$ and $h \in [-r, -r/3]$, so $|h - g| \le 2r/3$. On $D$: $g = r/3$ and $h \in [r/3, r]$, so $|h - g| \le 2r/3$.
13. On $A \setminus (B \cup D)$: $|h| < r/3$ and $|g| \le r/3$, so $|h - g| < 2r/3$. This proves the lemma.
14. Bounded case. Let $|f| \le M$ on $A$. If $M = 0$, then $f = 0$ and $F = 0$ works. Let $M > 0$.
15. We build continuous $g_0, g_1, \ldots \colon X \to \mathbb{R}$ with $|g_n| \le \tfrac{M}{3}(\tfrac{2}{3})^n$ on $X$ and $|f - s_n| \le M(\tfrac{2}{3})^{n+1}$ on $A$. Here $s_n = g_0 + \cdots + g_n$.
16. The lemma with $h = f$ and $r = M$ gives $g_0$. Given $g_0, \ldots, g_n$, the function $f - s_n|_A$ is continuous on $A$ by steps 6 and 7. Apply the lemma to it with $r = M(\tfrac{2}{3})^{n+1}$ to get $g_{n+1}$.
17. Then $|g_{n+1}| \le \tfrac{M}{3}(\tfrac{2}{3})^{n+1}$, and $|f - s_{n+1}| = |(f - s_n) - g_{n+1}| \le M(\tfrac{2}{3})^{n+2}$ on $A$.
18. Fix $x \in X$. For $m > n$, $|s_m(x) - s_n(x)| \le \sum_{k = n+1}^{m} \tfrac{M}{3}(\tfrac{2}{3})^k < M(\tfrac{2}{3})^{n+1}$, by the [[finite geometric sum|05APWSX53S]]. So $(s_n(x))$ is Cauchy, and it has a limit $F(x)$ by the [[completeness of the real numbers|E3CPZNJZNG]].
19. Letting $m \to \infty$ and using that [[limits preserve non-strict inequalities|0N32V0E3XJ]] gives $|F(x) - s_n(x)| \le M(\tfrac{2}{3})^{n+1}$ for all $x \in X$ and all $n$.
20. Also $|s_n(x)| \le \sum_{k=0}^{n} \tfrac{M}{3}(\tfrac{2}{3})^k < M$, so $|F(x)| \le M$ for all $x \in X$.
21. For $a \in A$, $|f(a) - F(a)| \le |f(a) - s_n(a)| + |s_n(a) - F(a)| \le 2M(\tfrac{2}{3})^{n+1}$ for each $n$. So $F(a) = f(a)$, and $F$ restricts to $f$.
22. $F$ is continuous. Let $x_0 \in X$ and $\varepsilon > 0$. Choose $n$ with $M(\tfrac{2}{3})^{n+1} < \varepsilon / 3$. Each $s_n$ is continuous by step 6, so (C) gives an open $W \ni x_0$ with $|s_n(x) - s_n(x_0)| < \varepsilon / 3$ on $W$.
23. For $x \in W$, step 19 gives $|F(x) - F(x_0)| \le |F(x) - s_n(x)| + |s_n(x) - s_n(x_0)| + |s_n(x_0) - F(x_0)| < \varepsilon$. By (C), $F$ is continuous. This proves the bounded part of the theorem.
24. General case. Let $\varphi \colon \mathbb{R} \to (-1, 1)$, $\varphi(t) = t / (1 + |t|)$, and $\psi \colon (-1, 1) \to \mathbb{R}$, $\psi(s) = s / (1 - |s|)$.
25. The map $t \mapsto |t|$ is continuous, since $||t| - |t_0|| \le |t - t_0|$ by the [[reverse triangle inequality|0C9S13WKMF]]. So $\varphi$ and $\psi$ are continuous, as [[quotients|0GR2APWTAC]] with nonzero denominators.
26. For $t \in \mathbb{R}$, $1 - |\varphi(t)| = 1/(1 + |t|)$, so $\psi(\varphi(t)) = t$. For $s \in (-1, 1)$, $1 + |\psi(s)| = 1/(1 - |s|)$, so $\varphi(\psi(s)) = s$.
27. The map $\varphi \circ f \colon A \to \mathbb{R}$ is continuous, by (C) and the [[epsilon-delta continuity|0W8YHHGCJG]] of $\varphi$. It satisfies $|\varphi \circ f| < 1$ on $A$.
28. The bounded case with $M = 1$ gives a continuous $G \colon X \to [-1, 1]$ with $G = \varphi \circ f$ on $A$.
29. Let $E = G^{-1}(\{-1, 1\})$. It is closed in $X$ by continuity via closed sets. It is disjoint from $A$, because $|G| < 1$ on $A$.
30. By Urysohn's lemma there is a continuous $v \colon X \to [0, 1]$ with $v = 0$ on $E$ and $v = 1$ on $A$. Let $H = vG$.
31. $H$ is continuous. For $x$ near $x_0$, $|H(x) - H(x_0)| \le |v(x)||G(x) - G(x_0)| + |G(x_0)||v(x) - v(x_0)| \le |G(x) - G(x_0)| + |v(x) - v(x_0)|$. Apply (C) to $G$ and $v$.
32. $|H| < 1$ on $X$. On $E$, $H = 0$. Off $E$, $|G| < 1$ and $0 \le v \le 1$, so $|H| \le |G| < 1$.
33. Let $F = \psi \circ H \colon X \to \mathbb{R}$. It is continuous by (C) and the epsilon-delta continuity of $\psi$ at $H(x_0)$.
34. For $a \in A$, $v(a) = 1$, so $H(a) = G(a) = \varphi(f(a))$, and $F(a) = \psi(\varphi(f(a))) = f(a)$ by step 26.
35. So $F$ is a continuous map $X \to \mathbb{R}$ whose [[restriction|0D2MXBV21T]] to $A$ is $f$. With the bounded case, this proves both parts.

## Idea

Urysohn's lemma lets us approximate a bounded function on $A$ by a function on all of $X$, with an error two thirds as large. Repeating this on the errors gives a geometric series of functions that converges uniformly to an extension. For unbounded $f$, squeeze $\mathbb{R}$ into $(-1, 1)$, extend, and use Urysohn again to keep the extension away from $\pm 1$.
