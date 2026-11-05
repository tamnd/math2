---
tag: 9EE1HV8V0T
kind: statement
role: proposition
name: Equivalent formulations of locality axiom
sources:
  - wikipedia: en:1287577@r1334573756
    locator: Vertex operator algebra, section Formal definition > Vertex algebra > Axioms > Equivalent formulations of locality axiom
    note: adopted
    mention: wikipedia://en/1287577#0M57
    sections: [Statement]
inventory: [K6HSYDQ2JQ]
---

## Statement

The locality axiom has several equivalent formulations in the literature, e.g., Frenkel–Lepowsky–Meurman introduced the Jacobi identity: $\forall u,v,w\in V$,

$$\begin{aligned}&z^{-1}\delta\left(\frac{x-y}{z}\right)Y(u,x)Y(v,y)w - z^{-1}\delta\left(\frac{-y+x}{z}\right)Y(v,y)Y(u,x)w \\&= y^{-1}\delta\left(\frac{x-z}{y}\right)Y(Y(u,z)v,y)w\end{aligned},$$

where we define the formal delta series by:

$$\delta\left(\frac{x-y}{z}\right) := \sum_{s \geq 0, r \in \mathbf{Z}} \binom{r}{s} (-1)^s y^{r-s}x^s z^{-r}.$$

Borcherds initially used the following two identities: for any $u,v,w\in V$ and integers $m,n$ we have

$$(u_m (v))_n (w) = \sum_{i \geq 0} (-1)^i \binom{m}{i} \left (u_{m-i} (v_{n+i} (w)) - (-1)^m v_{m+n-i} (u_i (w)) \right)$$

and

$$u_m v=\sum_{i\geq 0}(-1)^{m+i+1}\frac{T^{i}}{i!}v_{m+i}u.$$

He later gave a more expansive version that is equivalent but easier to use: for any $u,v,w\in V$ and integers $m,n,q$ we have

$$\sum_{i \in \mathbf{Z}} \binom{m}{i} \left(u_{q+i} (v) \right )_{m+n-i} (w) = \sum_{i\in \mathbf{Z}} (-1)^i \binom{q}{i} \left (u_{m+q-i} \left(v_{n+i} (w) \right ) - (-1)^q v_{n+q-i} \left (u_{m+i} (w) \right ) \right)$$

This identity is the same as the Jacobi identity by expanding both sides in all formal variables. Finally, there is a formal function version of locality: For any $u,v,w\in V$, there is an element

$$X(u,v,w;z,x) \in V[[z,x]] \left[z^{-1}, x^{-1}, (z-x)^{-1} \right]$$

such that $Y(u,z)Y(v,x)w$ and $Y(v,x)Y(u,z)w$ are the corresponding expansions of $X(u,v,w;z,x)$ in $V((z))((x))$ and $V((x))((z))$.
