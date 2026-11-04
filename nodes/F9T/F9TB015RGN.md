---
tag: F9TB015RGN
kind: statement
role: proposition
name: Change of variables formula in terms of Lebesgue measure
sources:
  - wikipedia: en:2146848@r1302582776
    locator: Change of variables, section Other examples > Integration > Change of variables formula in terms of Lebesgue measure
    note: adopted
    mention: wikipedia://en/2146848#PYNZ
    sections: [Statement]
inventory: [9Y04AMQWHP]
---

## Statement

The following theorem allows us to relate integrals with respect to Lebesgue measure to an equivalent integral with respect to the pullback measure under a parameterization G. The proof is due to approximations of the Jordan content.

> Suppose that $\Omega$ is an open subset of $\mathbb{R}^n$ and $G:\Omega \to \mathbb{R}^n$ is a $C^1$ diffeomorphism.
>
> If $f$ is a Lebesgue measurable function on $G(\Omega)$, then $f \circ G$ is Lebesgue measurable on $\Omega$. If $f \geq 0$ or $f\in L^1(G(\Omega),m),$ then $\int_{G(\Omega)} f(x) dx = \int_\Omega f\circ G(x)|\text{det}D_xG|dx$.
>
> If $E\subset \Omega$ and $E$ is Lebesgue measurable, then $G(E)$ is Lebesgue measurable, then $m(G(E)) = \int_E |\text{det}D_xG| dx$.

As a corollary of this theorem, we may compute the Radon–Nikodym derivatives of both the pullback and pushforward measures of $m$ under $T$.
