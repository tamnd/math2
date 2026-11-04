---
tag: 21PKVV5S4Y
kind: proof
name: Proof of de Moivre's formula from Euler's formula
msc: [33B10]
proves: 03MTBVG3VE
uses: [04R3CY41VJ, 0WM7DJCM6G, 054VXHMCA3, 0WB57D9488]
sources:
  - url: https://en.wikipedia.org/wiki/De_Moivre%27s_formula
    locator: Relation to Euler's formula
---

## Proof

1. Let $x$ be real. Since $x$ is real, the power series of $\cos x$ and $\sin x$ are the real [[sine and cosine|0WB57D9488]].
So [[Euler's formula|04R3CY41VJ]] gives $e^{i x} = \cos x + i \sin x$ for every real $x$.
2. In the series for the [[complex exponential|054VXHMCA3]] at $0$, every term with $k \ge 1$ is $0$. So $e^0 = 1$.
3. Claim: $(e^{i x})^n = e^{i n x}$ for each integer $n \ge 0$ and each real $x$. We argue by induction on $n$.
4. For $n = 0$, both sides equal $1$, by step 2.
5. Assume the claim for $n$. By the [[product of exponentials|0WM7DJCM6G]], $(e^{i x})^{n+1} = e^{i n x} e^{i x} = e^{i (n + 1) x}$.
This proves the claim.
6. By the product of exponentials and step 2, $e^{i x} e^{-i x} = e^0 = 1$. So $e^{i x} \neq 0$ and $(e^{i x})^{-1} = e^{-i x}$.
Thus negative powers of $e^{i x}$ are defined.
7. Let $n = -m$ with $m$ a positive integer. Then $(e^{i x})^n = \bigl((e^{i x})^{-1}\bigr)^m = (e^{-i x})^m$, by step 6.
8. Step 3, applied to the real number $-x$, gives $(e^{-i x})^m = e^{-i m x} = e^{i n x}$.
So $(e^{i x})^n = e^{i n x}$ for every integer $n$.
9. By step 1 for $x$ and for $n x$, $(\cos x + i \sin x)^n = (e^{i x})^n = e^{i n x} = \cos(n x) + i \sin(n x)$.

## Idea

Euler's formula turns $\cos x + i \sin x$ into $e^{i x}$.
Powers of an exponential multiply the exponent, because exponentials turn sums into products.
Negative powers work since $e^{-ix}$ is the inverse of $e^{ix}$.
