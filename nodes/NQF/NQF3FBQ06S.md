---
tag: NQF3FBQ06S
kind: proof
name: Proof of the product of exponentials by the Cauchy product
msc: [33B10]
proves: 0WM7DJCM6G
uses: [054VXHMCA3, 0EHWPWGHB2, 0AN28XQ45Z, 0B1K9PVWE9, 0HYNZE940T, 0KW2X0TFBX, 03HF5PMY5T, 0734RSVF2V, 0RAM4E07NR, 0XMF00T4XQ, 0FRSR10DWF]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_product
    locator: Examples
---

## Proof

We compare the partial sums of $e^{z+w}$ with products of partial sums, and bound the difference by the same comparison for $|z|$ and $|w|$.

1. A sequence $(u_N)$ of complex numbers converges to $u$ when $|u_N - u| \to 0$, with $|\cdot|$ the [[modulus|0KW2X0TFBX]].
Since $|\operatorname{Re} v|, |\operatorname{Im} v| \le |v| \le |\operatorname{Re} v| + |\operatorname{Im} v|$, this means that the real parts and the imaginary parts converge.
These inequalities follow by squaring, since $|v|^2 = (\operatorname{Re} v)^2 + (\operatorname{Im} v)^2$.
Limits of complex sequences are unique, because limits of real sequences are.
2. Fix $z, w \in \C$. For $j, k \ge 0$ let $t_{j k} = \dfrac{z^j w^k}{j! \, k!}$.
For $N \ge 0$ let $A_N = \sum_{j=0}^{N} \dfrac{z^j}{j!}$, $B_N = \sum_{k=0}^{N} \dfrac{w^k}{k!}$ and $D_N = \sum_{n=0}^{N} \dfrac{(z + w)^n}{n!}$.
By the definition of the [[complex exponential|054VXHMCA3]], $A_N \to e^z$, $B_N \to e^w$ and $D_N \to e^{z+w}$.
3. Since $\C$ is a commutative ring by [[the complex numbers form a field|0FRSR10DWF]], the [[binomial theorem|0EHWPWGHB2]] applies.
Using $\binom{n}{j} / n! = 1 / \bigl(j! (n - j)!\bigr)$, it gives $\dfrac{(z + w)^n}{n!} = \sum_{j + k = n} t_{j k}$.
4. Let $T_N$ be the set of pairs $(j, k)$ of natural numbers with $j + k \le N$, and $Q_N$ the set of pairs with $j \le N$ and $k \le N$.
By step 3, $D_N = \sum_{(j,k) \in T_N} t_{j k}$. By distributivity, $A_N B_N = \sum_{(j,k) \in Q_N} t_{j k}$.
5. Since $T_N \subseteq Q_N$, the difference is $\Delta_N = A_N B_N - D_N = \sum_{(j,k) \in Q_N \setminus T_N} t_{j k}$.
6. Let $x = |z|$ and $y = |w|$. Define $a_N$, $b_N$, $d_N$ and $\delta_N = a_N b_N - d_N$ by the same formulas with $x, y$ in place of $z, w$.
By steps 3 to 5 for $x$ and $y$, $\delta_N = \sum_{(j,k) \in Q_N \setminus T_N} \dfrac{x^j y^k}{j! \, k!}$.
7. Since the [[modulus is multiplicative|0HYNZE940T]], $|t_{j k}| = \dfrac{x^j y^k}{j! \, k!}$.
Also $|\operatorname{Re} t_{j k}| \le |t_{j k}|$, since $(\operatorname{Re} t)^2 \le (\operatorname{Re} t)^2 + (\operatorname{Im} t)^2$.
8. The real part of a sum is the sum of the real parts. By the [[triangle inequality|03HF5PMY5T]] for finite sums of reals and step 7, $|\operatorname{Re} \Delta_N| \le \delta_N$.
In the same way, $|\operatorname{Im} \Delta_N| \le \delta_N$.
9. The series $\sum x^j / j!$ and $\sum y^k / k!$ converge to the real numbers $e^x$ and $e^y$. Their terms are nonnegative, so they converge absolutely.
10. By the [[limit of a product|0734RSVF2V]], $a_N b_N \to e^x e^y$.
11. The [[Cauchy product|0B1K9PVWE9]] of these two series has $n$th term $\sum_{j + k = n} x^j y^k / (j! \, k!)$, so its partial sums are the $d_N$.
By the theorem on the [[Cauchy product of absolutely convergent series|0AN28XQ45Z]], $d_N \to e^x e^y$.
12. By steps 10 and 11 and the [[limit of a sum|0RAM4E07NR]], $\delta_N \to 0$.
13. By step 8, $-\delta_N \le \operatorname{Re} \Delta_N \le \delta_N$. The [[squeeze theorem|0XMF00T4XQ]] gives $\operatorname{Re} \Delta_N \to 0$. Likewise $\operatorname{Im} \Delta_N \to 0$, so $\Delta_N \to 0$.
14. We have $\operatorname{Re}(A_N B_N) = \operatorname{Re} A_N \operatorname{Re} B_N - \operatorname{Im} A_N \operatorname{Im} B_N$, and a similar formula for the imaginary part.
By the limit rules for real products and sums, $A_N B_N \to e^z e^w$.
15. By steps 13 and 14, $D_N = A_N B_N - \Delta_N \to e^z e^w$.
16. By step 2, also $D_N \to e^{z+w}$. Limits are unique, so $e^{z + w} = e^z e^w$.

## Idea

Multiplying two partial sums gives all terms $z^j w^k / (j! k!)$ in a square, while the binomial theorem shows that $e^{z+w}$ only collects a triangle.
The leftover corner is bounded by the same corner for $|z|$ and $|w|$.
For nonnegative reals the corner tends to $0$, by the theorem on Cauchy products.
