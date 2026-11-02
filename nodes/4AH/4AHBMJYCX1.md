---
tag: 4AHBMJYCX1
kind: statement
role: proposition
name: Hamiltonian Monte Carlo
msc: [65C05, 65C40, 60J22]
uses: [ZGNBR2SPZ0, 0ZY9DX8FBF, 0XN3K7RSZY, 0ABK9V9Y64, 0KRH5157WP, CTGN6CK1ZS, 0EDKGA2FAK, B4C25SXFRE, GP56NBN9RY, MKHF449E22]
about: [ZGNBR2SPZ0]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_Monte_Carlo
same_as:
  wikidata: Q1639846
  wikipedia: Hamiltonian Monte Carlo
---

## Statement

Let $U \colon \R^d \to \R$ be continuously differentiable with $Z = \int_{\R^d} e^{-U(q)} \, dq < \infty$, and let $\pi$ be the [[probability density|0ZY9DX8FBF]] $\pi(q) = e^{-U(q)} / Z$.
Let $H(q,p) = U(q) + \tfrac{1}{2} \abs{p}^2$ for $q, p \in \R^d$.
Fix a step size $\varepsilon > 0$ and a number of steps $L \ge 1$.
The leapfrog step $\Psi(q,p) = (q', p')$ is
$$p_{1/2} = p - \tfrac{\varepsilon}{2} \nabla U(q), \qquad q' = q + \varepsilon \, p_{1/2}, \qquad p' = p_{1/2} - \tfrac{\varepsilon}{2} \nabla U(q'),$$
where $\nabla U$ is the [[gradient|0ABK9V9Y64]] of $U$, and $\Phi = \Psi^{L}$ is $L$ leapfrog steps.
One *Hamiltonian Monte Carlo* step from $q \in \R^d$ is as follows.

1. Draw $p$ from the standard [[normal distribution|0XN3K7RSZY]] on $\R^d$.
2. Compute $(q^*, p^*) = \Phi(q, p)$.
3. With probability $\min\big(1, e^{H(q,p) - H(q^*, p^*)}\big)$ move to $q^*$; otherwise stay at $q$.

Then $\pi$ is a [[stationary distribution|0KRH5157WP]] of this Markov transition: if $q$ has density $\pi$, the new state also has density $\pi$.

## Remarks

The proof works on the joint density proportional to $e^{-H(q,p)}$ on $\R^{2d}$, whose $q$-marginal is $\pi$ and whose $p$-marginal is standard normal.
Let $R(q,p) = (q,-p)$; then $F = R \circ \Phi$ is an [[involution|GP56NBN9RY]], since each leapfrog step is reversed by flipping the momentum, and $F$ preserves volume, since each of the three substeps is a shear.
A Metropolis step with a deterministic, volume-preserving, involutive proposal $F$ and acceptance probability $\min(1, e^{H - H \circ F})$ satisfies [[detailed balance|CTGN6CK1ZS]] for $e^{-H}$, and $H \circ R = H$.
Resampling $p$ in step 1 also leaves $e^{-H}$ invariant, so the composition does, and hence its $q$-marginal $\pi$ is invariant.
The leapfrog map is a [[symplectic integrator|B4C25SXFRE]] for the [[Hamiltonian system|0EDKGA2FAK]] $\dot q = p$, $\dot p = -\nabla U(q)$.
The exact flow would keep $H$ constant and always accept, and the accept step corrects the discretisation error.
Example: for $U(q) = \tfrac{1}{2} q^2$ on $\R$, the target is standard normal, and with small $\varepsilon$ the trajectories follow circles in the $(q,p)$ plane, so the chain moves far in each step.
Invariance alone does not give convergence.
For this $U$, if $\varepsilon L$ is half a period of the exact flow, the chain nearly alternates between $q$ and $-q$.
For this reason $\varepsilon$ or $L$ is often randomised in practice.
More generally $p$ may be drawn from a normal law with a positive definite mass matrix $M$, with $\tfrac{1}{2} p^T M^{-1} p$ in $H$ and $q' = q + \varepsilon M^{-1} p_{1/2}$.

## Explanations

### L1 human

Hamiltonian Monte Carlo is a way to draw random samples from a probability distribution on a high-dimensional space.
It imagines a ball rolling on a landscape whose height is $U$, so that low places are likely places.
At each step the ball gets a random kick, rolls for a while under simulated physics, and its end point is the next proposal.
A final accept-or-reject check makes the method exact despite the errors of the simulation.
The result says that, in the long run, the samples follow the intended distribution.

### L2 human

HMC is a [[Markov chain Monte Carlo|ZGNBR2SPZ0]] method that uses the gradient of the log-density to make long, directed moves.
It is a special case of the [[Metropolis–Hastings algorithm|MKHF449E22]] on the extended space of positions and momenta.
The two properties of the leapfrog map that make the acceptance rule simple are reversibility and volume preservation; energy conservation is only needed for a high acceptance rate.
Compared with random-walk proposals, HMC scales much better with dimension for smooth targets, which is why it is the default sampler in several statistics packages.
Choosing $\varepsilon$ and $L$ is the main practical difficulty, and adaptive schemes such as the no-U-turn sampler address it.
