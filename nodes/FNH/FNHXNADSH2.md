---
tag: FNHXNADSH2
kind: definition
name: Overlapping generations model
msc: [91B62, 91B50]
defines: 1EGETCKQ02
uses: [GZZS4MTDG9, YTBPB52K27, JREVYHFY4T, 0GCM7B6PBK]
sources:
  - url: https://en.wikipedia.org/wiki/Overlapping_generations_model
---

## Definition

The *overlapping generations model with production* (Diamond model) has discrete time $t = 0, 1, 2, \dots$ and the following parts.

1. In each period $t$, a generation of $L_t = (1 + n)^t L_0$ agents is born, with $n > -1$, and each agent lives for two periods.
2. A young agent supplies one unit of labour for the wage $w_t$, consumes $c_{1,t}$ and saves $s_t = w_t - c_{1,t}$.
3. When old, the agent consumes $c_{2,t+1} = R_{t+1} s_t$, where $R_{t+1}$ is the gross return on capital.
4. Each agent maximises $u(c_{1,t}) + \beta u(c_{2,t+1})$, where $u$ is a strictly increasing and strictly [[concave|0GCM7B6PBK]] [[utility function|GZZS4MTDG9]] and $0 < \beta$.
5. Competitive firms use a production function with intensive form $f$, and capital depreciates fully in one period, so $R_t = f'(k_t)$ and $w_t = f(k_t) - k_t f'(k_t)$.
6. The savings of the young form the next capital stock, so $k_{t+1} = s_t/(1 + n)$, where $k_t$ is capital per young worker.

A *[[competitive equilibrium|YTBPB52K27]]* is a sequence $(k_t)$ with $k_0 > 0$ given, such that all six clauses hold at every $t$.

## Remarks

Example: let $u = \ln$ and $f(k) = k^\alpha$ with $0 < \alpha < 1$.
Maximising $\ln(w - s) + \beta \ln(R s)$ gives $1/(w - s) = \beta/s$, so $s = \beta w/(1 + \beta)$.
With $w_t = (1 - \alpha) k_t^\alpha$, the capital stock follows
$$k_{t+1} = \frac{\beta (1 - \alpha)}{(1 + \beta)(1 + n)} k_t^\alpha,$$
which converges to a unique positive steady state.

Non-example: a single household that lives forever, as in the Ramsey–Cass–Koopmans model, is not an overlapping generations model, since clause 1 requires finite lives.

The steady state may have more capital than the golden rule level.
Then the equilibrium is not [[Pareto efficient|JREVYHFY4T]], even though markets are competitive.
