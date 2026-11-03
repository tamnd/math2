---
tag: YBSTEYPVDF
kind: definition
name: Richardson number
msc: ["76E20", 76F45, 76M55]
defines: 6CXB96Y39R
uses: [T3R5FWV91P, XQ82TE42FH, TXQQQG9T2S]
sources:
  - url: https://en.wikipedia.org/wiki/Richardson_number
---

## Definition

Consider a horizontal shear flow $U(z)$ in a stratified [[Boussinesq|TXQQQG9T2S]] fluid with [[Brunt–Väisälä frequency|XQ82TE42FH]] $N(z)$, where $z$ is the height.
At a height where $U'(z) \ne 0$, the *gradient Richardson number* is
$$\mathrm{Ri}(z) = \frac{N^2(z)}{\big( U'(z) \big)^2}.$$
For a flow with a velocity difference $\Delta U \ne 0$ and a reduced gravity $g' = g \, \Delta\rho / \rho_0$ across a layer of thickness $h$, the *bulk Richardson number* is $\mathrm{Ri}_b = g' h / (\Delta U)^2$.

## Remarks

Both forms are dimensionless, since $N$ and $U'$ are rates with dimension $\mathsf{T}^{-1}$.
The [[Miles–Howard theorem|PAFD50PFXX]] states that an inviscid stratified parallel shear flow with $\mathrm{Ri} \ge 1/4$ everywhere is linearly stable.

Example: $U(z) = S z$ with constant shear $S = 10^{-2}$ s$^{-1}$ and $N = 10^{-2}$ s$^{-1}$ gives $\mathrm{Ri} = 1$, so the Miles–Howard criterion applies and the flow is linearly stable.

Non-example: the ratio $N / \abs{U'}$ is not the Richardson number; it is its square root, and the threshold $1/4$ would become $1/2$.
