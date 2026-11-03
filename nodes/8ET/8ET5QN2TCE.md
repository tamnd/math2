---
tag: 8ET5QN2TCE
kind: definition
name: Airy and Pratt models of isostasy
msc: [86A60, 86A30]
defines: 9W8W6DVCPX
uses: [7CJTGB6M0V]
sources:
  - url: https://en.wikipedia.org/wiki/Isostasy
---

## Definition

Consider land columns in [[isostatic equilibrium|7CJTGB6M0V]], and let $h \ge 0$ be the surface height of a column above sea level.

1. *Airy model.* The crust has constant density $\rho_c$, the mantle has constant density $\rho_m > \rho_c$, and a column of height $0$ has crustal thickness $H$. A column of height $h$ has a root of thickness $r$ below depth $H$, with
$$r = \frac{\rho_c}{\rho_m - \rho_c}\, h.$$
2. *Pratt model.* All columns have their base at the same depth $D$ below sea level, and a column of height $0$ has density $\rho_0$. A column of height $h$ has constant density $\rho(h)$, with
$$\rho(h)\,(D + h) = \rho_0\, D.$$

## Remarks

Check of the Airy relation: down to depth $H + r$, the column of height $h$ has mass $\rho_c (h + H + r)$ per unit area, and the reference column has $\rho_c H + \rho_m r$.
These are equal exactly when $\rho_c h = (\rho_m - \rho_c) r$.
Example: with $\rho_c = 2.8$ and $\rho_m = 3.3$ g/cm$^3$, a plateau of height $h = 5$ km has an Airy root of $r = 28$ km.
In the Pratt model with $D = 100$ km and $\rho_0 = 2.8$ g/cm$^3$, the same plateau has density $2.8 \cdot 100/105 \approx 2.67$ g/cm$^3$.
Non-example: a column of height $5$ km with density $\rho_c$ and no root fits neither model, since its extra mass is not compensated.
