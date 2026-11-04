---
tag: ZV3ZYCPZFE
kind: proof
name: Proof of the Arzelà–Ascoli theorem by total boundedness
msc: [54C35]
proves: 0381S8Z5P0
uses: [054Q5PW5GX, 0NMGJJ19HD, 0WE5BBHGM6, 0MW2WXTHMC, 06HE9J7DXF, 0V4DET59NW, 09GRCZVR5E, E3CPZNJZNG, 0SHC6Z304Z, 02TZDKG50Q, 068P0P32DW, 09GQ3ZTQJ9, 0YF82GBTND, 0QPHW703PV, 0B2305GNAZ, 0A3GWZ86AY, 0YVRNEDSVG, 0692CGQF00]
sources:
  - url: https://www.mileshwheeler.com/ma30252/sec-aa.html
    locator: Theorem 4.29
---

## Proof

We show that the closure is complete and totally bounded, and use [[compact iff complete and totally bounded|054Q5PW5GX]]. Write $d$ for the metric of $X$, $\norm{f - g} = d_\infty(f, g)$, and $G$ for the closure of $\mathcal{F}$ in $C(X)$.

Setting up.

1. If $X$ is empty, $C(X)$ has one element. Then $G$ is finite, hence compact, and $\mathcal{F}$ is vacuously equicontinuous and bounded with $M = 0$. From now on let $X$ be nonempty.
2. Let $f \in C(X)$. Since $X$ is [[compact|0QPHW703PV]], $f$ [[attains its bounds|0V4DET59NW]], so $f$ is bounded. Thus $d_\infty$ is the [[uniform metric|06HE9J7DXF]] restricted to $C(X)$, a metric.
3. The space $\R$ is complete by the [[completeness of the real numbers|E3CPZNJZNG]]. By step 2, $C(X)$ is the space of bounded continuous functions $X \to \R$. So $C(X)$ is [[complete|09GRCZVR5E]].
4. By [[the closure is the smallest closed superset|0SHC6Z304Z]], $\mathcal{F} \subseteq G$. By [[closure is closed|02TZDKG50Q]], $G$ is closed in $C(X)$.
5. If $\mathcal{F}$ is empty, then $G$ is empty and both sides hold. From now on let $\mathcal{F}$ be nonempty.

First, let $G$ be compact.

6. By [[compact iff complete and totally bounded|054Q5PW5GX]], $G$ is [[totally bounded|0WE5BBHGM6]]. By the [[epsilon-net characterisation|0NMGJJ19HD]], for each $\varepsilon > 0$ there are finitely many $g_1, \ldots, g_m \in G$ such that each $h \in G$ has $\norm{h - g_k} < \varepsilon$ for some $k$.
7. Uniform bound. Take $\varepsilon = 1$ in step 6. By step 2, choose $M_k$ with $\abs{g_k(x)} \le M_k$ for all $x$, and let $M = \max_k M_k + 1$.
8. Let $f \in \mathcal{F}$ and $x \in X$. Since $f \in G$, some $k$ has $\norm{f - g_k} < 1$. Then $\abs{f(x)} \le \abs{f(x) - g_k(x)} + \abs{g_k(x)} < 1 + M_k \le M$.
9. Equicontinuity. Let $a \in X$ and $\varepsilon > 0$. Take $g_1, \ldots, g_m$ as in step 6 for $\varepsilon / 3$.
10. Each $g_k$ is a continuous map $X \to \R$. By [[continuity via open sets|0YF82GBTND]] at the point $a$, there is $\delta_k > 0$ with $\abs{g_k(x) - g_k(a)} < \varepsilon / 3$ when $d(x, a) < \delta_k$. Let $\delta = \min_k \delta_k > 0$.
11. Let $f \in \mathcal{F}$ and $d(x, a) < \delta$. Choose $k$ with $\norm{f - g_k} < \varepsilon / 3$. Then $\abs{f(x) - f(a)} \le \abs{f(x) - g_k(x)} + \abs{g_k(x) - g_k(a)} + \abs{g_k(a) - f(a)} < \varepsilon$.
12. The number $\delta$ does not depend on $f$. So $\mathcal{F}$ is [[equicontinuous|0MW2WXTHMC]] at $a$, for each $a \in X$.

Conversely, let $\mathcal{F}$ be equicontinuous, with $\abs{f(x)} \le M$ for all $f \in \mathcal{F}$ and $x \in X$.

