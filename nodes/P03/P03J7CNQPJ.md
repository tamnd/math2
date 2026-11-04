---
tag: P03J7CNQPJ
kind: proof
name: Proof of the second fundamental theorem of calculus
msc: [26A42]
proves: 0XYAFCN0PT
uses: [0N1JQXZXHC, 0QM4TXT3DR, 0HBY48G8G1, 04GM4NYXJB, 069P20KYQT, 0A3GWZ86AY, 0BARQY52N5]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.45
---

## Proof

We show that $F(b) - F(a)$ is a Riemann sum of $f$ for every partition.

1. Let $a < b$, let $F$ be continuous on $[a, b]$ and differentiable on $(a, b)$, and let $f \colon [a, b] \to \mathbb{R}$ be [[Riemann integrable|0N1JQXZXHC]] with $f = F'$ on $(a, b)$. Let $I = \int_a^b f(x) \, dx$ be its [[integral|0QM4TXT3DR]].
2. Let $P = (x_0, \dots, x_n)$ be a [[partition|069P20KYQT]] of $[a, b]$. The sum telescopes: $F(b) - F(a) = \sum_{i=1}^{n} \big(F(x_i) - F(x_{i-1})\big)$.
3. Fix $i$. The function $F$ is continuous on $[x_{i-1}, x_i]$ and differentiable on $(x_{i-1}, x_i) \subseteq (a, b)$.
   By the [[mean value theorem|0BARQY52N5]], there is $c_i \in (x_{i-1}, x_i)$ with $F(x_i) - F(x_{i-1}) = F'(c_i)(x_i - x_{i-1}) = f(c_i)(x_i - x_{i-1})$.
4. The points $c_i$ are tags for $P$. By steps 2 and 3, $F(b) - F(a) = S(f, P, c)$, the [[Riemann sum|0HBY48G8G1]] of $f$ for $(P, c)$.
5. Let $\varepsilon > 0$. By integrability, there is $\delta > 0$ with $|S(f, P, t) - I| < \varepsilon$ for every tagged partition of [[mesh|04GM4NYXJB]] less than $\delta$.
6. By the [[Archimedean property|0A3GWZ86AY]], take $n$ with $n \delta > b - a$, and the partition $P$ with points $a + i (b - a)/n$. Its mesh is less than $\delta$.
7. With the tags $c$ of step 3 for this $P$, steps 4 and 5 give $|F(b) - F(a) - I| < \varepsilon$.
8. This holds for each $\varepsilon > 0$. So $\int_a^b f(x) \, dx = F(b) - F(a)$.

## Idea

On each piece of a partition, the mean value theorem turns the increase of $F$ into $f$ at some point times the length of the piece. So the total increase $F(b) - F(a)$ is exactly a Riemann sum of $f$, for every partition. Fine partitions make Riemann sums close to the integral, so the two numbers agree.
