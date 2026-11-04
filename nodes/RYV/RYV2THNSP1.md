---
tag: RYV2THNSP1
kind: proof
name: Proof of the derivative of a map into a product
msc: [26B05]
proves: 0QQMXFTX0A
uses: [08EVNYZF42, 0MN882VJ4P, 0F3K4C7XYW]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.3.9
---

## Proof

With the max norm, the error of $F$ is small exactly when both errors are small.

1. Let $V$, $W_1$, $W_2$, $U$, $x$, $f_1$, $f_2$ and $F$ be as in the statement. Put $A_1 = Df_1(x)$ and $A_2 = Df_2(x)$.
2. Define $A \colon V \to W_1 \times W_2$ by $A h = (A_1 h, A_2 h)$. It is linear, since $A_1$ and $A_2$ are linear and the vector operations on $W_1 \times W_2$ act on each factor.
3. Since $A_1$ and $A_2$ are [[bounded|0F3K4C7XYW]], there are $C_1, C_2 \ge 0$ with $\|A_i h\| \le C_i \|h\|$ for $i = 1, 2$ and each $h \in V$.
4. So $\|A h\| = \max(\|A_1 h\|, \|A_2 h\|) \le \max(C_1, C_2) \|h\|$, and $A$ is bounded.
5. For $h \in V$ with $x + h \in U$, put $r_i(h) = f_i(x + h) - f_i(x) - A_i h$ for $i = 1, 2$.
6. Then $F(x + h) - F(x) - A h = (r_1(h), r_2(h))$. Its norm is $\max(\|r_1(h)\|, \|r_2(h)\|)$.
7. Let $\varepsilon > 0$. By the [[little-o form of the derivative|0MN882VJ4P]] for $f_1$ and $f_2$, there are $\delta_1, \delta_2 > 0$ with $\|r_i(h)\| \le \varepsilon \|h\|$ for $\|h\| < \delta_i$ and $x + h \in U$.
8. Put $\delta = \min(\delta_1, \delta_2)$. For $\|h\| < \delta$ with $x + h \in U$, step 6 gives $\|F(x + h) - F(x) - A h\| \le \varepsilon \|h\|$.
9. So $F(x + h) - F(x) - A h = o(\|h\|)$. By the little-o form, $F$ is [[Fréchet differentiable|08EVNYZF42]] at $x$ with $DF(x) = A$.
10. That is, $DF(x)(h) = (Df_1(x)(h), Df_2(x)(h))$ for each $h \in V$.

## Idea

The error of the pair map is the pair of the two errors. In the max norm, a pair is small exactly when both of its entries are small. So the pair of the two derivatives is a derivative of the pair map.
