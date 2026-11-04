---
tag: J2R7KY3HTG
kind: proof
name: Proof of the primitive element theorem
msc: [12F10]
proves: 0SVX98HYV1
uses: [0NRYPM9Y27, 0N019F6RE9, 0P6SBR7YM2, 0MA5B744K3, 0DFYTNZ6AM, 0GK1WB9R98, 03J8BS7FMV, 01441KDGBY, 02NZZ1J0FH, 0SHMC00RJV, 03XVP8Q4GY, 067F8YVYMH, 0DQG39K2NH, 0VY3WPP9Y3, 99J1WXG3F7, 0KJVQV3E0F, 08RTDHX1SK, 0EBZ3G455G]
sources:
  - url: https://www.jmilne.org/math/CourseNotes/FT.pdf
    locator: Theorem 5.1
---

## Proof

We treat finite and infinite base fields separately. For infinite $K$ we first handle two generators, then argue by induction.

1. Let $L/K$ be a [[finite|0NRYPM9Y27]] [[separable extension|0N019F6RE9]], and let $n = [L : K]$.
2. Suppose first that $K$ is a [[finite field|08RTDHX1SK]] with $q$ elements. As a vector space, $L$ is isomorphic to $K^n$, so $L$ has $q^n$ elements and is a finite field.
3. By [[the cyclicity of the multiplicative group of a finite field|0EBZ3G455G]], there is $\theta \in L$ such that every nonzero element of $L$ is a power $\theta^k$.
4. Each power $\theta^k$ lies in the [[field|0MA5B744K3]] $K(\theta)$, and so does $0$. Hence $L = K(\theta)$, and $L/K$ is [[simple|0P6SBR7YM2]].
5. From now on, suppose that $K$ is infinite. We first prove a lemma: for $\alpha, \beta \in L$, there is $\theta \in L$ with $K(\alpha, \beta) = K(\theta)$.
6. Since [[finite extensions are algebraic|0DFYTNZ6AM]], $\alpha$ and $\beta$ have [[minimal polynomials|0GK1WB9R98]] $f$ and $g$ over $K$. Both are monic and nonzero.
7. Since $L/K$ is separable, $g$ is a [[separable polynomial|03J8BS7FMV]]. So there are $a, b \in K[x]$ with $a g + b g' = 1$, where $g'$ is the formal derivative.
8. Let $M$ be a [[splitting field|02NZZ1J0FH]] of $fg$ over $L$, which [[exists|01441KDGBY]]. Then $f$ and $g$ [[split|0SHMC00RJV]] over $M$.
9. Write $f = (x - \alpha_1) \cdots (x - \alpha_s)$ and $g = (x - \beta_1) \cdots (x - \beta_t)$ in $M[x]$. Since $f(\alpha) = 0$ and $g(\beta) = 0$, we may number the roots so that $\alpha_1 = \alpha$ and $\beta_1 = \beta$.
10. The roots $\beta_1, \dots, \beta_t$ are distinct. Indeed, if $\beta_j = \beta_k$ with $j \ne k$, then $(x - \beta_j)^2$ divides $g$. So $\beta_j$ has [[multiplicity|03XVP8Q4GY]] at least $2$.
11. Then $g(\beta_j) = 0$ and $g'(\beta_j) = 0$, by [[the derivative criterion for repeated roots|067F8YVYMH]]. Evaluating $a g + b g' = 1$ at $\beta_j$ gives $0 = 1$, a contradiction.
12. For $1 \le i \le s$ and $2 \le j \le t$, step 10 gives $\beta \ne \beta_j$. So the equation $\alpha_i + y \beta_j = \alpha + y \beta$ has exactly one solution $y = (\alpha_i - \alpha)/(\beta - \beta_j)$ in $M$.
13. These are finitely many elements of $M$, and $K$ is infinite. So we can choose $c \in K$ different from all of them. Then $\alpha_i + c \beta_j \ne \alpha + c \beta$ for all $i$ and all $j \ge 2$.
14. Let $\theta = \alpha + c \beta$ and $F = K(\theta)$. Since $\theta \in K(\alpha, \beta)$, we have $F \subseteq K(\alpha, \beta)$.
15. Let $h(x) = f(\theta - c x)$. Its coefficients lie in $F$, because $f \in K[x]$, $c \in K$ and $\theta \in F$. Also $h(\beta) = f(\alpha) = 0$.
16. The ring $F[x]$ is a [[Euclidean domain|0DQG39K2NH]]. By [[Bézout's identity|0VY3WPP9Y3]], $g$ and $h$ have a [[greatest common divisor|99J1WXG3F7]] $d \in F[x]$ with $d = u g + v h$ for some $u, v \in F[x]$.
17. Since $d$ divides $g \ne 0$, $d \ne 0$. Dividing by its leading coefficient, we may assume that $d$ is monic. This keeps $d$ a combination of $g$ and $h$.
18. Evaluating at $\beta$ gives $d(\beta) = u(\beta) g(\beta) + v(\beta) h(\beta) = 0$. So $d$ is not constant.
19. Let $2 \le j \le t$. If $d(\beta_j) = 0$, then $h(\beta_j) = 0$, since $d$ divides $h$. By step 9, $f(\theta - c\beta_j) = 0$ forces $\theta - c \beta_j = \alpha_i$ for some $i$.
20. That would give $\alpha_i + c \beta_j = \alpha + c \beta$, against step 13. So $d(\beta_j) \ne 0$ for all $j \ge 2$.
21. Write $g = d e$ with $e \in F[x]$; then $e \ne 0$. For $j \ge 2$, $0 = g(\beta_j) = d(\beta_j) e(\beta_j)$ in the field $M$, so $e(\beta_j) = 0$.
22. So $e$ has the $t - 1$ distinct roots $\beta_2, \dots, \beta_t$ in $M$. By [[the bound on the number of roots|0KJVQV3E0F]], $\deg e \ge t - 1$.
23. Hence $\deg d = \deg g - \deg e \le 1$. With steps 17 and 18, $d$ is monic of degree $1$ with root $\beta$. So $d = x - \beta$.
24. Since $d \in F[x]$, we get $\beta \in F$. Then $\alpha = \theta - c \beta \in F$.
25. The field $K(\alpha, \beta)$ is the smallest subfield of $L$ containing $K$, $\alpha$ and $\beta$. Hence $K(\alpha, \beta) \subseteq F$, and with step 14, $K(\alpha, \beta) = K(\theta)$. This proves the lemma.
26. Let $w_1, \dots, w_n$ be a basis of $L$ over $K$. Every subfield of $L$ containing $K$ and all $w_k$ contains all their $K$-linear combinations. So $L = K(w_1, \dots, w_n)$.
27. We show by induction on $k$ that $K(w_1, \dots, w_k) = K(\theta_k)$ for some $\theta_k \in L$. For $k = 1$, take $\theta_1 = w_1$.
28. Suppose $K(w_1, \dots, w_k) = K(\theta_k)$ with $k < n$. A subfield of $L$ containing $K$ contains $w_1, \dots, w_{k+1}$ if and only if it contains $\theta_k$ and $w_{k+1}$. So $K(w_1, \dots, w_{k+1}) = K(\theta_k, w_{k+1})$.
29. By the lemma, $K(\theta_k, w_{k+1}) = K(\theta_{k+1})$ for some $\theta_{k+1} \in L$. This completes the induction.
30. For $k = n$, step 26 gives $L = K(\theta_n)$. So $L/K$ is a simple extension.

## Idea

For a finite field, a generator of the multiplicative group already generates everything. For an infinite field, we try $\theta = \alpha + c\beta$ and choose $c$ to avoid finitely many bad values. Then $\beta$ is the only common root of $g(x)$ and $f(\theta - cx)$, so their gcd over $K(\theta)$ is $x - \beta$. This puts $\beta$, and then $\alpha$, inside $K(\theta)$.
