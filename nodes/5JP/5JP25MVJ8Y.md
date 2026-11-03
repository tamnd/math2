---
tag: 5JP25MVJ8Y
kind: statement
role: theorem
name: Deficiency zero theorem
msc: ["92E20", 37N25, 34D23]
uses: [KCGE92DJ1W, 0N8NGKDZDZ, 0NB689782W, 01REYCJ371]
about: [KCGE92DJ1W]
sources:
  - url: https://en.wikipedia.org/wiki/Chemical_reaction_network_theory
---

## Statement

Let $(\mathcal{C}, \mathcal{R})$ be a [[chemical reaction network|KCGE92DJ1W]] on $m$ species with deficiency $\delta = 0$.

1. If the network is not weakly reversible, then for every choice of rate constants the mass-action system has no [[equilibrium|0N8NGKDZDZ]] in $\R_{>0}^m$.
2. If the network is weakly reversible, then for every choice of rate constants, each positive stoichiometric compatibility class contains exactly one equilibrium in $\R_{>0}^m$. This equilibrium is [[asymptotically stable|0NB689782W]] relative to its class, and the system has no nonconstant periodic solution in $\R_{>0}^m$.

## Remarks

The theorem is due to Feinberg, Horn and Jackson.
The proof of part 2 shows first that deficiency zero and weak reversibility force every positive equilibrium to be complex balanced.
This means that, for each complex, the total rate of the reactions out of it equals the total rate of the reactions into it.
For complex balanced systems, Horn and Jackson showed that the function $G(x) = \sum_i \big(x_i (\ln x_i - \ln \bar x_i - 1) + \bar x_i\big)$ is a strict [[Lyapunov function|01REYCJ371]] around a positive equilibrium $\bar x$, which gives uniqueness in each class and stability.
Example: for $X_1 \rightleftharpoons 2X_2$ with rate constants $k_1, k_2$, the equilibria satisfy $k_1 x_1 = k_2 x_2^2$, and the class $x_1 + x_2/2 = c$ with $c > 0$ meets this curve in exactly one positive point.
For $X_1 \to X_2$, also of deficiency zero, $\dot x_1 = -k x_1$ has no positive equilibrium, as part 1 predicts.
The conclusion holds for all rate constants, which matters because rate constants are rarely known precisely.

## Explanations

### L1 human

Some reaction networks are so simple in structure that their behaviour can be predicted without knowing any reaction speeds.
The deficiency is a number computed by counting the complexes, the connected pieces of the reaction graph and the independent directions of change.
When it is zero and every reaction can be undone by a chain of reactions, the chemistry always settles to one balanced state.
There is no oscillation and no switch between several states.
When it is zero but some reaction cannot be undone, there is no balanced state with all species present.

### L2 human

The theorem is a model of how chemical reaction network theory works: a graph-theoretic and linear-algebraic count gives a dynamical conclusion valid for all parameters.
It rules out multistability and sustained oscillation, so networks that show these, such as the [[Brusselator|FZ6XTJ3FT9]], must have positive deficiency or fail weak reversibility.
The deficiency one theorem and the theory of complex balanced systems extend it.
Whether the unique equilibrium attracts the whole positive class, not only nearby points, is the [[global attractor conjecture|MFFYGC03GV]].
