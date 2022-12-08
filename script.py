def f(x):
    return (x + 1) ** 2


a = float(input("Skriv a verdien: "))
nøyaktighet = 0.00000001
pres = 6

print(f"Øvre grenseverdi: f({round(a - nøyaktighet, pres)}) = {round(f(a - nøyaktighet), pres)}")
print(f"Nedre grenseverdi: f({round(a + nøyaktighet, pres)}) = {round(f(a + nøyaktighet), pres)}")