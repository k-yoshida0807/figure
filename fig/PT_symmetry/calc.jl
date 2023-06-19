#!/bin/env julia
using Printf
a = 2
b = 1
Ep(g) = a + (g^2-b^2+0im)^0.5
Em(g) = a - (g^2-b^2+0im)^0.5

out = open("./out.dat", "w")
for g = -3:0.05:3
  @printf(out,"%15.5e %15.5e %15.5e %15.5e %15.5e \n", g, real(Ep(g)), imag(Ep(g)), real(Em(g)), imag(Em(g)) )
end


