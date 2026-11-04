---
tag: 7MQHPHHYZ0
kind: proof
name: Proof of the gradient theorem
msc: ["26B20"]
proves: 0SD237FEJD
uses: [0YS8RX87F4, 0NS2QYVC4Y, 0TCBZMEYGN, 0KXSK8TEEB, 0A8TJ0VHC7, 0W3W1VYWBP, 00ZEBSMNNV, 0NHGY0N0JB, 069P20KYQT]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient_theorem
    locator: Proof
---

## Proof

We reduce to $C^1$ pieces and apply the fundamental theorem of calculus to $\phi \circ \gamma$.

1. Since $\gamma$ is piecewise $C^1$, there is a [[partition|069P20KYQT]] $a = p_0 < \dots < p_m = b$ such that the restriction $\gamma^{(l)}$ of $\gamma$ to $[p_{l-1}, p_l]$ is $C^1$ for each $l$.
2. Since $\phi$ is of [[class $C^1$|0TCBZMEYGN]], its partial derivatives are continuous on $U$. So the [[gradient|0NS2QYVC4Y]] field $\nabla \phi$ is continuous, and its [[line integrals|0YS8RX87F4]] over $\gamma$ and over each $\gamma^{(l)}$ are defined.
3. By [[additivity under concatenation|00ZEBSMNNV]], applied $m - 1$ times, $\int_\gamma \nabla \phi \cdot d\mathbf{r} = \sum_{l=1}^{m} \int_{\gamma^{(l)}} \nabla \phi \cdot d\mathbf{r}$.
4. By the [[parametric formula|0W3W1VYWBP]], $\int_{\gamma^{(l)}} \nabla \phi \cdot d\mathbf{r} = \int_{p_{l-1}}^{p_l} \nabla \phi(\gamma(t)) \cdot \gamma'(t) \, dt$.
5. Since its partial derivatives are continuous, $\phi$ is differentiable at each point of $U$, by [[continuous partial derivatives imply differentiability|0KXSK8TEEB]].
6. Let $t \in (p_{l-1}, p_l)$. By the [[chain rule for a composition with a curve|0A8TJ0VHC7]] on the open interval $(p_{l-1}, p_l)$, $(\phi \circ \gamma)'(t) = D\phi(\gamma(t))(\gamma'(t))$.
7. By the definition of the gradient, $D\phi(\gamma(t))(\gamma'(t)) = \nabla \phi(\gamma(t)) \cdot \gamma'(t)$.
8. The function $\phi \circ \gamma$ is continuous on $[p_{l-1}, p_l]$. The function $t \mapsto \nabla \phi(\gamma(t)) \cdot \gamma'(t)$ is continuous there, and by steps 6 and 7 it is the derivative of $\phi \circ \gamma$ on the open interval.
9. By the [[fundamental theorem of calculus|0NHGY0N0JB]], $\int_{p_{l-1}}^{p_l} \nabla \phi(\gamma(t)) \cdot \gamma'(t) \, dt = \phi(\gamma(p_l)) - \phi(\gamma(p_{l-1}))$.
10. Summing over $l$ with steps 3 and 4, the sum telescopes: $\int_\gamma \nabla \phi \cdot d\mathbf{r} = \phi(\gamma(p_m)) - \phi(\gamma(p_0)) = \phi(\gamma(b)) - \phi(\gamma(a))$.

## Idea

Along the curve, the integrand $\nabla \phi(\gamma(t)) \cdot \gamma'(t)$ is the derivative of $\phi(\gamma(t))$, by the chain rule. So the line integral is the integral of a derivative, and the fundamental theorem of calculus leaves only the values of $\phi$ at the ends.