13. We first show that $\mathcal{F}$ is totally bounded. Fix $\varepsilon > 0$ and let $\eta = \varepsilon / 5$.
14. For each $a \in X$, equicontinuity gives $\delta_a > 0$ with $\abs{f(x) - f(a)} < \eta$ for all $f \in \mathcal{F}$ and all $x$ with $d(x, a) < \delta_a$.
15. The balls $B(a, \delta_a)$ are [[open|0B2305GNAZ]] and cover $X$. By compactness, there are $a_1, \ldots, a_p \in X$ with $X = B(a_1, \delta_{a_1}) \cup \cdots \cup B(a_p, \delta_{a_p})$.
16. Since [[the reals are Archimedean|0A3GWZ86AY]], choose an integer $N \ge 0$ with $N \eta \ge M$. Let $\Lambda = \set{j \eta : j \in \Z, \ \abs{j} \le N}$, a finite set.
17. Let $t \in [-M, M]$ and $j = \floor{t / \eta}$, the [[floor|0YVRNEDSVG]]. Since $-N \le t / \eta \le N$, we get $-N \le j \le N$. Also $j \eta \le t < j \eta + \eta$, so $\abs{t - j \eta} < \eta$ with $j \eta \in \Lambda$.
18. For each map $\varphi \colon \set{1, \ldots, p} \to \Lambda$, let $\mathcal{F}_\varphi$ be the set of $f \in \mathcal{F}$ with $\abs{f(a_k) - \varphi(k)} < \eta$ for each $k$. There are finitely many maps $\varphi$.
19. Each $f \in \mathcal{F}$ lies in some $\mathcal{F}_\varphi$. Indeed, $f(a_k) \in [-M, M]$, so step 17 gives $\varphi(k) \in \Lambda$ with $\abs{f(a_k) - \varphi(k)} < \eta$.
20. Let $f, g \in \mathcal{F}_\varphi$ and $x \in X$. By step 15, $d(x, a_k) < \delta_{a_k}$ for some $k$.
21. Then $\abs{f(x) - g(x)}$ is at most $\abs{f(x) - f(a_k)} + \abs{f(a_k) - \varphi(k)} + \abs{\varphi(k) - g(a_k)} + \abs{g(a_k) - g(x)}$. By steps 14 and 18, this is less than $4 \eta$.
22. Taking the supremum over $x$, $\norm{f - g} \le 4 \eta < \varepsilon$. So each nonempty $\mathcal{F}_\varphi$ has [[diameter|0692CGQF00]] less than $\varepsilon$.
23. By steps 19 and 22, the finitely many nonempty sets $\mathcal{F}_\varphi$ cover $\mathcal{F}$. So $\mathcal{F}$ is totally bounded.
24. Next, $G$ is totally bounded. Let $\varepsilon > 0$. By step 23 and the [[epsilon-net characterisation|0NMGJJ19HD]], there is a finite $H \subseteq \mathcal{F}$ with each $f \in \mathcal{F}$ within $\varepsilon / 2$ of some $h \in H$.
25. Let $g \in G$. By [[closure in a metric space|068P0P32DW]], some $f \in \mathcal{F}$ has $\norm{g - f} < \varepsilon / 2$. Choose $h \in H$ with $\norm{f - h} < \varepsilon / 2$. Then $\norm{g - h} < \varepsilon$.
26. Since $H \subseteq \mathcal{F} \subseteq G$, step 25 gives a finite $\varepsilon$-net of $G$ inside $G$. By the epsilon-net characterisation, $G$ is totally bounded.
27. Next, $G$ is complete. Let $(g_n)$ be a Cauchy sequence in $G$. By step 3, $g_n \to g$ for some $g \in C(X)$.
28. Since $G$ is closed, [[closed sets contain their limits|09GQ3ZTQJ9]], so $g \in G$. Thus $G$ is complete.
29. By steps 26 and 28 and [[compact iff complete and totally bounded|054Q5PW5GX]], $G$ is compact.

## Idea

In the complete space $C(X)$, a closed set is compact exactly when it is totally bounded. Equicontinuity lets finitely many sample points control a function everywhere, up to a small error. Uniform boundedness lets finitely many grid values control the samples, so finitely many small groups cover the family. Conversely, a finite net of continuous functions passes its boundedness and its continuity to the whole family.
