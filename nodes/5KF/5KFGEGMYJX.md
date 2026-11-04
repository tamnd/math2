---
tag: 5KFGEGMYJX
kind: proof
name: Proof of the fundamental theorem of symmetric polynomials by leading monomials
msc: ["05E05"]
proves: 0GW1ZZH0R4
uses: [0GYGHKX834, 0CES91M79A, 06CTFY2DEZ, 0ZMY8441GW]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_symmetric_polynomial
    locator: Alternative proof
---

## Proof

We use the lexicographic order on exponents. Existence is by induction on the leading exponent; uniqueness compares leading terms.

1. Let $R$ be a [[commutative ring|0GYGHKX834]] and $A = R[x_1, \dots, x_n]$ the [[polynomial ring|0CES91M79A]]. For $\alpha \in \N^n$, write $x^\alpha = x_1^{\alpha_1} \cdots x_n^{\alpha_n}$ and $\abs{\alpha} = \alpha_1 + \dots + \alpha_n$.
2. Order $\N^n$ lexicographically: $\alpha > \beta$ if $\alpha \neq \beta$ and the first nonzero entry of $\alpha - \beta$ is positive. This is a total order. If $\alpha > \beta$, then $\alpha + \gamma > \beta + \gamma$ for every $\gamma \in \N^n$.
3. For $f = \sum_\alpha c_\alpha x^\alpha \neq 0$, its leading exponent $\operatorname{LE}(f)$ is the largest $\alpha$ with $c_\alpha \neq 0$. Its leading coefficient is $c_{\operatorname{LE}(f)}$.
4. Let $f, g \neq 0$ with $\alpha = \operatorname{LE}(f)$, $\beta = \operatorname{LE}(g)$, and let $g$ have leading coefficient $1$. Each monomial of $fg$ comes from some $x^{\alpha'} x^{\beta'}$ with $\alpha' \le \alpha$ and $\beta' \le \beta$. By step 2, $\alpha' + \beta' \le \alpha + \beta$.
5. Equality $\alpha' + \beta' = \alpha + \beta$ holds only for $\alpha' = \alpha$, $\beta' = \beta$: if $\alpha' < \alpha$, then $\alpha' + \beta' < \alpha + \beta' \le \alpha + \beta$. So $fg$ has leading exponent $\alpha + \beta$ and the leading coefficient of $f$.
6. The [[elementary symmetric polynomial|0ZMY8441GW]] $e_k$ has leading exponent $(1, \dots, 1, 0, \dots, 0)$, with $k$ ones, and leading coefficient $1$.
7. For $a \in \N^n$, let $e^a = e_1^{a_1} \cdots e_n^{a_n}$. By steps 5 and 6, $e^a$ has leading coefficient $1$ and leading exponent $\mu(a) = (a_1 + \dots + a_n, \; a_2 + \dots + a_n, \; \dots, \; a_n)$.
8. The map $\mu$ is injective, since $a_n = \mu(a)_n$ and $a_k = \mu(a)_k - \mu(a)_{k+1}$. Its image is the set of $\lambda$ with $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n$: for such $\lambda$, take $a_k = \lambda_k - \lambda_{k+1}$ with $\lambda_{n+1} = 0$.

Existence.

9. Let $f$ be [[symmetric|06CTFY2DEZ]], and write $f = \sum_d f_d$, where $f_d$ collects the terms with $\abs{\alpha} = d$. A permutation of the variables maps monomials of degree $d$ to monomials of degree $d$. So each $f_d$ is symmetric, and it suffices to treat a symmetric $f$ whose monomials all have degree $d$.
10. For such $f$, we use induction on $\operatorname{LE}(f)$ in the finite totally ordered set $\set{\alpha \in \N^n : \abs{\alpha} = d}$. If $f = 0$, take $g = 0$.
11. Let $f \neq 0$, with $\lambda = \operatorname{LE}(f)$ and leading coefficient $c$. Suppose that $\lambda_i < \lambda_{i+1}$ for some $i$. Let $\lambda'$ be $\lambda$ with entries $i$ and $i+1$ swapped, so $\lambda' > \lambda$.
12. Swapping $x_i$ and $x_{i+1}$ in $f$ moves the coefficient of $x^\lambda$ to $x^{\lambda'}$. Since $f$ is symmetric, $f$ has coefficient $c \neq 0$ at $x^{\lambda'}$. This contradicts the maximality of $\lambda$, so $\lambda_1 \ge \dots \ge \lambda_n$.
13. By step 8, $\lambda = \mu(a)$ for some $a \in \N^n$. Let $h = f - c \, e^a$. Each $e_k$ has all monomials of degree $k$, so $e^a$ has all monomials of degree $\sum_k k a_k = \abs{\lambda} = d$.
14. So $h$ is symmetric with all monomials of degree $d$. All monomials of $f$ and of $e^a$ have exponent at most $\lambda$, and the coefficient of $x^\lambda$ in $h$ is $c - c = 0$.
15. So $h = 0$ or $\operatorname{LE}(h) < \lambda$. By induction, $h = g_1(e_1, \dots, e_n)$ for some $g_1 \in R[y_1, \dots, y_n]$. Then $f = g(e_1, \dots, e_n)$ with $g = g_1 + c \, y_1^{a_1} \cdots y_n^{a_n}$.

Uniqueness.

16. If $g(e_1, \dots, e_n) = g'(e_1, \dots, e_n)$, then $g - g'$ maps to $0$. So it suffices to show: if $g = \sum_a c_a y^a \neq 0$, then $g(e_1, \dots, e_n) = \sum_a c_a e^a \neq 0$.
17. The exponents $\mu(a)$ with $c_a \neq 0$ are distinct by step 8. Let $a^*$ be the one with the largest $\mu(a)$.
18. The term $c_{a^*} e^{a^*}$ has coefficient $c_{a^*}$ at $x^{\mu(a^*)}$, by step 7. Every other term $c_a e^a$ has all exponents at most $\mu(a) < \mu(a^*)$, so it contributes $0$ there.
19. So $g(e_1, \dots, e_n)$ has coefficient $c_{a^*} \neq 0$ at $x^{\mu(a^*)}$. Hence it is nonzero, and $g$ is unique.

## Idea

The leading monomial of a symmetric polynomial has decreasing exponents, and exactly one product of the $e_k$ has that same leading monomial with coefficient $1$. Subtracting the right multiple of it lowers the leading monomial, so the process ends. Different products of the $e_k$ have different leading monomials, so no nontrivial combination of them can vanish.
