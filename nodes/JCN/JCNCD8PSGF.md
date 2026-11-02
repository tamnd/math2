---
tag: JCNCD8PSGF
kind: example
name: Laplace transforms of sine and cosine
msc: [44A10]
illustrates: [0V49JEZW06]
uses: [05XT5AVJBK, 0WB57D9488, X5JYH26J3M, SHX9JPKJBE]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Example

Let $\omega$ be a real number.
The [[Laplace transforms|05XT5AVJBK]] of [[sine and cosine|0WB57D9488]] are
$$\mathcal{L}\{\cos \omega t\}(s) = \frac{s}{s^2 + \omega^2}, \qquad \mathcal{L}\{\sin \omega t\}(s) = \frac{\omega}{s^2 + \omega^2} \quad (\operatorname{Re} s > 0).$$
Check: write $\cos \omega t = \frac{1}{2}(e^{i\omega t} + e^{-i\omega t})$ and $\sin \omega t = \frac{1}{2i}(e^{i\omega t} - e^{-i\omega t})$.
By the [[transform of the exponential|X5JYH26J3M]], $\mathcal{L}\{e^{\pm i\omega t}\}(s) = 1/(s \mp i\omega)$ for $\operatorname{Re} s > 0$.
By [[linearity|SHX9JPKJBE]],
$$\mathcal{L}\{\cos \omega t\}(s) = \frac{1}{2}\left(\frac{1}{s - i\omega} + \frac{1}{s + i\omega}\right) = \frac{s}{s^2 + \omega^2},$$
$$\mathcal{L}\{\sin \omega t\}(s) = \frac{1}{2i}\left(\frac{1}{s - i\omega} - \frac{1}{s + i\omega}\right) = \frac{\omega}{s^2 + \omega^2}.$$
For $\omega \ne 0$ both transforms have poles at $s = \pm i\omega$ on the imaginary axis, which matches the abscissa of convergence $0$ of these bounded, non-decaying functions.

## Explanations

### L1 human

Oscillations of angular frequency $\omega$ show up on the transform side as a pair of poles at $\pm i\omega$.
The cosine starts at $1$ and the sine starts at $0$, which is why the cosine has $s$ in the numerator and the sine has the constant $\omega$.
These two lines of the table are what makes the Laplace transform useful for springs and electric circuits.
