---
tag: 9MGFVFWY9V
kind: proof
name: Proof that the reals form an ordered field, with the Cauchy sequence construction
msc: [12J15]
proves: 0QSPNASE50
uses: [0D8HE681SC, 0337CYB0VD, 0FGENPMPJX, 09RFKMBQ63, 0316AYH1SC, 010JCV9J4E]
sources:
  - url: https://pi.math.cornell.edu/~web304/reals.pdf
    locator: Lemma 1
---

## Proof

We use the [[construction from Cauchy sequences|0D8HE681SC]] and the [[order on the reals|0337CYB0VD]] defined there.

1. A real number is a class $x = [(x_n)]$ of Cauchy sequences of rational numbers. Two sequences give the same real number exactly when their difference tends to $0$.
2. The number $0$ is the class of the constant sequence $0$. Since $(x_n) + (-x_n)$ is the constant sequence $0$, we get $-x = [(-x_n)]$. So $y - x = [(y_n - x_n)]$.
3. By definition, $x < y$ means: there are a rational $\varepsilon > 0$ and an $N$ with $y_n - x_n > \varepsilon$ for all $n \ge N$.
4. This does not depend on the representatives. Let $(x'_n)$ and $(y'_n)$ be equivalent to $(x_n)$ and $(y_n)$. Choose $N' \ge N$ with $\abs{x'_n - x_n} < \varepsilon/4$ and $\abs{y'_n - y_n} < \varepsilon/4$ for $n \ge N'$.
5. Then $y'_n - x'_n > (y_n - x_n) - \varepsilon/2 > \varepsilon/2$ for $n \ge N'$. All computations here take place in the [[ordered field of rationals|09RFKMBQ63]].
6. Lemma. Let $(z_n)$ be a Cauchy sequence of rationals that does not tend to $0$. Then there are a rational $r > 0$ and a $P$ with $z_n > r$ for all $n \ge P$, or $z_n < -r$ for all $n \ge P$.
7. Proof of the lemma. Since $(z_n)$ does not tend to $0$, there is a rational $s > 0$ such that for each $N$ some $n \ge N$ has $\abs{z_n} \ge s$.
8. Since $(z_n)$ is Cauchy, there is $N$ with $\abs{z_m - z_n} < s/3$ for all $m, n \ge N$. Pick $P \ge N$ with $\abs{z_P} \ge s$.
9. If $z_P \ge s$, then $z_n > z_P - s/3 \ge 2s/3$ for each $n \ge P$. If $z_P \le -s$, then $z_n < z_P + s/3 \le -2s/3$ for each $n \ge P$. Take $r = 2s/3$.
10. Let $x \ne y$ be real numbers. Then $(y_n - x_n)$ does not tend to $0$, by step 1. By the lemma, $y_n - x_n > r$ eventually or $x_n - y_n > r$ eventually. So $x < y$ or $y < x$.
11. The relations $x < y$ and $y < x$ do not both hold. Otherwise, for all large $n$, $y_n - x_n > \varepsilon$ and $x_n - y_n > \varepsilon'$ with $\varepsilon, \varepsilon' > 0$. Adding gives $0 > \varepsilon + \varepsilon'$, which is false.
12. The relation $x < x$ never holds. By step 4 we may use the same representative twice, and then $x_n - x_n = 0$ is never larger than $\varepsilon > 0$.
13. Recall that $x \le y$ means $x < y$ or $x = y$. It is reflexive. It is antisymmetric: if $x \le y$, $y \le x$ and $x \ne y$, then $x < y$ and $y < x$, against step 11.
14. It is transitive. Let $x \le y \le z$. If one of the two relations is an equality, then $x \le z$ at once. Otherwise $z_n - y_n > \varepsilon$ and $y_n - x_n > \varepsilon'$ for large $n$. Then $z_n - x_n > \varepsilon + \varepsilon'$, so $x < z$.
15. It is total by step 10. So $\le$ is a [[total order|0316AYH1SC]] on $\R$.
16. Let $a \le b$ and let $c$ be real. If $a = b$, then $a + c = b + c$. If $a < b$, then $a + c$ and $b + c$ have the representatives $(a_n + c_n)$ and $(b_n + c_n)$. Their difference is $b_n - a_n$, which is eventually larger than some $\varepsilon > 0$. So $a + c < b + c$.
17. Let $0 \le a$ and $0 \le b$. If $a = 0$ or $b = 0$, then $a b = 0$ in the [[field of reals|0FGENPMPJX]], so $0 \le a b$.
18. Otherwise $0 < a$ and $0 < b$. By steps 2 and 3, there are rationals $\varepsilon, \varepsilon' > 0$ and an $N$ with $a_n > \varepsilon$ and $b_n > \varepsilon'$ for $n \ge N$.
19. The product $a b$ is represented by $(a_n b_n)$, and $a_n b_n > \varepsilon \varepsilon' > 0$ for $n \ge N$. So $0 < a b$.
20. The reals form a field, by the [[field property of the reals|0FGENPMPJX]]. With steps 15, 16, 17 and 19, $\R$ is an [[ordered field|010JCV9J4E]].

## Idea

A real number that is not zero is represented by a sequence that eventually stays on one side of zero, at a fixed distance. This gives the trichotomy, so the order is total. The two axioms of an ordered field then hold term by term, because they hold in $\Q$.
