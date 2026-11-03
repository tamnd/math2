---
tag: 5VV1H8XRJ0
kind: statement
role: proposition
name: Volterra's principle
msc: [92D25, 34C25, 92D40]
uses: [00Y5QZ82AA, 0AA97XA70K, 0N8NGKDZDZ]
about: [00Y5QZ82AA]
sources:
  - url: https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations
---

## Statement

Let $\alpha, \beta, \gamma, \delta > 0$, and consider the [[Lotka–Volterra equations|00Y5QZ82AA]]
$$x' = \alpha x - \beta x y, \qquad y' = \delta x y - \gamma y$$
for a prey population $x > 0$ and a predator population $y > 0$.

1. Every solution with $x(0), y(0) > 0$ is [[periodic|0AA97XA70K]], and if $T > 0$ is a period, then
$$\frac1T \int_0^T x(t) \, dt = \frac{\gamma}{\delta}, \qquad \frac1T \int_0^T y(t) \, dt = \frac{\alpha}{\beta}.$$
2. Let $0 < \varepsilon < \alpha$, and suppose that both species are removed at the same per capita rate $\varepsilon$, so that the system becomes $x' = (\alpha - \varepsilon) x - \beta x y$, $y' = \delta x y - (\gamma + \varepsilon) y$.
Then the time averages over a period become $(\gamma + \varepsilon)/\delta$ for the prey and $(\alpha - \varepsilon)/\beta$ for the predator.

So a moderate removal of both species raises the average prey population and lowers the average predator population.

## Remarks

For part 1, divide the second equation by $y$: $(\ln y)' = \delta x - \gamma$.
Integrate over a period; since $y(T) = y(0)$, the left side gives $0$, so $\delta \int_0^T x \, dt = \gamma T$.
The same step with $(\ln x)' = \alpha - \beta y$ gives the average of $y$.
So the time averages equal the coordinates of the positive [[equilibrium point|0N8NGKDZDZ]] $(\gamma/\delta, \alpha/\beta)$, and part 2 is part 1 with the new parameters $\alpha - \varepsilon$ and $\gamma + \varepsilon$.
The hypothesis $\varepsilon < \alpha$ is needed: if $\varepsilon \ge \alpha$, the prey has no positive growth rate even without predators, and there is no positive equilibrium.

## Explanations

### L1 human

In a predator–prey cycle, the averages of the two populations over a cycle equal the balance point of the system.
If fishing or a pesticide kills prey and predators alike, the balance point moves: more prey, fewer predators.
Vito Volterra used this to explain why the share of predatory fish in Adriatic catches rose when fishing was reduced during the First World War.

### L2 human

The principle comes from the simple fact that the averages over a cycle equal the equilibrium values, which is a feature of the Lotka–Volterra model and its first integral.
It warns that a pesticide that kills both a pest and its natural enemy can make the pest more abundant on average.
In models with self-limitation of the prey, such as a logistic prey term, the orbits are no longer closed.
Still, uniform harvesting moves the equilibrium in the same direction.
