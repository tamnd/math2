---
tag: E78DJVFY8M
kind: proof
name: Proof of the derivative of a continuous linear map
msc: [26B05]
proves: 0CYYAF8AD2
uses: [08EVNYZF42, 0RJF668P1T]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Example 8.3.3
---

## Proof

We check the definition directly: the error term is $0$.

1. Let $V$, $W$ and $A$ be as in the statement, and let $x \in V$. The domain of $A$ is $V$, which is open in $V$.
2. Let $h \in V$ with $h \ne 0$. Since $A$ is a [[linear map|0RJF668P1T]], $A(x + h) = A x + A h$.
3. So $A(x + h) - A(x) - A h = 0$, and the quotient $\|A(x + h) - A(x) - A h\| / \|h\|$ equals $0$ for each $h \ne 0$.
4. Hence this quotient tends to $0$ as $h \to 0$.
5. The map $A$ is linear and bounded by hypothesis. By the definition of the [[Fréchet derivative|08EVNYZF42]], $A$ is Fréchet differentiable at $x$ with $DA(x) = A$.
6. Since $x \in V$ was arbitrary, this holds at each point of $V$.

## Idea

A linear map is its own best linear approximation. The error $A(x + h) - A x - A h$ is exactly $0$ by linearity, so the quotient in the defining limit is $0$ for each $h$.
