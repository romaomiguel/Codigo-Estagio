sp = float(67.83643)
rj = float(36.67866)
mg = float(29.22988)
es = float(27.16548)
outros = float(19.84953)

Total = sp + rj + mg + outros

print("Percentual de representação indicado por cidade")
print(f"SP: {sp / (sp + rj + mg + es) * 100:.2f}%")
print(f"RJ: {rj / (sp + rj + mg + es) * 100:.2f}%")
print(f"MG: {mg / (sp + rj + mg + es) * 100:.2f}%")
print(f"ES: {es / (sp + rj + mg + es) * 100:.2f}%")
print(f"Outros: {outros / (sp + rj + mg + es) * 100:.2f}%")
