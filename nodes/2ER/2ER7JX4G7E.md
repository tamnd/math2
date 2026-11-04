---
tag: 2ER7JX4G7E
kind: proof
name: Proof of the area of a region as a line integral
msc: ["26B20"]
proves: 09CBQB6V67
uses: [0HR3N02317, 0YS8RX87F4, 0D032NSZKY, 0NKBMFC18R]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_theorem
    locator: Area calculation
---

## Proof

We apply Green's theorem three times.

1. The area of $D$ is $A = \iint_D 1 \, dA$, the [[double integral|0NKBMFC18R]] of the constant $1$ over $D$.
2. Take $L = 0$ and $M = x$. These have continuous partial derivatives on $\R^2$, and $\partial M / \partial x - \partial L / \partial y = 1$.
3. By [[Green's theorem|0HR3N02317]] for the [[simple closed curve|0D032NSZKY]] $C$, the [[line integral|0YS8RX87F4]] $\oint_C x \, dy$ equals $\iint_D 1 \, dA = A$.
4. Take $L = -y$ and $M = 0$. Then $\partial M / \partial x - \partial L / \partial y = 0 - (-1) = 1$. Green's theorem gives $-\oint_C y \, dx = \oint_C (-y) \, dx = A$.
5. Take $L = -y/2$ and $M = x/2$. Then $\partial M / \partial x - \partial L / \partial y = \tfrac{1}{2} + \tfrac{1}{2} = 1$. Green's theorem gives $\tfrac{1}{2} \oint_C (x \, dy - y \, dx) = A$.
6. Steps 3 to 5 give $A = \oint_C x \, dy = -\oint_C y \, dx = \tfrac{1}{2} \oint_C (x \, dy - y \, dx)$.

## Idea

Green's theorem turns a line integral into the double integral of $\partial M / \partial x - \partial L / \partial y$. If this expression is the constant $1$, the double integral is the area. Each of the three choices of $(L, M)$ has this property.
