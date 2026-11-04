---
tag: WYD7QF0XEH
kind: proof
name: Proof of Carathéodory's theorem by removing points
msc: [52A35]
proves: 0201Q4P2B5
uses: [0FQSDC2EQ2, 21SXYJYC59, 02AS45T3H9, 01BX15HSRR, 0CRMGPAH83, 08ZDRN6H41]
sources:
  - url: https://proofwiki.org/wiki/Carath%C3%A9odory%27s_Theorem_(Convex_Analysis)
    locator: Proof
---

## Proof

We take a shortest representation of $x$ as a convex combination and show that it has at most $d + 1$ points.

1. Let $K$ be the set of all [[convex combinations|21SXYJYC59]] $\sum_{i=1}^k \lambda_i y_i$ with $k \geq 1$, $y_i \in P$, $\lambda_i \geq 0$ and $\sum_i \lambda_i = 1$. Each $p \in P$ is in $K$, with $k = 1$.
2. The set $K$ is [[convex|02AS45T3H9]]. Let $x = \sum_i \lambda_i y_i$ and $x' = \sum_j \mu_j z_j$ be in $K$, and let $0 \leq t \leq 1$. Then $(1 - t)x + tx'$ is the combination of all $y_i$ and $z_j$ with the weights $(1 - t)\lambda_i$ and $t\mu_j$.
3. These weights are nonnegative, and they add up to $(1 - t) + t = 1$. So $(1 - t)x + tx' \in K$.
4. The [[convex hull|0FQSDC2EQ2]] $\operatorname{conv}(P)$ is the intersection of all convex sets that contain $P$, and $K$ is one of them. So $x \in \operatorname{conv}(P)$ implies $x \in K$.
5. By the [[well-ordering principle|01BX15HSRR]], there is a least $k$ such that $x = \sum_{i=1}^k \lambda_i y_i$ is a convex combination of $k$ points $y_i \in P$. Fix such a representation.
6. Suppose that $k \geq d + 2$. The $k - 1 \geq d + 1$ vectors $y_i - y_1$, for $2 \leq i \leq k$, lie in $\mathbb{R}^d$, which is spanned by $d$ vectors.
7. By the [[Steinitz exchange lemma|08ZDRN6H41]], these vectors are not [[linearly independent|0CRMGPAH83]]. So there are real numbers $\alpha_2, \dots, \alpha_k$, not all zero, with $\sum_{i=2}^k \alpha_i (y_i - y_1) = 0$.
8. Put $\alpha_1 = -\sum_{i=2}^k \alpha_i$. Then $\sum_{i=1}^k \alpha_i y_i = 0$ and $\sum_{i=1}^k \alpha_i = 0$, and not all $\alpha_i$ are zero.
9. Since the $\alpha_i$ add up to $0$ and are not all zero, some $\alpha_i$ is positive. Let $J = \set{i : \alpha_i > 0}$, and let $t = \min_{i \in J} \lambda_i / \alpha_i$. Then $t \geq 0$, and the minimum is attained at some $j \in J$.
10. Put $\lambda_i' = \lambda_i - t\alpha_i$. For $i \in J$, $t \leq \lambda_i/\alpha_i$ gives $\lambda_i' \geq 0$. For $i \notin J$, $\alpha_i \leq 0$ gives $\lambda_i' \geq \lambda_i \geq 0$. Also $\lambda_j' = 0$.
11. By step 8, $\sum_i \lambda_i' = \sum_i \lambda_i - t\sum_i \alpha_i = 1$ and $\sum_i \lambda_i' y_i = x - t \cdot 0 = x$.
12. Removing the term with $\lambda_j' = 0$, we get $x$ as a convex combination of $k - 1$ points of $P$. This contradicts the choice of $k$ in step 5. Hence $k \leq d + 1$.
13. Write $p_i = y_i$. It remains to show that $x \in \operatorname{conv}\set{p_1, \dots, p_k}$. We show that each convex set $S$ that contains $p_1, \dots, p_k$ contains each convex combination $\sum_{i=1}^k \mu_i p_i$, by induction on $k$.
14. For $k = 1$, the combination is $p_1 \in S$. Let $k \geq 2$. If $\mu_k = 1$, then all other $\mu_i$ are $0$, and the combination is $p_k \in S$.
15. If $\mu_k < 1$, put $z = \sum_{i < k} \frac{\mu_i}{1 - \mu_k} p_i$. This is a convex combination of $k - 1$ points, so $z \in S$ by induction.
16. Then $\sum_i \mu_i p_i = (1 - \mu_k)z + \mu_k p_k$, which lies in $S$ because $S$ is convex.
17. So $x$ lies in every convex set that contains $p_1, \dots, p_k$, that is, $x \in \operatorname{conv}\set{p_1, \dots, p_k}$, with $k \leq d + 1$. Step 5 also gives the equivalent form: $x$ is a convex combination of at most $d + 1$ points of $P$.

## Idea

If more than $d + 1$ points are used, they satisfy a linear relation whose coefficients add up to zero. Sliding the weights along this relation keeps the point $x$ and the total weight $1$ fixed. Stop at the first moment when a weight reaches zero, and one point drops out.
