---
tag: C6GP5HEZXT
kind: proof
name: Proof that linear maps on finite-dimensional normed spaces are continuous
msc: [47B01]
proves: 0C13E623WD
uses: [0S3SMRH0Z5, 0F3K4C7XYW, 03MC70ZRNR, 0J3578562S, 018W3V3TCT, 06MRNP4BNT, 059THXBRBB, 0FJZMBX0ZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_operator
    locator: Examples
---

## Proof

We show that $T$ is bounded and then use the equivalence of boundedness and continuity.

1. If $V = \{0\}$, then $T = 0$, and $\|Tx\|_W \le 0 \cdot \|x\|_V$. Let $V \neq \{0\}$.
2. Take a [[basis|06MRNP4BNT]] $e_1, \ldots, e_n$ of the [[finite-dimensional|018W3V3TCT]] space $V$. Write $x = \sum_j a_j(x) e_j$, with linear coordinates $a_j$ by [[this result|059THXBRBB]].
3. Let $\|x\|_\infty = \max_j |a_j(x)|$. It is a norm on $V$: it vanishes only at $0$, it is homogeneous, and $|a_j(x + y)| \le |a_j(x)| + |a_j(y)|$.
4. By the [[equivalence of norms in finite dimension|03MC70ZRNR]] and the definition of [[equivalent norms|0J3578562S]], there is $c > 0$ with $c \|x\|_\infty \le \|x\|_V$ for all $x \in V$.
5. By linearity, $Tx = \sum_j a_j(x) \, T e_j$. By the [[triangle inequality|0FJZMBX0ZZ]], $\|Tx\|_W \le \sum_j |a_j(x)| \, \|T e_j\|_W \le K \|x\|_\infty$, where $K = \sum_j \|T e_j\|_W$.
6. With step 4, $\|Tx\|_W \le (K / c) \|x\|_V$ for all $x \in V$. So $T$ is bounded.
7. By [[bounded linear maps are continuous|0F3K4C7XYW]], $T$ is a [[continuous linear map|0S3SMRH0Z5]].

## Idea

A linear map is fixed by its values on a basis, so $\|Tx\|$ is at most a constant times the largest coordinate of $x$. In finite dimension, the largest coordinate is controlled by the norm of $x$, because all norms are equivalent. So $T$ is bounded, hence continuous.
