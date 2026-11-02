---
tag: 2XK0YX7VMC
kind: example
name: Laplace transform of the Dirac delta
msc: [44A10, 46F12]
illustrates: [0V49JEZW06]
uses: [05XT5AVJBK, 0KPHENZ5S7, 099SXAG014, KHRTBP37VD]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_delta_function
---

## Example

Let $a \ge 0$ and let $\delta_a$ be the [[Dirac delta|0KPHENZ5S7]] at $a$, that is, the [[Dirac measure|099SXAG014]] that gives mass $1$ to the point $a$.
The delta is not a function, so its Laplace transform is defined as the [[Laplace–Stieltjes transform|KHRTBP37VD]] of the measure.
The point $0$ is included in the domain of integration:
$$\mathcal{L}\{\delta_a\}(s) = \int_{[0, \infty)} e^{-st}\, d\delta_a(t) = e^{-as} \quad (s \in \C).$$
Check: integrating a continuous function against $\delta_a$ evaluates it at $a$, and $t \mapsto e^{-st}$ is continuous.
In particular $\mathcal{L}\{\delta_0\} = 1$, with the convention that the lower limit is $0^-$.
This is consistent with the [[Laplace transform|05XT5AVJBK]] of the step $H(t - a)$, which is $e^{-as}/s$.
Indeed, the delta is the derivative of the step, and differentiation multiplies the transform by $s$ when the initial value is $0$.

## Explanations

### L1 human

The delta models an instant kick of total size $1$ at time $a$.
Its transform is $e^{-as}$, and for a kick at time $0$ it is just the constant $1$.
Since the transform of an ordinary function tends to $0$ as $s \to \infty$, the constant $1$ also shows that the delta is not an ordinary function.
In system theory, the response to the kick $\delta_0$ is the impulse response, and its transform is the transfer function.
