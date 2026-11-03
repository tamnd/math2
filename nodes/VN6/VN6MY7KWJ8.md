---
tag: VN6MY7KWJ8
kind: example
name: Upper-convected Maxwell model
msc: [76A10, 76A05]
instance_of: [8DT9MB9V6R]
uses: [F16YFCJRFJ, P1KWMQG4NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Upper-convected_Maxwell_model
same_as:
  wikidata: Q3318079
  wikipedia: Upper-convected Maxwell model
---

## Example

The *upper-convected Maxwell model* is a constitutive law for an incompressible viscoelastic fluid.
It has a relaxation time $\lambda > 0$ and a viscosity $\eta_0 > 0$.
The extra stress $\tau$ satisfies
$$\tau + \lambda \overset{\nabla}{\tau} = 2 \eta_0 D,$$
where $\overset{\nabla}{\tau}$ is the [[upper-convected time derivative|F16YFCJRFJ]] and $D$ is the [[strain rate tensor|P1KWMQG4NZ]].

Check in steady simple shear $u = (\dot\gamma y, 0, 0)$, with $\tau$ constant in space and time.
Then $\overset{\nabla}{\tau} = -L\tau - \tau L^T$, where the only nonzero entry of $L$ is $L_{12} = \dot\gamma$.
The $(2,2)$ entry of the law gives $\tau_{22} = 0$.
The $(1,2)$ entry gives $\tau_{12} - \lambda \dot\gamma \tau_{22} = \eta_0 \dot\gamma$, so $\tau_{12} = \eta_0 \dot\gamma$.
The $(1,1)$ entry gives $\tau_{11} - 2 \lambda \dot\gamma \tau_{12} = 0$, so $\tau_{11} = 2 \lambda \eta_0 \dot\gamma^2$.
The shear viscosity is the constant $\eta_0$, but the first normal stress difference $\tau_{11} - \tau_{22} = 2 \lambda \eta_0 \dot\gamma^2$ is nonzero.
A Newtonian fluid has $\tau_{11} = \tau_{22} = 0$ in this flow, so the model is a [[non-Newtonian fluid|8DT9MB9V6R]].

## Remarks

For $\lambda = 0$ the law reduces to the Newtonian law $\tau = 2 \eta_0 D$.
It is the special case without solvent viscosity of the [[Oldroyd-B model|VPACKRZSA8]].
The normal stress difference produces effects such as rod climbing, where a fluid climbs up a rotating rod.

## Explanations

### L1 human

The Maxwell model treats a fluid like a spring and a damper joined in series: quick pushes are partly stored elastically, slow pushes are dissipated by flow.
The time $\lambda$ says how long the fluid remembers being stretched.
The "upper-convected" version uses a derivative that follows the turning and stretching of the flow, so the law does not depend on the observer.
