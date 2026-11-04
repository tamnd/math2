---
tag: MVNYPYMTG4
kind: proof
name: Proof of the linearity of the integral
msc: [26A42]
proves: 080RWVVSB6
uses: [0N1JQXZXHC, 0QM4TXT3DR, 0HBY48G8G1, 04GM4NYXJB, 03HF5PMY5T, 0GMV7GP8W0]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorems 1.23, 1.24 and Definition 1.85
---

## Proof

We work directly with Riemann sums.

1. Let $a < b$, let $f, g \colon [a, b] \to \mathbb{R}$ be [[Riemann integrable|0N1JQXZXHC]], and let $\alpha, \beta \in \mathbb{R}$. Let $I_f$ and $I_g$ be their [[integrals|0QM4TXT3DR]], and let $h = \alpha f + \beta g$.
2. For each tagged partition $(P, t)$ with $P = (x_0, \dots, x_n)$, the [[Riemann sums|0HBY48G8G1]] satisfy
   $$S(h, P, t) = \sum_{i=1}^{n} \big(\alpha f(t_i) + \beta g(t_i)\big)(x_i - x_{i-1}) = \alpha S(f, P, t) + \beta S(g, P, t).$$
3. Let $\varepsilon > 0$. Take $\delta_f > 0$ with $|S(f, P, t) - I_f| < \frac{\varepsilon}{2(|\alpha| + 1)}$ for all tagged partitions of [[mesh|04GM4NYXJB]] less than $\delta_f$.
   Take $\delta_g > 0$ in the same way for $g$, with $\frac{\varepsilon}{2(|\beta| + 1)}$. Let $\delta = \min(\delta_f, \delta_g)$.
4. Let $(P, t)$ be a tagged partition of mesh less than $\delta$. By step 2, the [[triangle inequality|03HF5PMY5T]] and [[multiplicativity of the absolute value|0GMV7GP8W0]],
   $$\big|S(h, P, t) - (\alpha I_f + \beta I_g)\big| \le |\alpha| \, |S(f, P, t) - I_f| + |\beta| \, |S(g, P, t) - I_g|.$$
5. By step 3, the right side is at most $\frac{|\alpha| \varepsilon}{2(|\alpha| + 1)} + \frac{|\beta| \varepsilon}{2(|\beta| + 1)} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$.
6. So the number $\alpha I_f + \beta I_g$ has the property in the definition of integrability for $h$. Hence $h$ is Riemann integrable, and $\int_a^b h(x) \, dx = \alpha \int_a^b f(x) \, dx + \beta \int_a^b g(x) \, dx$.

## Idea

A Riemann sum is a finite sum, so it is linear in the function. If the sums of $f$ and of $g$ are close to their integrals for fine partitions, then the sums of $\alpha f + \beta g$ are close to $\alpha I_f + \beta I_g$ for the same partitions.
