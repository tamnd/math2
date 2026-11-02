---
tag: FWRW7BYX6T
kind: definition
name: Variational integrator
msc: [65P10, 37M15]
defines: 4KZ458T2QA
uses: [PS0VV149ET, VQ2BTYFST4, ESWE8Y3JD4]
sources:
  - url: https://en.wikipedia.org/wiki/Variational_integrator
---

## Definition

Let $L \colon \R^d \times \R^d \to \R$, $(q, \dot q) \mapsto L(q, \dot q)$, be a smooth Lagrangian, and fix a step size $h > 0$.
A discrete Lagrangian is a smooth function $L_h \colon \R^d \times \R^d \to \R$ that approximates the action:
$$L_h(q_0, q_1) \approx \int_0^h L(q(t), \dot q(t))\, dt.$$
Here $q$ is the solution of the [[Euler–Lagrange equation|PS0VV149ET]] with $q(0) = q_0$ and $q(h) = q_1$.
The discrete action of a sequence $q_0, \ldots, q_N$ is $S_h = \sum_{k=0}^{N-1} L_h(q_k, q_{k+1})$.
The *variational integrator* defined by $L_h$ is the map $(q_{k-1}, q_k) \mapsto (q_k, q_{k+1})$ given by the discrete Euler–Lagrange equations:
$$D_2 L_h(q_{k-1}, q_k) + D_1 L_h(q_k, q_{k+1}) = 0.$$
Here $D_1$ and $D_2$ denote the gradients with respect to the first and the second argument.
These are the equations $\partial S_h / \partial q_k = 0$ for $1 \le k \le N - 1$, with $q_0$ and $q_N$ fixed.

## Remarks

Example: take $L(q, \dot q) = \frac12 \abs{\dot q}^2 - V(q)$ and
$$L_h(q_0, q_1) = \frac{h}{2} \abs{\frac{q_1 - q_0}{h}}^2 - \frac{h}{2} \left( V(q_0) + V(q_1) \right).$$
Then $D_2 L_h(q_{k-1}, q_k) = \frac{q_k - q_{k-1}}{h} - \frac{h}{2} \nabla V(q_k)$ and $D_1 L_h(q_k, q_{k+1}) = -\frac{q_{k+1} - q_k}{h} - \frac{h}{2} \nabla V(q_k)$.
Their sum vanishes exactly when $q_{k+1} - 2 q_k + q_{k-1} = -h^2 \nabla V(q_k)$, which is the [[Störmer–Verlet method|ESWE8Y3JD4]].
Every variational integrator is symplectic in the variables $(q_k, p_k)$ with $p_k = -D_1 L_h(q_k, q_{k+1})$, when $L_h$ is regular, that is, when this relation can be solved for $q_{k+1}$.
So variational integrators are [[geometric integrators|VQ2BTYFST4]] for symplecticity.
If $L_h$ approximates the exact action to order $r$, then the method has order at least $r$.

## Explanations

### L1 human

Instead of discretising the equation of motion, one discretises the action and asks it to be stationary.
The equations that come out are the numerical method.
