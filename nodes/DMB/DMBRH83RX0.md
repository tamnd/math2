---
tag: DMBRH83RX0
kind: statement
role: theorem
name: Benjamin–Feir instability
msc: [76B15, "76E30"]
uses: [R9WC0Z7Z69, H7CFG2495H, GEJHRXC176, JT5EGBG2ZV]
about: [R9WC0Z7Z69]
sources:
  - url: https://en.wikipedia.org/wiki/Modulational_instability
---

## Statement

Consider a [[Stokes wave|H7CFG2495H]] on water of infinite depth, with gravity $g > 0$, wavenumber $k > 0$, small amplitude $a > 0$ and angular frequency $\omega \approx \sqrt{gk}$.
Perturb its amplitude by a small modulation of wavenumber $K > 0$, that is by sidebands of wavenumbers $k \pm K$.
In the weakly nonlinear approximation, to leading order in the steepness $ka$, the perturbation grows exponentially in time if and only if
$$0 < K < 2\sqrt{2}\,k^2 a.$$
The largest growth rate is $\tfrac{1}{2}\omega k^2a^2$, reached at $K = 2k^2a$.
So uniform Stokes wave trains on deep water are unstable.

## Remarks

The idea of the proof: write a slowly modulated wave train as $\eta \approx \operatorname{Re}\big(A(x, t)e^{i(kx - \omega t)}\big)$.
In a frame moving with the group velocity, with coordinate $\xi$, the envelope $A$ satisfies the focusing [[nonlinear Schrödinger equation|GEJHRXC176]]
$$iA_t - \frac{\omega}{8k^2}A_{\xi\xi} - \frac{\omega k^2}{2}\abs{A}^2A = 0.$$
The Stokes wave is the uniform solution $A = a\,e^{-i\omega k^2a^2t/2}$, and linearising about it gives perturbations $e^{iK\xi + st}$ with $s^2 = \frac{\omega^2K^2}{64k^4}\left(8k^4a^2 - K^2\right)$.
So $s$ is real and positive exactly when $K^2 < 8k^4a^2$.
The instability needs a dispersion relation and a nonlinear frequency correction of suitable signs; in water of finite depth $h$ it occurs only when $kh > 1.363$, approximately.
Benjamin and Feir found it in 1967, both in theory and in experiments, and it is now seen as one case of the general modulational instability.

## Explanations

### L1 human

A perfectly regular train of waves on deep water cannot last.
Tiny variations in the wave heights grow: some waves get bigger and others smaller, and the train breaks up into groups.
This came as a surprise, because the regular Stokes wave is an exact solution of the equations.
The effect helps explain why ocean waves come in sets, and it is one mechanism proposed for rogue waves.

### L2 human

The result is the water wave case of modulational instability, which also occurs in nonlinear optics and plasma physics.
The key ingredients are the [[dispersion relation|JT5EGBG2ZV]] $\omega^2 = gk$ and the amplitude dependence of the Stokes frequency, which make the envelope equation focusing.
Over longer times the modulations do not grow forever: in the nonlinear Schrödinger model the energy can return to the original wave, the Fermi–Pasta–Ulam type recurrence observed in experiments.
