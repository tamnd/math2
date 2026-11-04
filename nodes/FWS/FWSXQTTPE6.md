---
tag: FWSXQTTPE6
kind: proof
name: Proof of the general solution of an inhomogeneous linear equation
msc: [34A30]
proves: 0GHWEH6H15
uses: [0PB7K8M7FG, 0EQZSAB9EC, 0H4KNNCHPY, 0F2VBPXNP9, 0M0TKFRX2A]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_differential_equation
    locator: Linear differential operator
---

## Proof

1. Let $u, v : I \to \R$ be $n$ times differentiable and $\alpha, \beta \in \R$. By [[linearity of differentiation|0M0TKFRX2A]], applied $k$ times, $(\alpha u + \beta v)^{(k)} = \alpha u^{(k)} + \beta v^{(k)}$ for $k \le n$.
2. Multiplying by $a_k$ and adding over $k$ gives $L(\alpha u + \beta v) = \alpha L u + \beta L v$ on $I$. This is the computation of the [[superposition principle|0F2VBPXNP9]].
3. Let $S$ be the set of solutions of the [[homogeneous equation|0EQZSAB9EC]] $L y = 0$ on $I$. Since $(y_1, \dots, y_n)$ is a [[fundamental system|0H4KNNCHPY]], it is a basis of $S$.
4. Assume $y$ is a solution of the [[linear equation|0PB7K8M7FG]] $L y = b$ on $I$. Then $y - y_p$ is $n$ times differentiable, and $L(y - y_p) = L y - L y_p = b - b = 0$ by step 2.
5. So $y - y_p \in S$. By step 3, $y - y_p = c_1 y_1 + \dots + c_n y_n$ for some real numbers $c_1, \dots, c_n$. This gives the stated form of $y$.
6. Conversely, let $y = y_p + c_1 y_1 + \dots + c_n y_n$ with $c_1, \dots, c_n \in \R$. Then $y$ is $n$ times differentiable, as a combination of such functions.
7. By step 2, $L y = L y_p + c_1 L y_1 + \dots + c_n L y_n = b + 0 + \dots + 0 = b$ on $I$. So $y$ solves $L y = b$ on $I$.

## Idea

The operator $L$ is linear. So two solutions of $L y = b$ differ by a solution of $L y = 0$. The fundamental system describes all solutions of $L y = 0$, and adding $y_p$ describes all solutions of $L y = b$.
