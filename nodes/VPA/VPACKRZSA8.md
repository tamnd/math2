---
tag: VPACKRZSA8
kind: example
name: Oldroyd-B model
msc: [76A10, 76A05]
instance_of: [8DT9MB9V6R]
uses: [F16YFCJRFJ, P1KWMQG4NZ, VN6MY7KWJ8]
sources:
  - url: https://en.wikipedia.org/wiki/Oldroyd-B_model
same_as:
  wikidata: Q7085712
  wikipedia: Oldroyd-B model
---

## Example

The *Oldroyd-B model* is a constitutive law for an incompressible viscoelastic fluid, such as a dilute polymer solution.
It has a relaxation time $\lambda_1 > 0$, a retardation time $\lambda_2$ with $0 \le \lambda_2 < \lambda_1$, and a total viscosity $\eta_0 > 0$.
The extra stress $\tau$ satisfies
$$\tau + \lambda_1 \overset{\nabla}{\tau} = 2 \eta_0 \big( D + \lambda_2 \overset{\nabla}{D} \big),$$
where $\overset{\nabla}{\ }$ is the [[upper-convected time derivative|F16YFCJRFJ]] and $D$ is the [[strain rate tensor|P1KWMQG4NZ]].

Equivalently, $\tau = 2 \eta_s D + \tau_p$, where the solvent viscosity is $\eta_s = \eta_0 \lambda_2 / \lambda_1$ and the polymer stress $\tau_p$ obeys the [[upper-convected Maxwell model|VN6MY7KWJ8]] $\tau_p + \lambda_1 \overset{\nabla}{\tau_p} = 2 \eta_p D$ with $\eta_p = \eta_0 - \eta_s$.

Check in steady simple shear $u = (\dot\gamma y, 0, 0)$: the solvent part gives no normal stress, and the polymer part gives $(\tau_p)_{12} = \eta_p \dot\gamma$ and $(\tau_p)_{11} - (\tau_p)_{22} = 2 \lambda_1 \eta_p \dot\gamma^2$.
So the shear stress is $\eta_0 \dot\gamma$, and the first normal stress difference $2 \lambda_1 \eta_p \dot\gamma^2$ is nonzero.
A Newtonian fluid has no normal stress difference in this flow, so the model is a [[non-Newtonian fluid|8DT9MB9V6R]].

## Remarks

For $\lambda_2 = 0$ it is the upper-convected Maxwell model.
For $\lambda_2 = \lambda_1$ the Newtonian law $\tau = 2 \eta_0 D$ solves it, and the fluid behaves as Newtonian.
The model has a constant shear viscosity, so it captures elasticity but not shear-thinning; this fits Boger fluids well.

## Explanations

### L1 human

Picture a liquid with long elastic molecules mixed in.
The liquid itself flows like water, while the molecules act like tiny springs that get stretched by the flow and slowly relax.
The Oldroyd-B model adds these two stresses together.
It is the standard first model of elastic liquids in mathematics and numerical simulation.
