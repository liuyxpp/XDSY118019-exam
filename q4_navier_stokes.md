## Navier–Stokes Equations

The Navier–Stokes momentum equation can be derived as a particular form of the Cauchy momentum equation, whose general convective form is:

$$
\displaystyle \frac{D\mathbf{u}}{Dt} = \frac{1}{\rho}\,\nabla \cdot \boldsymbol{\sigma} + \mathbf{a}.
$$

By setting the Cauchy stress tensor $\boldsymbol{\sigma}$ to be the sum of a viscosity term $\boldsymbol{\tau}$ (the deviatoric stress) and a pressure term $-p\mathbf{I}$ (volumetric stress), we arrive at:

$$
\displaystyle \rho\,\frac{D\mathbf{u}}{Dt} = -\nabla p + \nabla \cdot \boldsymbol{\tau} + \rho\,\mathbf{a}
$$

where

- $\dfrac{D}{Dt}$ is the material derivative, defined as $\dfrac{\partial}{\partial t} + \mathbf{u} \cdot \nabla$,
- $\rho$ is the (mass) density,
- $\mathbf{u}$ is the flow velocity,
- $\nabla \cdot$ is the divergence,
- $p$ is the pressure,
- $t$ is time,
- $\boldsymbol{\tau}$ is the Deviatoric stress|deviatoric stress tensor, which has order 2,
- $\mathbf{a}$ represents body forces acting on the continuum, for example gravity, Fictitious force|inertial accelerations, Coulomb\'s law|electrostatic accelerations, and so on.

In this form, it is apparent that in the assumption of an inviscid fluid – no deviatoric stress – Cauchy equations reduce to the [Euler equations](https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics)).
